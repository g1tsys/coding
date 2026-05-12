"""
Based on the text provided from the webpage, here is the extracted question and the specific thought process for the Python solution.

### **The Question**

**Title:** 孙悟空吃蟠桃 (Sun Wukong Eating Peach)

**Description:**
Sun Wukong sneaks into the Peach Garden while the guards are away. There are $N$ peach trees, where the $i$-th tree has $N[i]$ peaches ($N[i] > 0$). The guards will return in $H$ hours ($H \ge N$).

Sun Wukong decides on an eating speed $K$ (peaches per hour). Each hour, he chooses one tree and eats $K$ peaches from it.
- If the tree has fewer than $K$ peaches, he eats all of them and stops eating for that hour (he does not move to another tree within the same hour).
- He wants to eat all peaches before the guards return.

**Goal:** Find the **minimum integer speed $K$** such that he can finish all peaches within $H$ hours.

**Input Format:**
1. First line: $N$ integers representing the number of peaches on each tree.
2. Second line: An integer $H$ representing the hours until the guards return.

**Output Format:**
- The minimum integer speed $K$.
- If the input is invalid, output `0`.

---

### **Python Thought Process**

The webpage outlines a specific algorithmic approach for solving this problem efficiently using Python:

*   **Core Strategy:** Use **Binary Search** (二分查找法) to optimize the search for the minimum speed $K$. A linear search (checking 1, 2, 3...) would be too slow for large inputs.
*   **Search Range:**
    *   **Minimum Possible Speed ($low$):** `1` (He must eat at least one peach per hour to make progress).
    *   **Maximum Possible Speed ($high$):** The maximum number of peaches on a single tree (e.g., `max(piles)`). If he eats this fast, he can clear any single tree in exactly one hour.
*   **Logic Flow:**
    1.  Initialize the binary search bounds: $low = 1$, $high = \text{max}(piles)$.
    2.  While $low \le high$:
        *   Calculate the middle speed: $mid = (low + high) // 2$.
        *   **Check Feasibility:** Calculate the total hours required to eat all peaches at speed $mid$.
            *   For each tree with $P$ peaches, the hours needed is $\lceil P / mid \rceil$. In integer arithmetic, this is calculated as `(P + mid - 1) // mid`.
            *   Sum these hours for all trees.
        *   **Decision:**
            *   If the total hours $\le H$: This speed is sufficient. Try to find a **smaller** valid speed. Update $high = mid - 1$ and store $mid$ as a potential answer.
            *   If the total hours $> H$: This speed is too slow. Need a **faster** speed. Update $low = mid + 1$.
    3.  Return the smallest valid $mid$ found.

This approach reduces the time complexity from linear to logarithmic relative to the number of peaches, making it suitable for the Huawei OD interview constraints.
"""



def can_finish(peaches, speed, H):
    """
    判断以特定速度 speed 是否能在 H 小时内吃完所有蟠桃。
    """
    hours_spent = 0
    for peach in peaches:
        # 对于每棵树，计算吃完需要的小时数，向上取整
        hours_spent += -(-peach // speed)  # 向上取整可以通过 -(-a // b) 来实现
    return hours_spent <= H  # 如果用时不超过 H，则返回 True

def min_eating_speed(peaches, H):
    """
    二分查找，确定孙悟空吃掉所有蟠桃的最小速度。
    """
    # 最低速度是1，最高速度是蟠桃最多的那棵树上的蟠桃数
    low, high = 1, max(peaches)
    
    # 当 low 和 high 相遇时，我们找到了最小的可能速度
    while low < high:
        mid = (low + high) // 2  # 计算中间速度
        # 检查是否能以 mid 的速度在 H 小时内吃完蟠桃
        if can_finish(peaches, mid, H):
            high = mid  # 如果可以，尝试更低的速度
        else:
            low = mid + 1  # 如果不行，提高速度
    return low  # low 将是我们找到的最小速度

# 输入处理
try:
    peaches = list(map(int, input().strip().split()))  # 第一行输入，将输入的字符串分割后转换为整数列表
    H = int(input().strip())  # 第二行输入，转换为整数
    # 判断输入是否异常，即 H 是否小于蟠桃树的数量
    if H < len(peaches):
        raise ValueError("守卫离开的时间不能小于蟠桃树的数量。")
    
    # 调用函数并输出结果
    K = min_eating_speed(peaches, H)
    print(K)
except Exception as e:
    print("0")  # 输入异常时输出0
