"""
题目
题目描述
小明今年升学到了小学1年级来到新班级后,发现其他小朋友身高参差不齐,然后就想基于各小朋友和自己
的身高差,对他们进行排序,请帮他实现排序。
输入输出
输入
第一行为正整数h和n,0<h<200为小明的身高,0<n<50为新班级其他他小朋友个数。
第二行为n个正整数,h1~hn分别是其他小朋友的身高,取值范围0<hi<200,n个正整数各不相同
输出
输出排序结果,各正整数以空格分割,
和小明身高差绝对值最小的小朋友排在前面,
和小明身高差绝对值最大的小朋友排在后面,
如果两个小朋友和小身高差一样,则个子较小的小朋友排在前面。
样例1
复制
java
AI写代码
1 输入
12
100 10
95 96 97 98 99 101 102 104 104 105
4
5
输出
6
99 101 98 102 97 103 96 104 95 105

Question
Question Description
Xiao Ming was promoted to the first grade of primary school this year. After arriving at the new class, he found that the heights of other children are uneven. Then he wants to sort them based on the height difference between each child and himself. Please help him implement the sorting.
Input and Output
Input
The first line contains positive integers h and n, where 0 < h < 200 is Xiao Ming's height, and 0 < n < 50 is the number of other children in the new class.
The second line contains n positive integers, h1 to hn, which are the heights of other children respectively. The value range is 0 < hi < 200, and the n positive integers are all different.
Output
Output the sorting result, with each positive integer separated by a space.
The child with the smallest absolute difference from Xiao Ming's height comes first,
the child with the largest absolute difference from Xiao Ming's height comes last,
if two children have the same absolute difference from Xiao Ming's height, the shorter child comes first.
Sample 1
java
Write code in Al
Copy
Input
100 10
3
95 96 97 98 99 101 102 104 105
4
Output
5
6
99 101 98 102 97 103 96 104 95 105

Python 语言思路
1、读取输入的小明的身高h和其他小朋友的个数n。
2、读取n个正整数,表示其他小朋友的身高。
3、创建一个列表heights,将输入的n个正整数存储其中。
4、对heights列表进行排序的关键是身高差的绝对值和个子转变小的小朋友排在前面。
5、定义一个排序的比较函数,函数的逻辑如下:
a.计算每个小朋友与小明身高之间的差值的绝对值。
b.如果差值相同,则比较小朋友的身高大小,个子较小的排在前面。
c.返回排序的结果。
6、使用sorted函数对heights列表进行排序,排序时指定比较函数为上述定义的函数。
7、输出排序结果,将排序后的结果以空格分隔输出。

Python language approach
1. Read the input values of Xiaoming's height h and the number of other children n.
2. Read n positive integers representing the heights of the other children.
3. Create a list called heights and store the input n positive integers in it.
4. The key to sorting the heights list is that children with a smaller absolute difference in height and those who are shorter come first.
5. Define a comparison function for sorting with the following logic:
a. Calculate the absolute difference between each child's height and Xiaoming's height.
b. If the differences are the same, compare the children's heights, with the shorter child coming first.
c. Return the sorting result.
6. Use the sorted function to sort the heights list, specifying the above-defined function as the comparison function.
7. Output the sorting result, with the sorted result separated by spaces.
"""


# 导入sys模块以读取输入
import sys

# 读取输入数据
input = sys.stdin.read

# 将输入数据拆分成列表
data = input().split()

# 读取小明的身高和其他小朋友的个数
ming_height = int(data[0])
num_friends = int(data[1])

# 读取其他小朋友的身高并添加到列表中
friend_heights = list(map(int, data[2:]))

# 定义一个排序函数，用于根据题目要求进行排序
def sort_key(height):
    # 计算和小明身高的差值的绝对值
    diff = abs(height - ming_height)
    return (diff, height)

# 使用sorted函数对列表进行排序
sorted_heights = sorted(friend_heights, key=sort_key)

# 输出排序结果
print(" ".join(map(str, sorted_heights)))

