"""
题目
题目描述
给定一个数组,编写一个函数来计算它的最大N个数与最小N个数的和。你需要对数组进行去重。
说明:
1、数组中数字范围[0,1000]
2、最大N个数与最小N个数不能有重叠,如有*重叠,输入非法**返回-1
3、输入非法返回-1
输入输出区
输入
第一行输入M,M表示数组大小
第二行输入M个数,表示数组内容
第三行输入N,N表达需要计算的最大、最小N个数
输出
输出最大N个数与最小N个数的和

Problem Description
Given an array, write a function to calculate the sum of its largest N numbers and smallest N numbers. You need to remove duplicates from the array.

Notes:
1. The range of numbers in the array is [0, 1000].
2. There must be no overlap between the largest N numbers and the smallest N numbers. If there is an overlap, the input is invalid, return -1.
3. Return -1 for invalid input.

Input/Output
Input
The first line inputs M, which represents the size of the array.
The second line inputs M numbers, representing the contents of the array.
The third line inputs N, which represents the number of largest and smallest numbers to be calculated.

Output
Output the sum of the largest N numbers and the smallest N numbers.

Python语言 思路
1.首先,定义一个函数max_min_sum(nums,N)来计算最大N个数和最小N个数的和。
2.如果N为0,直接返回0,因为没有数需要计算和。
3.检查数组中的数是否都在[0,1000]范围内,如果有不满足条件的数,返回-1
4.对数组进行去重,并转换成列表。
5.对去重后的数组进行排序,以便后续计算最大和最小N个数的和。
6.如果去重后的数组长度小于2N,说明最大N个数和最小N个数有重叠,返回-1。
7.计算最小N个数的和,即取前N个数进行求和。
8.计算最大N个数的和,即取后N个数进行求和。
9.返回最大N个数和最小N个数的和。
10.主程序部分,首先读入数组大小M,然后读入数组内容nums最后读入N值。
11.检查输入的数组大小是否与实际输入的数组长度一致,不一致则输出-1。
12.调用max_min_sum函数计算结果,并输出。

Python Language Approach
1. First, define a function max_min_sum(nums, N) to calculate the sum of the largest N numbers and the smallest N numbers.
2. If N is 0, directly return 0 because there are no numbers to calculate the sum for.
3. Check if all numbers in the array are within the range [0, 1000]. If there are numbers that do not meet the condition, return -1.
4. Remove duplicates from the array and convert it into a list.
5. Sort the array after removing duplicates to facilitate the subsequent calculation of the sum of the largest and smallest N numbers.
6. If the length of the array after removing duplicates is less than 2N, it indicates that there is an overlap between the largest N numbers and the smallest N numbers, return -1.
7. Calculate the sum of the smallest N numbers, that is, sum the first N numbers.
8. Calculate the sum of the largest N numbers, that is, sum the last N numbers.
9. Return the sum of the largest N numbers and the smallest N numbers.
10. In the main program part, first read the array size M, then read the array content nums, and finally read the N value.
11. Check if the input array size is consistent with the actual length of the input array. If not, output -1.
12. Call the max_min_sum function to calculate the result and output it.


def max_min_sum(nums, N):
    # 特殊情况处理：当N为0时，应直接返回0，因为没有数需要计算和
    if N == 0:
        return 0

    # 检查数组中的数是否都在[0, 1000]范围内，如果有不满足条件的数，返回-1
    if any(num < 0 or num > 1000 for num in nums):
        return -1

    # 对数组进行去重，并转换成列表
    unique_nums = list(set(nums))
    # 对去重后的数组进行排序，以便后续计算最大和最小N个数的和
    unique_nums.sort()

    # 如果去重后的数组长度小于2N，说明最大N个数和最小N个数有重叠，返回-1
    if len(unique_nums) < 2 * N:
        return -1

    # 计算最小N个数的和
    min_sum = sum(unique_nums[:N])
    # 计算最大N个数的和
    max_sum = sum(unique_nums[-N:])

    # 返回最大N个数和最小N个数的和
    return min_sum + max_sum

# 读入数组大小
M = int(input())
# 读入数组内容
nums = list(map(int, input().split()))
# 读入N值
N = int(input())

# 检查输入的数组大小是否与实际输入的数组长度一致，不一致则输出-1
if len(nums) != M:
    print(-1)
else:
    # 调用max_min_sum函数计算结果，并输出
    result = max_min_sum(nums, N)
    print(result)

"""