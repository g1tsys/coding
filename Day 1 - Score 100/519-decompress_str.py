"""
> The text is in Chinese and discusses a problem related to decompressing a compressed string according to a specific rule. The problem is part of the Huawei OD (OD stands for "Online Judge") coding interview questions. The goal is to determine whether the input string is a valid compressed string, and if it is, decompress it back to its original form. If it's not valid, output `!error`.

---

### **Problem Translation (Python Language Thought Process)**

#### **Problem Statement (Translated):**
There is a simple compression algorithm that works on strings consisting only of lowercase English letters. It compresses sequences of **more than two identical letters** into the number of consecutive letters followed by the letter itself. Other parts of the string remain unchanged. For example:

- `"aaabbccccd"` → `"3abb4cd"`

You are required to write a function to **decompress** a given string. If the input string is **not a valid compressed string**, output `"!error"`.

#### **Input/Output:**
- **Input:** A string of ASCII characters (length ≤ 100)
- **Output:** 
  - If valid, output the decompressed string.
  - If invalid, output `"!error"`

---

### **Python Language Thought Process**

1. **Check Validity of the Input String:**
   - The input must consist of a valid pattern of digits and letters.
   - A digit must be followed by a letter, and the digit must not be `1` or `2` (since compression only applies to sequences of more than two letters).
   - A letter must not be immediately followed by a digit unless the digit is part of a valid sequence.

2. **Decompress the String:**
   - Traverse the string and split it into parts that are either:
     - A number (e.g., `"3"`, `"4"`)
     - A letter (e.g., `"a"`, `"b"`)
   - For each number-letter pair, repeat the letter the number of times specified.
   - For letters not preceded by a number, just append them directly.

3. **Edge Cases:**
   - A single letter (e.g., `"a"`) is valid.
   - A letter with a number `1` or `2` is invalid (since compression would not have been applied).
   - A number not followed by a letter is invalid (e.g., `"34"`).

---

### **Example Walkthrough**

#### **Input:** `"3abb4cd"`

1. **Parse the String:**
   - `"3"` → number
   - `"a"` → letter → repeat `"a"` 3 times → `"aaa"`
   - `"b"` → letter → append `"b"`
   - `"b"` → letter → append `"b"`
   - `"4"` → number
   - `"c"` → letter → repeat `"c"` 4 times → `"cccc"`
   - `"d"` → letter → append `"d"`

2. **Combine the Results:**
   - `"aaa" + "b" + "b" + "cccc" + "d"` → `"aaabbccccd"`

3. **Output:** `"aaabbccccd"`

---

### **Example of Invalid Input: `"3b"`

- `"3"` is followed by `"b"` (valid).
- However, the number `3` is followed by only one letter.
- The original string would have been `"bbb"`, which would compress to `"3b"`.
- But the decompression would be `"bbb"`, which is valid.

Wait — this is **valid**. So why is it not an error?

Actually, the problem says that **only sequences of more than two identical letters are compressed**. So a sequence of exactly 3 letters is **valid** to be compressed.

So `"3b"` is a valid input, and decompresses to `"bbb"`.

---

### **Example of Invalid Input: `"2a"`

- `"2"` is followed by `"a"`.
- The original string would have been `"aa"`, which **should not be compressed** (since it's only 2 letters).
- So `"2a"` is **invalid**.

#### **Output:** `"!error"`

---

Let me know if you'd like the Python code for this solution!

"""


def decompress_and_validate(input_string):
    i = 0  # 初始化索引，用于遍历输入字符串
    n = len(input_string)  # 获取输入字符串的长度
    decompressed = ""  # 用于存储解压缩后的字符串

    while i < n:  # 循环遍历字符串的每一个字符
        if input_string[i].isdigit():  # 检查当前字符是否是数字
            num_start = i  # 记录数字的起始位置
            while i < n and input_string[i].isdigit():  # 找到完整的数字
                i += 1
            number = int(input_string[num_start:i])  # 将数字字符串转换为整数

            if number <= 2:  # 检查数字是否小于或等于2，不合法
                return "!error"

            if i < n and input_string[i].islower():  # 检查数字后面是否跟着小写字母
                decompressed += input_string[i] * number  # 将字母按数字次数重复添加到解压字符串
                i += 1
            else:  # 如果数字后不是小写字母，格式不合法
                return "!error"
        elif input_string[i].islower():  # 检查当前字符是否是小写字母
            decompressed += input_string[i]  # 直接添加到解压字符串
            i += 1
        else:  # 如果既不是数字也不是小写字母，格式不合法
            return "!error"

    # 内部函数，用于压缩字符串
    def compress(s):
        compressed = ""  # 用于存储压缩后的字符串
        count = 1  # 初始化计数器，用于统计连续字符的数量
        for j in range(1, len(s)):  # 从第二个字符开始遍历
            if s[j] == s[j - 1]:  # 如果当前字符与前一个字符相同
                count += 1  # 计数器加一
            else:
                if count > 2:  # 如果连续字符数量大于2
                    compressed += str(count) + s[j - 1]  # 添加数字和字符到压缩字符串
                else:
                    compressed += s[j - 1] * count  # 直接添加字符本身
                count = 1  # 重置计数器为1
        # 处理字符串末尾的字符
        if count > 2:
            compressed += str(count) + s[-1]
        else:
            compressed += s[-1] * count
        return compressed

    # 比较重新压缩后的字符串与输入字符串
    if compress(decompressed) == input_string:
        return decompressed  # 如果相同，返回解压缩后的字符串
    else:
        return "!error"  # 如果不同，返回"!error"


a=input()
print(decompress_and_validate(a))

