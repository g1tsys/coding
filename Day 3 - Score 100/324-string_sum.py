"""
给定一个字符串的摘要算法,请输出给定字符串的摘要值
1、去除字符串中非字母的符号
2、如果出现连续字符(不区分大小写),则输出:该字符(小写)+i车续出现的次数
3、如果是非连续的字符(不区分大小写),则输出:该字符(小写)+该字母之后字符串中出现
字符的次数
4、对按照以上方式表示后的字符串进行排序:字母和紧随的数字字作为一组进行排序,数字
在前,数字相同的,则按字母进行排序,字母小的在前
输入输出
输入
一行字符串,长度为[1,200]
输出
摘要字符串

Python语言 思路
1.使用正则表达式re.sub函数去除输入字符串中的所有非字母字符。
2.将处理后的字符串转换为小写(因为摘要算法不区分大小写)。
3.初始化一个空列表summary_parts来存储每个字符及其出现次数的字事。
4.通过一个while循环遍历处理后的字符串:
对每个字符,初始化计数器count为1。
使用一个内部while循环来检查当前字符是否连续出现,如果是,则增加count值并
引 i。
。如果count值为1(即字符不是连续的),使用count函数计算当前字符在其后面字符
出现次数。
。将字符及其出现次数格式化为一个字符串(如"a2"),然后添加到summary_parts 列
。移动索引 以检查下一个字符。
5.使用sort函数对summary_parts列表进行排序,排序键由两部分组成:首先是数字部分的
(-int(x[1:]),其次是字符部分的升序(x[0])。
6.使用join函数将排序后的摘要部分合并为一个字符串并返回。

"""
import re
from collections import Counter

def summarize_string(s):
    # 步骤1：去除字符串中的非字母字符
    s = re.sub(r'[^a-zA-Z]', '', s)

    # 步骤2和3：处理连续字符和非连续字符
    summary_parts = []  # 存储摘要部分的列表
    i = 0
    s_lower = s.lower()  # 将字符串转换为小写，便于处理不区分大小写的字符
    while i < len(s_lower):
        char = s_lower[i]
        count = 1  # 初始化当前字符的计数为1
        # 检查连续字符
        while i + 1 < len(s_lower) and s_lower[i] == s_lower[i + 1]:
            count += 1  # 如果字符连续，则计数增加
            i += 1
        if count == 1:
            # 如果是非连续字符，则计算其在后续字符串中的出现次数
            count = s_lower.count(char, i+1)
        # 将字符及其出现次数的字符串添加到列表中
        summary_parts.append(f"{char}{count}")
        i += 1

    # 步骤4：对摘要部分进行排序
    # 排序时，先按照数字大小降序排列，如果数字相同则按字母升序排列
    summary_parts.sort(key=lambda x: (-int(x[1:]), x[0]))

    # 将排序后的摘要部分组合成一个字符串并返回
    return ''.join(summary_parts)

# 示例用法：
input_string = "abcde"
print(summarize_string(input_string))
