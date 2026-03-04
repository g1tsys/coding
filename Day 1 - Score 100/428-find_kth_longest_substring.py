
"""
### Problem Translation

**Problem Description:**
Given a string containing only uppercase letters, find the length of the **k-th longest substring** where each substring consists of consecutive identical letters. For each letter, only consider its longest consecutive occurrence.

**Input:**
- Line 1: A string (1 < length ≤ 100) containing only uppercase letters
- Line 2: An integer k

**Output:**
- The length of the k-th longest consecutive substring

---

### Solution Chain of Thought (Python)

1. **Track Maximum Consecutive Counts:** Use a dictionary (`max_counts`) to store the longest consecutive count for each letter.

2. **Iterate Through String:** Traverse the string while tracking:
   - Current character (`current_char`)
   - Current consecutive count (`current_count`)

3. **Update on Character Change:** When encountering a different character, update the dictionary with the maximum count for that character.

4. **Sort in Descending Order:** Extract all maximum counts and sort them in descending order to rank consecutive substrings by length.

5. **Return k-th Element:** Return the k-th element from the sorted list (or -1 if k exceeds the number of unique letters).

---
"""
### Annotated Code with Example Walkthrough

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

# Example Walkthrough:
# Input: "AAABBBCCCCDD", k = 2
# 
# Step 1 - Identify consecutive substrings:
#   - 'A' appears 3 times consecutively
#   - 'B' appears 3 times consecutively
#   - 'C' appears 4 times consecutively
#   - 'D' appears 2 times consecutively
#
# Step 2 - max_counts = {'A': 3, 'B': 3, 'C': 4, 'D': 2}
#
# Step 3 - Sort in descending order: [4, 3, 3, 2]
#
# Step 4 - k = 2, so return sorted_counts[1] = 3
# Output: 3

