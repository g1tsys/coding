"""
# High and Short Queue Arrangement Problem

## Problem Description

There's a queue of children with different heights, represented by a positive integer array (e.g., {5,3,1,2,3}).

We want to arrange them in alternating "tall" "short" "tall" "short" order where:
- Each "tall" position child must be **greater than or equal to** adjacent positions
- Each "short" position child must be **less than or equal to** adjacent positions
- The **total movement distance must be minimized**
- Start with a "tall" position first

**Movement distance definition**: If a child at position 2 moves to position 3, the distance is 1; if they move to position 4, the distance is 2.

## Input/Output

**Input**: Space-separated positive integers representing children's heights
- Example: `4 3 5 7 8`
- Note: Less than 100 children

**Output**: Space-separated positive integers after arrangement
- Example: `4 3 7 5 8`
- Explanation: 4(tall) 3(short) 7(tall) 5(short) 8(tall). Only 5 and 7 swapped positions (distance = 1 each)

## Python Solution Approach

The key insight is to use a **greedy approach with local swaps**:

1. **Read and parse input** into an array
2. **Iterate through positions** checking alternating tall/short requirements:
   - Even indices (0, 2, 4...) should be "tall" positions: `arr[i] >= arr[i+1]`
   - Odd indices (1, 3, 5...) should be "short" positions: `arr[i] <= arr[i+1]`
3. **Swap adjacent elements** when the pattern is violated
4. **Output the result**

## Python Code

```python
# Read input and convert to integer list
heights = list(map(int, input().split()))

# Traverse the array and fix violations with local swaps
for i in range(len(heights) - 1):
    if i % 2 == 0:  # Even index - should be "tall" position
        # Current position should be >= next position
        if heights[i] < heights[i + 1]:
            heights[i], heights[i + 1] = heights[i + 1], heights[i]
    else:  # Odd index - should be "short" position
        # Current position should be <= next position
        if heights[i] > heights[i + 1]:
            heights[i], heights[i + 1] = heights[i + 1], heights[i]

# Output the result
print(' '.join(map(str, heights)))
```

## Example Walkthrough

**Input**: `4 3 5 7 8`

**Step-by-step process**:

| Step | Index | Check | Array State | Action |
|------|-------|-------|-------------|--------|
| Initial | - | - | [4, 3, 5, 7, 8] | - |
| 1 | i=0 (even) | 4 >= 3? ✓ | [4, 3, 5, 7, 8] | No swap needed |
| 2 | i=1 (odd) | 3 <= 5? ✓ | [4, 3, 5, 7, 8] | No swap needed |
| 3 | i=2 (even) | 5 >= 7? ✗ | [4, 3, 5, 7, 8] | **Swap 5↔7** |
| After swap | - | - | [4, 3, 7, 5, 8] | - |
| 4 | i=3 (odd) | 5 <= 8? ✓ | [4, 3, 7, 5, 8] | No swap needed |

**Output**: `4 3 7 5 8`

**Verification**:
- Position 0 (4): tall ✓ (4 > 3)
- Position 1 (3): short ✓ (3 < 7)
- Position 2 (7): tall ✓ (7 > 5)
- Position 3 (5): short ✓ (5 < 8)
- Position 4 (8): tall ✓ (end position)

**Movement distance**: Only one swap (5 and 7), each moved 1 position = minimal distance achieved! 🎉

"""



try:
    cap = list(map(int, input().split()))  # 读取一行输入，将每个数字转换成整数并存入列表cap
    n = len(cap)  # 获取cap列表的长度

    if n == 0:
        raise ValueError  # 如果输入为空，则抛出异常

    for i in range(n):  # 遍历cap列表的每个元素
        if i % 2 == 0 and i < n - 1 and cap[i] < cap[i + 1]:  # 如果索引为偶数且不是最后一个元素，并且当前元素小于下一个元素
            cap[i], cap[i + 1] = cap[i + 1], cap[i]  # 交换当前元素和下一个元素的位置
        if i % 2 == 1 and i < n - 1 and cap[i] > cap[i + 1]:  # 如果索引为奇数且不是最后一个元素，并且当前元素大于下一个元素
            cap[i], cap[i + 1] = cap[i + 1], cap[i]  # 交换当前元素和下一个元素的位置

    for i in range(n):
        if i != 0:  # 如果不是第一个元素
            print(" ", end="")  # 输出一个空格
        print(cap[i], end="")  # 输出当前元素
    print()  # 输出换行符

except ValueError:
    print([])  # 如果出现非法参数情况，输出空数组 []
