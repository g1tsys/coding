"""
### Question Translation:
A charging station provides `n` charging devices, each with a specific output power. Any combination of these devices forms a power sum, which is an element of the power set `P`. The optimal element of `P` is the one that is closest to the maximum output power of the charging station `p_max`, but must not exceed it.

#### Input:
- The first line contains the number of charging devices `n`.
- The second line contains a list of the output power of each charging device.
- The third line contains the maximum output power of the charging station `p_max`.

#### Output:
- The optimal element of the power set `P` (the maximum possible sum of power that does not exceed `p_max`).

#### Constraints:
- `n > 0`
- The optimal element must be less than or equal to `p_max`.

---

### Example:
**Input:**
```
4
50 20 20 60
90
```

**Output:**
```
90
```

**Explanation:**
The sum of 50 + 20 + 20 = 90, which is exactly the maximum allowed power (`p_max = 90`), so the optimal element is 90.

---

### Walkthrough Example:

Let's walk through the example step-by-step:

#### Step 1: Read Input
- `n = 4`
- `powers = [50, 20, 20, 60]`
- `p_max = 90`

#### Step 2: Initialize a DP Array
Create a 1D array `dp` of size `p_max + 1` (i.e., 91 elements), initialized to 0. This will store the maximum sum of power that can be achieved for each possible power level from 0 to `p_max`.

#### Step 3: Update the DP Array
Iterate through each power value in the list and update the `dp` array in reverse order (from `p_max` to 0).

For each power value `power` in `powers`:
- For `j` from `p_max` down to `power`:
  - `dp[j] = max(dp[j], dp[j - power] + power)`

This ensures that we do not reuse the same device multiple times.

#### Step 4: Find the Optimal Element
After processing all devices, the value `dp[p_max]` will be the maximum power sum that does not exceed `p_max`.

In the example, the final value of `dp[90]` is 90, which is the optimal element.

---

### Summary:
This problem is a classic **knapsack problem** where we are trying to maximize the sum of selected items (charging devices) without exceeding a given capacity (`p_max`). The optimal solution is found using **dynamic programming**.
"""






def find_optimal_power(n, powers, p_max):
    # 初始化一维数组m，用于记录最大输出功率的情况下的最优元素
    m = [0] * (p_max + 1)

    for i in range(1, n + 1):
        for j in range(p_max, powers[i - 1] - 1, -1):
            # 对于每个充电设备，从最大输出功率p_max开始逆序遍历
            # 更新m[j]为当前设备输出功率和之前状态下的最优元素之和的最大值
            m[j] = max(m[j], m[j - powers[i - 1]] + powers[i - 1])

    if m[p_max] > p_max:
        # 如果最优元素超过了最大输出功率p_max，则返回0
        return 0
    return m[p_max]


n = int(input())  # 读取充电设备个数n
powers = list(map(int, input().split()))  # 读取每个充电设备的输出功率列表powers
p_max = int(input())  # 读取充电站最大输出功率p_max

result = find_optimal_power(n, powers, p_max)  # 调用函数找到功率集合P的最优元素
print(result)  # 输出最优元素


