"""
The question is as follows:

---

### 🎃 Problem Description

Given a positive integer array `nums` (with a maximum of 100 elements), find the **minimum number of steps** to go from the **first element** to the **last element** of the array.

### 🎃 Requirements

1. The **first step** must start from the **first element**, and the **step size** must be between `1` and `len(nums)/2` (not inclusive of `len(nums)/2`).
2. From the **second step onward**, you can only move **exactly** the number of steps equal to the value of the current element you're on.
3. You can only move **toward the end** of the array (no backward movement).
4. If the destination is unreachable, return `-1`.

### 🎃 Input and Output

- **Input**: A list of positive integers separated by spaces.
- **Output**: A **positive integer** representing the **minimum number of steps** needed to reach the end. If it is **not possible**, return `-1`.

---

### 🎈 Python Language Thought Process

1. **Input Handling**:
   - Read the input as a list of integers.
   - Parse the array length `len(nums)`.

2. **Special Case Handling**:
   - If the array has only one element, return `0` (no steps needed).

3. **Breadth-First Search (BFS) Setup**:
   - Use a **queue** to track the current index and steps taken.
   - Use a **visited set** to avoid revisiting the same index.

4. **Step 1 (Initial Step)**:
   - From the first index, try all valid step sizes (from `1` to `len(nums)//2`).
   - Add these positions to the queue, with a step count of `1`.

5. **BFS Execution**:
   - While the queue is not empty:
     - Dequeue the current index and step count.
     - If the current index is the last index, return the step count.
     - Otherwise, move exactly the number of steps equal to the value at the current index.
     - If the new index is within bounds and not visited, enqueue it with step count + 1.

6. **Termination**:
   - If the queue is empty and the last index is not reached, return `-1`.

---

### 🎉 Example Walkthrough

#### Input:

[2, 3, 1, 1, 4]

#### Step-by-Step:

1. **Start at index 0** (value = 2).
   - Step sizes allowed: 1 (since `len(nums) = 5`, `len(nums)//2 = 2`, so 1 is the only valid step size).
   - Move to index `0 + 2 = 2` (value = 1).
   - Step count = 1.

2. **Now at index 2** (value = 1).
   - Move exactly 1 step to index `2 + 1 = 3` (value = 1).
   - Step count = 2.

3. **Now at index 3** (value = 1).
   - Move exactly 1 step to index `3 + 1 = 4` (last index).
   - Step count = 3.

#### Output:
3
"""


from collections import deque  # 导入deque，一个双端队列，可以从两端高效地添加或删除元素

def minimum_steps(nums):
    n = len(nums)  # 计算输入数组nums的长度
    if n < 2:  # 如果数组长度小于2，则不可能进行任何有效的移动
        return -1  # 直接返回-1表示不可达

    max_first_step = n // 2  # 根据题目要求计算第一步的最大步长，即数组长度的一半

    queue = deque()  # 创建一个双端队列用来存储探索的状态

    for i in range(1, max_first_step):  # 从1到max_first_step - 1循环，尝试所有合法的第一步长
        queue.append((i, 1))  # 将第一步达到的位置和步数（1步）加入队列

    visited = set()  # 创建一个集合，用来记录已经访问过的位置，防止重复访问

    while queue:  # 当队列不为空，继续循环
        current, steps = queue.popleft()  # 从队列中取出一个元素，包含当前位置和已走的步数

        next_step = current + nums[current]  # 计算下一步的目标位置
        if next_step == n - 1:  # 如果下一步正好走到了数组的最后一个元素
            return steps + 1  # 返回当前步数+1（因为这一步成功到达末尾）
        if next_step < n and next_step not in visited:  # 如果下一步的位置在数组内并且未被访问过
            visited.add(next_step)  # 将这个位置加入到访问过的集合中
            queue.append((next_step, steps + 1))  # 将这个新位置和步数加入队列以便继续探索

    return -1  # 如果所有可能都探索完毕仍未能到达数组末尾，返回-1表示不可达

nums1 = list(map(int, input().split()))  # 从标准输入读取一行数字，按空格分隔并转换为整数列表
print(minimum_steps(nums1))  # 调用函数并打印结果



