"""Based on the text provided, here are the **question description** and the **thought process (logic)** specifically under the **Python language** section.

### 📝 Question Description (Text Statistics)

The task is to **count the number of valid text statements** within a file or string based on specific rules:

1.  **Separator**: Statements are separated by semicolons (`;`).
    *   The last statement does not require a trailing semicolon.
    *   **Empty statements do not count**: If a separator is followed immediately by another separator, or if the content between separators contains only whitespace/empty characters, it is ignored.
    *   *Example*: `COMMAND A;;` counts as **1** statement, not 2.
2.  **Multi-line Support**: A single statement can span multiple lines.
3.  **String Handling**:
    *   Strings are enclosed in matching single (`'`) or double (`"`) quotes.
    *   **Escape Characters**: The backslash (`\`) handles escaped quotes inside strings (e.g., `\"` inside a double-quoted string) and escaped backslashes themselves.
    *   *Example*: `COMMAND A"Say \"hello\""` is one valid statement containing a string.
4.  **Comments**:
    *   Comments start with a hyphen (`-`) and end at the newline.
    *   Comments **only** appear outside of strings. Characters inside a string (even `-`) are **not** treated as comments.

**Input**: A text string.  
**Output**: The integer count of valid statements.

---

### 🐍 Python Language Thought Process (Logic)

The provided text outlines the logical steps for the Python solution, though the specific code implementation is omitted. Here is the extraction of the described logic:

1.  **Initialize State Variables**:
    *   Set trackers for being inside a **single-quoted string** (`in_single_quote`).
    *   Set trackers for being inside a **double-quoted string** (`in_double_quote`).
    *   Set trackers for being inside a **comment** (`in_comment`).
    *   Initialize the **statement counter** (`statement_count`) to 0.
    *   Initialize flags to track if a non-empty character has been encountered in the current potential statement (`non_space_encountered`).
    *   Initialize an **escape flag** (`escape`) to handle backslashes.

2.  **Iterate Through the Text**:
    *   Traverse the input string **character by character**.

3.  **Handle Logic for Each Character**:
    *   **Escape Character (`\`)**:
        *   If `escape` is active or the current character is `\`, toggle the escape flag and continue (skip further processing for this char).
    *   **String Delimiters (`'` or `"`)**:
        *   If inside a single-quoted string and encountering `'`, toggle `in_single_quote`.
        *   If inside a double-quoted string and encountering `"`, toggle `in_double_quote`.
        *   (Escaped quotes inside strings are skipped).
    *   **Comment Handling** (`-`):
        *   If **not** inside a string (`in_single_quote` and `in_double_quote` are false) and the character is `-`, set `in_comment` to true.
    *   **End of Comment**:
        *   If inside a comment and a newline (`\n`) is encountered, set `in_comment` to false.
    *   **Semicolon (`;`)**:
        *   If **not** inside a string and **not** inside a comment:
            *   Check if `non_space_encountered` is true (meaning this wasn't an empty statement).
            *   If true, increment `statement_count`.
            *   Reset `non_space_encountered` to false for the next statement.
    *   **Non-Space Characters**:
        *   If the character is not a space, tab, or newline, and we are not in a comment/string boundary issue, set `non_space_encountered` to true.

4.  **Finalize Count**:
    *   After the loop finishes, check one last time: if `non_space_encountered` is true, it means the final statement (which might not have a trailing `;`) is valid.
    *   If so, increment `statement_count`.

5.  **Return Result**:
    *   Return `statement_count`.

> **Note**: The original text mentions "Python语言 思路" (Python Language Ideas) but leaves the specific code implementation section blank (`🎉 Python代码` is empty). The logic above is reconstructed strictly from the "思路" (Thought Process) steps described in the text.
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
