"""
### Problem Description
Given a positive integer `NUM1`, calculate a new positive integer `NUM2` by removing exactly `N` digits from `NUM1`. The goal is to make the value of `NUM2` as small as possible.

---

### Input and Output

#### Input
1. The first line is a string composed of digits 0-9, representing the positive integer `NUM1`. The length of `NUM1` is less than 32.
2. The second line is the number of digits `N` to be removed, which is less than the length of `NUM1`.

#### Output
Output a string of digits representing the minimum possible value of `NUM2`.

---

Would you like me to also translate the corresponding solution approach for this problem?


# Python Language Approach
1. Scan the string from left to right, ensuring that after removing the specified number of digits, the remaining number is minimized.
2. Use a stack data structure to help implement this process.
3. Compare the current digit with the top element of the stack. If the current digit is smaller and the number of digits removed has not yet reached the specified count, remove the digit at the top of the stack.
4. If the number of digits removed has not reached the required count after the scan is complete, continue removing digits from the top of the stack until the count is met.
5. The digits remaining in the stack form the final result.

---

Would you like me to also provide the full Python code implementation for this problem?

"""

def remove_digits(num1, k):
    # 创建一个栈，用来存放最后结果中的字符
    stack = []
    # 用来记录已经移除的数字数量
    removed = 0

    # 遍历num1中的每一个字符
    for digit in num1:
        # 当栈不为空，且当前字符小于栈顶字符，并且我们还可以移除更多的字符时
        while stack and stack[-1] > digit and removed < k:
            # 弹出栈顶字符（移除数字）
            stack.pop()
            # 记录已移除的数字数量加1
            removed += 1
        # 将当前字符加入到栈中
        stack.append(digit)

    # 如果遍历完num1后，仍未移除足够数量的字符，则继续从栈顶移除
    while removed < k:
        stack.pop()
        removed += 1

    # 移除前导零（如果有的话）
    result = ''.join(stack).lstrip('0')

    # 如果结果为空，则返回'0'
    return result if result else '0'

# 输入处理
num1 = input().strip()
k = int(input().strip())

# 调用函数并输出结果
print(remove_digits(num1, k))

