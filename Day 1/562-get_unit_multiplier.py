"""
# Disk Capacity Sorting Problem
## Problem Description

Disk capacity commonly uses three units: M, G, and T, with the following conversion relationships:
- 1T = 1024G
- 1G = 1024M

Given n disks with their capacities, sort them in ascending order (stable sort). 

**Example:** Given 5 disks with capacities: `1T`, `20M`, `3G`, `10G6T`, `3M12G9M`
- Sorted result: `20M`, `3G`, `3M12G9M`, `1T`, `10G6T`

**Note:** Units can appear multiple times. For example, `3M12G9M` means 3M + 12G + 9M (equivalent to `12M12G`).

## Input/Output

**Input:**
- First line: integer n (2 ≤ n ≤ 100), number of disks
- Next n lines: each contains a string (length 2-30) representing disk capacity
- Format: one or more substrings like "mv" where m is size (1-1024) and v is unit (M, G, or T)

**Output:**
- n lines showing sorted disk capacities

## Solution Approach

### Key Steps:

1. **Parse capacity strings**: Extract all number-unit pairs from each capacity string (e.g., "3M12G9M" → 3M, 12G, 9M)
2. **Convert to base unit**: Convert all capacities to the same unit (e.g., megabytes)
   - M → multiply by 1
   - G → multiply by 1024
   - T → multiply by 1024 x 1024

3. **Sort by total capacity**: Use stable sort to maintain original order for equal values
4. **Output original strings**: Print the original capacity strings in sorted order

## Example Walkthrough

**Input:**

3
1T
20M
3G


**Step-by-step:**

1. **Parse and convert each disk:**
   - `1T` → 1 x 1024 x 1024 = 1,048,576 M
   - `20M` → 20 x 1 = 20 M
   - `3G` → 3 x 1024 = 3,072 M

2. **Sort by converted values:**
   - 20 M (smallest)
   - 3,072 M (middle)
   - 1,048,576 M (largest)

3. **Output original strings:**
   
   20M
   3G
   1T
   

**Complex Example:**

Input: 3M12G9M
Parse: 3M + 12G + 9M
Convert: (3 x 1) + (12 x 1024) + (9 x 1) = 3 + 12,288 + 9 = 12,300 M


## Algorithm Summary


For each disk capacity string:
  1. Extract all number-unit pairs using regex or character parsing
  2. For each pair (number, unit):
     - Convert to base unit (M)
     - Add to total capacity
  3. Store (original_string, total_capacity)
  
Sort all disks by total_capacity (stable sort)
Output original strings in sorted order
"""


# 定义磁盘容量的类
class Disk:
    def __init__(self, capacity):
        self.capacity = capacity  # 容量字符串
        self.converted_capacity = 0  # 转换为统一单位的容量数值

# 根据单位字符返回对应的容量单位数值
def get_unit_multiplier(unit):
    if unit == 'M':
        return 1
    elif unit == 'G':
        return 1024
    elif unit == 'T':
        return 1024 * 1024
    else:
        return 0  # 无效的单位字符

# 将容量字符串转换为统一单位的容量数值
def convert_to_capacity(capacity):
    total_capacity = 0
    unit = 'M'
    i = 0
    len_capacity = len(capacity)

    while i < len_capacity:
        j = i
        while j < len_capacity and capacity[j].isdigit():
            j += 1
        value = int(capacity[i:j])
        unit = capacity[j]
        total_capacity += value * get_unit_multiplier(unit)
        i = j + 1

    return total_capacity

# 比较函数，用于排序
def compare_disk(diskA, diskB):
    # 比较容量数值
    if diskA.converted_capacity < diskB.converted_capacity:
        return -1
    elif diskA.converted_capacity > diskB.converted_capacity:
        return 1
    else:
        # 容量数值相等时，根据单位字符的 ASCII 值进行比较
        return ord(diskA.capacity[-1]) - ord(diskB.capacity[-1])

n = int(input())

disks = []

for _ in range(n):
    capacity = input().strip()
    disk = Disk(capacity)
    disk.converted_capacity = convert_to_capacity(capacity)
    disks.append(disk)

# 使用稳定排序函数对磁盘容量进行排序
sorted_disks = sorted(disks, key=lambda x: (x.converted_capacity, ord(x.capacity[-1])))

# 输出排序结果
for disk in sorted_disks:
    print(disk.capacity)


