"""
> **Question Translation**: Given a string containing only letters (no spaces), count the occurrences of each letter (case-sensitive), and output the letters and their counts in descending order of frequency. If counts are the same, sort by natural order, with lowercase letters appearing before uppercase letters.

> **Python Language Thought Process**:
1. Use the `collections.Counter` module to count the frequency of each letter.
2. Define a custom sorting function that:
   - Sorts primarily by frequency in descending order.
   - If frequencies are equal, sorts by natural order, with lowercase letters appearing before uppercase letters.
3. Use the `sorted()` function with the custom sorting function to sort the letter-count pairs.
4. Format the output as required: use colons (`:`) to separate letters and counts, and semicolons (`;`) to separate the pairs. Ensure a semicolon is at the end.

> **Example Walkthrough**:
Input: `"aAbBcC"`

1. Count the frequencies:
   - `a`: 1
   - `A`: 1
   - `b`: 1
   - `B`: 1
   - `c`: 1
   - `C`: 1

2. Sort the letters:
   - Since all frequencies are equal, sort by natural order, with lowercase letters before uppercase letters.
   - Sorted order: `a`, `A`, `b`, `B`, `c`, `C`

3. Output:
   ```
   a:1;A:1;b:1;B:1;c:1;C:1;
   ```
"""
from collections import Counter, OrderedDict

def count_letters(string):
    # 统计字母出现次数
    letter_counts = Counter(string)

    # 自定义排序函数
    def custom_sort(item):
        letter, count = item
        return (-count, letter.swapcase())

    # 排序字母出现次数
    sorted_counts = sorted(letter_counts.items(), key=custom_sort)

    # 输出结果
    for letter, count in sorted_counts:
        print(f"{letter}:{count};", end="")
    print()

# 读取输入的字符串
string = input()

# 统计字母出现次数并输出结果
count_letters(string)


