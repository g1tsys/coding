"""
# Jump Grid Game - Problem Translation and Solution

## Problem Description

Xiao Ming and his friends are playing a grid jumping game. Each grid has a specific score, for example: `score = [1, -1, -6, 7, -17, 7]`. Starting from `score[0]`, with a maximum step length of `k`, return the maximum score Xiao Ming can achieve when jumping to the endpoint `score[n-1]`.

## Input/Output

**Input:**
- Line 1: Total number of grids `n`
- Line 2: Score for each grid `score[i]`
- Line 3: Maximum step length `k`

**Output:**
- Maximum score achievable

**Constraints:**
- Grid length `n` and step length `k` are in range `[1, 100000]`
- Each grid score `score[i]` is in range `[-10000, 10000]`

## Solution Approach (Dynamic Programming with Sliding Window)

### Key Idea:
Use **dynamic programming** where `dp[i]` represents the maximum score achievable when reaching position `i`. Use a **deque (double-ended queue)** to maintain the maximum value within the sliding window efficiently.

### Algorithm Steps:

1. **Initialize** `dp` array where `dp[i]` stores max score to reach position `i`
2. Set `dp[0] = score[0]` (starting position)
3. Use a deque to track indices of positions with maximum `dp` values within window `k`
4. For each position `i` from 1 to n-1:
   - Remove indices outside the window `[i-k, i-1]`
   - Calculate `dp[i] = score[i] + dp[deque.front()]`
   - Maintain deque in decreasing order of `dp` values
5. Return `dp[n-1]`

## Python Code

```python
from collections import deque

def maxScore(n, score, k):
    # dp[i] represents max score to reach position i
    dp = [0] * n
    dp[0] = score[0]
    
    # Deque stores indices, maintaining decreasing dp values
    dq = deque([0])
    
    for i in range(1, n):
        # Remove indices outside window [i-k, i-1]
        while dq and dq[0] < i - k:
            dq.popleft()
        
        # Calculate max score to reach position i
        dp[i] = score[i] + dp[dq[0]]
        
        # Maintain deque: remove smaller dp values from back
        while dq and dp[i] >= dp[dq[-1]]:
            dq.pop()
        
        # Add current index
        dq.append(i)
    
    return dp[n - 1]

# Input
n = int(input())
score = list(map(int, input().split()))
k = int(input())

# Output
print(maxScore(n, score, k))
```

## Example Walkthrough

**Input:**
```
6
1 -1 -6 7 -17 7
4
```

**Step-by-step execution:**

| Position | Score | Window (k=4) | Best Previous | dp[i] Calculation | dp[i]  |  Deque      |  
|----------|-------|--------------|---------------|-------------------|--------|-------------|
| 0        | 1     |       -      |       -       |         1         |   1    |   [0]       |
| 1        | -1    |      [0]     |    dp[0]=1    |      -1 + 1       |   0    |  [0, 1]     |
| 2        | -6    |     [0,1]    |    dp[0]=1    |      -6 + 1       |  -5    | [0, 1, 2]   |
| 3        | 7     |    [0,1,2]   |    dp[0]=1    |       7 + 1       |   8    |   [3]       |
| 4        | -17   |   [0,1,2,3]  |    dp[3]=8    |      -17 + 8      |  -9    |  [3, 4]     |
| 5        | 7     |   [1,2,3,4]  |    dp[3]=8    |       7 + 8       | **15** |  [3, 5]     |

**Output:** `15`

**Optimal path:** 0 → 3 → 5 (scores: 1 + 7 + 7 = 15)

The algorithm efficiently finds the maximum score by considering all valid jumps within the step limit `k`.
"""



from collections import deque

# 动态规划解决问题
def maxScore(n, score, k):
    # 初始化dp数组
    dp = [0] * n
    dp[0] = score[0]

    # 初始化双端队列，并放入第一个元素的索引
    dq = deque([0])

    # 从第二个位置开始遍历
    for i in range(1, n):
        # 移除窗口之外的元素
        if dq[0] < i - k:
            dq.popleft()

        # 计算到达当前位置的最大得分
        dp[i] = score[i] + dp[dq[0]]

        # 维护双端队列，保证队列首元素是最大值的索引
        while dq and dp[i] >= dp[dq[-1]]:
            dq.pop()
        dq.append(i)

    # 返回到达终点的最大得分
    return dp[n-1]

# 输入处理
n = int(input())
score = list(map(int, input().split()))
k = int(input())

# 计算最大得分
result = maxScore(n, score, k)

# 输出结果
print(result)



