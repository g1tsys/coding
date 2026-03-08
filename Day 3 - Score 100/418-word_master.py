"""
*题目问题：**  
定一个字符串数组 `words` 和一个字符串 `chars`，判断 `words` 中有多少个单词可以用 `chars` 中的字符拼写出来。其中 `chars` 可能包含小写字母和万能字符 `?`（可代替任意一个小写字母），每个字符（包括 `?`）在拼写一个单词时只能使用一次。

*输入格式：**  
 第 1 行：整数 N，表示 `words` 数组的长度。  
 第 2 至 N+1 行：每行一个字符串，表示 `words` 中的单词。  
 第 N+2 行：字符串 `chars`，用于拼写单词。

*输出格式：**  
 一个整数，表示能拼写出的单词个数。若没有单词能拼写，输出 0。

图片内容为一段 Python 代码，用于判断是否可以用 `chars` 中的字符拼写 `word`。代码逻辑如下：

1. 定义函数 `can_spell(word, chars)`，用于判断是否能用 `chars` 拼写 `word`。
2. 统计 `chars` 中每个字符的出现次数，存入字典 `char_count`。
3. 遍历 `word` 中的每个字符：
   - 若字符在 `char_count` 中且计数 > 0，则计数减 1。
   - 否则，返回 `False`（表示无法拼写）。
4. 若所有字符都能匹配，则返回 `True`。

> 注意：此代码**未处理万能字符 `?`**，仅适用于纯字母匹配场景。若需支持 `?`，需额外逻辑判断。
"""
# 定义一个函数来判断是否可以用chars拼写出word
def can_spell(word, chars):
    # 对chars中的每个字符进行计数
    char_count = {}
    for char in chars:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # 检查word中的每个字符是否可以在chars中找到
    for w in word:
        if w in char_count and char_count[w] > 0:
            char_count[w] -= 1
        elif '?' in char_count and char_count['?'] > 0:
            char_count['?'] -= 1
        else:
            # 如果word中的字符在chars中找不到，或者没有足够的'?'
            # 则返回False，表示不能拼写出word
            return False
    return True


# 读取words的个数
N = int(input().strip())

# 读取words中的每个单词
words = []
for _ in range(N):
    words.append(input().strip())

# 读取chars字符串
chars = input().strip()

# 初始化掌握的单词个数为0
count = 0

# 遍历words中的每个单词，检查是否能够拼写
for word in words:
    if can_spell(word, chars):
        count += 1  # 如果能够拼写，掌握单词个数加1

# 输出掌握的单词个数
print(count)
