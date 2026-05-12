"""Based on the text provided from the web page, here is the extracted information regarding the problem description, input/output format, and the Python-specific thought process for the Huawei OD exam question "Matrix Matching: Minimum of the K-th Largest Number".

### 📋 Problem Description
From an $N \times M$ matrix (where $N \le M$), select $N$ numbers such that **no two numbers are in the same row or the same column**. The goal is to find the **minimum value** among the **K-th largest numbers** of all possible valid combinations.

*   **Constraints:** $1 \le K \le N \le M \le 150$
*   **Logic:** There are $M! / N!$ possible combinations. For each combination, identify the K-th largest number. The answer is the minimum of these values.

### 📥 Input Format
The input consists of two parts:
1.  Three integers: $N$, $M$, and $K$.
2.  The $N \times M$ matrix elements (usually row by row).

### 📤 Output Format
A single integer representing the **minimum value** of the K-th largest number found in the valid combinations.

---

### 🐍 Python Thought Process & Algorithm

The solution combines **Binary Search on the Answer** with **Depth-First Search (DFS) for Bipartite Matching**.

#### 1. Core Logic: Binary Search on the Answer
Since we are looking for the *minimum* value that satisfies a condition, and the possible values are bounded by the elements in the matrix, we can sort the unique elements of the matrix and perform a binary search on this sorted list.
*   **Goal:** Find the smallest value `limit` such that we can select at least $K$ numbers $\le$ `limit` in a valid configuration (or specifically, ensure the K-th largest in the selection is $\le$ `limit`).
*   **Check Function:** `can_choose(matrix, limit, k)` checks if it's possible to construct a valid selection where the condition holds.

#### 2. The Check Function (`can_choose`)
This function determines if we can pick $N$ numbers (one per row, distinct columns) such that the K-th largest number in the selection is $\le$ `limit`.
*   **Reframing the Condition:** If the K-th largest number in a set of $N$ numbers is $\le$ `limit`, it implies that at least $N - K + 1$ numbers in the set must be $\le$ `limit`.
    *   *Correction based on typical K-th largest logic:* If we sort the selection in descending order, the K-th element is $\le$ `limit`. This means there are at most $K-1$ elements strictly greater than `limit`. Therefore, there must be at least $N - (K - 1) = N - K + 1$ elements that are $\le$ `limit`.
*   **Algorithm:**
    1.  Initialize a `match` array (size $M$) to track which row is assigned to each column (initially -1).
    2.  Use a **DFS** approach to find a maximum matching in a bipartite graph where an edge exists between `row` and `col` only if `matrix[row][col] <= limit`.
    3.  Count how many rows can be successfully matched under this constraint.
    4.  **Verification:** If the number of matched rows is at least $N - K + 1$, does this guarantee the K-th largest is $\le$ `limit`?
        *   *Refined Logic from the text:* The text suggests checking if we can match enough rows such that the K-th largest condition is met. The text states: `return valid >= k` in the context of checking if at least `k` rows can be matched with values $\le$ `limit`.
        *   *Wait, let's re-read the specific Python logic provided:* The text says `can_choose(matrix, elements[mid], n-k+1)`. It checks if we can find a matching of size `n-k+1` using only numbers $\le$ `limit`.
        *   **Interpretation:** If we can find $N-K+1$ numbers $\le$ `limit` in a valid selection (distinct rows/cols), then in the final set of $N$ numbers, at least $N-K+1$ are small. This ensures the K-th largest (which is the $(N-K+1)$-th smallest) is $\le$ `limit`.

#### 3. DFS Implementation Details
The `dfs(row, vis, match, limit)` function attempts to find a column for the current `row`:
*   Iterate through all columns `col` from $0$ to $M-1$.
*   **Condition:** `matrix[row][col] <= limit` AND `col` is not visited in the current DFS path.
*   **Action:**
    *   Mark `col` as visited.
    *   If `match[col]` is unassigned (`-1`) OR we can successfully reassign `match[col]` to a different row (recursive DFS call), then assign `match[col] = row` and return `True`.
*   If no column works, return `False`.

#### 4. Main Execution Flow
1.  **Read Input:** Parse $N, M, K$ and the matrix.
2.  **Preprocess:** Extract all unique elements from the matrix, sort them to create the `elements` list for binary search.
3.  **Binary Search:**
    *   `low = 0`, `high = len(elements) - 1`, `best = infinity`.
    *   While `low <= high`:
        *   `mid = (low + high) // 2`
        *   `threshold = elements[mid]`
        *   Call `dfs` to count max matching using only values $\le$ `threshold`.
        *   **Check:** If `match_count >= N - K + 1`:
            *   This `threshold` is feasible. Update `best = threshold`.
            *   Try smaller values: `high = mid - 1`.
        *   Else:
            *   Need larger values: `low = mid + 1`.
4.  **Output:** Print `best`.

### 💻 Key Python Code Structure (Inferred)
"""
def solve():
    # 1. Input Parsing
    # n, m, k = map(int, input().split())
    # matrix = [list(map(int, input().split())) for _ in range(n)]
    
    # 2. Prepare unique sorted values for Binary Search
    elements = sorted(list(set(val for row in matrix for val in row)))
    
    # 3. Helper: DFS for Bipartite Matching
    def dfs(row, limit, visited, match):
        for col in range(m):
            if matrix[row][col] <= limit and not visited[col]:
                visited[col] = True
                if match[col] == -1 or dfs(match[col], limit, visited, match):
                    match[col] = row
                    return True
        return False

    # 4. Check Function
    def can_achieve_kth_le(limit):
        # We need at least (n - k + 1) numbers <= limit in a valid selection
        required_count = n - k + 1
        match = [-1] * m
        count = 0
        for i in range(n):
            visited = [False] * m
            if dfs(i, limit, visited, match):
                count += 1
        return count >= required_count

    # 5. Binary Search
    low, high = 0, len(elements) - 1
    ans = elements[-1]
    
    while low <= high:
        mid = (low + high) // 2
        val = elements[mid]
        if can_achieve_kth_le(val):
            ans = val
            high = mid - 1
        else:
            low = mid + 1
            
    print(ans)



