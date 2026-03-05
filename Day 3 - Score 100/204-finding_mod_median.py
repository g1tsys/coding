"""
题目描述
1、众数是指一组数据中出现次数量多的那个数,众数可以是多个7
2、中位数是指把一组数据从小到大排列,最中间的那个数,如果是这组数据的个数是奇数,那最中间那个
就是中位数,如果这组数据的个数为偶数,那就把中间的两个数之和除以2,所得的结果就是中位数
3、查找整型数组中元素的众数并组成一个新的数组,求新数组的的中位数
输入输出 

输入
输入一个一维整型数组,数组大小取值范围0<N<1000,数组中每个元素取值范围0<E<1000
输出
输出众数组成的新数组的中位数
Python语言 思路
1、首先,我们使用Counter对象对输入的整型数组进行统计,得到每个元素出现的次数
2、接下来,我们找到出现次数最多的元素,即众数。我们将其记录在mode_list中
3、对mode_list进行排序,得到有序的众数列表mode_list_sorted
4、根据mode_list_sorted的长度,判断众数的个数是奇数还是偶数 
5、如果是奇数,中位数即为mode_list_sorted中间位置的元素
6、如果是偶数,中位数为中间两个位置元素的平均值
7、返回计算得到的中位数作为结果
"""

from collections import Counter

def calculate_median(nums):
    count_dict = Counter(nums)  # 使用Counter统计元素出现次数

    # 将出现次数最多的元素找出来，即众数
    max_count = max(count_dict.values())
    mode_list = [num for num, count in count_dict.items() if count == max_count]

    mode_list_sorted = sorted(mode_list)  # 对众数列表进行排序

    n = len(mode_list_sorted)
    if n % 2 == 1:  # 奇数个众数，返回中间位置的数作为中位数
        median = mode_list_sorted[n // 2]
    else:  # 偶数个众数，取中间两个数之和除以2得到中位数
        middle1 = mode_list_sorted[n // 2 - 1]
        middle2 = mode_list_sorted[n // 2]
        median = (middle1 + middle2) // 2

    return median


# 输入示例
input_nums = [10 ,11 ,21 ,19 ,21, 17 ,21 ,16 ,21 ,18, 15]

# 计算新数组的中位数
median = calculate_median(input_nums)

# 输出结果
print(median)
