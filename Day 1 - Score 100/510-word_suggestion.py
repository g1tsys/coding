"""
The question requires you to implement a function for an English input method that suggests words based on a given prefix. The task is to extract all the English words from a given sentence, filter those that start with the given prefix, and output them in lexicographical order. If no words match the prefix, output the prefix itself.

### Python Language Thought Process:
1. **Extract Words**: Parse the input sentence to extract all valid English words, ignoring punctuation.
2. **Filter by Prefix**: Check each word to see if it starts with the given prefix.
3. **Remove Duplicates**: Ensure the final list of words has no duplicates.
4. **Sort Words**: Sort the list lexicographically.
5. **Output Result**: If the list is not empty, print the words separated by spaces. Otherwise, print the prefix.

### Example Walkthrough:
Input:
```
"Hello, world! This is a test. Hello again."
"Hel"
```

**Step-by-step**:
1. Extract words: `["Hello", "world", "This", "is", "a", "test", "Hello", "again"]`
2. Filter by prefix `"Hel"`: `["Hello", "Hello"]`
3. Remove duplicates: `["Hello"]`
4. Sort: `["Hello"]`
5. Output: `"Hello"`

This approach ensures that the solution is efficient and adheres to the problem constraints.
"""


import re


def word_suggestion(sentence, prefix):
    # 使用正则表达式将句子中的单词分割出来，并正确处理缩略形式
    # 注意：缩略形式如 "don't" 被视为两个单词 "don" 和 "t"
    words = re.findall(r'\b\w+(?:\'\w+)?\b', sentence)

    # 将缩略词分割成两个单词
    split_words = []
    for word in words:
        if "'" in word:
            split_words.extend(word.split("'"))
        else:
            split_words.append(word)

    # 使用集合来存储唯一的单词
    unique_words = set(split_words)

    # 使用列表推导式找到所有以前缀开始的单词，注意区分大小写
    suggested_words = sorted(word for word in unique_words if word.startswith(prefix))

    # 如果有联想到的单词，则按字典序输出，否则输出前缀
    return ' '.join(suggested_words) if suggested_words else prefix


# 读取两行输入
sentence = input().strip()
prefix = input().strip()

# 输出联想到的单词序列或单词前缀
print(word_suggestion(sentence, prefix))


