"""
### Problem Description
Given a string `s`, find a substring that satisfies the following two conditions:
1. Any character in this substring appears at most **2 times**.
2. This substring **does not contain** a specified character.

Please find the length of the **longest** substring that meets these criteria.

---

### Input and Output

**Input:**
- First line: A single character (the specified character to exclude), which can be a digit (0-9) or a letter (a-z, A-Z).
- Second line: The string `s`, where each character is also a digit or letter (0-9a-zA-Z), and its length ranges from 1 to 10,000.

**Output:**
- An integer: the length of the longest valid substring.
- If no valid substring exists, return **0**.

---

Do you want me to also provide the corresponding Python code implementation for this problem?

# Python Language Approach
1. First, we define a **specified character** (`specified_char`) and a **string** (`s`).
2. Initialize the starting position (`left`) of the substring to 0, and set the length of the longest substring (`max_length`) to 0.
3. Create a character count dictionary (`char_count`) to record the occurrence frequency of each character.
4. Iterate over each character in the string `s` using the index `i`.
5. If the current character (`charnum`) is equal to the specified character (`specified_char`), it means we need to restart the search for the substring from the position immediately after this character. Therefore, we clear the character count dictionary (`char_count`) and update the starting position (`left`) of the substring to `i + 1`.
6. If the current character (`charnum`) is **not** equal to the specified character (`specified_char`), it means we can add this character to the substring.
7. Update the character count: increment the count of the current character (`charnum`) by 1. Use `char_count.get(charnum, 0)` to retrieve the character’s count from the dictionary; if the character does not exist in the dictionary, the default count is 0.
8. If the count of the current character (`charnum`) reaches 3, it means the character has exceeded the limit of occurrences in the substring. At this point, we need to remove the **leftmost character** of the substring (i.e., the character at the `left` index). We increment `left` by 1 and decrement the count of the removed character by 1.
9. In each iteration, update the length of the longest substring by comparing the length of the current substring with `max_length`.
10. Finally, return the length of the longest substring as the result.

### Key Terminology Notes
- **specified character**: 指定字符
- **substring**: 子串
- **character count dictionary**: 字符计数字典
- **occurrence frequency**: 出现次数/频率
- **leftmost character**: 最左边的字符
"""


def find_longest_substring(specified_char, s):
    left = 0  # 子串的起始位置
    max_length = 0  # 最长子串的长度
    char_count = {}  # 字符计数字典，记录字符出现的次数
    
    for i in range(len(s)):
        charnum = s[i]  # 当前字符
        
        if charnum == specified_char:
            char_count.clear()  # 遇到指定字符，清空字符计数字典
            left = i + 1  # 更新子串的起始位置为指定字符的下一个位置
            continue
        
        char_count[charnum] = char_count.get(charnum, 0) + 1  # 更新字符计数
        
        while char_count[charnum] == 3:
            rm_char = s[left]  # 需要移除的字符
            left += 1  # 更新子串的起始位置，排除最左边的字符
            char_count[rm_char] -= 1  # 更新字符计数，减去移除的字符的计数
        
        max_length = max(max_length, i - left + 1)  # 更新最长子串的长度
    
    return max_length


specified_char = 'D'
input_string = 'ABACA123D'
result = find_longest_substring(specified_char, input_string)
print(result)


