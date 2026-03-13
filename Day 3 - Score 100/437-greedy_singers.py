"""
歌手准备从A城去B城参加演出
有如下规则:
1、按照合同，他必须在T天内赶到
2、歌手途径N座城市
3、歌手不能往回走
4、每两座城市之间需要的天数都可以提前获知
5、歌手在每座城市都可以在路边卖唱赚钱，经过调研，歌手提前获知了每座城市卖唱的收入预期，如果在一座城市第- 天卖唱可以赚M，后续每天的收入会减少D(第二天赚的钱是M-D，第三天是M-2D...);如果收入减到0就不会再少了
6、歌手到达后的第二天才能开始卖唱。如果今天卖过唱，第二天才能出发
贪心的歌手最多可以赚多少钱?

输入
第一行两个数字T和N，中间用空格隔开，T代表总天数;N代表路上经过N座城市，0<T<1000，0<N<100
第二行N+1个数字，中间用空格隔开，代表每两座城市之间耗费的时间，其总和<=T接下来N行，每行两个数字M和D，中间用空格隔开，代表每个城市的收入预期，0<M<1000，0<D<100
输出一个数字，代表歌手最多可以赚多少钱

输入
10 2
1 1 2
120 20
90 10

输出
540

说明：
总共10天，路上经过2座城市。
路上共花 1+1+2=4 天
剩余6天最好的计划是在第一座城市待3天，在第二座城市待3天
在第一座城市赚的钱：120 + 100 + 80 = 300
在第二座城市赚的钱：90 + 80 + 70 = 240
一共 300 + 240 = 540

输入
10 1
1 1
120 20

输出
420

首先，根据合同要求的总旅行时间T和每个城市之间需要的旅行时间travel days，计算出除去旅行时间剩余的时间remaining time。
然后，创建一个小顶堆daily profits，用于存放每天的收益
接下来，遍历每个城市的收益city earnings。对于每个城市，从第一天开始卖唱，收益为M，后续每天收益减少D。使用 一个计数器day_counter记录卖唱的天数，每天更新当前日收益为M-day counter * D.
在每次更新当前日收益后，判断以下情况:
。如果剩余时间内的收益天数还没有填满，将当前日收益加入小顶堆dailyprofits。
。如果当前日收益大于堆顶元素，替换堆顶元素为当前更高的日收益。
如果当前日收益不大于堆顶元素，结束循环。
最后，计算小顶堆daily_profits中所有元素的总和，即为最大收益。
"""

import heapq

# 定义计算最大收益的函数
def calculate_max_earnings(T, travel_days, city_earnings):
    # 计算总的旅行时间
    total_travel_time = sum(travel_days)
    # 计算除去旅行时间后剩余的时间
    remaining_time = T - total_travel_time

    # 如果没有剩余时间，直接返回0收益
    if remaining_time <= 0:
        return 0

    # 创建一个小顶堆，用于存放每天的收益
    daily_profits = []

    # 遍历每个城市的收益
    for M, D in city_earnings:
        current_day_profit = M  # 当前日收益从M开始
        day_counter = 0  # 计数器，记录卖唱的天数

        # 当当前日收益大于0时继续循环
        while current_day_profit > 0:
            # 如果剩余时间内的收益天数还没有填满
            if len(daily_profits) < remaining_time:
                heapq.heappush(daily_profits, current_day_profit)  # 将当前日收益加入小顶堆
            elif current_day_profit > daily_profits[0]:  # 如果当前日收益大于堆顶元素
                # 替换堆顶元素为当前更高的日收益
                heapq.heappop(daily_profits)
                heapq.heappush(daily_profits, current_day_profit)
            else:
                # 如果当前日收益不大于堆顶元素，结束循环
                break

            day_counter += 1  # 卖唱天数加一
            current_day_profit = M - day_counter * D  # 更新下一天的收益

    # 计算总收益
    total_earnings = sum(daily_profits)
    return total_earnings

# 读取输入数据
T, N = map(int, input().split())
travel_days = list(map(int, input().split()))
city_earnings = [list(map(int, input().split())) for _ in range(N)]

# 输出最大收益
print(calculate_max_earnings(T, travel_days, city_earnings))

