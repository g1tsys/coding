"""
题目描述
有一种特殊的加密算法，明文为一段数字串，经过密码本查找转换，生成另一段密文数字。
串。
规则如下:
1、明文为一段数字串由0~9组成
2、密码本为数字0~9组成的二维数组
3、需要按明文串的数字顺序在密码本里找到同样的数字串，密码本里的数字串是由相邻的单元格数字组成，上下和左右是相邻的，注意:对角线不相邻，同一个单元格的数字不能重复使用。
4、每一位明文对应密文即为密码本中找到的单元格所在的行和列序号(序号从0开始)组成的两个数宇。
如明文第|位Datal对应密码本单元格为Book冈M，则明文第|位对应的密文为XY，X和Y之间用空格隔开。
如果有多条密文，返回字符序最小的密文。
如果密码本无法匹配，返回"error"。
请你设计这个加密程序。

示例1:
密码本:
002
134
664
明文:"3"，密文:"11"
示例2:
密码本:
002
134
664
明文:"03"，密文:"0111"
示例3:
密码本:
0024134634156665
明文:"0024"，密文:"00010203"和"00010212"，返回字典序最小的"00010203"明文:"8223"，密文:"error"，密码本中无法匹配

输入输出
输入第一行输入1个正整数N，代表明文的长度(1sNs200)第二行输入N个明文组成的序列Data[(0sData[≤9)第三行输入1个正整数M，代表密文的长度接下来M行，每行M个数，代表密文矩阵输出输出字典序最小密文，如果无法匹配，输出"error"

输入
2
0 3
3
0 0 2
1 3 4
6 6 4


输出
0 1 1 1

1.定义一个函数find_positions(suw，Book)来导找给定数字在密码本中的所月本的每一行和每一列。如果找到了对应的数字，刻将其位置(行号和咧号)添加一个列表中。
2.定义一个函款1_a时ac=m(pos1，pos3)来检查两个位(仅水平或口如果两个位置在同一行或同一列，并且它们的行号或列号相荃1。则它们是相邻的。
3定义一个國期Z款backirwck(imle。pat)米五长大等丁味文长大，说明己经找到了一个光整的出义，将当前路径添加的始果列表中。否则，获取当色敌子日码本中的所有可器位量。识历议些位量，如果当的路径为空，或者最亿一个位量和当的位量是相锁心，则可以堰要说5加逻路径中，详口调用，处理下一个故字，然C回期，将当的位量移山路径。4.视始化一个列表ophen然C调用回期函故1ckirsck(，[)从第一个敏子开始回莱慢索。
5.如果没有找到任何密文
6.将找到的密文按格式转换为字符串，并按字典序排序，
7.返回字典序最小的空文，
CSON SHAR
"""

//此代码会通不过用例7和8
def find_cypher(N, Data, M, Book):
    # 定义一个函数来寻找给定数字在密码本中的所有位置
    def find_positions(num, Book):
        positions = []
        # 遍历密码本的每一行和每一列
        for i in range(len(Book)):
            for j in range(len(Book[i])):
                # 如果找到了对应的数字，则将其位置（行号和列号）添加到列表中
                if Book[i][j] == num:
                    positions.append((i, j))
        return positions

    # 定义一个函数来检查两个位置是否是相邻的（仅限水平或垂直）
    def is_adjacent(pos1, pos2):
        # 如果两个位置在同一行或同一列，并且它们的行号或列号相差1，则它们是相邻的
        return (abs(pos1[0] - pos2[0]) == 1 and pos1[1] == pos2[1]) or \
               (abs(pos1[1] - pos2[1]) == 1 and pos1[0] == pos2[0])

    # 定义一个回溯函数来查找所有可能的密文
    def backtrack(index, path):
        # 如果路径长度等于明文长度，说明已经找到了一个完整的密文
        if index == N:
            cyphers.append(path[:])  # 添加当前路径到结果列表中
            return

        # 获取当前数字，以及它在密码本中的所有可能位置
        current_num = Data[index]
        positions = find_positions(current_num, Book)

        # 遍历这些位置
        for pos in positions:
            # 如果当前路径为空，或者最后一个位置和当前位置是相邻的，则可以继续递归搜索
            if not path or is_adjacent(path[-1], pos):
                path.append(pos)  # 将当前位置添加到路径中
                backtrack(index + 1, path)  # 递归调用，处理下一个数字
                path.pop()  # 回溯，将当前位置移出路径

    cyphers = []  # 初始化一个列表来存储所有可能的密文
    backtrack(0, [])  # 从第一个数字开始回溯搜索

    # 如果没有找到任何密文，则返回"error"
    if not cyphers:
        return "error"

    # 将找到的密文按格式转换为字符串，并按字典序排序
    formatted_cyphers = [' '.join(f'{x} {y}' for x, y in cypher) for cypher in cyphers]
    formatted_cyphers.sort()  # 排序

    # 返回字典序最小的密文
    return formatted_cyphers[0]

# 读取输入数据
N = int(input().strip())  # 明文长度
Data = list(map(int, input().strip().split()))  # 明文数据
M = int(input().strip())  # 密码本大小
Book = [list(map(int, input().strip().split())) for _ in range(M)]  # 密码本内容

# 调用函数来找到密文，并打印结果
result = find_cypher(N, Data, M, Book)
print(result)
