"""
# Sliding Window Maximum Sum Problem

## Problem Description

Given an array of N integers and a window of size M, the window slides from the first element of the array until it can no longer slide. Each time the window slides, it produces a window sum (sum of all numbers in the window). Find the **maximum value** among all window sums produced during sliding.

## Input/Output Format

**Input:**
- First line: A positive integer N, representing the number of integers (0 < N < 100,000)
- Second line: N integers, each in range [-100, 100]
- Third line: A positive integer M, representing window size (M ≤ 100,000 and M ≤ N)

**Output:**
- The maximum sum among all sliding window sums

## Key Points

- The sliding window must be a **contiguous subarray** within the array boundaries
- The window does NOT wrap around (no circular behavior)
- The window moves continuously within the array

## Solution Approach

1. Read the array length N and array elements
2. Read the window size M
3. Calculate the initial window sum (sum of first M elements)
4. Initialize `max_sum` with this initial window sum
5. Slide the window from position M+1 onwards:
   - Remove the leftmost element from the previous window
   - Add the new rightmost element
   - Update `max_sum` if current window sum is larger
6. Output `max_sum`

## Example Walkthrough

**Input:**
```text
5
2 3 -1 4 5
3
```

**Step-by-step:**
- Array: [2, 3, -1, 4, 5]
- Window size: 3

| Window Position | Elements | Sum | Max So Far |
|----------------|----------|-----|------------|
| Window 1 | [2, 3, -1] | 4 | 4 |
| Window 2 | [3, -1, 4] | 6 | 6 |
| Window 3 | [-1, 4, 5] | 8 | **8** |

**Output:** `8`

The algorithm efficiently computes this in O(N) time by reusing the previous window sum rather than recalculating from scratch each time.

"""


# 获取整数个数N
N = int(input())
# 获取整数数组arr的字符串形式，然后分割成字符串列表
arr_str = input().split()
# 手动将字符串列表转换为整数列表
arr = [int(x) for x in arr_str]
# 获取窗口大小M
M = int(input())

# 初始化窗口和为窗口的前M个数的和
window_sum = sum(arr[:M])
# 初始化最大和为窗口的和
max_sum = window_sum

# 从第M个数开始遍历数组
for i in range(M, N):
    # 窗口和等于上一个窗口和减去窗口第一个数再加上当前数
    window_sum = window_sum - arr[i - M] + arr[i]
    # 更新最大和
    max_sum = max(max_sum, window_sum)

# 输出最大和
print(max_sum)

