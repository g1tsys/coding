"""
I'll help translate and explain the problem, thought process, and provide an example walkthrough.
## Problem Description

**RSA Encryption Algorithm - Prime Factorization**
Given a 32-bit positive integer, perform prime factorization to find which two prime numbers multiply to give this number.
**Input:**
- A positive integer `num` where 0 < num ≤ 2,147,483,647

**Output:**
- If successful: output the two prime numbers separated by a space, in ascending order
- If unsuccessful: output "-1 -1"

## Python Approach (Thought Process)

1. **Handle special cases**: Check if the input is 0, negative, or 1. If so, return `-1 -1`
2. **Iterate through potential factors**: Use a loop starting from 2 to try factorizing the number
3. **Check three conditions** for each potential factor `i`:
   - `num` is divisible by `i` (num % i == 0)
   - `i` is a prime number
   - `num / i` is also a prime number
4. **Return the result**: If both factors are prime, return them. Otherwise, return `-1 -1`

## Example Walkthrough

**Example 1: num = 15**

- Start with i = 2: 15 % 2 ≠ 0, skip
- Try i = 3: 15 % 3 = 0 ✓
  - Is 3 prime? Yes ✓
  - Is 15/3 = 5 prime? Yes ✓
- **Output: 3 5**

**Example 2: num = 21**

- Try i = 2: 21 % 2 ≠ 0, skip
- Try i = 3: 21 % 3 = 0 ✓
  - Is 3 prime? Yes ✓
  - Is 21/3 = 7 prime? Yes ✓
- **Output: 3 7**

**Example 3: num = 12**

- Try i = 2: 12 % 2 = 0 ✓
  - Is 2 prime? Yes ✓
  - Is 12/2 = 6 prime? No (6 = 2×3) ✗
- Continue checking but no valid pair found
- **Output: -1 -1**

The key insight is that you only need to check factors up to √num, and both the factor and quotient must be prime numbers.

"""


import math

# 判断一个数是否为素数
def is_prime(num):
    if num <= 1:
        return False

    if num == 2:
        return True

    if num % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False

    return True

# 因数分解
def factorize(num):
    prime1 = -1
    prime2 = -1

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0 and is_prime(i) and is_prime(num // i):
            prime1 = i
            prime2 = num // i
            break

    if prime1 != -1 and prime2 != -1:
        return prime1, prime2
    else:
        return -1, -1

# 读取输入的正整数
num = int(input())

# 调用因数分解函数进行计算
result = factorize(num)

# 输出结果
print(result[0], result[1])


