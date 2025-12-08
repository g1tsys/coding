"""
> The question is about matching teams in a game based on their strength values. The goal is to pair teams whose strength difference is within a given threshold `d`, and to maximize the number of such pairs while minimizing the total strength difference across all pairs.

### **Translation of the Question:**
Given `n` teams with their respective strength values, match them in pairs such that the difference in strength between the two teams in a pair is at most `d`. The objective is to **maximize the number of such pairs** and, among all such pairings, **minimize the total strength difference** across all pairs.

### **Input:**
- First line: `n` (number of teams), `d` (maximum allowed strength difference)
- Second line: `n` space-separated integers representing the strength of each team

### **Output:**
- The **minimum total strength difference** of the matched pairs.
- If no pairs can be formed, output `-1`.

---

### **Detailed Thought Process (Python Approach):**

1. **Input Processing and Sorting**: First, read the number of teams `n` and the maximum allowed strength difference `d`, then read each team's strength value and sort them. Sorting makes it easier to find matches among adjacent teams.

2. **Dynamic Programming Array Definition**: Define a 2D array `dp`, where `dp[i][j]` represents the minimum total strength difference when matching `j` pairs from the first `i` teams. The array size is `(n+1) x (n//2+1)` because at most `n//2` pairs can be formed.

3. **Initialization**: For the case with no teams (i.e., `i=0`), matching 0 pairs has a total strength difference of 0, so `dp[0][0] = 0`. All other initial values are set to infinity (`float('inf')`), representing impossible states.

4. **Filling the DP Table**:
   - For each team `i` from 1 to `n`:
     - **Option 1: Don't match team `i`** - carry forward the previous state: `dp[i][j] = dp[i-1][j]`
     - **Option 2: Match team `i` with team `i-1`** - if the strength difference between teams `i-1` and `i` is within the allowed threshold `d`, then: `dp[i][j] = min(dp[i][j], dp[i-2][j-1] + difference)`
   - This ensures we consider both matching and not matching each team to find the optimal solution.

5. **Finding the Result**: Starting from the maximum possible number of pairs, check `dp[n][j]` to find the first `j` that is not infinity, which represents the maximum number of pairs that can be matched. If `j` is 0, it means no matches were successful, so return `-1`. Otherwise, return `dp[n][j]`.

---

### **Example Walkthrough (Sample 1):**

**Input:**
```
6 2
1 2 3 4 5 6
```

**Step-by-step Execution:**

1. **Sort the array**: `[1, 2, 3, 4, 5, 6]`

2. **Initialize DP table**: `dp[7][4]` (7 rows for 0-6 teams, 4 columns for 0-3 pairs)
   - `dp[0][0] = 0`, all others = infinity

3. **Fill DP table**:
   - For team 1 (strength=1): Can't form pairs yet
   - For team 2 (strength=2): Can pair with team 1, difference = 1
     - `dp[2][1] = dp[0][0] + 1 = 1`
   - For team 3 (strength=3): Can pair with team 2, difference = 1
     - `dp[3][1] = min(dp[2][1], dp[1][0] + 1) = 1`
   - For team 4 (strength=4): Can pair with team 3, difference = 1
     - `dp[4][2] = dp[2][1] + 1 = 2` (pairs: (1,2), (3,4))
   - Continue this process...

4. **Final result**: Maximum pairs = 3, with pairs (1,2), (3,4), (5,6)
   - Total strength difference = `1 + 1 + 1 = 3`

**Output:**
```
3
```

---

### **Key Points:**
- **Sorting** ensures adjacent teams have minimal strength differences
- **DP state** tracks both the number of pairs and minimum total difference
- **Greedy + DP** approach ensures we maximize pairs first, then minimize total difference
"""

def min_total_difference(n, d, skills):
    # 对队伍的实力值进行排序
    skills.sort()

    # 初始化动态规划数组 dp
    # dp[i][j] 表示考虑前 i 个队伍中，匹配 j 对时的最小总实力差
    dp = [[float('inf')] * (n // 2 + 1) for _ in range(n + 1)]

    # 当没有队伍参与时，匹配 0 对的总实力差为 0
    dp[0][0] = 0

    # 填充动态规划表
    for i in range(1, n + 1):  # i 表示当前考虑的队伍数量
        for j in range(0, i // 2 + 1):  # j 表示匹配的对数
            # 不匹配第 i 个队伍的情况，继承之前的状态
            dp[i][j] = dp[i - 1][j]

            # 如果可以匹配并且有足够的队伍进行匹配
            if i > 1 and j > 0 and skills[i - 1] - skills[i - 2] <= d:
                # 更新 dp[i][j]，尝试将第 i-1 和 i-2 组成一对
                dp[i][j] = min(dp[i][j], dp[i - 2][j - 1] + skills[i - 1] - skills[i - 2])

    # 寻找能够匹配的最多对数并输出结果
    for j in range(n // 2, -1, -1):
        if dp[n][j] < float('inf'):
            if j == 0:
                return -1
            return dp[n][j]

    # 如果没有任何队伍可以匹配，返回 -1
    return -1


#
if __name__ == "__main__":
    # 读取输入的 n 和 d
    n, d = map(int, input().split())
    # 读取各个队伍的实力值
    skills = list(map(int, input().split()))

    # 调用函数计算并输出结果
    result = min_total_difference(n, d, skills)
    print(result)


