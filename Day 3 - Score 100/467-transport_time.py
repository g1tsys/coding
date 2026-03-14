"""
题目描述
M(1<=M<=20)辆车需要在一条不能超车的单行道到达终点，起点到终点的距离为N(1<=N<=400)，速度快的车追上前车后，只能以前车的速度继续行驶，求最后一车辆到达目的地花费的时间
注:每辆车固定间隔一小时出发，比如第一辆车0时出发，第二辆车1时出发，以此类推
前入前出
输入第一行两个数字:M，N分别代表车辆数和到终点的距离，以空格分隔。接下来M行，每行1个数字S，代表每辆车的速度，0<S<30
输出最后一辆车到达目的地花费的时间

输入
2 11
3
2

输出
5.5

说明:
2 辆车，距离 11，0 时出发的车速度快，1 时出发的车，到达目的的花费为 5.5

//注意:大家记得处理需要保留多少位小数,我这里是不做处理的,大家根据要求变化

Python四语言思路
1.读取输入的车辆数和到终点的距离。
2.创建一个变量min_time，用于记录最小时间，初始化为0。
3.使用一个循环，从1到车辆数遍历每辆车的速度。
4.在循环内部，读取当前车辆的速度。
5.根据当前车辆的速度和到终点的距离，计算当前车辆到达目的地所需的时间，保存在变量cur_time中。
6.判断是否为第一辆车(即当前循环变量是否为1)。
。如果是第一辆车，将当前时间设为最小时间，即将min_time赋值为cur_time。
，如果不是第一辆车，进入下一步。
7.判断当前时间是否比最小时间减1还要小。
。如果是，说明当前车辆需要等待前一辆车，将最小时间减1，即将min_time赋值为min_time-1.
如果不是，说明当前车辆可以直接行驶，更新最小时间为当前时间，即将min_time赋值为cur_time.
8.循环结束后，输出最小时间，即最后一辆车到达目的地的时间。
"""

def process_transport_time(count, distance, inputs):
    min_time = 0  # 初始化最小时间为0
    for i in range(count):  # 遍历每辆车的速度
        speed = int(inputs[i])  # 获取当前车辆的速度
        cur_time = distance / speed  # 计算当前车辆到达目的地所需的时间
        if i == 0:  # 如果是第一辆车
            min_time = cur_time  # 设置当前时间为最小时间
            continue  # 跳过本次循环
        if cur_time < min_time - 1:  # 如果当前时间小于最小时间减去1
            min_time = min_time - 1  # 将最小时间减去1，表示当前车需要等待前车
        else:
            min_time = cur_time  # 否则，更新最小时间为当前时间
    print(min_time)  # 输出最后一辆车到达目的地的时间

# 读取输入
line = input()  # 读取一行输入
cnt_distance = line.split(" ")  # 按空格分隔输入行
count = int(cnt_distance[0])  # 获取车辆数量
distance = int(cnt_distance[1])  # 获取到终点的距离

inputs = []
for i in range(count):
    inputs.append(input())  # 读取每辆车的速度

# 调用函数计算最后一辆车到达目的地的时间
process_transport_time(count, distance, inputs)

