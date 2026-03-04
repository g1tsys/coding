"""
### Extracted Full Content
---
#### Subscription Notice
**Subscribe to this column to unlock online OJ question-swiping permissions**

#### Column Introduction
🍎Column Introduction: The latest summary of Huawei OD machine test questions is solved in five languages: C++, Java, Python, C, and JS. The ideas and analysis of each question are very detailed, and it supports online OJ review and problem-solving!!! Get permission after subscribing, add new illustrated ideas, problem solving, multi-example testing, reference analysis of ideas with more than 100 words, continuous updates, code is only for learning reference

Question bank learning: *Huawei OD Technical Interview Hand Tear Questions*

---
### I. Title
#### 🎃Title Description
Given a string `s`, you can only perform a transformation at most once, and return the smallest string you can get after the transformation (compare it in lexicographical order).

Transformation rule: swap characters at any two different positions in a string

#### 🎃Input Output
**Enter**
A string of lowercase letters `s`

**Output**
The minimum string obtained by transforming as required.

Here's the step-by-step extraction of the algorithm:

1.  Convert the input string into a list so that the characters can be modified.
2.  Initialize the swap counter `t` to `-1` to record whether a swap operation has occurred.
3.  Start at index `0` and iterate over all elements in the list except the last element.
4.  For the currently traversed element `l[i]`, find the smallest character `tmp2` in the sublist after it.
5.  If the current element `l[i]` is greater than the minimum character `tmp2`, it means that a swap operation is required.
6.  If the minimum character `tmp2` appears multiple times after the current element, find the index of the last minimum character:
    *   Find the index of all minimum characters `tmp2` using list comprehensions and enumerate functions.
    *   Select the last index as the swap position.
7.  If the minimum character `tmp2` appears only once after the current element, directly find the index of the character.
8.  Swap the current element `l[i]` and the found character `l[index]`.
9.  Add one to the swap counter `t` to indicate that a swap occurred.
10. After finding the first position to be swapped, break out of the loop.
11. If the swap counter `t` is still `-1`, it means that no swap operation has occurred, that is, the string is already in the form with the smallest lexicographic order.
12. Return the original string as the result.
13. Otherwise, convert the list to a string and return it as a result.

---

Would you like me to translate this into a complete Python function that implements this exact logic?

"""

def rearrange_string(s):
    l = list(s)  # 将输入字符串转换为列表
    t = -1  # 初始化交换计数器
    for i in range(len(l) - 1):  # 遍历列表中除最后一个元素之外的所有元素
        tmp2 = min(l[i + 1:])  # 找到当前元素后面的最小字符
        if l[i] > tmp2:  # 如果当前元素大于最小字符，则需要进行交换
            if l[i + 1:].count(tmp2) > 1:  # 如果最小字符在当前元素后面出现多次
                indices = [j for j, char in enumerate(l[i + 1:]) if char == tmp2]  # 获取所有最小字符的索引
                index = i + 1 + indices[-1]  # 获取最后一个最小字符的索引
            else:
                index = l.index(tmp2, i + 1)  # 获取最小字符的索引
            l[i], l[index] = l[index], l[i]  # 交换当前元素和最小字符
            t += 1  # 交换计数器加一
            break  # 找到第一个需要交换的位置后，结束循环
    if t == -1:  # 如果没有发生交换
        return s  # 返回原始字符串
    return "".join(l)  # 将列表转换为字符串并返回


input_string = input()
result = rearrange_string(input_string)
print(result)
