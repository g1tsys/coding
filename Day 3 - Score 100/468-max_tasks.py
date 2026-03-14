"""
题目描述
在某个项目中有多个任务(用tasks数组表示)需要您进行处理，其中tasks[=[si，ei，你可以在si=day<=ei中的任意一天处理该任务:请返回你可以处理的最大任务数
注:一天可以完成一个任务的处理
输入输出Q
输入
第一行为任务数量n，1<=n=100000，后面n行表示各个任务的开始时间和终止时间，用si和ei表示，1= si=ei<=100000
输出
输出为一个整数，表示可以处理的最大任务数

输入
3
1 1 
1 2 
1 3


输出
3

说明:
第一天处理任务1,第二天处理任务2,第三天处理任务3

输入
3
1 1 
1 1
1 1


输出
1

Python四语言思路
1.首先，将任务列表按照开始时间进行排序，确保按照开始时间的顺序处理任务。
2.初始化变量:total_days为任务列表中的最大结束时间，task_idx为任务列表的索引,current_day为当前处理的天数，max_tasks为可以处理的最大任务数，available_tasks为可执行任务的优先队列(使用堆实现，按照结束时间从小到大排列)。
3.在每一天，将当天开始的任务加入到可执行任务队列中:
。遍历任务列表，将开始时间小于等于当前天数的任务的结束时间加入到可执行任务队列中。
。 更新任务列表索引，指向下一个未加入可执行任务队列的任务。4.移除已经过期的任务:
。从可执行任务队列中移除结束时间小于当前天数的任务，确保只保留还未结束的任务。5.如果可执行任务队列中有任务，则执行任务:
。 从可执行任务队列中弹出结束时间最小的任务，即执行该任务。
。 更新已处理任务数，max_tasks加1。
6.处理下一天的任务，current_day加1。
7.重复步骤3-6，直到遍历完所有的天数。
8.返回最大任务数，即max_tasks。
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


