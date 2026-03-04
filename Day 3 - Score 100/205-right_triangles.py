"""
有N条线段,长度分别为a[1]-a[n]
现要求你计算这N条线段最多可以组合成几个直角三角形
每条线段只能使用一次,每个三角形包含三条线段
输入输出区
输入
第一行输入一个正整数T(1<=T<=100),表示有T组测试数据
对于每组测试数据,接下来有T行,每行第一个正整数N,表示线段个个数(3<=N<=20),接着是N个正整数,表示每条线段长度,
(0<a[i]<100)
输出
对于每组测试数据输出一行,每行包括一个整数,表示最多能组合的直角三角角形个数

1.创建一个字典segment_counts,用来记录每种长度的线段有多少条。
2.遍历输入的线段列表,如果线段的长度已经在字典中,则将其数量加一;否则将其添加到字典
中,并设置数量为1。
3.创建一个空列表possible_triangles,用来存储所有可能的直角三角形的组合。
4.遍历线段列表中的每条线段,再次遍历,寻找第二条线段,确保不与第一条线段重复,再次遍
历,寻找第三条线段,确保不与前两条线段重复。判断这三条线段是否能组成直角三角形,如果
能,则将它们的组合添加到列表中。
5.创建一个回溯函数backtrack,参数为remaining和count,其中remaining是一个字典,表示剩余
的线段数量,count表示当前已经组合的直角三角形数量。
6.初始化最大组合数max_count为count。
7.遍历所有可能的直角三角形组合,检查字典remaining中是否有足够的线段来形成当前的三角形。
如果有,则将已经使用的线段数量减去,并递归调用backtrack<函数,尝试其他的组合,并更新最
大组合数。递归调用结束后,恢复字典remaining中的线段数量量。
8.返回最大的组合数max_count。
9.在主函数中,读取输入的测试数据组数T,然后遍历每组测试数据。读取每组测试数据,并转换
为整数列表。调用max_right_triangles函数计算并打印最多能组合的直角三角形个数。
"""

def is_right_triangle(a, b, c):
    sides = sorted([a, b, c])  # 将输入的三条边长从小到大排序
    return sides[0]**2 + sides[1]**2 == sides[2]**2  # 判断最短的两条边的平方和是否等于最长边的平方

def max_right_triangles(segments):
    # 统计各个长度的线段数量
    segment_counts = {}  # 创建一个字典，用来记录每种长度的线段有多少条
    for seg in segments:  # 遍历输入的线段列表
        if seg in segment_counts:  # 如果这条线段的长度已经在字典中
            segment_counts[seg] += 1  # 就将其数量加一
        else:  # 如果这条线段的长度不在字典中
            segment_counts[seg] = 1  # 将其添加到字典中，并设置数量为1

    # 找出所有可能的直角三角形组合
    possible_triangles = []  # 创建一个空列表，用来存储所有可能的直角三角形的组合
    n = len(segments)  # 获取线段列表的长度
    for i in range(n):  # 遍历线段列表中的每条线段
        for j in range(i+1, n):  # 再次遍历，寻找第二条线段，确保不与第一条线段重复
            for k in range(j+1, n):  # 再次遍历，寻找第三条线段，确保不与前两条线段重复
                if is_right_triangle(segments[i], segments[j], segments[k]):  # 判断这三条线段是否能组成直角三角形
                    possible_triangles.append((segments[i], segments[j], segments[k]))  # 如果能，就将它们的组合添加到列表中

    # 使用回溯法尝试不同的组合
    def backtrack(remaining, count):
        max_count = count  # 初始化最大组合数为当前的组合数
        for triangle in possible_triangles:  # 遍历所有可能的直角三角形组合
            if all(remaining.get(side, 0) > 0 for side in triangle):  # 检查字典中是否有足够的线段来形成当前的三角形
                for side in triangle:  # 对于三角形中的每条边
                    remaining[side] -= 1  # 在字典中减去已经使用的线段
                max_count = max(max_count, backtrack(remaining, count+1))  # 递归调用，尝试其他的组合，并更新最大组合数
                for side in triangle:  # 回溯，恢复字典中的线段数量
                    remaining[side] += 1
        return max_count  # 返回最大的组合数

    return backtrack(segment_counts, 0)  # 从一个空的组合开始，调用回溯函数并返回结果

# 读取输入并处理
T = int(input().strip())  # 读取测试数据组数T
for _ in range(T):  # 遍历每组测试数据
    data = list(map(int, input().strip().split()))  # 读取每组测试数据，并转换为整数列表
    N = data[0]  # 获取线段的数量
    segments = data[1:]  # 获取所有线段的长度列表
    print(max_right_triangles(segments))  # 调用函数计算并打印最多能组合的直角三角形个数


