"""
The problem is to find the **length of the longest substring** in a **circular string** (i.e., a string where the first and last characters are connected) that contains an **even number of 'o' characters**.

### Problem Summary:
- Input: A string `s` consisting of lowercase letters.
- Output: An integer representing the **length of the longest substring** with an **even number of 'o' characters**.
- The string is **circular**, meaning the end connects to the beginning.

---

### Python Language Thought Process:

1. **Understand the Circular Nature of the String:**
   - Since the string is circular, we can treat it as if it is doubled in length (i.e., `s + s`), but only consider substrings of length up to the original string length.

2. **Count the Total 'o' Characters:**
   - First, count the total number of 'o's in the string.
   - If the total number of 'o's is **even**, then the entire string is a valid substring, and its length is the answer.
   - If the total number of 'o's is **odd**, then we need to **remove one 'o'** to make the count even. The result will be the original string length minus 1.

3. **Find the Longest Valid Substring:**
   - If the total number of 'o's is even, the answer is simply the length of the string.
   - If the total number of 'o's is odd, the answer is the length of the string minus 1.

---

### Example Walkthrough:

#### Input:

s = "ooxo"


#### Step-by-Step:

1. **Count 'o's in the string:**
   - 'o', 'o', 'x', 'o' → total of 3 'o's (odd).

2. **Since the count is odd, we need to remove one 'o' to make it even.**
   - The maximum length of the substring with even 'o's is `4 - 1 = 3`.

3. **Output:**
   
   3
   

---

### Python Code (Example):

python
def longest_even_substring(s):
    o_count = s.count('o')
    if o_count % 2 == 0:
        return len(s)
    else:
        return len(s) - 1

# Example usage
s = "ooxo"
print(longest_even_substring(s))  # Output: 3


Let me know if you'd like a more detailed explanation or a version that handles all edge cases.
"""


# 输入字符串
s = input().strip()

# 计算字符串中'o'字符的总次数
total_o_count = s.count('o')

# 如果字符串中的'o'字符总次数是偶数
if total_o_count % 2 == 0:
    # 直接返回字符串长度，因为整个字符串已经满足条件
    print(len(s))
else:
    # 如果字符串中的'o'字符总次数是奇数
    # 需要删除一个'o'字符使得剩余部分'o'的次数变为偶数
    print(len(s) - 1)

