"""
### Problem Description
On a phone keypad, there are two input modes: **numeric mode** and **alphabetic mode**, with numeric mode as the default.
- In **numeric mode**, inputting digits will directly output the corresponding digits.
- In **alphabetic mode**, consecutive presses on the same key will cycle through the corresponding characters on that key.

If the input contains characters other than digits (0-9), `*`, or `#`, the program should terminate immediately.

The character mapping of the keypad is as follows:

| Key | Corresponding Characters |
| :-- | :----------------------- |
| 1   | (No characters)          |
| 2   | abc                      |
| 3   | def                      |
| 4   | ghi                      |
| 5   | jkl                      |
| 6   | mno                      |
| 7   | pqrs                     |
| 8   | tuv                      |
| 9   | wxyz                     |
| #   | (No characters)          |
| 0   | (No characters)          |
| /   | (Not an input key)       |

---

### Input and Output Rules

#### Input
The input consists of digits (0-9) and the characters `*` and `#`.
- **Example**: Inputting `1234` in numeric mode will output `1234`.
- **Example**: Inputting `1234` in alphabetic mode will output `adg`.

#### Output Rules
1. `*` is the **mode switch key**: Pressing it once toggles between numeric mode and alphabetic mode (default is numeric).
2. `#` is the **confirmation key**: For example, in alphabetic mode, inputting `2222#` will output `bc`.
3. In alphabetic mode, pressing the **same key multiple times** cycles through characters: For example, inputting `2222` will output `b`.

---

### Input/Output Summary
- **Input**: A string composed of 0-9, `*`, and `#` (illegal characters trigger immediate termination).
- **Output**: The final string generated according to the keypad input rules and mode switches.
# Python Language Approach
1. If the mode switch key `*` is encountered, toggle the input mode: if the current mode is numeric, switch to alphabetic mode; if the current mode is alphabetic, switch to numeric mode. At the same time, reset the key press count.
2. If the confirmation key `#` is encountered, determine the output character based on the number of consecutive presses on the current key, and reset the current key and press count.
3. If the current mode is numeric, directly add the input character to the result list.
4. If the current mode is alphabetic, process the pressed key as follows:
   - If the pressed key is the same as the previous one, increment the press count.
   - If the pressed key is different, first determine the output character based on the previous key's press count, then update the current key and reset the press count to 1.
5. Finally, convert the result list to a string and return it.

---

Would you like me to also provide the full Python code implementation for this problem?
"""

def nine_key_input(input_str):
    # 初始模式为数字模式
    mode = 'number'
    
    # 存储结果的列表
    result = []

    # 九宫格按键对应的字母和数字关系
    key_map = {
        '1': '1', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz', '0': '0'
    }

    # 当前正在处理的按键
    current_key = ''
    # 当前按键被按了多少次
    current_count = 0

    # 遍历输入字符串中的每个字符
    for char in input_str:
        if char == '#':  # 如果遇到模式切换符号
            if mode == 'number':  # 从数字模式切换到字母模式
                mode = 'alpha'
            else:  # 从字母模式切换到数字模式
                mode = 'number'
            # 重置当前按键和计数
            current_key = ''
            current_count = 0
        elif char == '/':  # 如果遇到延迟符号
            if current_key:  # 如果有正在处理的按键
                # 根据按键被按的次数确定要输出的字母
                result.append(key_map[current_key][(current_count - 1) % len(key_map[current_key])])
            # 重置当前按键和计数
            current_key = ''
            current_count = 0
        elif mode == 'number':  # 数字模式下，直接输出字符
            result.append(char)
        else:  # 字母模式下
            if char == current_key:  # 如果按的是相同的按键
                current_count += 1  # 按键次数加一
            else:  # 如果按的是不同的按键
                if current_key:  # 如果有正在处理的按键
                    # 根据按键被按的次数确定要输出的字母
                    result.append(key_map[current_key][(current_count - 1) % len(key_map[current_key])])
                # 更新当前按键和计数
                current_key = char
                current_count = 1

    # 处理最后一个按键的输出
    if current_key:
        result.append(key_map[current_key][(current_count - 1) % len(key_map[current_key])])

    # 返回结果字符串
    return ''.join(result)

# 获取输入字符串
input_str = input()
# 输出九宫格按键处理后的结果
print(nine_key_input(input_str))
