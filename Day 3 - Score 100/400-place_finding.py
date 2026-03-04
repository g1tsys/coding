"""
题目描述
小朋友出操,按学号从小到大排成一列;小明来迟了,请你给小明出个主意,让他尽快找到他应该排的位置。
输入输出
输入
第一行:输入已排成队列的小朋友的学号(正整数),以","隔开;
第二行:小明学号
输出
输出一个数字,代表队列位置(从1开始)

题目描述
小朋友出操,按学号从小到大排成一列;小明来迟了,请你给小明出个主意,让他尽快找到他应该排的位置。
输入输出
输入
第一行:输入已排成队列的小朋友的学号(正整数),以","隔开;
第二行:小明学号
输出
输出一个数字,代表队列位置(从1开始)
"""

def find_position(numbers, xiaoming):
    # 将输入的字符串转换为整数列表
    number_list = list(map(int, numbers.split(' ')))
    # 用二分查找的方式寻找小明的位置
    left, right = 0, len(number_list)
    while left < right:
        mid = (left + right) // 2
        if number_list[mid] < xiaoming:
            left = mid + 1
        else:
            right = mid
    return left + 1 

# 输入
numbers = input().strip()
xiaoming = int(input().strip())

# 处理并输出结果
position = find_position(numbers, xiaoming)
print(position)
