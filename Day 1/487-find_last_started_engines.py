"""
> **Question Translation:**
The *Wandering Earth* plan has uniformly deployed N thrusters along the equator, numbered from 0 to N-1 in order of their positions. Initially, all thrusters are in an unstarted state. There are two ways to start a thruster: "manual start" and "associated start." If a thruster is started manually at time T, the two adjacent thrusters will be automatically started at time T+1. If a thruster is already started, no action is needed. Thruster 0 and thruster N-1 are considered adjacent. The Earth Union Government plans to manually start certain thrusters at certain times, and eventually, all thrusters will be started. Which thrusters are the last to be started?

> **Input:**  
The first line contains two numbers N and E, separated by a space.  
N represents the total number of thrusters, and E represents the total number of manually started thrusters.  
The next E lines each contain two numbers T and P, separated by a space. T represents the manual start time, and P represents the position of the thruster.  

> **Output:**  
The first line is a number N, representing the number of thrusters that were last to be started.  
The second line contains N numbers in ascending order, representing the positions of the last-started thrusters.

---

### **Python Solution Chain of Thoughts**

1. **Understand the problem logic:**
   - Manual starts at time T will cause adjacent thrusters to be automatically started at time T+1.
   - Each thruster has a start time, and we need to find the thrusters with the **maximum** start time.

2. **Data Structures:**
   - Use a list or array to store the start time of each thruster. Initially, all values are set to -1 (unstarted).
   - Use a queue to process the manual starts and propagate the associated starts.

3. **Steps:**
   - Initialize a list `start_time` of size N, initialized to -1.
   - Initialize a queue with the manually started thrusters. Each entry in the queue will be a tuple: (time, position).
   - For each entry in the queue:
     - If the thruster is already started, skip it.
     - Otherwise, set its start time to the current time.
     - Enqueue the adjacent thrusters with time = current time + 1.
   - After processing, find the maximum start time and collect all thrusters with that time.

4. **Edge Cases:**
   - The engine list is circular (thruster 0 is adjacent to thruster N-1).
   - Multiple manual starts may affect the same thruster.

---

### **Example Walkthrough**

**Input:**

5 2
0 0
1 2


**Step-by-Step Explanation:**

1. **Initialize:**
   - `start_time = [-1, -1, -1, -1, -1]`
   - Queue = [(0, 0), (1, 2)]

2. **Process (0, 0):**
   - Set `start_time[0] = 0`
   - Enqueue (1, 4) and (1, 1) (adjacent thrusters to 0)

3. **Process (1, 2):**
   - Set `start_time[2] = 1`
   - Enqueue (2, 1) and (2, 3) (adjacent thrusters to 2)

4. **Process (1, 4):**
   - Set `start_time[4] = 1`
   - Enqueue (2, 3) and (2, 0) (adjacent thrusters to 4)

5. **Process (1, 1):**
   - Already started (start_time[1] = -1 → no action)

6. **Process (2, 1):**
   - Set `start_time[1] = 2`
   - Enqueue (3, 0) and (3, 2)

7. **Process (2, 3):**
   - Set `start_time[3] = 2`
   - Enqueue (3, 2) and (3, 4)

8. **Continue processing...**

9. **Final start_time = [0, 2, 1, 2, 1]**

10. **Find the maximum start time (2) and collect positions:**
    - Positions with start time 2: [1, 3]

**Output:**

2
1 3

"""


def find_last_started_engines(N, E, start_info):
    # 初始化一个列表用于存储每个发动机的启动时刻，初始时刻设为无穷大
    start_times = [float('inf')] * N
    
    # 遍历手动启动信息，更新对应发动机的启动时刻
    for T, P in start_info:
        # 确保如果同一个发动机有多个启动时刻时，只保留最早的
        start_times[P] = min(start_times[P], T)
    
    # 创建一个待处理列表，按启动时刻排序
    to_process = sorted(start_info, key=lambda x: x[0])
    
    # 模拟启动过程
    while to_process:
        # 从队列中取出一个待处理的启动事件
        T, P = to_process.pop(0)
        
        # 计算相邻发动机的位置，注意循环连接
        left = (P - 1) % N
        right = (P + 1) % N
        
        # 检查并更新左侧相邻发动机的启动时刻
        if start_times[left] > T + 1:
            start_times[left] = T + 1
            # 将更新后的相邻发动机加入待处理队列
            to_process.append((T + 1, left))
        
        # 检查并更新右侧相邻发动机的启动时刻
        if start_times[right] > T + 1:
            start_times[right] = T + 1
            # 将更新后的相邻发动机加入待处理队列
            to_process.append((T + 1, right))
    
    # 找出启动时刻的最大值
    max_time = max(start_times)
    
    # 找出所有在最大启动时刻启动的发动机
    last_started_engines = [i for i in range(N) if start_times[i] == max_time]
    
    # 输出这些发动机的数量
    print(len(last_started_engines))
    # 输出这些发动机的位置编号，按升序排列
    print(" ".join(map(str, sorted(last_started_engines))))

# 读取输入，N表示发动机数量，E表示手动启动事件数量
N, E = map(int, input().split())
# 读取每个手动启动事件的时刻和发动机编号
start_info = [tuple(map(int, input().split())) for _ in range(E)]

# 计算并输出最后启动的发动机
find_last_started_engines(N, E, start_info)

