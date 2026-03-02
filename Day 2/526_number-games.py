"""
### Problem Description
Xiao Ming is playing a game.

The system deals `1 + n` cards, each with an integer on it.
The first card is given to Xiao Ming, and the next `n` cards are dealt in order and arranged in a row.

Xiao Ming needs to determine whether there exists a consecutive sequence of one or more cards among the `n` cards such that their sum is divisible by the number on the card in Xiao Ming's hand.

---

### Input and Output

**Input:**
The input contains multiple test cases. Each test case has two lines, and the input ends at EOF.

- The first line has two integers `n` and `m`, separated by a space. `m` represents the number on the card dealt to Xiao Ming.
- The second line has `n` integers, representing the numbers on the `n` cards dealt subsequently, separated by spaces.

**Output:**
For each test case, if there exists a consecutive sequence of cards that satisfies the condition, output `1`; otherwise, output `0`.

---

**Note:**
- \(1 \le n \le 1000\)
- \(1 \le \text{integer on each card} \le 400000\)
- The number of test cases does not exceed 1000
- The test cases are guaranteed to be correct; no need to consider invalid input.

---

Would you like me to also translate the corresponding Python solution steps for this problem?

# Python Language Approach
1.  **Read input data**: First, we need to read the input data. Since the input may contain multiple test cases, we need to use a loop to read until the end of the file.
2.  **Parse data**: For each test case, the first line contains two integers, `n` (the number of cards) and `m` (the number on Xiao Ming's card). The second line contains `n` integers, representing the numbers on the subsequent cards.
3.  **Check if the sum of a consecutive subarray is divisible by `m`**:
    *   Use the **prefix sum** technique to transform the problem into finding two prefix sums `prefix[j]` and `prefix[i]` (where `j > i`) such that `prefix[j] - prefix[i]` is divisible by `m`.
    *   Use a hash table (dictionary) to record the first occurrence position of the remainder of each prefix sum when divided by `m`. If the remainder of the current prefix sum when divided by `m` has already appeared in the hash table, it means there exists a subarray whose sum is divisible by `m`.
4.  **Output the result**: For each test case, if a subarray that meets the condition exists, output `1`; otherwise, output `0`.

---

Do you want me to also provide the full Python code implementation for this problem?

"""


# 导入系统模块以便读取标准输入
import sys


# 定义主函数以处理多组输入
def main():
    # 从标准输入中读取所有输入数据
    input = sys.stdin.read()

    # 按行分割输入数据
    data = input.splitlines()

    # 初始化行号
    index = 0

    # 循环处理每组输入数据
    while index < len(data):
        # 读取当前行，获取 n 和 m 的值
        n, m = map(int, data[index].split())

        # 移动到下一行
        index += 1

        # 读取当前行，获取 n 个数的牌
        cards = list(map(int, data[index].split()))

        # 移动到下一行
        index += 1

        # 前缀和初始化为0
        prefix_sum = 0

        # 使用哈希表记录前缀和模 m 的值及其首次出现的位置
        mod_map = {0: -1}

        # 初始化是否找到满足条件的标志
        found = False

        # 遍历所有牌
        for i in range(n):
            # 更新前缀和
            prefix_sum += cards[i]

            # 计算前缀和模 m 的值
            mod_value = prefix_sum % m

            # 如果模值已经在哈希表中，则找到满足条件的子数组
            if mod_value in mod_map:
                found = True
                break

            # 否则将当前模值及其位置存入哈希表
            mod_map[mod_value] = i

        # 输出结果，1 表示找到，0 表示未找到
        if found:
            print(1)
        else:
            print(0)


# 调用主函数
if __name__ == "__main__":
    main()

