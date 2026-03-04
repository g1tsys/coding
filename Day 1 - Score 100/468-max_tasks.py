"""
Based on the web page content, here's a translation and explanation of the problem:

## Problem Translation

**Title:** Maximum Number of Tasks That Can Be Processed

**Description:**
In a project, there are multiple tasks (represented by a `tasks` array) that need to be processed. Each task is represented as `tasks[i] = [si, ei]`, where you can process the task on any day within the range `si <= day <= ei`. Return the maximum number of tasks you can process.

**Note:** Only one task can be completed per day.

**Input:**
- First line: number of tasks `n` (1 ≤ n ≤ 100,000)
- Next `n` lines: start time `si` and end time `ei` for each task (1 ≤ si ≤ ei ≤ 100,000)

**Output:**
- An integer representing the maximum number of tasks that can be processed

## Solution Approach (General Strategy)

This is a **greedy interval scheduling problem**. The key insight is:

1. **Sort tasks by their end time** (earliest deadline first)
2. **Greedily select tasks** that don't conflict with previously scheduled tasks
3. Track which days are already occupied
4. For each task, try to schedule it on the latest available day within its time window

## Example Walkthrough

**Example Input:**
```
3
1 2
2 3
1 3
```

**Step-by-step:**
1. Tasks: [1,2], [2,3], [1,3]
2. Sort by end time: [1,2], [2,3], [1,3]
3. Process task [1,2]: Schedule on day 2 → Tasks completed: 1
4. Process task [2,3]: Day 2 is taken, schedule on day 3 → Tasks completed: 2
5. Process task [1,3]: Days 2,3 taken, schedule on day 1 → Tasks completed: 3

**Output:** 3 (all tasks can be completed)

The greedy approach works because scheduling tasks as late as possible within their windows maximizes flexibility for future tasks.

"""


import heapq
def maxTasks(tasks):
    # 首先，将任务按开始时间排序
    tasks.sort(key=lambda x: x[0])
    total_days = max(task[1] for task in tasks)  # 获取最大的结束时间作为遍历的天数边界
    task_idx = 0  # 用于遍历tasks列表的索引
    current_day = 1  # 当前天数
    max_tasks = 0  # 可以处理的最大任务数
    available_tasks = []  # 可执行的任务队列，按照结束时间从小到大排列
    
    while current_day <= total_days:
        # 将当天开始的所有任务加入到可执行任务队列中
        while task_idx < len(tasks) and tasks[task_idx][0] <= current_day:
            # 将任务的结束时间加入优先队列，Python的heapq默认是小根堆，因此直接按结束时间排序即可
            heapq.heappush(available_tasks, tasks[task_idx][1])
            task_idx += 1
        
        # 移除已经过期的任务（结束时间小于当前天数的任务）
        while available_tasks and available_tasks[0] < current_day:
            heapq.heappop(available_tasks)
        
        # 如果有可以执行的任务，则执行任务（优先队列中结束时间最小的任务）
        if available_tasks:
            heapq.heappop(available_tasks)  # 执行任务，即弹出最小结束时间的任务
            max_tasks += 1  # 已处理任务数加1
        
        current_day += 1  # 处理下一天的任务
    
    return max_tasks

# 输入处理
n = int(input().strip())  # 任务数量
tasks = [list(map(int, input().strip().split())) for _ in range(n)]

# 计算可以处理的最大任务数
max_tasks_result = maxTasks(tasks)
print(max_tasks_result)


