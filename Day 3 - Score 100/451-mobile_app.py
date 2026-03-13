"""
智能手机方便了我们生活的同时，也侵占了我们不少的时间。“手机App防沉送系统-能够让我们每天合理的规划手App使用时间，在正确的时间做正瑞的事。
它的大概原理是这样的:
1、在一天24小时内，可注册每个App的允许使用时段
2800
2、一个时段只能使用一个App;举例说明:不能同时在09:00-10:00注册App2和App3
3、App有优先级，致值越高，优先级越高。注册使用时段时。如果高优先级的App时间和低优先级的时段有冲交则系统会自动注销低优先级的时段，如果App的优先级相同，则后添加的App不能注册
举例1:
(1)注册App3前:
C0:10
+2是0
(2)App3注册时段和App2有冲突
60.00
+2-10
2有p3的注册，自动注销App2的注册:(3)App3优先级高，系统接受
00-00
+2600
老便2:
(烊一]注册App4.
00:00
(2] A中D4弄0AD02座A00号省有中的注册效果如下
00-00
+24:00
p3低，这种场景下App4注册不上，最
240
4、一个App可以在一天内注册多个时段

辘入
输入分3部分:
第一行表示注册的App数N(N<=100);第二部分包括N行，每行表示条App注册致据，最后一行输入一个时间点，程序即返回该时间点的可用APP
说明如下
1、N行注册鼓据以空格分隔，四项数据依次表示:App名称、优先级、起始时间、结来时间
2、优先级1-5，数李佰越大，优先级拉要
3、时间格式HH:MM，小时和分钟都是两位，不足两位前面0
4、起始时间需小于结束时间，否则注册不上
5、注册信息中的时间段包含起始时间点，不包含结来时间点
输出
输出一个字符串，表示App名称，没有就返回NA

输入
2
App1 1 09:00 10:00
App2 2 11:00 11:30    
09:30

输出
App1 

输入
2
App1 1 09:00 10:00
App3 2 09:00 10:00
09:30


输出
App3

输入
2
App1 1 09:00 10:00
App2 2 09:10 09:30
09:20



输出
App2

说明
App1和App2的时段有冲突，App2优先级高，注册App2之后，App1自动注销，因此输出App2             

输入
2
App1 1 09:00 10:00
App2 2 09:10 09:30
09:50

输出
NA

说明：
App2优先级高会被注册, 然后App1被注销, App1被注销后, 09:50时刻没有应用注册，因此输出NA

2
App1 1 09:00 10:00
App2 2 09:10 09:30
09:20

尝试注册App2 (优先级 2，时间 09:10-09:30)
[------ App1 ------]
        [App2]
        
发现App1和App2时间冲突，但App2的优先级更高，因此注销App1，注册App2。
[------ App2 ------]

查询时间09:20，只有App2注册在这个时间段内。
返回"App2"

|--------|--------|--------|--------|--------|
09:00    09:10    09:20    09:30    10:00
         [------- App2 -------]
         
返回结果：App2

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

