"""
The problem involves a drawing machine that starts at the origin (0, 0) and draws a line along the x-axis toward a given endpoint E. During this process, it can be instructed to move vertically (up or down) at specific x-coordinates. The goal is to calculate the total area formed by these vertical offsets and the x-axis, up to the line x = E.

### **Python Language Thought Process**
1. Read the input values N (number of instructions) and E (the x-coordinate of the endpoint).
2. Initialize `prevX` and `prevY` to 0, representing the starting position.
3. Initialize `area` to 0, which will accumulate the total area.
4. Loop through each instruction:
   - Read the x-coordinate and offsetY for the current instruction.
   - Calculate the width of the rectangle formed between the previous x-coordinate and the current x-coordinate: `abs(x - prevX)`.
   - Calculate the height of the rectangle using the previous y-coordinate: `abs(prevY)`.
   - Multiply the width and height to get the area of the rectangle and add it to the total area.
   - Update `prevX` and `prevY` with the current x and the sum of the previous y and the current offsetY.
5. After processing all instructions, calculate the area of the last segment from the last instruction to the endpoint E using the same method.
6. Output the total area.

### **Example Walkthrough**
Let's say the input is:
```
2 5
1 2
3 -1
```

- **Step 1:** Read N = 2 and E = 5.
- **Step 2:** Initialize `prevX = 0`, `prevY = 0`, `area = 0`.
- **Step 3:** First instruction is x = 1, offsetY = 2:
  - Width = `abs(1 - 0) = 1`
  - Height = `abs(0) = 0`
  - Area = `1 * 0 = 0`
  - Update `prevX = 1`, `prevY = 0 + 2 = 2`
- **Step 4:** Second instruction is x = 3, offsetY = -1:
  - Width = `abs(3 - 1) = 2`
  - Height = `abs(2) = 2`
  - Area = `2 * 2 = 4` (total area = 0 + 4 = 4)
  - Update `prevX = 3`, `prevY = 2 - 1 = 1`
- **Step 5:** After all instructions, calculate the last segment from x = 3 to x = 5:
  - Width = `abs(5 - 3) = 2`
  - Height = `abs(1) = 1`
  - Area = `2 * 1 = 2` (total area = 4 + 2 = 6)
- **Final Output:** `6`
"""


N, E = map(int, input().split())  # 输入N和E

prevX = 0
prevY = 0
area = 0

for i in range(N):
    x, offsetY = map(int, input().split())  # 输入每条指令的x和offsetY

    area += abs(x - prevX) * abs(prevY)

    prevX = x
    prevY += offsetY

area += abs(E - prevX) * abs(prevY)

print(area)

