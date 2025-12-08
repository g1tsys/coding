"""
# Chip Resource Allocation Problem - Translation and Walkthrough

## Problem Description

A business chip has a minimum capacity unit of 1.25G, with total capacity of M × 1.25G. The chip resources are numbered 1, 2, ..., M. The chip supports 3 different configurations:

- **Configuration A**: Occupies 1.25 × 1 = 1.25G (1 unit)
- **Configuration B**: Occupies 1.25 × 2 = 2.5G (2 units)
- **Configuration C**: Occupies 1.25 × 8 = 10G (8 units)

A board has N chips numbered 1, 2, ..., N. Each chip is independent - resources cannot span across chips.

**Goal**: Given N chips, capacity M per chip, and a user configuration sequence, output the resource occupation status of each chip while **minimizing the number of chips used**.

**Allocation Rules**:
- Allocate resources to chips in order (chip 1, then 2, etc.)
- Occupied resources marked as `1`, unoccupied as `0`
- If a configuration exceeds chip capacity, discard it and continue

## Input/Output Format

**Input**:
- M: Capacity per chip (1-256 units)
- N: Number of chips (1-32)
- Sequence: Configuration string (e.g., "ACABA"), max length 1000

**Output**:
- Resource occupation status for each chip (space-separated binary strings)


## Example Walkthrough

**Input**:

M = 10 (each chip has 10 units)
N = 2 (2 chips available)
Sequence = "ACABA"


**Step-by-step execution**:

1. **Initial state**:
   - Chip 1: `[0,0,0,0,0,0,0,0,0,0]` (10 free)
   - Chip 2: `[0,0,0,0,0,0,0,0,0,0]` (10 free)

2. **Process 'A'** (needs 1 unit):
   - Chip 1: `[1,0,0,0,0,0,0,0,0,0]` (9 free)

3. **Process 'C'** (needs 8 units):
   - Chip 1: `[1,1,1,1,1,1,1,1,1,0]` (1 free)

4. **Process 'A'** (needs 1 unit):
   - Chip 1: `[1,1,1,1,1,1,1,1,1,1]` (0 free - FULL)

5. **Process 'B'** (needs 2 units):
   - Chip 1 full, try Chip 2
   - Chip 2: `[1,1,0,0,0,0,0,0,0,0]` (8 free)

6. **Process 'A'** (needs 1 unit):
   - Chip 2: `[1,1,1,0,0,0,0,0,0,0]` (7 free)

**Output**:

1 1 1 1 1 1 1 1 1 1
1 1 1 0 0 0 0 0 0 0


This solution ensures chips are filled sequentially, minimizing the total number of chips used.



"""


def allocate_resources(M, N, sequence):
    # 初始化每块芯片的资源占用情况列表
    chip_allocations = [['0'] * M for _ in range(N)]

    # 初始化每块芯片的剩余容量列表
    chip_capacities = [M] * N

    # 遍历用户配置序列
    for config in sequence:
        # 根据配置的类型确定资源占用量
        if config == 'A':
            allocation = 1
        elif config == 'B':
            allocation = 2
        elif config == 'C':
            allocation = 8

        # 在每块芯片中查找可用的位置来分配资源
        allocated = False
        for chip_index in range(N):
            # 如果当前芯片的剩余容量足够，则分配资源
            if chip_capacities[chip_index] >= allocation:
                start_index = M - chip_capacities[chip_index]
                for i in range(start_index, start_index + allocation):
                    chip_allocations[chip_index][i] = '1'
                chip_capacities[chip_index] -= allocation
                allocated = True
                break

        # 如果无法在任何芯片上分配资源，则丢弃该配置
        if not allocated:
            continue

    # 将每块芯片的资源占用情况转换为字符串
    chip_allocations = [''.join(chip) for chip in chip_allocations]

    return chip_allocations


# 读取输入
M = int(input())  # 每块芯片容量
N = int(input())  # 每块板卡上芯片数量
sequence = input()  # 用户配置序列

# 调用函数进行资源分配
result = allocate_resources(M, N, sequence)

# 输出结果
for allocation in result:
    print(allocation)

