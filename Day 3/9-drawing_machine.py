"""
Here's the translation of the problem:

---

### Problem Description

A drawing machine's pen starts at the origin **(0, 0)**. After starting, it follows these rules to draw straight lines:

1. It attempts to draw a line along the **positive x-axis direction** until a given endpoint **E**
2. During this process, instructions can be issued to **offset in the y-axis direction** — positive `offsetY` means upward, negative means downward

Given the x-coordinate endpoint **E** and several drawing instructions, **calculate the area** of the figure formed by the drawn line, the x-axis, and the line `x = E`.

---

### Input / Output

**Input:**
- First line: two integers **N** and **E** — number of instructions and the x-coordinate endpoint
- Next **N** lines: each contains two integers **x** and **offsetY** representing one instruction
- Guaranteed that x values appear in **strictly increasing order** with no duplicates

**Output:**
- A single integer representing the calculated area
- Guaranteed result is in range **0 to 4,294,967,295**

---

### Python Thought Process

1. Read two integers **N** and **E** using `map(int, input().split())`
2. Initialize `prevX = 0`, `prevY = 0`, and `area = 0`
3. Loop **N** times:
   - Read instruction values **x** and **offsetY**
   - Add `abs(x - prevX) * abs(prevY)` to `area` (width × height of current segment)
   - Update `prevX = x` and `prevY = prevY + offsetY`
4. After the loop, add the final segment: `abs(E - prevX) * abs(prevY)`
5. Print `area`
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

