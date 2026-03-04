
"""
Here's the translation of the problem:

---

### Problem Description

A parking lot of a specific size is represented by an array `cars[]`, where **1 means a parking spot is occupied** and **0 means it is empty**.

Vehicles vary in size:
- **Small car** → occupies **1 spot**
- **Truck (货车)** → occupies **2 spots**
- **Large truck (卡车)** → occupies **3 spots**

**Count the minimum number of vehicles** that could be parked in the lot, and return that number.

---

### Input / Output

- **Input:** An integer string array `cars[]`, where `1` = occupied, `0` = empty. Array length < 1000.
- **Output:** An integer representing the **minimum number of vehicles**.

---

### Python Thought Process

1. Read the input parking lot array and parse it into a string list.
2. Initialize a counter variable `count = 0`.
3. Traverse each element of the array while maintaining a pointer `i` for the current position.
4. When a `1` is encountered, determine the vehicle size:
   - If **3 consecutive 1s** → it's a large truck (3 spots), advance `i` by 3
   - If **2 consecutive 1s** → it's a medium truck (2 spots), advance `i` by 2
   - If **only 1** → it's a small car (1 spot), advance `i` by 1
   - Increment `count` by 1 in each case
5. When a `0` is encountered, simply advance `i` by 1.
6. Continue until the array is fully traversed.
7. Output the final `count` — the **minimum number of vehicles**.
"""

cars = input().strip().split(',')

count = 0
size = len(cars)
i = 0

while i < size:
    if cars[i] == '1':
        if i + 2 < size and cars[i + 1] == '1' and cars[i + 2] == '1':
            count += 1
            i += 3  # 卡车占据3个车位
        elif i + 1 < size and cars[i + 1] == '1':
            count += 1
            i += 2  # 货车占据2个车位
        else:
            count += 1
            i += 1  # 小车占据1个车位
    else:
        i += 1

print(count)


