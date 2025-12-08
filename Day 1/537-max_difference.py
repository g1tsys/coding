"""
# Translation and Analysis

## Problem Description

**Judge whether a group of inequalities satisfies constraints and output the maximum difference**

Given a group of inequalities, determine if they all hold true and output the maximum difference (integer part of the floating-point result).

**Requirements:**
1. Inequality coefficients are **double type** (2D array)
2. Variables are **int type** (1D array)
3. Target values are **double type** (1D array)
4. Constraint operators are strings: ">", ">=", "<", "<=", "="

**Example inequality system:**
```
a11*x1 + a12*x2 + a13*x3 + a14*x4 + a15*x5 <= b1
a21*x1 + a22*x2 + a23*x3 + a24*x4 + a25*x5 <= b2
a31*x1 + a32*x2 + a33*x3 + a34*x4 + a35*x5 <= b3
```

**Maximum difference** = max of all (left_side - right_side) values

---

## Python Solution Approach

### Thought Process:

1. **Parse input data:**
   - Coefficients matrix (2D array)
   - Variables array (1D array)
   - Target values array (1D array)
   - Operators array (strings)

2. **For each inequality:**
   - Calculate left side: sum of (coefficient x variable)
   - Get right side: target value
   - Calculate difference: left_side - right_side
   - Check if constraint is satisfied based on operator

3. **Determine result:**
   - If ALL inequalities satisfied → output "true" + max difference
   - If ANY inequality fails → output "false" + max difference

4. **Output integer part** of max difference

---

## Example Walkthrough

**Input:**
- Coefficients: `[[2, 3, 1], [1, 1, 1]]`
- Variables: `[1, 2, 3]`
- Targets: `[10, 8]`
- Operators: `["<=", "<="]`

**Step-by-step:**

1. **First inequality:** `2x1 + 3x2 + 1x3 = 11`
   - Target: 10, Difference: 11-10 = **1**
   - Check: 11 ≤ 10? **False** ❌

2. **Second inequality:** `1x1 + 1x2 + 1x3 = 6`
   - Target: 8, Difference: 6-8 = **-2**
   - Check: 6 ≤ 8? **True** ✓

3. **Result:**
   - Max difference: max(1, -2) = **1**
   - All satisfied? **No**
   - Output: `"false 1"`
"""



# 解析输入
str_input = input().split(";")  # 将输入字符串按分号分割成列表
num_eq = len(str_input) - 3  # 等式的数量
num_x = len(str_input[0].split(","))  # 系数和未知数的数量

a = [[0.0] * num_x for _ in range(num_eq)]  # 初始化系数矩阵a
x = [0] * num_x  # 初始化未知数列表x
b = [0.0] * num_eq  # 初始化目标值列表b
eq = [""] * num_eq  # 初始化约束条件列表eq
res = [0] * num_eq  # 初始化结果列表res
max_val = 0  # 最大差值的初始值为0
flag = True  # 初始的不等式约束成立标志为True

# 处理系数矩阵a
for i in range(num_eq):
    a[i] = list(map(float, str_input[i].split(",")))  # 将系数字符串按逗号分割后转换为浮点数列表，并赋值给系数矩阵a的对应行

# 处理未知数列表x
x = list(map(int, str_input[num_eq].split(",")))  # 将未知数字符串按逗号分割后转换为整数列表，并赋值给未知数列表x

# 处理目标值列表b
b = list(map(float, str_input[num_eq + 1].split(",")))  # 将目标值字符串按逗号分割后转换为浮点数列表，并赋值给目标值列表b

# 处理约束条件列表eq
eq = str_input[num_eq + 2].split(",")  # 将约束条件字符串按逗号分割后赋值给约束条件列表eq

# 计算不等式结果
for i in range(num_eq):
    tmp = sum(a[i][j] * x[j] for j in range(num_x))  # 根据不等式的系数和未知数的乘积累加计算结果
    if eq[i] == "<=":
        flag = flag and (tmp <= b[i])  # 判断不等式是否满足约束条件，并更新不等式成立标志
    elif eq[i] == "<":
        flag = flag and (tmp < b[i])
    elif eq[i] == "=":
        flag = flag and (tmp == b[i])
    elif eq[i] == ">=":
        flag = flag and (tmp >= b[i])
    elif eq[i] == ">":
        flag = flag and (tmp > b[i])
    res[i] = int(tmp - b[i])  # 计算不等式的差值并将结果转换为整数存储在结果列表res中

# 计算最大差值
max_val = max(res)  # 更新最大差值

# 输出结果
print(flag, max_val)
