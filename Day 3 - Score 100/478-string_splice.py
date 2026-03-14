"""
Docstri题目描述:
给定M(0<M≤30)个字符(a-z)，从中取出任意字符(每个字符只能用一次)拼接成长度为N(0<N≤5)的字符串
要求相同的字符不能相邻，计算出给定的字符列表能并接出多少种满足条件的字符串，输入非法或者无法拼接出满足条件的字符串则返回0。
前入输出园
输入给定的字符列表和结果字符串长度，中间使用空格“")拼接
输出满足条件的字符串个数:ng for coding.Day 3 - Score 100.478-string_splice

输入
abc 1



输出
3


说明：
给定的字符为a,b,c，结果字符串长度为1，可以拼接成a,b,c，共3种

2Python四语言思路
1.首先判断输入是否合法，如果字符列表为空，结果字符串长度小于等于0或大于5、字符列表长度大于30，则遥回0。
2.使用Counter函数统计李符列表中每个字符的数量，得到一个字典char_coumt，key为字持，value为该李特的数量。
3.定义回溯困数backtack，参数为上一个选择的字符和当前字符串的长度。
4.如果当前字符率的长度等于结果字符串的长度N明已经得到一个满足条件的字符中，返回1。
5.初始化计数count为0。
6.遍历字符列表中的每个字符，如二符不一个选择的字符并且该字符的数量大于0，则可以选择该字符。
7.选择当前字符，更新计数器》将学前手符的数量减1。
入当前选择的字符和字符事长度加1，将返回值加到计数count上。8.渤归调用backtrack19.回潮，的故量加1。
10.返回计(count,
11.在main困数中，首先设取输入并拆分为字符列表和姑果字符串长座。
12.调用count_stings困数，传入字符列表和结果字符串长度，返同满足条件的字符串个数。
CSDNWRUIK

"""

from collections import Counter

def count_strings(chars, N):
    """
    计算给定字符列表能拼接出的满足条件的字符串个数

    参数:
    chars -- 字符列表
    N -- 结果字符串的长度

    返回值:
    满足条件的字符串个数
    """
    if not chars or N <= 0 or N > 5 or len(chars) > 30:
        return 0

    # 统计每个字符的数量
    char_count = Counter(chars)

    # 使用回溯法计算可能的字符串个数
    def backtrack(last_char, length):
        if length == N:
            return 1
        count = 0
        for char, available in char_count.items():
            if char != last_char and available > 0:
                # 选择当前字符，更新计数器
                char_count[char] -= 1
                count += backtrack(char, length + 1)
                # 回溯，恢复计数器
                char_count[char] += 1
        return count

    # 从一个空字符开始回溯
    return backtrack('', 0)

# 解析输入，并调用函数计算结果
def main():
    input_str = input()
    parts = input_str.split()
    if len(parts) != 2:
        return 0

    chars, N_str = parts
    N = int(N_str)
    return count_strings(list(chars), N)


print(main())
