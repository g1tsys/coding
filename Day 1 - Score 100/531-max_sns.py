"""
The problem is about finding the **maximum number of SMS messages** a customer can get based on their **budget** and a **price list** that indicates how many SMS messages you can get for each amount of money. The goal is to **maximize the number of SMS messages** within the budget.

### Problem Summary:
- **Input:**
  - `M`: The customer's budget (an integer, 0 ≤ M ≤ 10⁶).
  - `P1, P2, ..., Pn`: A list of prices where `Pi` is the number of SMS messages you get for `i` yuan (1 ≤ Pi ≤ 1000, 1 ≤ n ≤ 100).
- **Output:**
  - The **maximum number of SMS messages** that can be obtained within the budget.

### Python Solution Approach:
1. **Dynamic Programming (DP) Setup:**
   - Create a 1D DP array `dp` of size `M + 1`, where `dp[i]` represents the **maximum SMS messages** obtainable with `i` yuan.
   - Initialize `dp[0] = 0` because with 0 yuan, you can't buy any SMS.

2. **DP Transition:**
   - For each amount `i` from 1 to `M`, iterate through the price list.
   - If `i >= j`, then `dp[i] = max(dp[i], dp[i - j] + Pj)`, where `j` is the price index (from 1 to n).

3. **Final Result:**
   - The result is `dp[M]`, which is the maximum number of SMS messages obtainable with the budget.

### Example Walkthrough:
**Input:**
- Budget `M = 5`
- Price list `P = [1, 2, 3]` (i.e., 1 yuan = 1 SMS, 2 yuan = 2 SMS, 3 yuan = 3 SMS)

**Step-by-step:**
1. Initialize `dp = [0, 0, 0, 0, 0, 0]` (for budget 0 to 5).
2. For `i = 1`:
   - Try `j = 1`: `i >= j` → `dp[1] = max(0, dp[0] + P[0]) = 1`
3. For `i = 2`:
   - Try `j = 1`: `dp[2] = max(0, dp[1] + P[0]) = 2`
   - Try `j = 2`: `dp[2] = max(2, dp[0] + P[1]) = 2`
4. For `i = 3`:
   - Try `j = 1`: `dp[3] = max(0, dp[2] + P[0]) = 3`
   - Try `j = 2`: `dp[3] = max(3, dp[1] + P[1]) = 3`
   - Try `j = 3`: `dp[3] = max(3, dp[0] + P[2]) = 3`
5. Continue this for all values up to `i = 5`.

**Final `dp[5] = 5`** (you can buy 5 SMS messages with 5 yuan).

### Python Code (Example):
```python
def max_sms_messages(M, P):
    dp = [0] * (M + 1)
    for i in range(1, M + 1):
        for j in range(1, len(P) + 1):
            if i >= j:
                dp[i] = max(dp[i], dp[i - j] + P[j - 1])
    return dp[M]

# Example usage:
M = 5
P = [1, 2, 3]
print(max_sms_messages(M, P))  # Output: 5
```

"""


def main():
    max_num = int(input())  # 最大值
    values = list(map(int, input().split()))  # 物品价值列表
    n = len(values)  # 物品个数

    dp = [[0] * (max_num + 1) for _ in range(n + 1)]  # 动态规划表格初始化
    for i in range(1, n + 1):
        for j in range(1, max_num + 1):
            if j < i:
                # 当前背包容量不足以装下第 i 个物品，继承上一行的最优解
                dp[i][j] = dp[i - 1][j]
            else:
                # 比较选择装入和不装入第 i 个物品的价值，取较大值作为最优解
                dp[i][j] = max(dp[i - 1][j], dp[i][j - i] + values[i - 1])

    print(dp[n][max_num])  # 输出最大价值

if __name__ == "__main__":
    main()
