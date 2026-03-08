"""
**问题输入输出：**

**输入：**  
- 第一行：一个整数 `n`，表示指令的总个数（1 ≤ n ≤ 100）  
- 第二行：一个整数 `m`，表示幸运数（-100 ≤ m ≤ 100）  
- 第三行：n 个整数，表示每条指令（-100 ≤ 指令值 ≤ 100）  

**输出：**  
- 输出在整个游戏过程中，小明所处的最大坐标值。  
- 异常情况下输出：`12345`  

**规则说明：**  
- 小明初始位置在坐标轴原点（0）。  
- 每个指令为一个整数：  
  - 若指令值等于幸运数 `m`，则小明前进 `|指令值| + 1` 步（方向由符号决定）。  
  - 否则，小明前进 `|指令值|` 步（正为正方向，负为负方向）。  
- 每次移动后，更新当前坐标，并记录最大坐标值。  
- 最终输出最大坐标值。

以下是图片中提取的 Python 解题思路：

1. 首先检查输入的指令总数 `n` 和幸运数 `m` 是否符合规定范围。若不符合则输出 `12345` 并结束程序。
2. 接下来，将输入的 `n` 个指令存储在一列 `Instructions` 中。
3. 初始化每个指令的当前位置 `current_position` 为 0，最大坐标值 `max_position` 为 0。
4. 遍历每个指令 `Instruction`：
   - 如果指令值不等于 0，则小明行进步数在指令值基础上加 1（如果指令值大于 0）或减 1（如果指令值小于 0）。
   - 否则，按照指令值前进或后退。
5. 在每次移动后，更新小明所处的最大坐标值 `max_position` 为当前位置 `current_position` 和最大坐标值 `max_position` 中的较大值。
6. 遍历结束后，输出整个游戏过程中小明所处的最大坐标值 `max_position`。
"""

# 输入指令的总个数n
n = int(input())
# 如果n不符合规定范围,则输出12345并结束程序
if n < 1 or n > 100:
    print(12345)
    exit()

# 输入幸运数m
m = int(input())
# 如果m不符合规定范围,则输出12345并结束程序
if m < -100 or m > 100:
    print(12345)
    exit()

# 输入n个指令,并转化为整数列表
instructions = list(map(int, input().split()))
# 检查指令列表长度是否为n且每个指令值是否在规定范围内,若不符合则输出12345并结束程序
if len(instructions) != n or any(instruction < -100 or instruction > 100 for instruction in instructions):
    print(12345)
    exit()


current_position = 0  # 初始化小明当前坐标为0
max_position = 0  # 初始化小明所处的最大坐标值为0

# 遍历每个指令
for instruction in instructions:
    # 如果指令值等于幸运数
    if instruction == m:
        # 并且指令不等于0时,小明行进步数在指令值的基础上加1
        if instruction != 0:
            current_position += instruction + 1 if instruction > 0 else instruction - 1
    else:
        # 如果指令值不等于幸运数,按指令值前进或后退
        current_position += instruction

    # 更新小明所处的最大坐标值
    max_position = max(max_position, current_position)

# 输出整个游戏过程中,小明所处的最大坐标值
print(max_position)
