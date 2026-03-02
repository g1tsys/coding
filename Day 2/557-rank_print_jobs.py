"""
### Problem Description
A printer executes tasks according to a print queue. Print tasks have nine priority levels, represented by the digits 1-9, where a higher number indicates a higher priority.

The printer operates as follows:
1. It takes the first task `A` from the head of the queue.
2. It then checks if there are any tasks remaining in the queue with a **higher priority** than `A`.
3. If such tasks exist, `A` is moved to the end of the queue.
4. If no such tasks exist, task `A` is executed.

Please write a program that, given the print queue, outputs the actual execution order of the tasks.

---

### Input and Output

#### Input
A single line containing the priority levels of the tasks in the print queue, separated by spaces. The priority values range from 1 to 9.

#### Output
A single line containing the print order of each task, starting from 0, separated by commas.

---

Would you like me to also translate the corresponding solution approach for this problem?


# Python Language Approach
1.  **Understand the problem**: We need to simulate the printer's workflow. Tasks are printed in order of priority from highest to lowest. If the current task's priority is not the highest, it is moved to the end of the queue until it becomes the highest priority task.
2.  **Use a queue and a max-heap**: We use a standard queue (FIFO) to simulate the print queue, and a max-heap (using Python's `heapq` module) to quickly find the current highest-priority task.
3.  **Initialize the queue and heap**:
    *   The queue stores the priority of each task.
    *   The max-heap stores the priority of each task along with its initial position in the queue. We take the negative of the priority values to implement a max-heap (since `heapq` defaults to a min-heap).
4.  **Process the print tasks**:
    *   Dequeue the task from the head of the queue.
    *   Pop the highest-priority task from the max-heap.
    *   If the priority of the dequeued task is the same as the highest priority, record its print order.
    *   If the priorities are different, enqueue the current task back to the end of the queue and continue processing the next task.
5.  **Output the result**: Finally, output the recorded print order for each task.

---

Would you like me to also provide the full Python code implementation for this problem?


"""


import heapq  # 导入堆队列模块

def print_sort(input_str):
    s = input_str.split(',')  # 将输入字符串按照逗号分割成列表
    nums = [int(num) for num in s]  # 将字符串列表转换为整数列表

    queue = []  # 用于存储打印任务的队列
    prior = []  # 用于存储任务优先级的最大堆

    for i, num in enumerate(nums):
        queue.append(num)  # 将任务加入队列
        heapq.heappush(prior, (-num, i))  # 将任务优先级和索引作为元组加入最大堆，优先级取负数以实现最大堆

    res = [0] * len(nums)  # 初始化结果列表，长度与任务列表相同
    index = 0  # 用于记录打印顺序的索引

    while queue:
        poll1 = queue.pop(0)  # 从队列头部取出一个任务
        poll2 = heapq.heappop(prior)  # 从堆中取出优先级最高的任务

        if poll1 == -poll2[0]:  # 如果队列头部任务的优先级与堆中最高优先级相同
            res[poll2[1]] = index  # 记录该任务的打印顺序
            index += 1  # 更新打印顺序的索引
        else:
            queue.append(poll1)  # 将优先级较低的任务放回队列尾部
            heapq.heappush(prior, poll2)  # 将堆中取出的任务重新放回堆中

    print(','.join(map(str, res)))  # 输出最终的打印顺序

input_str = input()  # 接收输入字符串
print_sort(input_str)  # 调用函数进行处理并输出结果

