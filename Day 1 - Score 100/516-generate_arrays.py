"""
# Array Concatenation Problem

## Problem Description

You have multiple groups of integer arrays that need to be merged into a new array.

**Merging Rules:**
- Take a fixed length of content from each array in order and merge it into the new array
- The taken content is deleted from the original array
- If a row has insufficient length or is already empty, take the remaining content and move to the next row
- Continue until all arrays are processed

## Input/Output

**Input:**
- Line 1: Fixed length to read each time (0 < length < 10)
- Line 2: Number of integer arrays (0 < count < 1000)
- Lines 3-n: Arrays to be merged (separated by newlines, elements separated by commas, max 100 elements per array)

**Output:**
- A new merged array, elements separated by commas

## Python Solution Approach

### Thought Process:

1. **Input Reading:**
   - Read the fixed length `m` (how many elements to take from each array per round)
   - Read the number of arrays `n`
   - Read each array and store them in a list of lists

2. **Initialize Result List:**
   - Create an empty list to store the merged result

3. **Merge Arrays:**
   - While there are still non-empty arrays:
     - Iterate through each array
     - Take up to `m` elements from the current array
     - Add these elements to the result
     - Remove the taken elements from the original array
     - Remove empty arrays from the list

4. **Output Result:**
   - Join all elements with commas and print

## Example Walkthrough

**Input:**
```
3
2
1,2,3,4,5,6
7,8,9,10,11
```

**Step-by-step execution:**

- `m = 3` (take 3 elements at a time)
- Arrays: `[[1,2,3,4,5,6], [7,8,9,10,11]]`

**Round 1:**
- From array 1: take `[1,2,3]` → result = `[1,2,3]`, array 1 becomes `[4,5,6]`
- From array 2: take `[7,8,9]` → result = `[1,2,3,7,8,9]`, array 2 becomes `[10,11]`

**Round 2:**
- From array 1: take `[4,5,6]` → result = `[1,2,3,7,8,9,4,5,6]`, array 1 becomes `[]` (removed)
- From array 2: take `[10,11]` (only 2 left) → result = `[1,2,3,7,8,9,4,5,6,10,11]`, array 2 becomes `[]` (removed)

**Output:**
```
1,2,3,7,8,9,4,5,6,10,11
```

## Python Code

```python
# Read fixed length
m = int(input())
# Read number of arrays
n = int(input())

# Read all arrays
arrays = []
for _ in range(n):
    line = input().strip()
    if line:
        arr = list(map(int, line.split(',')))
        arrays.append(arr)

# Result list
result = []

# Merge arrays
while arrays:
    # Remove empty arrays
    arrays = [arr for arr in arrays if arr]
    
    if not arrays:
        break
    
    # Take m elements from each array
    for arr in arrays:
        # Take up to m elements
        take_count = min(m, len(arr))
        result.extend(arr[:take_count])
        # Remove taken elements
        del arr[:take_count]

# Output result
print(','.join(map(str, result)))
```

This solution efficiently handles the round-robin merging of multiple arrays with a fixed chunk size.
"""


m = int(input())  # 读取固定长度
n = int(input())  # 读取整数数组的数目

num_arrays = []  # 初始化一个空数组来存储所有的整数数组
for _ in range(n):
    num_array = list(map(int, filter(lambda x: x != '', input().split(','))))  # 读取当前行的整数数组并过滤掉空串
    num_arrays.append(num_array)

result = []  # 初始化一个空数组来存储合并后的结果

while any(num_arrays):  # 只要还有未处理完的数组
    for index in range(len(num_arrays)):
        single_array = num_arrays[index]  # 获取当前数组
        for _ in range(m):
            # 若当前数组已经为空，则跳过
            if len(single_array) == 0:
                break
            result.append(str(single_array.pop(0)))  # 取出第一个元素并添加到结果数组中
    # 移除空数组
    num_arrays = [array for array in num_arrays if len(array) > 0]

output = ','.join(result)  # 将合并后的结果数组转换为字符串，用逗号分隔元素
print(output)  # 输出结果
