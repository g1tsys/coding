"""
题目描述
开头和结尾都是元音字母(aeiouAEIOU)的字符串为元音字符串,其中混杂的非元音字母数量为其瑕疵
度。比如:
1、"a"、"aa"元音字符串,其瑕疵度都为0
2、"aiur"不是元音字符串(结尾不是元音字符)
3、"abira"是元音字符串,其瑕疵度为2
给定一个字符串,请找出指定瑕疵度的最长元音字符子串,并输出其长度,如果找不到满足条件的元音
字符子串,输出0。
子串:字符串中任意个连续的字符组成的子序列称为该字符串的子串
输入输出口
输入
首行输入是一个整数,表示预期的瑕疵度flaw,取值范围[0,655355]。
接下来一行是一个仅由字符a-z和A-Z组成的字符串,字符串长度(0,655535]
输出
输出为一个整数,代表满足条件的元音字符子串的长度。

Python语言 思路
1.定义辅助函数:首先,定义一个辅助函数is_vowel(ch)来判断给定的字符ch是否是元音字母(a,e,
i,o,u)
2.遍历和判断:为了找到满足条件的最长子串,我们对原始字符串进行遍历。遍历的目的是找到所有可能的
子串起点(即元音字母的位置)。
3.内层遍历:对于每一个找到的起点,我们从该位置开始向字符串的末尾进行内层遍历。这个过程中,我们
统计非元音字母的个数(即瑕疵度),直到瑕疵度超过给定的值。在这个过程中,每当我们遇到一个元音
字母,并且当前的瑕疵度正好等于给定的瑕疵度时,我们就找到了一个满足条件的子串。
4.更新最长子串长度:在内层遍历过程中,每当找到一个满足条件的子串时,我们就计算它的长度,并与当
前记录的最长子串长度进行比较。如果当前找到的子串更长,我们就更新记录的最长子串长度。
5.输出结果:遍历完成后,我们得到了满足条件的最长子串的长度。最后,输出这个长度。
Problem Description
A string that starts and ends with a vowel letter (aeiouAEIOU) is called a vowel string. The number of non-vowel letters mixed in it is its flaw degree. For example:
1. "a" and "aa" are vowel strings, and their flaw degrees are both 0.
2. "aiur" is not a vowel string (the ending is not a vowel character).
3. "abira" is a vowel string, and its flaw degree is 2.

Given a string, please find the longest vowel substring with a specified flaw degree and output its length. If no such vowel substring is found, output 0.

Substring: A subsequence consisting of any number of consecutive characters in a string is called a substring of the string.

Input/Output
Input
The first line of input is an integer representing the expected flaw degree, with a value range of [0, 65535].
The next line is a string consisting only of characters a-z and A-Z, with a length in the range (0, 655535].

Output
Output an integer representing the length of the vowel substring that meets the conditions.
Python Language Approach
1. Define an auxiliary function: First, define an auxiliary function is_vowel(ch) to determine whether a given character ch is a vowel letter (a, e, i, o, u).
2. Traversal and judgment: To find the longest substring that meets the conditions, we traverse the original string. The purpose of the traversal is to find all possible starting points of the substring (i.e., the positions of vowel letters).
3. Inner traversal: For each found starting point, we perform an inner traversal from that position to the end of the string. During this process, we count the number of non-vowel letters (i.e., the defect degree) until the defect degree exceeds the given value. In this process, whenever we encounter a vowel letter and the current defect degree is exactly equal to the given defect degree, we have found a substring that meets the conditions.
4. Update the maximum substring length: During the inner traversal, whenever a substring that meets the conditions is found, we calculate its length and compare it with the currently recorded maximum substring length. If the currently found substring is longer, we update the recorded maximum substring length.
5. Output the result: After the traversal is completed, we obtain the length of the longest substring that meets the conditions. Finally, output this length.
"""

# 检查一个字符是否是元音字符的函数
def is_vowel(ch):
    """检查字符是否为元音"""
    # 将字符转换为小写，并检查它是否在元音字符集中
    return ch.lower() in "aeiou"

# 查找具有指定瑕疵度的最长子串的函数
def find_longest_substring_with_flaw(s, flaw):
    # 获取输入字符串的长度
    n = len(s)
    # 初始化最长子串长度为0
    max_length = 0
    # 外层循环：遍历字符串的每个字符
    for i in range(n):
        # 如果当前字符是元音字符，则考虑它作为子串的起始位置
        if is_vowel(s[i]):
            # 初始化当前子串的瑕疵度为0
            current_flaw = 0
            # 内层循环：从当前元音字符开始，向后遍历
            for j in range(i, n):
                # 如果当前字符不是元音字符，瑕疵度加1
                if not is_vowel(s[j]):
                    current_flaw += 1
                # 如果瑕疵度超过了允许的最大值，结束内层循环
                if current_flaw > flaw:
                    break
                # 如果当前字符是元音字符且瑕疵度与预期相符，更新最长子串长度
                if is_vowel(s[j]) and current_flaw == flaw:
                    max_length = max(max_length, j - i + 1)
    # 返回最长子串的长度
    return max_length

# 读取输入数据
flaw = int(input())  # 预期的瑕疵度
s = input()  # 输入的字符串

# 计算并输出结果
print(find_longest_substring_with_flaw(s, flaw))


