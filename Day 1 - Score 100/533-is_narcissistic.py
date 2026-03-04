"""
Here's a **translation** of the question and the **Python language thought process** from the web page content, followed by a **walkthrough example**:

---

### 🎃 Question Translation:
A **narcissistic number** (also known as an **armstrong number**) is a positive integer with **n digits** such that the **sum of each digit raised to the power of n** equals the number itself. For example, 153 is a narcissistic number because it is a 3-digit number and 1³ + 5³ + 3³ = 153.

#### 📌 Input:
- The first line is an integer `n` (3 ≤ n ≤ 7), representing the number of digits.
- The second line is an integer `m`, representing the index of the narcissistic number you want to retrieve (starting from 0).

#### 📌 Output:
- Return the **m-th narcissistic number** with `n` digits.
- If `m` is greater than the number of narcissistic numbers with `n` digits, return the **product of the last narcissistic number and `m`**.
- If the input is invalid, return **-1**.

---

### 🐍 Python Language Thought Process:

1. **Input Validation**:
   - Check if `n` is between 3 and 7 (inclusive).
   - Ensure `m` is a non-negative integer.

2. **Determine the Range of Numbers**:
   - For a number with `n` digits, the minimum is `10^(n-1)` and the maximum is `10^n - 1`.

3. **Check for Narcissistic Numbers**:
   - Iterate through all numbers in the range.
   - For each number, split it into its digits.
   - Compute the sum of each digit raised to the power of `n`.
   - If the sum equals the number, it is a narcissistic number.

4. **Store Narcissistic Numbers**:
   - Store all valid narcissistic numbers in a list.

5. **Output the Result**:
   - If the list is empty or `m` is out of bounds, return the product of the last narcissistic number and `m`.
   - If the input is invalid, return `-1`.

---

### 🧪 Example Walkthrough:

#### Input:

3
2


#### Step-by-Step:

1. **Input Validation**:
   - `n = 3` is valid (between 3 and 7).
   - `m = 2` is valid (non-negative).

2. **Range of Numbers**:
   - For `n = 3`, the range is from 100 to 999.

3. **Check for Narcissistic Numbers**:
   - 153 is a narcissistic number (1³ + 5³ + 3³ = 153).
   - 370 is another (3³ + 7³ + 0³ = 370).
   - 371, 407, etc., are also narcissistic numbers.

4. **Store in List**:
   - The list of narcissistic numbers with 3 digits is: `[153, 370, 371, 407]`.

5. **Output the Result**:
   - The 2nd narcissistic number is **370**.

#### Output:

370


---

Let me know if you want the actual Python code for this!

"""


def is_narcissistic(num, n):
    """检查一个数字是否是水仙花数，给定数字的位数为n。"""
    # 将数字转换为字符串，然后将每个字符转换为整数，得到数字的各个位
    digits = [int(d) for d in str(num)]
    # 计算每个位上的数字的n次方之和，并检查是否等于原数字
    return sum(d ** n for d in digits) == num


def find_narcissistic_number(n, m):
    """查找第m个n位的水仙花数。"""
    # 检查n是否在有效范围内，如果不在则返回-1
    if n < 3 or n > 7:
        return -1

    # 计算需要检查的数字范围，范围从10^(n-1)到10^n - 1
    start = 10 ** (n - 1)
    end = 10 ** n - 1

    # 用于存储所有找到的n位水仙花数
    narcissistic_numbers = []

    # 遍历范围内的所有数字
    for num in range(start, end + 1):
        # 如果当前数字是水仙花数，则添加到列表中
        if is_narcissistic(num, n):
            narcissistic_numbers.append(num)

    # 如果m小于找到的水仙花数的数量，则返回第m个水仙花数
    if m < len(narcissistic_numbers):
        return narcissistic_numbers[m]
    # 如果m大于等于找到的水仙花数的数量，返回最后一个水仙花数和m的乘积
    elif narcissistic_numbers:
        return narcissistic_numbers[-1] * m
    else:
        # 如果没有找到任何水仙花数，返回-1
        return -1



try:
    # 获取用户输入的位数n
    n = int(input())
    # 获取用户输入的索引m
    m = int(input())

    # 调用函数获取结果
    result = find_narcissistic_number(n, m)
    # 输出结果
    print(result)
except ValueError:
    # 处理非整数输入的异常
    print(-1)

