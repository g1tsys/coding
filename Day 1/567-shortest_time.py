"""
> **Question Translation (Task Optimal Scheduling):**  
Given a list of positive integers representing tasks to be executed by a system, where each element represents a task type, calculate the minimum time required to complete all tasks.

**Task Execution Rules:**
1. Tasks can be executed in any order, and each task takes 1 time unit to execute.
2. There must be a cooling period of N time units between two tasks of the same type. For example, if a task of type 3 is executed at time K, then it cannot be executed again at time K+1 or K+2 if N is 2.
3. The system can execute one task or remain idle in any time unit.

**Input:**  
- The first line is an array of integers (separated by commas) representing the list of tasks. The length of the array is at most 1000.
- The second line is the cooling time N (a positive integer, N ≤ 100).

**Output:**  
- Output the minimum time required to complete all tasks.

---

> **Python Thought Process (Translation):**  
1. Traverse the task list and use a dictionary (`task_count`) to count the occurrences of each task type.
2. Find the maximum number of occurrences (`max_count`) of any task type.
3. Calculate the minimum time required using the formula:  
   `(max_count - 1) * (N + 1) + task_count_max`,  
   where `task_count_max` is the number of task types that have the maximum occurrence.
4. Compare the total number of tasks with the calculated minimum time. If the total number of tasks is greater than the minimum time, return the total number of tasks. Otherwise, return the calculated minimum time.

---

> **Example Walkthrough (Sample Input):**  
Let’s say the input is:  
- Task list: `[1, 1, 2, 2, 3]`  
- Cooling time: `N = 2`

**Step-by-step process:**
1. Count the occurrences:  
   - Task 1 appears 2 times  
   - Task 2 appears 2 times  
   - Task 3 appears 1 time  
   - So, `task_count = {1: 2, 2: 2, 3: 1}`

2. The maximum occurrence is `2` (for tasks 1 and 2), and `task_count_max = 2`.

3. Calculate the minimum time:  
   `(2 - 1) * (2 + 1) + 2 = 1 * 3 + 2 = 5`

4. Total number of tasks = 5  
   Since 5 = 5, the result is `5`.

**Output:** `5`
"""
def shortestTime(tasks, N):
    # 统计每个任务的出现次数
    task_count = {}
    for task in tasks:
        if task in task_count:
            task_count[task] += 1
        else:
            task_count[task] = 1
    
    # 找出出现次数最多的任务和出现次数
    max_count = max(task_count.values())
    task_count_max = sum(1 for count in task_count.values() if count == max_count)
    
    # 计算至少需要的时间
    min_time = (max_count - 1) * (N + 1) + task_count_max
    
    # 如果任务的总数大于了最小时间，那么总时间就是任务的总数
    return max(len(tasks), min_time)


# 获取输入
tasks = input().split(",")
N = int(input())

# 转换任务列表中的元素为整数
tasks = [int(task) for task in tasks]

# 调用函数计算最短时间
min_time = shortestTime(tasks, N)

# 输出最短时间
print(min_time)


