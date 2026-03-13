"""
给一个正整数列nums，一个跳数jump，及幸存数量left，运算过程为:从索引为0的位置开始向后跳，中间跳过J个数字，命中索引为J+1的数字，该数被敲出，并从该点起跳。以此类推，直到幸存left个数为止。然后返回幸存数之和
约束:
1、0是第一个起跳点
2、起跳点和命中点之间间隔jump个数字，已被敲出的数字不计入在内
3、跳到未尾时无缝从头开始(循环查找)，并可以多次循环
若起始时left>len(nums)则无需跳数处理过程4、

输入
第一行输入正整数数列
第二行输入跳数
第三行输入幸存数量
输出幸存数之和

输入
1,2,3,4,5,6,7,8,9
4
3


输出
13

说明:
从1 (索引为0)开始起跳,中间跳过4个数字因此依次删除6,2,8,5,4,7;剩余1,3,9,返回和为13

输入
1,2,3,4
1
2


输出
6

1.首先判断left是否大于等于nums的长度，如果是，则直接返回nums所有元素之和。
2.定义一个变量index，初始值为0，表示当前的索引位置。
3.创建一个新的列表surviors，将nums的所有元素复制到surviors中。4.当surviors的长度大于left时，执行以下循环:
。计算下一个要删除的元素的索引位置，使用(index+jump+1)%len(surviors)来实现循环查找。
移除该索引位置的元素，使用surviors.pop(index)D
由于删除元素后，后面的元素会往前移，所以需要将索引index减1，以保持正确的索引位置。
。减少需要移除的元素数量，即left减去1。
5.循环结束后，返回surviors中剩余元素的和作为结果，使用sum(sunviors)。
"""


def sum_of_left(nums, jump, left):
    # 当剩余数大于等于数组长度时，直接返回数组所有元素的和
    if left >= len(nums):
        return sum(nums)

    # 索引指针初始化为0
    index = 0
    # 通过数组长度减去剩余数来确定需要移除多少个元素
    surviors = list(nums)

    # 当需要移除的元素数量大于0时循环继续
    while len(surviors)> left:
        # 计算下一个移除元素的索引位置，由于可能循环，所以取余数
        index = (index + jump+1) % len(surviors)
        # 移除该索引位置的元素
        surviors.pop(index)
        # 因为移除元素后，后面的元素会往前移，所以不需要更新索引
        # 减少需要移除的元素数量
        index-= 1

    # 当移除完成后，返回剩余元素的和
    return sum(surviors)




# 获取输入数据
nums = list(map(int, input().split(',')))  # 第一行输入转换为整数列表
jump = int(input())  # 第二行输入转换为整数
left = int(input())  # 第三行输入转换为整数

# # 计算结果并打印输出
print(sum_of_left(nums, jump, left))
