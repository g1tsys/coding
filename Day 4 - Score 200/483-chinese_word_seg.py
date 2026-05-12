"""
Based on the text provided from the web page, here is the extracted information regarding the **Chinese Word Segmentation Simulator** problem, specifically focusing on the Python implementation context.

### **Problem Statement**
**Title:** Chinese Word Segmentation Simulator (华为OD机试真题 483)

**Description:**
Given a continuous string without spaces containing only lowercase English letters and punctuation (commas, semicolons, periods), and a provided dictionary of words, perform **precise word segmentation**.

**Rules:**
1.  **No Overlap:** Segmented words cannot overlap. For example, in `ilovechina`, you cannot output `i`, `love`, `china` if `ilove` is a valid word and appears earlier in the logic, as that would imply `i` and `ilove` overlap in the decision process (though the rule specifically states "i" appearing in both `i` and `ilove` is the conflict if `ilove` is prioritized).
2.  **Punctuation:** Punctuation marks do not form words; they are only used to break sentences (act as delimiters).
3.  **Dictionary:** A list of valid words provided as input (e.g., `["i", "love", "china", "lovechina", "ilove"]`).
4.  **Segmentation Principles:**
    *   **Order Priority:** Scan from left to right.
    *   **Longest Match:** If multiple words in the dictionary match the current starting position, choose the **longest** one.
    *   *Example:* For `ilovechina` with dictionary `[i, ilove, lo, love, ch, china, lovechina]`:
        *   At index 0: Matches `i` (len 1) and `ilove` (len 5). Choose `ilove`.
        *   Remaining string: `china`.
        *   At index 5: Matches `ch` (len 2) and `china` (len 5). Choose `china`.
        *   **Result:** `ilove, china`
        *   **Incorrect:** `i, lovechina` (Because `ilove` was prioritized over `i` at the start).
        *   **Incorrect:** `i, love, china` (Because `ilove` > `i`).

---

### **Input Format**
The input consists of two lines:
1.  **String to segment:** A continuous string of lowercase letters and punctuation (e.g., `ilovechina`).
    *   Constraint: $0 < \text{length} < 256$.
2.  **Dictionary:** A comma-separated list of words (e.g., `i,love,china,ch,na,ve,lo,this,is,word`).
    *   Constraint: $1 < \text{length} < 100,000$.

### **Output Format**
*   Output the segmented words in order, separated by commas.
*   Example Output: `ilove,china`

---

### **Python Thought Process & Algorithm**

To solve this in Python, we need to implement a greedy algorithm that respects the "Left-to-Right, Longest Match" rule.

**Step-by-Step Logic:**

1.  **Parse Input:**
    *   Read the target string.
    *   Read the dictionary line, split by commas, and store it in a data structure for fast lookup. A Python `set` is ideal for $O(1)$ average time complexity lookups.
    *   *Optimization:* We also need to know the maximum word length in the dictionary to limit the scanning window.

2.  **Handle Punctuation:**
    *   The problem states punctuation acts as a delimiter. We should treat punctuation as boundaries. If the string contains `ilove,china`, the comma splits the logic. We might need to split the main string by punctuation first or skip punctuation during the scan.
    *   *Refined Approach:* Iterate through the string. If the current character is punctuation, add it to the result (or skip it if the output format strictly wants words) and move to the next character. The problem description says "Punctuation does not form a word, only for breaking sentences". The sample output `ilove,china` implies the output is a comma-separated list of *words*. If the input has punctuation, it likely splits the segments but isn't printed as a word itself unless the output format requires preserving it (the sample output `i,love,china` in the description seems to be a list of words, not the original punctuation).
    *   *Correction based on "Precise Segmentation":* Usually, in these OD problems, if the input is `ilove,china`, the comma breaks the stream. We process `ilove`, then the comma breaks, then `china`. The output is the list of found words.

3.  **Greedy Scanning (The Core Loop):**
    *   Initialize an empty list for results.
    *   Use a pointer `i` starting at 0.
    *   While `i` is less than the string length:
        *   If `s[i]` is punctuation:
            *   Move `i` forward (skip punctuation).
            *   Continue loop.
        *   If `s[i]` is a letter:
            *   Look ahead: Check substrings starting at `i` with lengths ranging from `max_len` down to 1.
            *   Find the **longest** substring `s[i : i + L]` that exists in the dictionary.
            *   If a match is found:
                *   Add the word to results.
                *   Move `i` forward by `L`.
            *   If **no** match is found (even for length 1):
                *   This case implies the character is not in the dictionary. The problem says "precise segmentation", usually implying the input is valid or we just skip invalid chars. However, based on the "Longest Match" rule, if no word starts there, we might skip the character or treat it as an error. Given the constraints, we usually assume valid input or simply skip the unmatched char. *Self-correction:* The problem says "string contains letters and punctuation". If a letter sequence isn't in the dictionary, it's not a word. We skip it or move 1 char. Let's assume we skip unmatched characters to proceed.

4.  **Formatting Output:**
    *   Join the `results` list with commas and print.

**Python Code Structure (Mental Draft):**

```python
def solve():
    # Read inputs
    try:
        s = input().strip()
        dict_str = input().strip()
    except EOFError:
        return

    # Process dictionary
    words = set(dict_str.split(','))
    if not words or not s:
        print("")
        return

    max_len = max(len(w) for w in words)
    punctuation = {',', ';', '.'}
    
    result = []
    i = 0
    n = len(s)
    
    while i < n:
        if s[i] in punctuation:
            i += 1
            continue
        
        # Try to find the longest match
        matched = False
        # Limit the search to max_len or end of string
        limit = min(i + max_len, n)
        
        # Check from longest possible down to 1
        for l in range(limit - i, 0, -1):
            sub = s[i : i + l]
            if sub in words:
                result.append(sub)
                i += l
                matched = True
                break
        
        if not matched:
            # If no word found, skip the character (or handle as per specific edge case rules)
            # Usually in these problems, if it's not in dict, we skip it to continue
            i += 1

    print(",".join(result))

solve()
```

**Key Considerations for the Python Solution:**
*   **Efficiency:** Since the dictionary can be large (100k words), using a `set` is crucial. A naive list search would be too slow.
*   **Max Length:** Calculating `max_len` prevents unnecessary string slicing beyond the longest possible word.
*   **Punctuation Handling:** The logic must correctly skip punctuation without treating them as part of a word or printing them in the final list (unless the specific test case requires preserving them, but the "longest match" logic usually applies to the words between delimiters).
*   **Overlap Prevention:** The greedy approach (taking the longest match immediately) naturally prevents overlap because once a word is taken, the pointer moves past it.

This approach ensures the "Order Priority" (we are at `i`) and "Longest Match" (we check longest first) constraints are met efficiently.

"""


