"""
一、题目
题目描述:
存储阵列上使用的一批固态硬盘，根据硬盘磨损值给定一个数组endurances，数组中每个元素表示单块硬盘的磨损度(0到10000之间)
磨损度越大，表示此盘需要更换的概率越高，需要找出磨损度最高三块盘下标和磨损度最低的三块盘下标:

输入输出
a
输入
一组硬盘磨损度的数组
说明:
(1)数组endurances中无重复值
(2)数组的长度范围:[6,200]
(2)数组的下标从0开始:
输出
第一行:磨损度最高三块盘下标，按下标升序展示第二行:磨损度最低的三块盘下标，按下标升序展示。

输入
1 50 40 68 72 86 35 14 87 99 63 75


输出
5 8 9
0 6 7

输入
23 34 56 12 11 10


输出
0 1 2
3 4 5     

1.定义一个函数find_high_low_endurances(endurances)来处理磨损度数组并输出结果。
2.创建一个空列表indexed_endurances来存储索引卜-磨损度对。
3.使用enumerat。函数遍历磨损度数组endurances，同时获取索引和磨损度，将其以元组的形式添加到indexed_endurances列表中。
4.对indexed_endurances列表进行排序，按照磨损度从大到小的顺序进行排序，即sorted_by_high=sorted(indexed_endurances, key=lanbda x: x[1], reverse=True)
5.对indexed_endurances列表进行排序，按照磨损度从小到大的顺序进行排序，即soted_by_1ov-sorted(indexed_endurances, key=lambda x: x[1]) .
6.提取磨损度最高的三块盘的索引,即high_endurance_indexes=[index forindex,enduranceinsorted_by_high[:3]].
7.将磨损度最高的三块盘的索引按照升序进行排序，即high_endurance_indexes.sort()。
8.提取磨损度最低的三块盘的索引I,即low_endurance_indexes =[index for index,endurance insorted_by_low[:3]]
9.将磨损度最低的三块盘的索引按照升序进行排序，即1o_endurance_indexes.sort()。
10.返回吉果,即 return high_endurance_indexes, low_endurance_indexes.
11.读取输入的磨损度数组，将其存储在变量endurances_input中。
12.将endurances_input以空格为分隔符拆分成字符串数组，即endurances_input.split()。
13.将字符串数组中的每个元素转换为整数，形成磨损度数组，即endurances-[imt(e)foreinendurances_input].
14.调用函数find_high_lowcendurances(endurances)，将磨损度数组作为参数传入，获取结果。15.将磨损度最高的三块盘的索引转换为字符串，并以空格为分隔符，使用join函数连接成一个字符串,即.join(map(str,high_indexes))。
16.将磨损度最低的三块盘的索引转换为字符串，并以空格为分隔符，使用join函数连接成一个字符串,即.join(map(str,lowcindexes))。
17.打印磨损度最高的三块盘的索引字符串和磨损度最低的三块盘的索引字符串。
"""

# 定义一个函数来处理磨损度数组并输出结果
def find_high_low_endurances(endurances):
    # 将磨损度数组及其对应的索引转换为一个索引-磨损度对的列表
    indexed_endurances = list(enumerate(endurances))

    # 对这个列表根据磨损度进行排序，磨损度高的在前
    sorted_by_high = sorted(indexed_endurances, key=lambda x: x[1], reverse=True)

    # 对这个列表根据磨损度进行排序，磨损度低的在前
    sorted_by_low = sorted(indexed_endurances, key=lambda x: x[1])

    # 提取磨损度最高的三块盘的索引，按索引升序排序
    high_endurance_indexes = [index for index, endurance in sorted_by_high[:3]]
    high_endurance_indexes.sort()

    # 提取磨损度最低的三块盘的索引，按索引升序排序
    low_endurance_indexes = [index for index, endurance in sorted_by_low[:3]]
    low_endurance_indexes.sort()

    # 返回结果，分别是磨损度最高和最低的三块盘的索引
    return high_endurance_indexes, low_endurance_indexes


# 读取输入的磨损度数组
endurances_input = input().strip().split()  # 从标准输入读取并去除空格，分割成数组
endurances = [int(e) for e in endurances_input]  # 将字符串数组转换为整数数组

# 调用函数处理并获取结果
high_indexes, low_indexes = find_high_low_endurances(endurances)

# 输出结果
print(' '.join(map(str, high_indexes)))  
print(' '.join(map(str, low_indexes)))  


