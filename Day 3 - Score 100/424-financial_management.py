"""
Here's the extracted problem statement, input/output format, and detailed steps to solve it:

---

### **Problem Statement**
You are given:
- `M`: the number of months available to complete all requirements.
- `requirements`: an array where `requirements[i]` represents the workload (in person-months) of the i-th requirement.

**Goal**: Assign requirements to months such that:
1. Each month can handle **at most 2 requirements**.
2. The total workload assigned to any month must not exceed the **monthly人力 (human resources)**.
3. All requirements must be completed within `M` months.

**Objective**: Find the **minimum monthly人力** needed to complete all requirements under these constraints.

---

### **Input/Output Format**

**Input:**
- First line: `M` (number of months)
- Second line: `requirements` (space-separated integers representing workload of each requirement)

**Output:**
- A single integer: the **minimum monthly人力** required.

---

### **Detailed Steps to Solve**

1. **Understand the Constraints**:
   - You can assign **at most 2 requirements per month**.
   - You must assign **all N requirements** across **M months**.
   - The monthly人力 must be **at least the sum of workloads** assigned to that month.
   - You want to **minimize the maximum monthly人力** across all months.

2. **Key Insight**:
   - Since each month can handle at most 2 requirements, you need at least `ceil(N / 2)` months.
   - If `M < ceil(N / 2)`, it’s **impossible** → return `-1` (though problem assumes feasible input).
   - To minimize the maximum monthly人力, **greedily pair large requirements with small ones** to balance the load.

3. **Algorithm**:
   - Sort `requirements` in **descending order**.
   - Use **two pointers** (or greedy pairing):
     - Pair the largest remaining requirement with the smallest remaining one (if possible).
     - If only one requirement left, assign it alone.
   - Track the **maximum sum** across all months → this is your answer.

4. **Example Walkthrough**:
   - Input: `M=3`, `requirements = [3, 2, 1, 4]`
   - Sort descending: `[4, 3, 2, 1]`
   - Month 1: 4 + 1 = 5
   - Month 2: 3 + 2 = 5
   - Month 3: (empty, but not needed since all assigned)
   - Answer: **5**

5. **Edge Cases**:
   - If `N == 0`: return `0`.
   - If `M == 1` and `N > 2`: impossible → return `-1` (if allowed by problem).

---

### **Why This Works**
- Pairing the largest with the smallest minimizes the maximum sum per month (greedy optimality).
- Sorting ensures we always try to balance the load.

Let me know if you’d like code in a specific language!
"""
def can_complete_in_time(tasks, M, P):
    # 计算任务的总数
    n = len(tasks)
    # 计算所有任务完成的掩码值，每个任务对应一个位
    all_tasks_mask = (1 << n) - 1
    # 初始化动态规划数组，每个元素是一个集合，用于存储每个月可以完成任务的状态
    dp = [set() for _ in range(M + 1)]
    # 第0月没有任务完成
    dp[0].add(0)

    # 遍历每个月
    for month in range(1, M + 1):
        # 遍历前一个月可能的任务完成状态
        for mask in dp[month - 1]:
            # 计算未完成的任务掩码
            submask = all_tasks_mask ^ mask
            # 开始尝试这个月可能完成的任务子集
            subset = submask
            while subset > 0:
                # 计算当前子集中的任务数和总工作量
                task_count = sum(1 for i in range(n) if subset & (1 << i))
                task_workload = sum(tasks[i] for i in range(n) if subset & (1 << i))
                # 如果当前子集的任务总工作量小于等于每月人力，并且任务数不超过2，则可以在这个月完成这些任务
                if task_workload <= P and task_count <= 2:
                    # 更新这个月的完成状态
                    new_mask = mask | subset
                    dp[month].add(new_mask)
                    # 如果所有任务都完成了，返回True
                    if new_mask == all_tasks_mask:
                        return True
                # 移动到下一个可能的子集
                subset = (subset - 1) & submask
    return False

def minimum_workforce(tasks, M):
    # 初始化人力范围，最小是单个任务的最大工作量，最大是所有任务总和
    low, high = max(tasks), sum(tasks)

    # 二分搜索最小人力
    while low < high:
        mid = (low + high) // 2
        # 检查中间值是否能在M个月内完成所有任务
        if can_complete_in_time(tasks, M, mid):
            high = mid
        else:
            low = low + 1

    return low

# 读取输入
M = int(input().strip())
tasks = list(map(int, input().strip().split()))

# 输出结果
print(minimum_workforce(tasks, M))




