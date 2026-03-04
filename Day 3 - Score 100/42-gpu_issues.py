"""
Problem Description
To fully utilize the GPU's [computing power], we need to assign as many tasks as possible to the GPU for execution. Now, there is a task array where each element represents the number of new tasks added in that second, and new tasks are added every second.

Assume that the GPU can execute at most n tasks at a time, and each execution takes 1 second. Under the condition that the GPU is not idle, what is the minimum time required to complete all tasks?

Input and Output
Input
The first parameter is the maximum number of tasks the GPU can execute at a time, with a value range of 1 to 100000.
The second parameter is the length of the task array, with a value range of [1, 10000].
The third parameter is the task array, where the numbers range from 1 to 10000.
Output
The minimum number of seconds required to complete all tasks.

输入
3
5
1 2 3 4 5

输出
6

说明:
一次最多执行3个任务，最少耗时6s


CPytnon Q ANHTMLOGERERSTRING
1. First, obtain the input number of tasks and time through the input() function.
2. Use the input().split() function to get the input task array, and convert the elements in the array to integers through map(int;....), then store them in the task_array list.
3. Initialize a variable named flag to 0, which is used to store the remainder.
4. For each task current_task in the task array task_array, perform the following operations:
Copy
python
1Al write code
Update the value of flag to (current_task + flag) - task_num, which represents the number of remaining tasks after completing the current task. If the result is small
This operation is equivalent to adding the remaining number of the previous task to the number of the current task, then subtracting the total number of tasks to get the remaining tasks after completing the current task.
2
5. After iterating through the task array, process the remainder flag through a loop:
● Al write code
Copy
python
1
If flag is greater than 0, it means there are remaining tasks to be processed.
2
Update the value of flag to flag - task_num, which represents the new remainder after processing the remaining tasks; if the result is less than 0, set it to
3
4
5
Increase the value of time, which represents the time consumed after processing a round of tasks.
6. Finally, output the value of the variable time, which is the minimum time required to complete all tasks.
"""

def calc_time():
    task_num = int(input())  # 输入任务个数
    time = int(input())  # 输入时间

    task_array = list(map(int, input().split()))  # 输入任务数组并转换为整数列表

    flag = 0  # 余数

    for current_task in task_array:
        flag = max((current_task + flag) - task_num, 0)  # 更新余数

    while flag > 0:
        flag = max(flag - task_num, 0)  # 更新余数
        time += 1  # 增加时间

    print(time)  # 输出最少需要的时间

calc_time()


