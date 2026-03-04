"""
# Translation and Explanation

## Problem Statement

Given two strings `s1` and `s2` and a positive integer `k`, where `s1` has length `n1` and `s2` has length `n2`, find a substring in `s2` that satisfies:

- The substring length is `n1 + k`
- The substring contains all letters from `s1`
- Each letter in the substring appears at least as many times as it does in `s1`

We call this "s2 covers s1 with redundancy length k". Return the **index of the first character** of the **leftmost** such substring in `s2`. If no such substring exists, return `-1`.

**Input:**
- Line 1: String `s1`
- Line 2: String `s2`
- Line 3: Integer `k`
- Both strings contain only lowercase letters

**Output:**
- The starting index of the leftmost valid substring, or `-1` if none exists

## Python Approach

1. **Count character frequencies in s1**: Use an array of size 26 to store how many times each letter appears in `s1`.
2. **Initialize sliding window**: Set `start = 0` and `end = 0` to represent the window boundaries. Create another array to track character counts in the current window.
3. **Expand the window**: Move `end` pointer to the right, adding characters to the window and updating their counts.
4. **Check validity when window reaches target size**: When the window size equals `n1 + k`, check if all character counts in the window are ≥ their counts in `s1`.
5. **Slide the window**: If valid, return `start` index. If not valid, shrink from the left by incrementing `start` and updating counts.
6. **Continue until end of s2**: If no valid substring is found, return `-1`.

## Example Walkthrough

**Input:**
```text
s1 = "abc"
s2 = "dabbcac"
k = 1
```

**Step-by-step:**

- `n1 = 3`, target window size = `3 + 1 = 4`
- `count_s1`: a=1, b=1, c=1

**Window sliding:**

| Step | Window | Start | End | Window Content | Valid? |
|------|--------|-------|-----|----------------|--------|
| 1 | [0:4) | 0 | 3 | "dabb" | No (missing c) |
| 2 | [1:5) | 1 | 4 | "abbc" | No (missing a after shift) - Wait, "abbc" has a=1,b=2,c=1 | **Yes!** |

**Result:** Index `1`

The substring `"abbc"` starting at index 1 contains all letters from `"abc"` with sufficient counts (a≥1, b≥1, c≥1), and has length 4 (3+1).

**Key insight:** The sliding window technique efficiently checks all possible substrings of the required length without redundant comparisons, achieving O(n2) time complexity.
"""



def find_leftmost_substring(s1, s2, k):
    n1 = len(s1)
    n2 = len(s2)

    # 统计s1中每个字母出现的次数
    count_s1 = [0] * 26
    for char in s1:
        count_s1[ord(char) - ord('a')] += 1

    # 统计滑动窗口中每个字母出现的次数
    count_window = [0] * 26

    # 初始化滑动窗口的起始位置和结束位置
    start = 0
    end = 0

    while end < n2:
        # 将当前字符加入滑动窗口
        count_window[ord(s2[end]) - ord('a')] += 1

        # 当滑动窗口的大小大于等于n1+k时，开始检查是否满足条件
        if end - start + 1 >= n1 + k:
            # 检查滑动窗口中每个字母的出现次数是否满足条件
            if all(count_window[i] >= count_s1[i] for i in range(26)):
                return start  # 返回最左侧子串的起始位置

            # 将滑动窗口的起始位置右移一位，并更新字母出现次数
            count_window[ord(s2[start]) - ord('a')] -= 1
            start += 1

        end += 1  # 滑动窗口的结束位置右移一位

    return -1  # 没有找到满足条件的子串，返回-1

# 读取输入
s1 = input()
s2 = input()
k = int(input())

# 调用函数查找最左侧满足条件的子串的首个元素下标
result = find_leftmost_substring(s1, s2, k)

# 输出结果
print(result)


