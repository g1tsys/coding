"""
Based on the text provided from the webpage, here is the extracted question and the specific thought process (algorithm) outlined in the **Python** section.

### **Question**
**Title:** Huawei OD Machine Test Question 448: Pair Programming (结对编程)

**Description:**
A department plans to carry out project development through pair programming. There are $N$ employees in the department, each with a unique level. Groups of three employees are formed for pair programming according to the following rules:

Select three employees with indices $i$, $j$, and $k$ (where $0 \le i < j < k < n$) whose levels are $level[i]$, $level[j]$, and $level[k]$. The group must satisfy one of the following conditions:
1. $level[i] < level[j] < level[k]$ (Strictly increasing)
2. $level[i] > level[j] > level[k]$ (Strictly decreasing)

Calculate the number of possible valid combinations. Note that the same employee can participate in multiple groups.

**Input:**
- First line: Total number of employees $n$.
- Second line: Levels of employees in order, separated by spaces.

**Output:**
- The total number of possible pair programming groups.

---

### **Thought Process (Python Approach)**

The core logic involves treating the **middle employee** ($j$) as the pivot point for every possible triplet $(i, j, k)$.

**Step-by-Step Logic:**

1.  **Iterate through potential middle elements:**
    Traverse the array. For each employee at index $j$ (acting as the middle of the triplet), we determine how many valid groups can be formed with them in the center.

2.  **Count neighbors on the Left:**
    For the current employee at index $j$:
    -   Count how many employees to the left ($i < j$) have a **lower** level (`less_left`).
    -   Count how many employees to the left ($i < j$) have a **higher** level (`greater_left`).

3.  **Count neighbors on the Right:**
    For the same employee at index $j$:
    -   Count how many employees to the right ($k > j$) have a **lower** level (`less_right`).
    -   Count how many employees to the right ($k > j$) have a **higher** level (`greater_right`).

4.  **Calculate Valid Combinations for Index $j$:**
    A valid triplet centered at $j$ can be formed in two ways:
    -   **Increasing Sequence ($i < j < k$):** Requires a smaller element on the left and a larger element on the right.
        -   Count = `less_left` $\times$ `greater_right`
    -   **Decreasing Sequence ($i > j > k$):** Requires a larger element on the left and a smaller element on the right.
        -   Count = `greater_left` $\times$ `less_right`

    **Total for index $j$** = (`less_left` $\times$ `greater_right`) + (`greater_left` $\times$ `less_right`)

5.  **Sum Results:**
    Sum the calculated counts for every index $j$ from $0$ to $n-1$ to get the final answer.

**Example Walkthrough (Input: `1 2 3 4`):**
-   **Index 1 (Value 2):**
    -   Left: Smaller (1) = 1, Larger = 0
    -   Right: Smaller = 0, Larger (3, 4) = 2
    -   Calc: $(1 \times 2) + (0 \times 0) = 2$
-   **Index 2 (Value 3):**
    -   Left: Smaller (1, 2) = 2, Larger = 0
    -   Right: Smaller = 0, Larger (4) = 1
    -   Calc: $(2 \times 1) + (0 \times 0) = 2$
-   **Total:** $2 + 2 = 4$

**Final Output:** `4` (The groups are: (1,2,3), (1,2,4), (1,3,4), (2,3,4)).

员工职级:  1   2   3   4
索引:       0   1   2   3

中间职级员工是2 (索引1):
左侧: less_left = 1 (职级1), greater_left = 0
右侧: less_right = 0, greater_right = 2 (职级3和4)
组合数: 1 * 2 + 0 * 0 = 2 (组合: (1,2,3), (1,2,4))

中间职级员工是3 (索引2):
左侧: less_left = 2 (职级1和2), greater_left = 0
右侧: less_right = 0, greater_right = 1 (职级4)
组合数: 2 * 1 + 0 * 0 = 2 (组合: (1,3,4), (2,3,4))

中间职级员工是4 (索引3):
左侧: less_left = 3 (职级1、2和3), greater_left = 0
右侧: less_right = 0, greater_right = 0
组合数: 3 * 0 + 0 * 0 = 0 (没有合法组合)

总共可能的组合数 = 2 + 2 + 0 = 4
"""


def count_teams(n, levels):
    # 初始化小组数量为0
    count = 0

    # 遍历每个可能成为中间职级的员工
    for j in range(n):
        less_left = greater_left = 0

        # 对于中间员工j，遍历其左侧所有员工
        for i in range(j):
            if levels[i] < levels[j]:
                less_left += 1
            elif levels[i] > levels[j]:
                greater_left += 1

        less_right = greater_right = 0
        # 对于中间员工j，遍历其右侧所有员工
        for k in range(j + 1, n):
            if levels[k] < levels[j]:
                less_right += 1
            elif levels[k] > levels[j]:
                greater_right += 1

        # 计算以j为中间职级的小组数量，并累加到总数中
        count += less_left * greater_right + greater_left * less_right

    return count


# 输入输出处理
n = int(input())  # 输入员工总数
levels = list(map(int, input().split()))  # 输入员工的职级，将其转换成整数列表

# 调用函数并输出结果
print(count_teams(n, levels))

