"""
# Project Scheduling Problem - Translation and Explanation

## Problem Description

A project team has **N developers**, and the project manager receives **M independent requirements**. Each requirement has different workload, and each requirement can only be completed by one developer independently (no collaboration). Assuming no dependencies between requirements, design an algorithm to help the project manager arrange work so the entire project can be delivered in the minimum time.

## Input/Output

**Input:**
- Line 1: M requirements' workloads in days, comma-separated (e.g., X1, X2, X3... Xm)
  - Constraints: 0 < M < 30, 0 < Xm < 200
- Line 2: Number of developers N
  - Constraint: 0 < N < 10

**Output:**
- Minimum days to complete all work

## Python Approach (Backtracking)

**Key Ideas:**

1. **Sort tasks in descending order** - Assign larger tasks first to balance workload better
2. **Track each developer's total workload** - Use a list of size N, initialized to 0
3. **Use backtracking** - Try assigning each task to each developer and find the optimal solution
4. **Pruning optimization** - If current max workload exceeds known minimum, stop exploring that branch

## Python Code with Example

```python
def min_project_time(tasks, n):
    # Sort tasks in descending order (largest first)
    tasks.sort(reverse=True)
    
    # Track each developer's total workload
    developers = [0] * n
    min_time = float('inf')
    
    def backtrack(task_index):
        nonlocal min_time
        
        # Base case: all tasks assigned
        if task_index == len(tasks):
            min_time = min(min_time, max(developers))
            return
        
        # Pruning: if current max already exceeds min_time, stop
        if max(developers) >= min_time:
            return
        
        # Try assigning current task to each developer
        for i in range(n):
            developers[i] += tasks[task_index]  # Assign task
            backtrack(task_index + 1)           # Recurse
            developers[i] -= tasks[task_index]  # Backtrack
    
    backtrack(0)
    return min_time

# Example usage
tasks_input = "6,2,7,7,9"
n = 3

tasks = list(map(int, tasks_input.split(',')))
result = min_project_time(tasks, n)
print(f"Minimum completion time: {result} days")
```

## Example Walkthrough

**Input:**
- Tasks: `6, 2, 7, 7, 9` (days)
- Developers: `3`

**Step-by-step:**

1. **Sort tasks:** `[9, 7, 7, 6, 2]` (descending)

2. **Initial state:** `developers = [0, 0, 0]`

3. **Backtracking process:**
   - Assign task 9 → Developer 0: `[9, 0, 0]`
   - Assign task 7 → Developer 1: `[9, 7, 0]`
   - Assign task 7 → Developer 2: `[9, 7, 7]`
   - Assign task 6 → Developer 1: `[9, 13, 7]`
   - Assign task 2 → Developer 2: `[9, 13, 9]`
   - **Max workload = 13 days**

4. **Try other combinations...**
   - Optimal: Developer 0: `[9, 2]` = 11, Developer 1: `[7, 6]` = 13, Developer 2: `[7]` = 7
   - **Best result: 13 days**

**Output:** `13`

## Time Complexity

- **Worst case:** O(N^M) - trying N developers for M tasks
- **With pruning:** Significantly faster in practice
- **Alternative approach:** Use priority queue (greedy) for O(M log N) but may not always find optimal solution
"""



# 解法在面对大数据的时候,算法复杂度较高,大家记得优化一下
# 定义分配任务的函数，接受任务工作量列表和员工数量作为参数
def distributeTasks(workloads, N):
    # 首先将工作量列表从大到小排序，这样可以先分配大任务，尽可能平衡每个人的工作量
    workloads.sort(reverse=True)
    # 初始化一个列表，记录每个员工的总工作量
    employee_hours = [0] * N
    # 设置一个变量记录目前找到的最短完成时间，初始化为无穷大
    min_time = float('inf')

    # 定义回溯函数，用于递归地尝试所有的分配方案
    def backtrack(i):
        # 使用nonlocal声明，使得可以在此函数内修改外层函数的变量
        nonlocal min_time
        # 如果已经分配完所有任务，则更新最短完成时间
        if i == len(workloads):
            min_time = min(min_time, max(employee_hours))
            return
        # 如果当前的最大工作量已经超过了目前的最短完成时间，则不需要继续尝试
        if max(employee_hours) > min_time:
            return

        # 遍历每个员工，尝试将当前任务分配给他们
        for j in range(N):
            employee_hours[j] += workloads[i]  # 将当前任务分配给员工j
            backtrack(i+1)  # 递归调用，继续分配下一个任务
            employee_hours[j] -= workloads[i]  # 回溯，撤销当前任务的分配，尝试其他分配方案

    # 从第一个任务开始分配
    backtrack(0)
    # 返回所有方案中的最短完成时间
    return min_time


# 主函数
if __name__ == "__main__":
    # 读取输入的任务工作量和员工数量
    workloads_input = input()
    N_input = input()

    # 将输入的任务工作量字符串分割并转换成整数列表
    workloads = [int(x) for x in workloads_input.split()]
    # 将输入的员工数量转换成整数
    N = int(N_input)

    # 调用函数并打印结果
    print(distributeTasks(workloads, N))