def word_break(s, dict_set):
    """
    分词函数
    :param s: 待分词的字符串
    :param dict_set: 词库集合
    :return: 分词结果列表
    """
    res = []  # 用于存储分词结果
    i = 0
    while i < len(s):
        # 如果是标点符号，则跳过连续的标点，直到遇到非标点符号
        if s[i] in {',', ';', '.'}:
            # 将连续的标点视作一个断句点，直接添加到结果中
            if not res or (res and res[-1] != ' '):  # 避免连续添加空格
                res.append(' ')
            while i < len(s) and s[i] in {',', ';', '.'}:
                i += 1
            continue

        # 尝试找出最长匹配的单词
        max_word = ''
        for j in range(i + 1, len(s) + 1):
            # 只有当切割的字符串在字典中并且比当前最长的单词长时，才更新最长单词
            if s[i:j] in dict_set and len(s[i:j]) > len(max_word):
                max_word = s[i:j]
        # 如果找到了最长单词，添加到结果中，并更新当前位置
        if max_word:
            res.append(max_word)
            i += len(max_word)
        else:
            # 如果没有在字典中找到匹配的单词，将当前字母作为单词添加到结果中
            res.append(s[i])
            i += 1
    return res


def main():
    # 输入待分词的字符串
    s = input().strip()
    # 输入词库字符串，并转化为集合形式
    dictionary = set(input().strip().split(','))
    # 调用分词函数
    result = word_break(s, dictionary)
    # 输出分词结果
    print(','.join(filter(lambda x: x != ' ', result)))  # 过滤掉结果中的空格


# 调用主函数
if __name__ == '__main__':
    main()

