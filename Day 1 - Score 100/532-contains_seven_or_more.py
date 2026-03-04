"""
> The question involves a game where N people are sitting in a circle and take turns counting numbers starting from 1. If the number is a multiple of 7 or contains the digit 7, the person says "over" instead of the number. Given an array of the number of times each person said "over" (but in a shuffled order), the task is to restore the array to the correct order, where the i-th element represents the count for the person with the i-th number in the circle.

### Python Language Thought Process

1. **Understand the Game Logic**:  
   - Each person in the circle counts from 1 to K.
   - If the number is a multiple of 7 or contains the digit 7, the person says "over".
   - We need to simulate this process to determine how many times each person said "over".

2. **Input Parsing**:  
   - Read the shuffled array of "over" counts.
   - Determine the number of people (N) from the length of the array.

3. **Simulate the Game**:  
   - For each number from 1 to K, determine which person would say "over".
   - Count how many times each person says "over".

4. **Restore the Order**:  
   - Match the counts with the correct person based on the simulation.

5. **Output the Result**:  
   - Output the counts in the correct order (1st person to Nth person).

---

### Example Walkthrough

**Input**:  
`3 1 2` (This is the shuffled array of "over" counts)

**Step-by-step**:

1. **Determine N**:  
   The input has 3 elements, so N = 3.

2. **Simulate the Game**:  
   - Assume K = 15 (we can determine this by simulating the counts).
   - For numbers from 1 to 15, check which are multiples of 7 or contain 7.
     - Numbers that meet the condition: 7, 14, 17 (but 17 is beyond K = 15).
     - So the numbers are 7 and 14.
   - Each person takes turns counting, so:
     - Person 1: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
     - Person 2: 16, 17, ...
     - Person 3: 18, 19, ...
   - Only numbers 7 and 14 are valid, and these fall on person 1 and person 2 respectively.

3. **Count "over" per person**:  
   - Person 1: 1 (for number 7)
   - Person 2: 1 (for number 14)
   - Person 3: 0

4. **Restore the Order**:  
   The correct order is `[1, 1, 0]`.

**Output**:  
`1 1 0`

"""


def contains_seven_or_multiple(n):
    """
    检查数字是否是7的倍数或者包含7
    :param n: 待检查的数字
    :return: 如果数字是7的倍数或者包含7，返回True，否则返回False
    """
    return n % 7 == 0 or '7' in str(n)

def restore_order(over_counts):
    """
    还原正确顺序的喊“过”次数
    :param over_counts: 打乱顺序的喊“过”次数
    :return: 正确顺序的喊“过”次数
    """
    n = len(over_counts)  # 获取人数，即数组长度
    order_counts = [0] * n  # 初始化每个人的喊“过”次数为0
    current_number = 1  # 从数字1开始喊
    current_person = 0  # 从编号为1的人开始（0索引表示编号1）

    # 总的“过”次数是输入数组的总和
    total_over_count = sum(over_counts)

    # 当“过”次数没有达到总的“过”次数时，一直循环
    while sum(order_counts) < total_over_count:
        # 如果当前数字需要喊“过”
        if contains_seven_or_multiple(current_number):
            order_counts[current_person] += 1  # 当前编号的人“过”次数加1
        
        # 当前数字增加1，移动到下一个人
        current_number += 1
        current_person = (current_person + 1) % n  # 确保当前人编号循环在0到n-1之间

    return order_counts

# 输入处理
input_data = input().strip().split()  # 读取输入，并去除首尾空白，按空格分隔
over_counts = list(map(int, input_data))  # 将输入的每个元素转换为整数，形成列表

# 调用函数还原正确顺序的喊“过”次数，并输出结果
result = restore_order(over_counts)
print(" ".join(map(str, result)))  # 将结果列表转换为字符串并按空格分隔输出


