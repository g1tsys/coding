"""### **Question: 寻找最优的路测线路**

**Problem Description:**
You are tasked with evaluating network signal quality by selecting an optimal route for a road test. The network is divided into a grid of $R$ rows and $C$ columns. Each cell in the grid contains an integer value $S$ representing the signal quality (normalized, higher is better).

*   **Start Point:** Top-left corner `[0, 0]`
*   **End Point:** Bottom-right corner `[R-1, C-1]`
*   **Movement:** You can move up, down, left, or right (no diagonals).
*   **Scoring Rule:** The score of a route is determined by the **minimum** signal quality value among all cells in that route.
*   **Goal:** Find a route from start to end that **maximizes** this score. Return the maximum possible score.

**Constraints:**
*   $1 \le R, C \le 20$
*   $0 \le S \le 65535$

**Input Format:**
1.  Integer $R$ (rows)
2.  Integer $C$ (columns)
3.  $R$ lines, each containing $C$ integers representing the grid.

**Output Format:**
*   A single integer representing the optimal route's score.

---

### **Thought Process (Python Implementation)**

The problem asks us to **maximize the minimum value** along a path. This is a classic "Bottleneck Path" or "Maximum Capacity Path" problem. While it resembles a shortest path problem (like Dijkstra), the metric is different: instead of summing weights, we are looking for the path where the weakest link is as strong as possible.

#### **Approach: Binary Search + Depth First Search (DFS)**

Since the signal values are bounded and we want to find the **maximum** possible minimum value, we can use **Binary Search** on the answer (the signal strength).

1.  **Define the Search Space:**
    *   The possible score lies between the minimum value in the grid (0 or `min(grid)`) and the maximum value in the grid (`max(grid)`).
    *   Let `low` be the minimum possible score and `high` be the maximum.

2.  **Binary Search Logic:**
    *   Calculate `mid = (low + high + 1) // 2`. This `mid` represents a **candidate** for the minimum signal strength we want to achieve on our path.
    *   **Check Feasibility:** Can we travel from `[0, 0]` to `[R-1, C-1]` such that **every** cell visited has a signal value $\ge mid$?
    *   To check this, we use **Depth First Search (DFS)** or **Breadth First Search (BFS)**:
        *   Start at `[0, 0]`.
        *   If `grid[0][0] < mid`, return `False` immediately (start point is invalid).
        *   Explore neighbors (up, down, left, right).
        *   Only move to a neighbor if its value is $\ge mid$ and it hasn't been visited yet.
        *   If we reach `[R-1, C-1]`, return `True`.
        *   If the search exhausts all possibilities without reaching the end, return `False`.

3.  **Update Search Range:**
    *   **If feasible (`True`):** It means a path exists with a minimum value of at least `mid`. We might be able to do better, so we try higher values.
        *   Set `low = mid`.
    *   **If not feasible (`False`):** The value `mid` is too high; no path exists where every cell is $\ge mid$. We must lower our expectations.
        *   Set `high = mid - 1`.

4.  **Termination:**
    *   The loop continues while `low < high`.
    *   When `low == high`, we have found the maximum possible minimum value.

#### **Why this works:**
Binary Search reduces the complexity from checking every possible path (exponential) to checking $\log(\text{max\_val})$ scenarios. Each check is a standard traversal ($O(R \times C)$). Given the constraints ($R, C \le 20$), this is extremely efficient ($20 \times 20 = 400$ cells per check).

#### **Alternative Approach (Mentioned for context):**
Dijkstra's algorithm can also be adapted (often called a "Maximum Bottleneck Path" algorithm). Instead of summing distances, the "cost" to reach a node is `max(current_path_min, neighbor_value)`. However, the Binary Search + DFS approach is often easier to implement and very intuitive for this specific "maximize the minimum" constraint.

---

### **Python Code Implementation**
"""

import sys

# Increase recursion depth just in case, though 20x20 is small enough
sys.setrecursionlimit(5000)

def solve():
    # Reading input
    try:
        # Handling potential empty input or malformed lines gracefully
        input_data = sys.stdin.read().split()
    except Exception:
        return

    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        R = int(next(iterator))
        C = int(next(iterator))
        
        grid = []
        for _ in range(R):
            row = []
            for _ in range(C):
                row.append(int(next(iterator)))
            grid.append(row)
    except StopIteration:
        return

    # Edge case: 1x1 grid
    if R == 1 and C == 1:
        print(grid[0][0])
        return

    # Helper function for DFS to check if a path exists with min_val >= target
    def can_reach(target):
        # If start or end is below target, impossible
        if grid[0][0] < target or grid[R-1][C-1] < target:
            return False
        
        visited = [[False for _ in range(C)] for _ in range(R)]
        stack = [(0, 0)]
        visited[0][0] = True
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while stack:
            r, c = stack.pop()
            
            if r == R - 1 and c == C - 1:
                return True
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                    if grid[nr][nc] >= target:
                        visited[nr][nc] = True
                        stack.append((nr, nc))
        
        return False

    # Binary Search for the answer
    # Range of possible answers: min(grid) to max(grid)
    # Since constraints say 0 <= S, we can start low at 0, but min(grid) is tighter
    min_val = min(min(row) for row in grid)
    max_val = max(max(row) for row in grid)
    
    low = min_val
    high = max_val
    ans = min_val
    
    while low <= high:
        mid = (low + high) // 2
        
        if can_reach(mid):
            ans = mid  # This mid is possible, try to find a higher one
            low = mid + 1
        else:
            high = mid - 1
            
    print(ans)

if __name__ == "__main__":
    solve()


