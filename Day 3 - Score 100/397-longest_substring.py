'''
给你一个字符串s,字符串s首尾相连成一个环形,请你在环中找出 T、'o'x'字符都恰好出现了偶数次最长子字
符串的长度
输入输出
输入
输入小写字母组成的字符串
输出
一个整数

输入
alolobo

输出
6

输入
looxdolx

输出
7

Python 语言思路
1.获取输入字符串的长度n。
2.将字符串s扩展为两倍长度,得到扩展字符串extended s。
3.初始化最大长度maxlen为0。
4.初始化状态变量status为0,用于跟踪字符'I、'o'和'x'出现次数的奇偶性。
5.初始化一个字典status_positions,用于存储特定状态首次出现的位置,初始状态位置设为-1。
6.遍历扩展字符串extended s的每个字符。
7.如果当前字符是T',将状态变量status的第3位进行异或操作,切换T'出现次数的奇偶状态。
8.如果当前字符是'o',将状态变量status的第2位进行异或操作,切换'o'出现次数的奇偶状态。
9.如果当前字符是'x',将状态变量status的第1位进行异或操作,切换'x'出现次数的奇偶状态。
10.如果当前状态status之前已经出现过,计算当前子字符串的长度。curr_len为i减去status_positions[status]
11.如果当前子字符串的长度不超过原字符串的长度n,更新最大长度max_len为max(max_len,curr_len).
12.如果当前状态是首次出现,记录其位置i到status_positionns[status]
13.返回最大长度maxlen。
'''

def find_longest_even_o(s):
    # 获取输入字符串的长度
    n = len(s)
    # 将字符串扩展为两倍长度，以便处理成环形
    extended_s = s * 2
    # 初始化最大长度为0
    max_len = 0
    # 初始化状态变量，用于跟踪 'l', 'o', 和 'x' 字符的出现次数的奇偶性
    status = 0
    # 初始化一个字典，用于存储特定状态首次出现的位置
    status_positions = {0: -1}

    # 遍历扩展字符串的每个字符
    for i in range(2 * n):
        # 如果当前字符是 'l'
        if extended_s[i] == 'l':
            # 切换 'l' 出现次数的奇偶状态
            status ^= 1 << 2
        # 如果当前字符是 'o'
        elif extended_s[i] == 'o':
            # 切换 'o' 出现次数的奇偶状态
            status ^= 1 << 1
        # 如果当前字符是 'x'
        elif extended_s[i] == 'x':
            # 切换 'x' 出现次数的奇偶状态
            status ^= 1

        # 如果当前状态之前已经出现过
        if status in status_positions:
            # 计算当前子字符串的长度
            curr_len = i - status_positions[status]
            # 如果当前子字符串的长度不超过原字符串的长度
            if curr_len <= n:
                # 更新最大长度
                max_len = max(max_len, curr_len)
        else:
            # 如果当前状态是首次出现，记录其位置
            status_positions[status] = i

    # 返回最大长度
    return max_len


s = input()
# 输出最长子字符串的长度
print(find_longest_even_o(s))


