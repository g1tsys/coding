"""
# Translation and Explanation

## Problem Description

A scientist wants to copy files from an antique computer using only a 3.5-inch floppy disk as the transfer medium. The goal is to maximize the total size of files copied to the disk.

**Constraints:**
- Floppy disk capacity: 1,474,560 bytes
- Block size: 512 bytes
- Each file occupies complete blocks (rounded up)
- Files must be copied completely (no compression or partial copying)

**Input:**
- First line: N (number of files)
- Next N lines: Size of each file in bytes

**Output:**
- Maximum total size of files that can be copied

## Python Approach (0/1 Knapsack Problem)

This is a classic **0/1 Knapsack problem** where:
- **Knapsack capacity** = Total blocks available = 1,474,560 ÷ 512 = 2,880 blocks
- **Items** = Files (each file has a size and occupies a certain number of blocks)
- **Goal** = Maximize total file size without exceeding capacity

### Algorithm Steps:

1. **Calculate blocks needed** for each file: `blocks = (file_size + 511) // 512` (ceiling division)
2. Use **dynamic programming** with array `dp[j]` where `dp[j]` = maximum file size using `j` blocks
3. For each file, iterate **backwards** through capacities to avoid using the same file twice
4. Update: `dp[j] = max(dp[j], dp[j - blocks_needed] + file_size)`

### Python Code:


n = int(input())
V = 1474560 // 512  # Total blocks available = 2880

dp = [0] * (V + 1)  # dp[j] = max file size using j blocks

for _ in range(n):
    file_size = int(input())
    blocks_needed = (file_size + 511) // 512  # Ceiling division
    
    # Iterate backwards to prevent reusing same file
    for j in range(V, blocks_needed - 1, -1):
        dp[j] = max(dp[j], dp[j - blocks_needed] + file_size)

print(dp[V])

## Example Walkthrough

**Input:**
3
737270
737272
737288


**Step-by-step:**

1. **Initialize:** `V = 2880 blocks`, `dp = [0] * 2881`

2. **File 1: 737,270 bytes**
   - Blocks needed: `(737270 + 511) // 512 = 1440 blocks`
   - Update `dp[2880] = max(0, dp[1440] + 737270) = 737270`
   - Update `dp[1440] = 737270`

3. **File 2: 737,272 bytes**
   - Blocks needed: `(737272 + 511) // 512 = 1440 blocks`
   - Update `dp[2880] = max(737270, dp[1440] + 737272) = max(737270, 1474542) = 1474542`

4. **File 3: 737,288 bytes**
   - Blocks needed: `(737288 + 511) // 512 = 1441 blocks`
   - Cannot fit with other files (1440 + 1441 > 2880)
   - `dp[2880]` remains `1474542`

**Output:** `1474542` (Files 1 and 2)

The algorithm efficiently finds the optimal combination of files that maximizes total size while respecting the block allocation constraint.
"""


N = int(input())

V = 2880  # 软盘的总容量为 2880 块
f = [0] * (V + 1)  # f[j] 表示背包容量为 j 时的最大文件总大小

for _ in range(N):
    w = int(input())  # 文件的大小
    v = (w + 511) // 512  # 文件需要占用的块数
    for j in range(V, v - 1, -1):  # 背包容量逆序遍历
        f[j] = max(f[j], f[j - v] + w)  # 不放入当前文件和放入当前文件两种情况取最大值

print(f[V])  # 输出最大文件总大小

