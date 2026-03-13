"""
·题目描述
老李是货运公司承运人，老李的货车额定载货重量为wt。现有两种货物，货物A单件重量为wa，单件运费利润为pa。货物B单件重量为wb，单件运费利润为pb。
老李每次发车时载货总重量刚好为货车额定载货重量wt，车上必须同时有货物A和货物B，货物A、B 不可切割。
老李单车次满载运输可获得的最高利润是多少?
由输入输出 园
输入
输入一行五个正整数。
第一个数字为货物A的单件重量wa，0<wa<10000第二个数字为货物B的单件重量wb，0<wb<10000第三个数字为货车的额定载重wt，0<wt<100000第四个数字为货物A的单件运费利润pa，0<pa<1000第五个数字为货物B的单件运费利润pb，0<pb<1000
输出单次满载运输的最高利润

输入
10 8 36 15 7


输出
44

说明：
运送2个A货物，2个B货物。

输入
1 1 2 1 1



输出
2

1.定义一个函数calculate max profit，接收货物A的单件重量wa，货物B的单件重量wb，货车的额定载重wt，货物A的单件运费利润pa，货物B的单件运费利润pb作为参数。
2.初始化最大利润max profit为0。
3.使用for循环遍历所有可能的货物A的数量，从1到wt/wa。因为货物A至少要有一个，最多不超过wt // wa个。
4.在循环中，使用if语句判断剩余重量是否可以被wb整除，如果可以，则可以装载B货物。
5.计算B货物的数量b count，通过将剩余重量wt-a count*wa除以wb得到。
6.使用if语句确保B货物数量大于0。
7.计算当前装载方案的利润profit，通过a count*pa+b count*pb得到。
8.使用max函数更新最大利润max profit，将当前profit与max profit比比较取较大值。
9.循环结束后，返回最大利润max profit。
10.从标准输入读取数据，并通过map函数将输入的字符串转换为整数。
11.调用calculate max proft函数，并将输入的参数传递进去。
12.输出最大利润。
"""

# 定义一个函数，用于计算最大利润
def calculate_max_profit(wa, wb, wt, pa, pb):
    max_profit = 0  # 初始化最大利润为0

    # 考虑所有可能的装载方式，对货物A的数量进行遍历
    for a_count in range(1, wt // wa + 1):  # 货物A至少要有一个，最多不超过wt/wa个
        if (wt - a_count * wa) % wb == 0:  # 如果剩余重量可以被wb整除，则可以装载B货物
            b_count = (wt - a_count * wa) // wb  # 计算B货物的数量
            if b_count > 0:  # 确保B货物数量大于0
                profit = a_count * pa + b_count * pb  # 计算当前装载方案的利润
                max_profit = max(max_profit, profit)  # 更新最大利润

    return max_profit  # 返回最大利润


# 从标准输入读取数据
wa, wb, wt, pa, pb = map(int, input().split())

# 计算并输出最大利润
print(calculate_max_profit(wa, wb, wt, pa, pb))

