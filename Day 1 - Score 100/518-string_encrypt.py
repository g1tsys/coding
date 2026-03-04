"""
> The task is to process a command string composed of multiple command words, and to replace the command word at a specified index with "******". The command words are separated by one or more underscores (`_`). Additionally, command words that contain underscores or are empty must be enclosed in double quotes (`""`). The goal is to process the string and ensure that the final output has no extra underscores at the beginning or end.

### Python Language Thought Process:
1. Read the input: the command index `K` and the command string `S`.
2. Process the command string `S` to extract the individual command words.
3. Ensure that the command words are correctly identified, including those that are enclosed in quotes.
4. Check if the index `K` is valid (i.e., it corresponds to an actual command word).
5. If the index is valid, replace the command word at index `K` with `"******"`.
6. Reconstruct the final command string with the modified command word and ensure that there are no extra underscores at the beginning or end.
7. If the index is invalid, output `"ERROR"`.

### Example Walkthrough:
Input:

1
"a_b_c__d"


Steps:
1. Parse the command string `"a_b_c__d"` into command words: `["a", "b", "c__d"]`.
2. The index `K = 1` corresponds to the command word `"b"`.
3. Replace `"b"` with `"******"`, resulting in `["a", "******", "c__d"]`.
4. Reconstruct the final string: `"a_******_c__d"`.

Output:

a_******_c__d

"""


str1 = int(input())
str2 = input()
result = []
current_command = ''
in_command = False  # 表示是否处于一个命令字内部
in_double_quotes = False  # 表示是否处于双引号内部

# 去除命令字符串末尾的多余下划线
str2 = str2.rstrip('_')

# 对命令字符串进行处理，提取命令字
for char in str2:
    if char == '_':  # 遇到下划线
        if not in_command and not in_double_quotes:  # 进入命令字
            result.append(current_command)  # 将当前命令字加入结果列表
            current_command = ''  # 重置临时字符串
            in_command = True  # 设置命令字开关为True，表示处于命令字内部
        elif in_command and not in_double_quotes:  # 处于命令字内部，遇到另一个下划线
            continue  # 跳过，不处理另一个下划线
        elif not in_command and in_double_quotes:  # 处于双引号内部，双引号后面是下划线
            current_command += char  # 在临时字符串中加入下划线
    elif char == '"':  # 遇到双引号
        if not in_double_quotes:  # 不在双引号内部
            in_command = False  # 设置命令字开关为False，表示离开命令字内部
            in_double_quotes = True  # 设置双引号开关为True，表示进入双引号内部
            current_command += char  # 在临时字符串中加入双引号
        else:  # 在双引号内部，遇到另一个双引号
            in_double_quotes = False  # 设置双引号开关为False，表示离开双引号内部
            current_command += char  # 在临时字符串中加入双引号
    else:
        in_command = False  # 非下划线和双引号，设置命令字开关为False
        current_command += char  # 在临时字符串中加入字符

# 添加处理空命令字的逻辑
if in_command and current_command == '""':
    result.append('""')
else:
    result.append(current_command)

result[str1] = '*' * 6  # 将指定索引的命令字替换为******
result = '_'.join(result)  # 将处理后的命令字列表拼接成字符串
print(result)  # 输出结果

