"""
The problem involves determining the **minimum number of electrical boxes (电箱)** required for a row of server cabinets (机柜) in a data center. The layout is represented as a string of characters where:

- `M` represents a **server cabinet**.
- `I` represents an **interval** (empty space).

### Problem Summary:
Each **server cabinet (`M`)** must have **at least one electrical box** either on its **left or right side**, and that side must be an **interval (`I`)**. If a cabinet is **surrounded by intervals** on both sides, it requires **two boxes**. If only one side has an interval, it requires **one box**. If **no intervals** are adjacent to a cabinet, it's **not possible to place a box**, and the result should be **-1**.

---

###  Solution Walkthrough

Let’s walk through an example:

#### Input:

layout = "MIMMMI"


#### Step-by-step:

1. Initialize a counter `box_count = 0` and an index `i = 0`.

2. Traverse the string character by character:
   - At index `0`, the character is `'M'` (a cabinet).
     - Check the **left** (no character, so no interval).
     - Check the **right** (index `1` is `'I'`).
     - Only one interval is adjacent → `box_count += 1`.
     - Skip to the next cabinet (i.e., skip index `1` and `0` → `i = 2`).

   - At index `2`, the character is `'M'`.
     - Left is `'I'` (index `1`).
     - Right is `'M'` (index `3`).
     - Only one interval is adjacent → `box_count += 1`.
     - Skip to the next cabinet (i.e., skip index `3` and `2` → `i = 4`).

   - At index `4`, the character is `'M'`.
     - Left is `'M'` (index `3`).
     - Right is `'I'` (index `5`).
     - Only one interval is adjacent → `box_count += 1`.
     - Skip to the next cabinet (i.e., skip index `5` and `4` → `i = 6`).

   - At index `6`, the loop ends.

3. Final result: `box_count = 3`.
"""

###  Code (Example):

string = input()  # 输入机柜和间隔的字符串表示

count = 0  # 计数器，记录电箱的数量
i = 0  # 索引，用于遍历字符串
while i < len(string):  # 循环遍历字符串中的每个字符
    c = string[i]  # 当前字符
    if c == 'M':  # 如果是机柜
        if i + 1 < len(string) and string[i + 1] == 'I':  # 如果下一个字符是间隔
            count += 1  # 需要一个电箱
            i += 3  # 跳过机柜和间隔，直接跳到下一个机柜
        elif i - 1 >= 0 and string[i - 1] == 'I':  # 如果前一个字符是间隔
            count += 1  # 需要一个电箱
            i += 1  # 跳过当前机柜，直接跳到下一个机柜
        else:
            count = -1  # 无解，设置电箱数量为-1
            break  # 结束循环
    else:
        i += 1  # 跳过间隔字符

print(count)  # 输出电箱数量
