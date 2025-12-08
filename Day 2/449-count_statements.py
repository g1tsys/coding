"""
The question is about counting the number of text segments in a given string, based on specific rules. The rules are as follows:

1. Text segments are separated by `;` characters. The last segment may not end with `;`, and empty text segments (such as those containing only whitespace or no characters at all) should not be counted.
2. Text segments can span multiple lines.
3. Strings (enclosed in either single `'` or double `"` quotes) are supported, and they may contain escaped quotes (e.g., `\"` or `\'`).
4. Comments (starting with `-` and ending at a newline) are supported, but they are not counted as text segments. However, the `-` inside strings is not considered a comment.

### Python Language Thought Process

1. **Initialize State Variables**:
   - `in_single_quote`, `in_double_quote`: Track whether we are inside a single or double quote string.
   - `in_comment`: Track whether we are inside a comment.
   - `statement_count`: Count the number of valid text segments.
   - `escape`: Track if the current character is an escape character.
   - `non_space_encountered`: Track whether a non-whitespace character has been seen since the last `;` or the start of the text.

2. **Iterate Through Each Character**:
   - For each character, determine if it is inside a string or a comment.
   - If the character is a `;` and we are not inside a string or comment, it marks the end of a text segment.
   - If the character is not whitespace and we are not inside a string or comment, set `non_space_encountered` to `True`.

3. **Count Valid Text Segments**:
   - After processing all characters, if `non_space_encountered` is `True`, increment the `statement_count`.

4. **Return the Result**:
   - Return the value of `statement_count`.

### Example Walkthrough

**Input**:
```
COMMAND A"Say "hello""; -this is comment
COMMAND B;
```

**Processing**:
- The first segment is `COMMAND A"Say "hello""` (before the `;`).
- The second segment is `COMMAND B` (before the `;`).
- The comment `-this is comment` is ignored.
- The final `;` after `COMMAND B` marks the end of the second segment.

**Output**:
```
2
```

This example demonstrates how the code correctly counts the number of valid text segments while ignoring comments and empty segments.
"""




def count_statements(input_text):
    # 初始化状态
    in_single_quote = False
    in_double_quote = False
    in_comment = False
    statement_count = 0
    escape = False
    non_space_encountered = False

    # 遍历文本字符
    for i, char in enumerate(input_text):
        # 检查注释
        if char == '-' and not in_single_quote and not in_double_quote and \
                i < len(input_text) - 1 and input_text[i + 1] == '-':
            in_comment = True
            continue

        # 检查换行符，结束注释
        if char == '\n':
            in_comment = False

        # 如果在注释中，忽略当前字符
        if in_comment:
            continue

        # 跳过转义的字符
        if escape:
            escape = False
            continue

        # 检查转义字符
        if char == '\\' and (in_single_quote or in_double_quote):
            escape = True
            continue

        # 检查单引号
        if char == "'" and not in_double_quote:
            in_single_quote = not in_single_quote
            non_space_encountered = True
            continue

        # 检查双引号
        if char == '"' and not in_single_quote:
            in_double_quote = not in_double_quote
            non_space_encountered = True
            continue

        # 如果字符不是空白，标记非空字符出现
        if char.strip():
            non_space_encountered = True

        # 检查分隔符；如果不在引号中，则计数
        if char == ';' and not in_single_quote and not in_double_quote:
            if non_space_encountered:
                statement_count += 1
                non_space_encountered = False

    # 检查最后是否有非空的文本
    if non_space_encountered:
        statement_count += 1

    return statement_count


# 输入样例
input_text = '''COMMAND TABLE IF EXISTS "UNITED STATE";
COMMAND A GREAT (
ID ADSAB,
download_length INTE-GER, -- test
file_name TEXT,
guid TEXT,
mime_type TEXT,
notifica-tionid INTEGER,
original_file_name TEXT,
pause_reason_type INTEGER,
resumable_flag INTEGER,
start_time INTEGER,
state INTEGER,
folder TEXT,
path TEXT,
total_length INTE-GER,
url TEXT
);'''

# 调用函数，并打印结果
print(count_statements(input_text))
