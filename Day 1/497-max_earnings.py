"""
# Maximum Reward Problem - Translation and Walkthrough

## Problem Description

Xiao Ming receives a weekly work list containing **n tasks**. Each task has:
- **Time required** (in hours)
- **Reward** (payment)

The total reward is the sum of all completed tasks. Help Xiao Ming schedule his work to **maximize income** within the specified working hours.

## Input/Output

**Input:**
- First line: Two positive integers `T` and `n`
  - `T` = total available work time (0 < T < 1,000,000 hours)
  - `n` = number of tasks (1 < n ≤ 3,000)
- Next `n` lines: Two integers `t` and `w`
  - `t` = time required for the task (hours, t > 0)
  - `w` = reward for the task

**Output:**
- Maximum reward achievable within time `T`

## Solution Approach (Hints)

This is a classic **0/1 Knapsack Problem**:

1. Create a 2D DP array where `dp[i][j]` = maximum reward using first `i` tasks with time limit `j`
2. For each task `i` and time `j`:
   - If task time ≤ available time: `dp[i][j] = max(dp[i-1][j], dp[i-1][j-time[i]] + reward[i])`
   - Otherwise: `dp[i][j] = dp[i-1][j]`
3. Answer is `dp[n][T]`

## Example Walkthrough

**Input:**
```text
10 3
5 10
4 8
6 12
```

**Interpretation:**
- Total time available: 10 hours
- 3 tasks:
  - Task 1: 5 hours, reward 10
  - Task 2: 4 hours, reward 8
  - Task 3: 6 hours, reward 12

**Step-by-step DP:**

| Time | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|------|---|---|---|---|---|---|---|---|---|---|-----|
| Task 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Task 1 (5h, 10) | 0 | 0 | 0 | 0 | 0 | **10** | 10 | 10 | 10 | 10 | 10 |
| Task 2 (4h, 8) | 0 | 0 | 0 | 0 | **8** | 10 | 10 | 10 | 10 | **18** | 18 |
| Task 3 (6h, 12) | 0 | 0 | 0 | 0 | 8 | 10 | **12** | 12 | 12 | 18 | **20** |

**Optimal Selection:**
- Choose Task 2 (4 hours, reward 8) + Task 3 (6 hours, reward 12)
- Total time: 4 + 6 = 10 hours
- Total reward: 8 + 12 = **20**

**Output:** `20`
"""



def maximum_earnings(T, n, jobs):
    # 创建二维动态规划数组
    dp = [[0] * (T + 1) for _ in range(n + 1)]

    # 动态规划填充dp数组
    for i in range(1, n + 1):
        for j in range(1, T + 1):
            # 当前工作的耗时时间和报酬
            time = jobs[i - 1][0]
            earnings = jobs[i - 1][1]

            # 判断是否选择当前工作
            if time <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - time] + earnings)
            else:
                dp[i][j] = dp[i - 1][j]

    # 返回最大报酬
    return dp[n][T]


# 读取输入
T, n = map(int, input().split())
jobs = []
for _ in range(n):
    t, w = map(int, input().split())
    jobs.append((t, w))

# 计算最大报酬
result = maximum_earnings(T, n, jobs)

# 输出结果
print(result)

