"""
·题目描述
给定一个字符串，只包含大写字母，求在包含同一字母的子串中，长度第k长的子串的长度，相同字母只取最长的那个子串
咖输入输出
输入
第一行有一个子串(1<长度<=100)，只包含大写字母第二行为k的值
输出
输出连续出现次数第k多的字母的次数

输入
AAAAHHHBBCDHHHH
3


输出
2

输入
AABAAA
2


输出
1

说明：
同一字母连续出现的最多的是A,三次;
第二多的还是A,两次,但A已经存在最大连续次数三次,故不考虑;
下个最长子串是B,所以输出1


说明:
同一字母连续出现的最多的是A和H,出现四次;
第二多的是H, 3次,但是H已经存在4个连续的,故不考虑;
下个最长子串是BB，所以最终答案应该输出2


1.遍历给定的字符串，记录每个字母的最长连续出现次数。
2.在遍历过程中，如果遇到不同的字母，就更新当前连续子串的字母和长度，并将当前连续子串的最长连续出现次数更新到max counts字典中。
3.将max counts字典中的值按照隆序排序。
4.根据给定的k值，返回第k长的子串的长度，如果k大于排序后的列表长度，则返回-1表示没有第k长的子串。
"""

def find_kth_longest_substring(s, k):
    # 存储每个字母的最长连续出现次数
    max_counts = {}

    # 当前连续子串的字母和长度
    current_char = s[0]
    current_count = 1

    # 遍历字符串，找到每个字母的最长连续出现次数
    for char in s[1:] + '#':  # 加上'#'是为了处理字符串最后一个字符的情况
        if char == current_char:
            current_count += 1  # 如果字符与当前字符相同，则增加计数
        else:
            # 如果字符不同，说明当前连续子串结束，更新最长出现次数
            if current_char not in max_counts or current_count > max_counts[current_char]:
                max_counts[current_char] = current_count

            # 重置当前连续子串的字母和长度
            current_char = char
            current_count = 1

    # 将最长连续出现次数按照次数降序排列
    sorted_counts = sorted(max_counts.values(), reverse=True)

    # 根据k值获取第k长的子串长度
    # 如果k值大于排序后的列表长度，则输出-1（表示没有第k长的子串）
    return sorted_counts[k - 1] if k <= len(sorted_counts) else -1


# 读取输入
input_string = input().strip()
k = int(input().strip())

# 调用函数并输出结果
print(find_kth_longest_substring(input_string, k))



