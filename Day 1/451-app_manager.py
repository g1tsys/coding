"""


Since the Python code section is missing from the web page content you provided, I'll help you understand the problem and provide a **Python solution** from scratch, along with a **walkthrough** using an example.

---

### 📌 Problem Translation (Phone App Anti-Addiction System)

**Problem Description:**

Smartphones have made our lives convenient but also consumed a lot of our time. The "Phone App Anti-Addiction System" helps us reasonably plan our phone app usage time and do the right thing at the right time.

The system works like this:

1. In a 24-hour period, each app can be registered for allowed usage time slots.
2. Only one app can be used in a time slot — no overlapping.
3. Apps have a priority level (1-5, higher = more important). If a high-priority app's time slot overlaps with a low-priority app, the low-priority app's slot is automatically canceled.
4. If two apps have the same priority, the one added later cannot be registered.
5. An app can have multiple time slots in a day.

**Input:**

- First line: Number of apps `N` (N ≤ 100)
- Next `N` lines: Each line contains the app's name, priority, start time, and end time (in `HH:MM` format)
- Last line: A query time (in `HH:MM` format)

**Output:**

- Return the name of the app that is available at the query time.
- If no app is available, return `"NA"`

---

### 🔍 Python Solution Chain of Thoughts

1. **Parse Input:**
   - Read the number of apps `N`.
   - Read `N` lines of app registration data.
   - Read the query time.

2. **Store App Data:**
   - Use a list to store app data with the following structure: `[(name, priority, start_time, end_time), ...]`

3. **Sort Apps by Priority:**
   - Sort apps in descending order of priority. This ensures that higher-priority apps are processed first.

4. **Resolve Conflicts:**
   - For each app, check if its time slot overlaps with any previously processed app.
   - If a conflict is found and the current app has a **lower priority**, it is **not added**.
   - If a conflict is found and the current app has a **higher priority**, the **lower-priority app is removed**.
   - If the priority is the same and the app was added later, it is **not added**.

5. **Check for App at Query Time:**
   - After resolving all conflicts, check which app (if any) is active at the query time.

---

### 🧪 Example Walkthrough

**Input:**


3
AppA 3 09:00 10:00
AppB 2 09:30 10:30
AppC 4 09:15 09:45
09:20


**Step-by-Step Explanation:**

1. **Parse Input:**
   - N = 3
   - AppA: priority 3, time 09:00–10:00
   - AppB: priority 2, time 09:30–10:30
   - AppC: priority 4, time 09:15–09:45
   - Query time: 09:20

2. **Sort Apps by Priority (Descending):**
   - AppC (priority 4), AppA (priority 3), AppB (priority 2)

3. **Resolve Conflicts:**
   - Add AppC (09:15–09:45) — no conflict.
   - Add AppA (09:00–10:00) — overlaps with AppC. Since AppA has lower priority, it is **not added**.
   - Add AppB (09:30–10:30) — overlaps with AppC. AppB has lower priority, so it is **not added**.

4. **Check Query Time (09:20):**
   - Only AppC is active at 09:20.

**Output:**

AppC
"""

from datetime import datetime, timedelta

class TimeSlot:
    def __init__(self, app_name, priority, start_time, end_time):
        # TimeSlot类构造函数，用来初始化时间段
        self.app_name = app_name  # App的名称
        self.priority = priority  # App的优先级
        self.start_time = start_time  # 时间段的开始时间
        self.end_time = end_time  # 时间段的结束时间

    def overlaps_with(self, other):
        # 检查两个时间段是否有重叠
        return self.start_time < other.end_time and self.end_time > other.start_time
        # 如果当前时间段的开始时间早于另一个时间段的结束时间，且当前时间段的结束时间晚于另一个时间段的开始时间，则两时间段重叠

class AppManager:
    def __init__(self):
        # AppManager类的构造函数，用来初始化App管理器
        self.registered_slots = []  # 存储已注册的时间段

    def register_app(self, input_line):
        # 根据输入信息注册App的时间段
        parts = input_line.split(" ")  # 分解输入行
        app_name, priority = parts[0], int(parts[1])  # 获取App名称和优先级
        start_time = datetime.strptime(parts[2], "%H:%M").time()  # 将字符串时间转换为时间对象
        end_time = datetime.strptime(parts[3], "%H:%M").time()  # 将字符串时间转换为时间对象

        if start_time < end_time:  # 检查开始时间是否早于结束时间
            new_slot = TimeSlot(app_name, priority, start_time, end_time)  # 创建新的时间段对象
            to_remove = []  # 存储需要被移除的时间段

            for slot in self.registered_slots:  # 遍历已注册的时间段
                if slot.overlaps_with(new_slot):  # 检查时间段是否重叠
                    if slot.priority < new_slot.priority:  # 如果存在的时间段优先级低于新的时间段
                        to_remove.append(slot)  # 添加到移除列表
                    elif slot.priority >= new_slot.priority:  # 如果存在的时间段优先级不低于新的时间段
                        return  # 不注册新的时间段

            for slot in to_remove:  # 移除低优先级的时间段
                self.registered_slots.remove(slot)

            self.registered_slots.append(new_slot)  # 添加新的时间段

    def get_app_at_time(self, time_str):
        # 根据查询的时间点返回正在使用的App
        query_time = datetime.strptime(time_str, "%H:%M").time()  # 将查询时间转换为时间对象
        for slot in self.registered_slots:  # 遍历已注册的时间段
            if slot.start_time <= query_time < slot.end_time:  # 如果查询时间在时间段内
                return slot.app_name  # 返回App名称
        return "NA"  # 如果没有找到对应的App，则返回"NA"

def main():
    manager = AppManager()  # 创建App管理器
    N = int(input())  # 输入App的数量
    for _ in range(N):  # 根据数量进行循环
        registration_data = input()  # 输入App注册数据
        manager.register_app(registration_data)  # 注册App
    time_query = input()  # 输入查询时间
    print(manager.get_app_at_time(time_query))  # 输出查询时间点的App

if __name__ == "__main__":
    main()  # 程序入口

