# Word Guessing Game - Problem Translation

## Problem Description
"""
A simple word guessing game where you're given incorrect words (riddles) and need to find the correct words from a dictionary. A guess is correct if it satisfies **either** condition:

1. **Same letters, different order**: The riddle word can be rearranged to match the dictionary word (anagrams)
   - Example: "nwes" matches "news" (rearrange w and e)

2. **Same letters after deduplication**: After removing duplicate letters, both words have the same unique characters
   - Example: "woood" matches "wood" (both become "wod" after deduplication)

## Input/Output

**Input:**
1. Line 1: Riddle words separated by commas
2. Line 2: Dictionary words separated by commas

**Output:**
- Matching correct words separated by commas
- If no match found: "not found"

## Example Walkthrough

### Example 1:
**Input:**
```text
conection
connection,today
```

**Process:**
- Riddle: "conection"
- Dictionary: ["connection", "today"]

Check "connection":
- Remove duplicates from "conection" → {c, o, n, e, t, i}
- Remove duplicates from "connection" → {c, o, n, e, t, i}
- ✓ Same character sets!

Check "today":
- Remove duplicates from "today" → {t, o, d, a, y}
- ✗ Different character sets

**Output:** `connection`

### Example 2:
**Input:**
```text
bdni,wooood
bind,wrong,wood
```

**Process:**

**Riddle 1: "bdni"**
- Unique chars: {b, d, n, i}
- Check "bind": {b, i, n, d} → ✓ Match!
- Check "wrong": {w, r, o, n, g} → ✗
- Check "wood": {w, o, d} → ✗

**Riddle 2: "wooood"**
- Unique chars: {w, o, d}
- Check "bind": {b, i, n, d} → ✗
- Check "wrong": {w, r, o, n, g} → ✗
- Check "wood": {w, o, d} → ✓ Match!

**Output:** `bind,wood`

## Algorithm Hints

1. For each riddle word, extract its unique character set
2. For each dictionary word, extract its unique character set
3. Compare the sets - if they match, it's a valid answer
4. Collect all matches; if none found, return "not found"
"""

def find_correct_words():
    # 输入谜面单词列表和谜底库单词列表
    err_words = input().split(",")
    lib_words = input().split(",")

    words_set = set(lib_words)  # 用于存储匹配到的正确单词的集合
    result = []

    for err_word in err_words:
        err_chars = set(err_word)  # 谜面单词去重后的字符集合
        found = False  # 标记是否找到匹配的谜底单词

        for lib_word in lib_words:
            # 判断谜底单词的字符集合与谜面单词去重后的字符集合是否相等
            if len(set(lib_word)) == len(err_chars) and set(lib_word) == err_chars:
                result.append(lib_word)  # 将匹配到的谜底单词添加到结果列表中
                found = True  # 标记为找到匹配的谜底单词
                break

        if not found:
            result.append("not found")  # 如果未找到匹配的谜底单词，则添加 "not found" 到结果列表中

    return result


result = find_correct_words()

if len(result) == 0:
    print("not found")
else:
    print(",".join(result))  # 使用逗号连接结果列表，并打印最终结果




