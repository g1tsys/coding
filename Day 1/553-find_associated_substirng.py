"""
# Problem Translation and Explanation

## Problem Description

Given two strings `str1` and `str2`, if **any permutation (anagram)** of `str1` is a substring of `str2`, then `str1` is considered an "associated substring" of `str2`.
Return the starting position of the substring in `str2`. If it's not an associated substring, return `-1`.
Both strings have lengths in the range `[1, 100000]`.

## Key Concept
This is essentially asking: **Find if any anagram of `str1` exists as a contiguous substring in `str2`**.
## Approach (Sliding Window)

The solution uses a **sliding window technique** with character frequency counting:
# Python Solution Thought Process (Translated)

Here's the step-by-step thought process from the Python section:

1. **Get the lengths of str1 and str2**. If the length of str1 is greater than str2, directly return -1.
2. **Use Counter to calculate the character frequency of str1**.
3. **Initialize the sliding window's character frequency**, taking the first `len1` characters of str2.
4. **Check if the first window matches str1**, i.e., whether the window's character frequency equals str1's character frequency. If it matches, return starting position 0.
5. **Use sliding window to traverse str2**, starting from index `len1`, moving right one position at a time.
6. **Each time the window moves right**, add the new character and remove the leftmost character from the window.
7. **If the frequency of the removed character becomes 0**, delete that key.
8. **Check if the current window matches str1**, i.e., whether the window's character frequency equals str1's character frequency. If it matches, return the current match's starting position.
9. **If we finish traversing str2 and still haven't found a matching substring**, return -1.

---

This approach uses a **sliding window with hash map (Counter)** to efficiently check if any permutation of str1 exists as a contiguous substring in str2, with O(n) time complexity.
## Example Walkthrough

**Example 1:**

str1 = "abc"
str2 = "defbcaghijk"


**Step-by-step:**

1. `str1` frequency: `{a:1, b:1, c:1}`
2. Check windows of size 3 in `str2`:
   - Window `"def"` → `{d:1, e:1, f:1}` ❌
   - Window `"efb"` → `{e:1, f:1, b:1}` ❌
   - Window `"fbc"` → `{f:1, b:1, c:1}` ❌
   - Window `"bca"` → `{b:1, c:1, a:1}` ✅ **Match!**

3. Return starting position: `3`

**Example 2:**

str1 = "ab"
str2 = "cdefg"


- No window of size 2 in `str2` contains both 'a' and 'b'
- Return: `-1`

**Example 3:**

str1 = "aab"
str2 = "xbaayz"


1. `str1` frequency: `{a:2, b:1}`
2. Check windows:
   - `"xba"` → `{x:1, b:1, a:1}` ❌ (needs 2 a's)
   - `"baa"` → `{b:1, a:2}` ✅ **Match!**
3. Return: `1`

The algorithm efficiently finds anagram substrings in O(n) time using the sliding window technique.

"""




from collections import Counter  # 导入Counter用于计算字符频率


def find_associated_substring(str1, str2):
    len1, len2 = len(str1), len(str2)  # 获取str1和str2的长度

    # 如果str1长度大于str2，则不可能是其子串，直接返回-1
    if len1 > len2:
        return -1

    # 计算str1的字符频率
    str1_count = Counter(str1)
    # 初始化滑动窗口的字符频率
    window_count = Counter(str2[:len1])

    # 检查第一个窗口是否匹配
    if window_count == str1_count:
        return 0  # 如果匹配，返回起始位置0

    # 滑动窗口遍历str2
    for i in range(len1, len2):
        # 窗口右移一位，加入新字符
        window_count[str2[i]] += 1
        # 移除窗口左边的字符
        window_count[str2[i - len1]] -= 1

        # 如果移除字符的频率变为0，删除该键
        if window_count[str2[i - len1]] == 0:
            del window_count[str2[i - len1]]

        # 检查当前窗口是否匹配
        if window_count == str1_count:
            return i - len1 + 1  # 返回当前匹配的起始位置

    return -1  # 如果没有找到匹配子串，返回-1



str1,str2 = input().split()
result = find_associated_substring(str1, str2)
print(result)  

