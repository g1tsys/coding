"""
# Translation and Explanation

## Problem Description

In recent years, China has made significant progress in desertification control. A desert has planted N poplar trees (numbered 1 to N) in a row. After one month, M trees did not survive. Now K trees can be replanted (only replanting in dead positions, not planting new ones). How should we replant to get the maximum number of consecutive living poplar trees?

## Input/Output

**Input:**
- N: Total number of trees planted, 1 ≤ N ≤ 100000
- M: Number of dead trees, followed by M space-separated numbers (tree positions), sorted in ascending order
- K: Maximum number of trees that can be replanted, 0 ≤ K ≤ M

**Output:**
- Maximum number of consecutive poplar trees possible

## Python Approach (Sliding Window)

The key insight is to use a **sliding window technique**:

1. **Convert dead tree positions to a set** for O(1) lookup
2. **Initialize variables**: left boundary = 0, right boundary = 0, dead count in window = 0, max consecutive = 0
3. **Expand the window** by moving right boundary:
   - If current position is a dead tree, increment dead count
   - If dead count exceeds K (replanting budget), shrink window from left
   - Update maximum consecutive count
4. **Return the maximum** consecutive count found

## Example Walkthrough

**Example Input:**
```text
N = 10 (total trees: positions 1-10)
Dead trees: [3, 5, 7]
K = 2 (can replant 2 trees)
```

**Step-by-step:**

| Step | Left | Right | Dead in Window | Window Range | Consecutive Count | Action |
|------|------|-------|----------------|--------------|-------------------|---------|
| 1 | 0 | 1 | 0 | [1] | 1 | Move right |
| 2 | 0 | 2 | 0 | [1,2] | 2 | Move right |
| 3 | 0 | 3 | 1 | [1,2,3] | 3 | Tree 3 dead, count=1 ≤ K |
| 4 | 0 | 4 | 1 | [1,2,3,4] | 4 | Move right |
| 5 | 0 | 5 | 2 | [1,2,3,4,5] | 5 | Tree 5 dead, count=2 ≤ K |
| 6 | 0 | 6 | 2 | [1,2,3,4,5,6] | 6 | Move right |
| 7 | 0 | 7 | 3 | [1,2,3,4,5,6,7] | - | Tree 7 dead, count=3 > K! |
| 8 | 3 | 7 | 2 | [4,5,6,7] | 4 | Shrink: remove tree 3 |
| 9 | 3 | 8 | 2 | [4,5,6,7,8] | 5 | Move right |
| 10 | 3 | 9 | 2 | [4,5,6,7,8,9] | 6 | Move right |
| 11 | 3 | 10 | 2 | [4,5,6,7,8,9,10] | 7 | Move right |

**Answer: 7** consecutive trees (positions 4-10, replanting trees at positions 5 and 7)

## Sample Python Code Structure

```python
def max_consecutive_trees(N, dead_positions, K):
    dead_set = set(dead_positions)
    left = 0
    dead_count = 0
    max_consecutive = 0
    
    for right in range(1, N + 1):
        # Check if current position is dead
        if right in dead_set:
            dead_count += 1
        
        # Shrink window if dead count exceeds K
        while dead_count > K:
            left += 1
            if left in dead_set:
                dead_count -= 1
        
        # Update maximum
        max_consecutive = max(max_consecutive, right - left)
    
    return max_consecutive
```

The algorithm runs in **O(N)** time complexity with **O(M)** space complexity.

"""


import math

def calculate_minimum_z(x, y):
    # 计算字母组合的数量
    letter_combinations = 26 ** y
    # 需要的数字组合数量
    required_number_combinations = x / letter_combinations
    # 计算最小的数字长度 z，确保至少为 1
    z = max(1, math.ceil(math.log10(required_number_combinations)))
    return z

# 示例输入
x, y = map(int, input().split())

# 计算最小的数字长度 Z
z = calculate_minimum_z(x, y)

# 输出结果
print(z)

