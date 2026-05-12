"""Based on the text you provided, here is the extracted information for the "Lumberjack" (伐木工) problem.

**Note:** The provided text is a table of contents and description page. It **does not contain the actual Python code, specific algorithmic thought process, or the full sample data** mentioned in the headers (e.g., `🎈 Python 语言 思路` and `🎉 Python 代码` are just titles). The actual logic is locked behind a subscription or further scrolling not included in your snippet.

However, based on the problem description and standard algorithmic patterns for this specific type of problem (Integer Break/Max Product), I can reconstruct the **likely** logic and solution that would appear in that section.

### 📄 Problem Extraction

**Question:**
A tree of length $X$ meters needs to be cut into smaller pieces of integer lengths. The transaction price is the **product** of the lengths of the cut pieces. The goal is to maximize this product while using the **minimum number of cuts**.
*   Each piece must be a positive integer.
*   You can choose not to cut (product = $X$).
*   Input: An integer $X$ ($X \le 50$).
*   Output: The lengths of the pieces that result in the maximum product, sorted in ascending order and separated by spaces.

**Sample Logic (Inferred):**
*   If $X=4$:
    *   No cut: 4 (Product = 4)
    *   Cut into 2+2: Product = $2 \times 2 = 4$. (Same product, but more cuts? Actually, the problem says "minimize cuts" *to achieve* max product. If 4 is max, 0 cuts is better than 1 cut. Wait, usually for $X>4$, splitting yields higher products).
    *   Let's look at $X=10$:
        *   $3+3+4 \rightarrow 3 \times 3 \times 4 = 36$
        *   $2+2+2+2+2 \rightarrow 32$
        *   $5+5 \rightarrow 25$
    *   **Mathematical Principle:** To maximize the product of integers summing to $X$, you should break $X$ into as many **3s** as possible. If a remainder of 1 is left, combine it with a 3 to make two 2s (since $2 \times 2 > 3 \times 1$). If a remainder of 2 is left, keep it as 2.

**Expected Output Format:**
Space-separated integers in ascending order.
*   Example for $X=10$: `3 3 4` (Product 36) or `2 2 3 3`?
    *   $3 \times 3 \times 4 = 36$.
    *   $2 \times 2 \times 3 \times 3 = 36$.
    *   The problem asks for **minimum cuts**.
    *   $3, 3, 4$ requires 2 cuts (3 pieces).
    *   $2, 2, 3, 3$ requires 3 cuts (4 pieces).
    *   So the answer for 10 would be `3 3 4`.

---

### 💻 Reconstructed Python Solution & Thought Process

Since the actual code wasn't in your snippet, here is the standard Python implementation for this specific Huawei OD problem based on the "Max Product Integer Break" logic.

**Thought Process:**
1.  **Edge Cases:** If $X \le 3$, the maximum product is usually the number itself (no cuts), but sometimes the problem implies at least one cut if $X$ is small. However, the prompt says "can also not cut".
    *   $X=1, 2, 3$: Best product is $X$ (1 cut=0).
    *   $X=4$: $2 \times 2 = 4$ (1 cut) vs $4$ (0 cuts). Since we want to minimize cuts for the *same* max product, we prefer 0 cuts? Actually, usually in these problems, $2 \times 2$ is considered the "split" version. But strictly, $4$ is a higher or equal product with fewer cuts. Let's assume standard decomposition rules where we split if it increases product.
    *   *Correction for "Min Cuts":* If $X=4$, product 4 (0 cuts) vs product 4 (1 cut). 0 cuts wins.
    *   If $X=5$: $2 \times 3 = 6$ (1 cut) > 5. Must cut.
    *   If $X=6$: $3 \times 3 = 9$ (1 cut) > 6.
    *   If $X=7$: $3 \times 4 = 12$ (1 cut) > $3 \times 2 \times 2$ (12, 2 cuts).
2.  **Algorithm:**
    *   While $X > 4$, take a 3 and add to the list. $X = X - 3$.
    *   When $X \le 4$, add the remaining $X$ to the list.
    *   This strategy maximizes the product (using 3s).
    *   **Special handling for minimum cuts:** The greedy approach of taking 3s naturally minimizes the number of pieces for a given max product because 3 is the most efficient base.
    *   Sort the result.

**Python Code:**

```python
def solve_lumberjack(x):
    # Edge cases where no cut yields better or equal results with fewer cuts
    # But for X=4, 2*2=4 (1 cut) vs 4 (0 cuts). 0 cuts is better.
    # For X=5, 2*3=6 (1 cut) > 5.
    # For X=6, 3*3=9 (1 cut) > 6.
    
    if x <= 3:
        return [x]
    
    if x == 4:
        # 4 vs 2*2. Both product 4. 0 cuts is better than 1 cut.
        return [4]
    
    # For x > 4, we break into 3s.
    # Logic: Maximize 3s.
    # If remainder is 1: change a 3+1 to 2+2 (2*2=4 > 3*1=3)
    # If remainder is 2: keep 2.
    
    parts = []
    while x > 4:
        parts.append(3)
        x -= 3
    
    # Add the remainder (which will be 2, 3, or 4)
    parts.append(x)
    
    # Sort as required by output
    parts.sort()
    return parts

# Example Usage
if __name__ == "__main__":
    try:
        # Simulating input reading
        import sys
        # In the actual OJ, input might be sys.stdin or input()
        # x = int(input()) 
        x = 10 # Sample test
        
        result = solve_lumberjack(x)
        print(" ".join(map(str, result)))
        
    except ValueError:
        pass
```

**Output Explanation:**
*   **Input:** `10`
*   **Process:**
    *   $10 > 4 \rightarrow$ take 3, remaining 7. List: `[3]`
    *   $7 > 4 \rightarrow$ take 3, remaining 4. List: `[3, 3]`
    *   $4$ is not $> 4$, stop loop. Append 4. List: `[3, 3, 4]`
    *   Sort: `3 3 4`
    *   Product: $3 \times 3 \times 4 = 36$.
    *   Cuts: 2.
*   **Output:** `3 3 4`

*   **Input:** `6`
*   **Process:**
    *   $6 > 4 \rightarrow$ take 3, remaining 3. List: `[3]`
    *   $3$ is not $> 4$, stop. Append 3. List: `[3, 3]`
    *   Product: 9.
*   **Output:** `3 3`

This logic aligns with the standard "Integer Break" dynamic programming or greedy solution often found in Huawei OD exams.

"""


def max_profit(X):
    # 如果木材长度小于等于4，直接返回该长度，因为不切割收益更大
    if X <= 4:
        return [X]

    # 初始化切割结果的列表
    lengths = []

    # 尽量切割成长度为3的小段
    while X > 4:
        lengths.append(3)
        X -= 3

    # 处理剩余的长度
    if X == 1:
        # 如果剩余1，组合前面的一个3和1为4
        lengths[-1] = 4
    elif X > 0:
        lengths.append(X)

    # 返回排序后的结果
    return sorted(lengths)


X = int(input())
result = max_profit(X)

# 输出结果，按升序排列并用空格分隔
print(" ".join(map(str, result)))

