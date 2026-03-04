"""
订阅本专栏后即可解锁在线OJ刷题权限
专栏介绍:最新的华为OD机试题目总结,使用C++、Java、Pythorn、C语言、JS五种语言进行解
答,每个题目的思路分析都非常详细,支持

在线OJ评测刷题!!!!订阅后获取权限,新增图解思路,
问题解疑,多样例测试,超过百字的思路参考解析,持续更新,代码仅供学习参考
题库学习:华为OD技术面试手撕真题
题目
题目描述
在一个狭小的路口,每秒只能通过一辆车,假设车辆的颜色只有3种,,找出N秒内经过的最多颜色的车辆
数量
三种颜色编号为0,1,2
请注意:这里是假设3中颜色,实际考试中不止3中颜色

Python语言 思路
1.创建一个空的Counter对象color_counter来记录每种颜色的;出现次数,并初始化最大颜色数量
max_color_count为0。
2.遍历车辆颜色列表car_colors。
3.将当前颜色添加到color_counter中,并更新该颜色的出现次数。
4.如果窗口中的车辆数超过了时间窗口大小w,需要从窗口最左侧移除一辆车。
5.从color_counter中减去被移除车辆的颜色的出现次数,并检查该颜色的车辆数是否减到了0。如果是,则
从color_counter中移除该颜色。
6.更新最大颜色数量max_color_count为当前颜色的出现次数和max_color_count中的较大值。
7.返回最大颜色数量max_color_count作为结果。

"""
from collections import Counter


def max_color_in_window(car_colors, w):
    # 创建一个空的Counter对象来记录每种颜色的出现次数
    color_counter = Counter()
    max_color_count = 0

    # 遍历车辆颜色列表
    for i, color in enumerate(car_colors):
        # 添加当前颜色到Counter
        color_counter[color] += 1

        # 如果窗口中的车辆数超过了w，我们需要从窗口最左侧移除一辆车
        if i >= w:
            color_to_remove = car_colors[i - w]
            color_counter[color_to_remove] -= 1
            # 如果某颜色的车辆数减到了0，我们从Counter中移除这种颜色
            if color_counter[color_to_remove] == 0:
                del color_counter[color_to_remove]

        # 更新最大颜色数量
        max_color_count = max(max_color_count, color_counter[color])

    return max_color_count


# 从输入中读取车辆颜色信息和统计时间窗口
car_colors = list(map(int, input().split()))
w = int(input())

# 调用函数并输出结果
print(max_color_in_window(car_colors, w))
