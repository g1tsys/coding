"""
The question is as follows:

**Problem Description**  
A number is considered "不含101" (not containing "101") if its binary representation does not include the substring "101". Given a range of integers [l, r], determine how many numbers in this range are "不含101".

**Input**  
Two positive integers l and r.

**Output**  
An integer indicating the count of numbers in the range [l, r] that do not contain the substring "101" in their binary representation.

---

### 🐍 Python Language Thought Process

1. Initialize a counter `count` to 0.
2. Iterate through each number `num` in the range [l, r].
3. Convert the number `num` to its binary string representation, removing the "0b" prefix.
4. Check if the binary string contains the substring "101".
5. If it does **not** contain "101", increment the counter.
6. After processing all numbers, return the counter value.

---

### 📌 Example Walkthrough

Let’s take the range [1, 10] as an example:

- Binary representations:
  - 1 → `1`
  - 2 → `10`
  - 3 → `11`
  - 4 → `100`
  - 5 → `101` → **contains "101"** → not counted
  - 6 → `110`
  - 7 → `111`
  - 8 → `1000`
  - 9 → `1001`
  - 10 → `1010` → **contains "101"** → not counted

So, the valid numbers are: 1, 2, 3, 4, 6, 7, 8, 9 → **8 numbers**.

---

"""



def countNumbers(l, r):
    count = 0

    for num in range(l, r + 1):
        binary = bin(num)[2:]  # 将数字转换为二进制表示，去掉开头的"0b"
        if '101' not in binary:  # 检查二进制表示中是否包含 "101"
            count += 1

    return count


# 读取输入的区间范围
l, r = map(int, input().split())

# 调用函数计算不含101的数的个数
result = countNumbers(l, r)

# 输出结果
print(result)

