"""
题目描述
现有若干个会议，所有会议共享一个会议室，用数组表示各个会议的开始时间和结束时间，格式为:
[[会议1开始时间，会议1结束时间]，[会议2开始时间，会议2结束时间1
请计算会议室占用时间段
当输入输出 Q
输入第一行输入一个整数 n，表示会议数量之后输入n行，每行两个整数，以空格分隔，分别表示会议开始时间，会议结束时间
输出输出多行，每个两个整数，以空格分隔，分别表示会议室占用时间段开始和结束

输入
4
1 4
2 5
7 9
14  18


输出
1 5 
7 9
14 18

输入
2
1 4
4 5


输出
1 5 

1、首先，定义了一个函数 merge_intervals 来合并四时间段。该函数的输入是一个时间段的列表intervals，其中每个时间段表示为一个包含开始时间和结束时间的列表。函数首先对时间段进行排序，以开始时间为关键字 Q进行排序。
2、然后，初始化四一个空列表 merged 来保存合并Q后的时间段。接下来，遍历排序后的时间段列表 sorted intervals，对于每个当前时间段 current ，判断是否与已合并的时间段列表 merged 有重叠。如果没有重叠，则将当前时间段添加到合并后的列表中。如果有重叠，则更新已合并时间段的结束时间为当前时间段的结束时间与已合并时间段的结束时间中的较大值。
3、最后，返回合并后的时间段列表 merged
4、在主程序中，首先读取输入的会议数量n。然后，初始化Q会议时间段列表intervals。接下来，读取每个会议的开始和结束时间，将其添加到会议时间段列表中。然后，调用函数merge intervals 来合并时间段，并将合并后的时间段保存在变量merged intervals 中。最后，打印合并后的会议室占用时间段。
"""

# 定义一个函数来合并时间段
def merge_intervals(intervals):
    # 对时间段进行排序，以开始时间为关键字进行排序
    sorted_intervals = sorted(intervals, key=lambda x: x[0])

    # 初始化合并后的时间段列表
    merged = []

    for current in sorted_intervals:
        # 如果合并后的时间段列表为空，或者当前时间段的开始时间大于已合并时间段的结束时间
        # 则将当前时间段添加到合并后的列表中
        if not merged or current[0] > merged[-1][1]:
            merged.append(current)
        else:
            # 否则，当前时间段与已合并的最后一个时间段有重叠，更新已合并时间段的结束时间
            merged[-1][1] = max(merged[-1][1], current[1])

    return merged


# 读取输入的会议数量
n = int(input())

# 初始化会议时间段列表
intervals = []

# 读取每个会议的开始和结束时间，添加到会议时间段列表中
for _ in range(n):
    start, end = map(int, input().split())
    intervals.append([start, end])

# 调用函数合并时间段
merged_intervals = merge_intervals(intervals)

# 打印合并后的会议室占用时间段
for interval in merged_intervals:
    print(interval[0], interval[1])

