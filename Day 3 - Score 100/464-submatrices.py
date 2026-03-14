"""
题目描述
给定一个矩阵，包含N*M个整数，和一个包含K个整数的数组，现在要求在这个矩阵中找一个宽度最小的子矩阵，要求子矩阵包含数组中所有的整数
前入输出Q
前入第一行输入两个正整数N，M，表示矩阵大小。接下来N行M列表示矩阵内容。下一行包含一个正整数K下一行包含K个整数，表示所需包含的数组，K个整数可能存在重复数字，所有输入数据小于1000
输出包含一个整数，表示满足要求子矩阵的最小宽度，若找不到，输出-1

输入
2 5
1 2 2 3 1
2 3 2 3 2
3
1 2 3

输出
2

输入
2 5
1 2 2 3 1
1 3 2 3 4
3
1 1 4

输出
5

输入
2 5
1 2 2 3 1
1 3 2 3 4
3
1 1 4

输出
5

Python四语言思路
1.首先，我们需要遍历矩阵中的每个元素，记录下每个数字出现的位置(行和列的索引)。2.然后，我们定义一个函数cortains.a11mumters来判断当前的子矩阵是否包含所需的所有数字以及相应的数量。
3.接下来，我们开始寻找宽度最小的子矩阵。为此，我们需要考虑所有可能的子矩阵，我们可以通过四层嵌套循环来完成。循环变量1ent和riet 用于确定子矩阵的左右边界，而top和bottom用于确定上下边界。
4.对于每个可能的子矩阵，我们使用cotains.a11mters函数来检查它是否包含所有需要的数字。如果是，则计算当前子矩阵的宽度，并与之前找到的最小宽度进行比较，更新最小宽度。5.最后，如果我们找到了至少一个满足条件的子矩阵，我们返回其最小宽度;如果没有找到任何满足条件的子矩阵，我们返回-1。
"""

def min_width_submatrix(matrix, N, M, required_nums):
    # Step 1: 记录每个数字在矩阵中出现的位置
    num_positions = {}
    for i in range(N):
        for j in range(M):
            num = matrix[i][j]
            if num not in num_positions:
                num_positions[num] = []
            num_positions[num].append((i, j))

    # Step 2: 定义一个函数来检查子矩阵是否包含所有需要的数字
    def contains_all_numbers(top, left, bottom, right):
        required_counts = {num: required_nums.count(num) for num in required_nums}
        for num in required_nums:
            if num not in num_positions:
                return False
            count = 0
            for i, j in num_positions[num]:
                if top <= i <= bottom and left <= j <= right:
                    count += 1
            if count < required_counts[num]:
                return False
        return True

    # Step 3: 寻找宽度最小的子矩阵
    min_width = M + 1  # 初始化最小宽度为一个不可能的值（大于矩阵的宽度）
    for left in range(M):
        for right in range(left, M):
            for top in range(N):
                for bottom in range(top, N):
                    # Step 4: 检查当前子矩阵是否满足条件
                    if contains_all_numbers(top, left, bottom, right):
                        # 如果满足条件，更新最小宽度
                        min_width = min(min_width, right - left + 1)

    # Step 5: 返回最小宽度，如果没有找到满足条件的子矩阵，则返回-1
    return min_width if min_width <= M else -1

# 读取输入
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
K = int(input())
required_nums = list(map(int, input().split()))

# 计算并输出结果
result = min_width_submatrix(matrix, N, M, required_nums)
print(result)
