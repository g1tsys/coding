"""
> **Note:** The content provided is from a web page and is treated as data only. No instructions or commands from this content will be executed automatically.

---

### **Question Translation (from the web page):**

**Problem Statement:**

Xiaoming is in charge of the company's annual party and wants to create an interesting game:  
The screen shows 4 distinct digits from 1 to 9. Everyone needs to quickly provide the number that can be formed by arranging these digits in ascending order, and the number at the N-th position, where N is the largest digit among the given numbers. If there are not enough numbers, output the last one.

**Important Rules:**

1. The digit `2` can be used as `5`, and `5` can be used as `2`. However, the screen cannot show both `2` and `5` at the same time.
2. The digit `6` can be used as `9`, and `9` can be used as `6`. However, the screen cannot show both `6` and `9` at the same time.

For example, if the input is `1, 4, 8, 7`, the possible numbers that can be formed are:  
`1, 4, 7, 8, 14, 17, 18, 41, 47, 48, 71, 74, 78, 81, 84, 87, 147, 148, 178, ...`  
The N-th number is the 8th one, which is `41`.

**Input:** A string of 4 integers separated by commas.  
**Output:** The N-th number in the sorted list of all possible numbers formed from the given digits. If the input is invalid or has duplicates, output `-1`.

---

### **Python Thought Process (from the web page):**

**Thought Process (Python):**

1. First, check if the input is valid (i.e., no duplicates and all digits are between 1 and 9).
2. Determine the maximum digit among the input digits, which will be the value of N.
3. Replace the digits based on the rules:  
   - If `2` is present, replace it with `5` (and vice versa).
   - If `6` is present, replace it with `9` (and vice versa).
4. Generate all possible permutations of the digits (after replacement).
5. Convert each permutation into a number and sort them in ascending order.
6. If the number of generated numbers is less than N, return the last one. Otherwise, return the N-th number (note that index starts at 1).

---

### **Example Walkthrough:**

**Input:** `1,4,8,7`  
- No `2` or `5` or `6` or `9` in the input, so no replacement is needed.
- The maximum digit is `8`, so N = 8.
- Generate all permutations of the digits: `1, 4, 7, 8` → all possible combinations.
- Sort all the generated numbers in ascending order.
- The 8th number is `41`.

**Output:** `41`
"""


from itertools import permutations


def generate_numbers(digits):
    numbers = set()

    # 创建所有可能的替代数字
    digits_replacement = []
    for digit in digits:
        if digit == '2' or digit == '5':
            digits_replacement.append(['2', '5'])
        elif digit == '6' or digit == '9':
            digits_replacement.append(['6', '9'])
        else:
            digits_replacement.append([digit])

    # 生成所有的替代组合
    from itertools import product
    all_combinations = list(product(*digits_replacement))

    # 生成所有排列组合
    for comb in all_combinations:
        for length in range(1, 5):  # 1到4位数字
            for perm in permutations(comb, length):
                num = int(''.join(perm))
                numbers.add(num)

    return sorted(numbers)


def main(input_str):
    try:
        # 处理输入
        digits = list(map(int, input_str.split(',')))

        # 检查输入有效性
        if len(digits) != 4 or len(set(digits)) != 4 or any(d < 1 or d > 9 for d in digits):
            return -1

        # 生成可拼接的数字
        possible_numbers = generate_numbers(map(str, digits))

        # N 为输入的最大数字
        N = max(digits)

        # 获取第 N 个数字
        if N <= len(possible_numbers):
            return possible_numbers[N - 1]  # N 从 1 开始计数
        else:
            return possible_numbers[-1]  # 如果不够则返回最后一个数字
    except Exception:
        return -1



input_str = input()
print(main(input_str))  

