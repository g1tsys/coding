"""
**题目输入：**
- 第一行：一个整数 `N`（任务数量，1 ≤ N ≤ 100）
- 第二行：一个整数 `T`（可用处理时间，1 ≤ T ≤ 100）
- 接下来 `N` 行：每行两个空格分隔的整数 `SLA`（最晚处理时间，1 ≤ SLA ≤ 100）和 `V`（积分值，0 ≤ V ≤ 100000）

**题目输出：**
- 一个整数，表示在有限时间内可获得的**最多积分**。

```text
1. 读取任务的数量和可用处理时间。
2. 读取每个任务的最晚处理时间和对应的积分，并将其存储为元组的列表。
3. 根据最晚处理时间对任务进行排序。
4. 初始化积分分为0，并创建一个用于记录任务是否已经处理的列表。
5. 对于每个可用的时间单位，遍历所有任务，找到可以在当前时间处理且积分最高的任务，并标记已处理，增加对应的积分。
6. 输出最多可获得的积分。
```
"""

# 读取任务数量和可用处理时间
N = int(input().strip())
T = int(input().strip())

# 读取任务信息，并存储为元组的列表
tasks = []
for _ in range(N):
    SLA, V = map(int, input().split())
    tasks.append((SLA, V))

# 根据最晚处理时间对任务进行排序
tasks.sort(key=lambda x: x[0])

# 初始化积分
total_score = 0

# 初始化一个用于记录任务是否已经处理的列表
processed = [False] * N

# 对于每个可用的时间单位，从后往前查找最优的任务处理
for time in range(T, 0, -1):
    # 初始化用于选择当前时间点的任务的变量
    idx = -1
    max_score = 0
    for i in range(N):
        # 如果当前任务可以在当前时间处理，并且积分高于已记录的最高积分，且未被处理
        if tasks[i][0] >= time and tasks[i][1] > max_score and not processed[i]:
            idx = i
            max_score = tasks[i][1]
    # 如果找到了合适的任务，处理它
    if idx != -1:
        processed[idx] = True  # 标记为已处理
        total_score += max_score  # 增加积分

# 输出最多可获得的积分
print(total_score)
