"""
The question is as follows:

> Given a string `s`, you can perform **at most one swap** of any two characters in the string. Return the **lexicographically smallest** string that can be obtained after this operation.

### Python Language Thought Process

1. Convert the input string `s` into a list for easier character manipulation.
2. Initialize an exchange counter `t` to `-1` to track if any swap occurs.
3. Traverse the list from the first character to the second-to-last character.
4. For each character `l[i]`, search the rest of the list for the smallest character `tmp2`.
5. If `l[i]` is greater than `tmp2`, a swap is needed:
   - If `tmp2` appears multiple times in the remaining part of the list, find the **last occurrence** of `tmp2`.
   - If `tmp2` appears only once, directly get its index.
6. Swap `l[i]` with `tmp2` and increment the counter `t`.
7. After the first swap, break the loop to ensure only one swap is performed.
8. If `t` remains `-1`, no swap occurred, so return the original string.
9. Otherwise, return the modified list as a string.

---

### Example Walkthrough

**Input:** `s = "cba"`

1. Convert to list: `['c', 'b', 'a']`
2. Start with `i = 0`, `l[i] = 'c'`
3. Look for the smallest character in the sublist `['b', 'a']` → it is `'a'`
4. Since `'c' > 'a'`, a swap is needed.
5. The index of `'a'` is `2`.
6. Swap `l[0]` with `l[2]` → `['a', 'b', 'c']`
7. Increment `t` to `0` and break the loop.
8. Return the new string: `"abc"`

---

This approach ensures that you get the smallest possible string after **at most one swap**.
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
