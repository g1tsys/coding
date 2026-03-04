"""
The problem is about dividing a set of apples between two people, A and B, based on a specific rule. Here's the translation of the problem and the Python language thought process:

### Problem Description:
A and B want to divide the apples into two piles. A's rule for dividing is based on **binary addition without carry** (i.e., using XOR). B wants to maximize the total weight of the apples he gets, but under the condition that A's rule is satisfied. If it's not possible to satisfy A's rule, output `-1`.

### Input:
- The first line contains the number of apples.
- The second line contains the weights of the apples.

### Output:
- The total weight of the apples B gets if A's condition is satisfied.
- If A's condition cannot be satisfied, output `-1`.

### Python Language Thought Process:
1. Use the **XOR** operation to determine if there exists a number `x` such that the XOR of all apple weights equals `x`. If such an `x` exists, it means it is possible to divide the apples according to A's rule.
2. If the XOR result is `0`, it means that there exists a valid split (i.e., A's condition is satisfied).
3. In this case, sort the apple weights and sum all weights **except** the smallest one (since B wants to maximize his total weight).
4. If the XOR result is not `0`, it means it's not possible to split the apples according to A's rule, and we output `-1`.

### Example Walkthrough:
Let's say the apple weights are `[12, 5]`.

- XOR of 12 and 5 is `9` (1100 XOR 0101 = 1001 = 9).
- Since the XOR result is not `0`, it is **not** possible to divide the apples according to A's rule.
- So, the output is `-1`.

If the apple weights were `[1, 2, 3]`:
- XOR of all weights is `0` (1 XOR 2 = 3, then 3 XOR 3 = 0).
- This means A's condition is satisfied.
- Sort the list: `[1, 2, 3]`.
- B gets all apples except the smallest (1), so B's total weight is `2 + 3 = 5`.

Thus, the output would be `5`.

"""


import math

def calculate_minimum_z(x, y):
    # 计算字母组合的数量
    letter_combinations = 26 ** y
    # 需要的数字组合数量
    required_number_combinations = x / letter_combinations
    # 计算最小的数字长度 z，确保至少为 1
    z = max(1, math.ceil(math.log10(required_number_combinations)))
    return z

# 示例输入
x, y = map(int, input().split())

# 计算最小的数字长度 Z
z = calculate_minimum_z(x, y)

# 输出结果
print(z)

