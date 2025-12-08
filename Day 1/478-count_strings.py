
"""

Based on the web page content, here's a translation and explanation of the programming problem:

## Problem Translation

**Description:**
Given M characters (0 < M ≤ 30) from a-z, select any characters (each character can only be used once) to form a string of length N (0 < N ≤ 5).

**Constraint:** The same characters cannot be adjacent to each other.

**Task:** Calculate how many valid strings can be formed. Return 0 if input is invalid or no valid strings can be formed.

**Input:** A character list and target string length, separated by space
**Output:** Number of valid strings that meet the conditions

## Solution Approach (Chain of Thought)

This is a **backtracking/permutation problem** with constraints:

1. **Count character frequencies** - Track how many of each character we have
2. **Use backtracking** to build strings character by character
3. **Pruning condition** - Ensure the next character is different from the last character added
4. **Base case** - When string length reaches N, count it as one valid solution
5. **Try each available character** - For each position, try placing each character type (if available)

## Example Walkthrough

**Input:** `"aab 2"`
- Characters: a, a, b (2 a's and 1 b)
- Target length: 2

**Process:**
1. Start with empty string
2. Try 'a' first → "a" (1 'a' remaining)
   - Next must be ≠ 'a', try 'b' → "ab" ✓ (length 2, valid!)
3. Try 'b' first → "b" (2 a's remaining)
   - Next can be 'a' → "ba" ✓ (length 2, valid!)

**Result:** 2 valid strings ("ab" and "ba")

The algorithm systematically explores all possibilities while respecting the "no adjacent duplicates" constraint and character availability.
"""



from collections import Counter

def count_strings(chars, N):
    """
    计算给定字符列表能拼接出的满足条件的字符串个数

    参数:
    chars -- 字符列表
    N -- 结果字符串的长度

    返回值:
    满足条件的字符串个数
    """
    if not chars or N <= 0 or N > 5 or len(chars) > 30:
        return 0

    # 统计每个字符的数量
    char_count = Counter(chars)

    # 使用回溯法计算可能的字符串个数
    def backtrack(last_char, length):
        if length == N:
            return 1
        count = 0
        for char, available in char_count.items():
            if char != last_char and available > 0:
                # 选择当前字符，更新计数器
                char_count[char] -= 1
                count += backtrack(char, length + 1)
                # 回溯，恢复计数器
                char_count[char] += 1
        return count

    # 从一个空字符开始回溯
    return backtrack('', 0)

# 解析输入，并调用函数计算结果
def main():
    input_str = input()
    parts = input_str.split()
    if len(parts) != 2:
        return 0

    chars, N_str = parts
    N = int(N_str)
    return count_strings(list(chars), N)


print(main())
