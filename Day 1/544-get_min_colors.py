"""
# Digital Coloring Problem - Translation and Solution

## Problem Description

After the pandemic, Hope Elementary School has finally reopened. On the first day of Class 2, Grade 3, the task is to remake the blackboard bulletin.
There are already **N positive integers** written on the blackboard, and students need to assign a color to each number.
To make the bulletin both beautiful and educational, the teacher requires that **all numbers of the same color must be divisible by the smallest number in that color group**.
Now, please help the students calculate the **minimum number of colors** needed to color these N numbers.

## Input/Output

**Input:**
- First line: A positive integer N
- Second line: N integers (guaranteed to be in range [1, 100])

**Output:**
- A single integer representing the minimum number of colors needed

## Python Solution Approach

### Thought Process:

1. **Create a tracking array**: Use a boolean array `is_divisible` to track whether each number can be divided by another number in the array
2. **Initialize color counter**: Set `color_count = 0` to track the number of colors needed
3. **Two-layer loop to check divisibility**:
   - For each number `nums[i]`, check if any other number `nums[j]` (where `j ≠ i` and `nums[j] < nums[i]`) can divide it
   - If `nums[i] % nums[j] == 0`, mark `is_divisible[i] = True`

4. **Count independent numbers**: Numbers that cannot be divided by any other number in the array need their own color
5. **Return the count**: The result is the number of elements where `is_divisible[i] == False`


# Read input
n = int(input())
nums = list(map(int, input().split()))

# Get and print result
print(get_min_colors(nums))


## Example Walkthrough

**Input:**

4
2 4 6 8


**Step-by-step execution:**

1. **Initial array**: `nums = [2, 4, 6, 8]`
2. **Check divisibility**:
   - `nums[0] = 2`: No smaller number exists → `is_divisible[0] = False`
   - `nums[1] = 4`: Can be divided by 2 → `is_divisible[1] = True`
   - `nums[2] = 6`: Can be divided by 2 → `is_divisible[2] = True`
   - `nums[3] = 8`: Can be divided by 2 → `is_divisible[3] = True`

3. **Count colors**: Only `nums[0] = 2` needs its own color
4. **Result**: `1` (all numbers can use the same color since they're all divisible by 2)

**Output:** `1`

---

**Another Example:**

4
2 3 4 9


- `2`: Not divisible by any smaller number → needs color 1
- `3`: Not divisible by any smaller number → needs color 2
- `4`: Divisible by 2 → can share color 1
- `9`: Divisible by 3 → can share color 2

**Output:** `2`

"""



def get_min_colors(nums):
    N = len(nums)
    is_divisible = [False] * N  # 用于记录每个数是否能被其他数整除
    color_count = 0  # 记录需要的颜色种数

    # 检查每个数是否能被其他数整除
    for i in range(N):
        for j in range(i + 1, N):
            if nums[j] % nums[i] == 0:
                is_divisible[j] = True
            elif nums[i] % nums[j] == 0:
                is_divisible[i] = True

    # 统计不需要被其他数整除的数的个数
    for i in range(N):
        if not is_divisible[i]:
            color_count += 1

    return color_count

# 读取输入的数据
N = int(input())
nums = list(map(int, input().split()))

# 调用函数计算最少需要的颜色种数
result = get_min_colors(nums)

# 输出结果
print(result)


