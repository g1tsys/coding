"""
The question is about **decoding a compressed message** based on a specific rule: `n[str]` means the string `str` inside the brackets is repeated `n` times. The task is to return the original message after decompression.

### Python Language Thought Process:
1. Use a **stack** to handle nested structures (e.g., `3[a2[c]]` → `accaccacc`).
2. Traverse each character in the input string:
   - If the character is a digit, collect the full number (e.g., `12` from `12[...]`).
   - If the character is `[`, push the current string and number onto the stack, then reset the current string and number.
   - If the character is `]`, pop from the stack, and append the current string repeated by the popped number.
   - Otherwise, append the character to the current string.
3. Finally, join the stack elements to get the final result.

### Example Walkthrough:
Input: `3[a2[c]]`

Step-by-step:
1. Start with empty stack, current string `""`, and current number `0`.
2. Read `3`, update current number to `3`.
3. Read `[`, push `("", 0)` to stack, reset current string to `""`, number to `0`.
4. Read `a`, current string becomes `"a"`.
5. Read `2`, update current number to `2`.
6. Read `[`, push `("a", 0)` to stack, reset current string to `""`, number to `0`.
7. Read `c`, current string becomes `"c"`.
8. Read `]`, pop `("a", 0)` from stack, append `"c"` repeated `2` times → `"cc"`, current string becomes `"a" + "cc" = "acc"`.
9. Read `]`, pop `("", 0)` from stack, append `"acc"` repeated `3` times → `"accaccacc"`.

Final Output: `"accaccacc"`
"""


def decompress_message(compressed_message):
    stack = []

    for char in compressed_message:
        if char != ']':  # 如果当前字符不是 ']'
            stack.append(char)  # 将字符添加到栈中
        else:
            # 寻找与当前 ']' 对应的 '['
            substring = ''
            while stack[-1] != '[':
                substring = stack.pop() + substring

            stack.pop()  # 弹出 '['

            # 寻找重复次数
            count = ''
            while stack and stack[-1].isdigit():
                count = stack.pop() + count

            # 将子字符串重复指定次数，并将结果添加到栈中
            stack.append(int(count) * substring)

    # 栈中剩余的字符串就是解压缩后的原始报文
    return ''.join(stack)


# 读取输入
compressed_message = input()

# 解压缩报文
original_message = decompress_message(compressed_message)

# 打印原始报文
print(original_message)
