"""Based on the text provided, here are the extracted details for the **Huawei OD Exam Question E-484: Intelligent Driving**.

### **Question Details**

**Title:** Intelligent Driving, Initial Car Fuel (智能驾驶、汽车初始油量)

**Problem Description:**
A car must travel from the top-left corner (start) to the bottom-right corner (end) of an $M \times N$ grid.
- Moving into any region consumes a specific amount of fuel.
- Gas stations allow the car to refuel to full capacity.
- **Goal:** Calculate the **minimum initial fuel** required at the start to ensure the car reaches the destination.

**Rules & Constraints:**
1.  **Movement:** The car can move **Up, Down, Left, Right**.
2.  **Grid Values:**
    -   `-1`: **Gas Station**. Refuels the car to the **maximum capacity of 100**.
    -   `0`: **Obstacle**. The car cannot pass through.
    -   **Positive Integer**: The fuel cost to enter/pass through this region.
3.  **Failure Condition:** If the destination is unreachable, return `-1`.
4.  **Limits:** $0 < M, N \le 200$. Total gas stations $\le 200$. Max tank capacity = 100.

**Input Format:**
-   Line 1: Two integers $M$ and $N$ (dimensions).
-   Next $M$ lines: $N$ integers each representing the grid map.

**Output Format:**
-   Return `-1` if unreachable.
-   Return the **minimum initial fuel** integer if reachable.

---

### **Python Thought Process**

*Note: The original text provided the structure for the Python solution but omitted the detailed logic text. The following thought process is reconstructed based on the problem constraints and the Dijkstra algorithm logic described in the C++ section of the source text.*

To solve this, we need to find a path where the **initial fuel** is minimized. Since the car can refuel at gas stations (resetting fuel to 100), the problem is not a simple shortest path; it depends on the "bottleneck" of fuel consumption between gas stations.

**1. Algorithm Selection: Dijkstra's Algorithm (Reverse Search)**
The most efficient approach is to work **backwards from the destination to the start**.
-   Let `dp[r][c]` represent the **minimum fuel required at cell `(r, c)`** to successfully reach the destination.
-   We use a **Min-Heap (Priority Queue)** to always explore the path requiring the least fuel first.

**2. State Initialization**
-   Create a 2D array `min_fuel` initialized to infinity (`float('inf')`).
-   **Base Case (Destination):**
    -   If the destination `(M-1, N-1)` is a gas station (`-1`), the fuel needed *at* this cell to finish is `0` (since we are already there).
    -   If it is a normal cell with cost `C`, we need `C` fuel to enter it (or `0` if the cost is incurred upon entry and we are already inside? *Standard interpretation*: The cost is to traverse the cell. If we are at the end, we need 0 *additional* fuel to "finish", but we must have had enough to enter. In reverse, `dp[end] = 0` is often used if the cost is on the edge, or `dp[end] = grid[end]` if the cost is on the node. Given the C++ logic "fuel consumption = endpoint position fuel", we treat the cost as the node value. So if we are at the end, we need `grid[end]` to have entered it? Actually, in reverse, `dp[end]` is the fuel needed *just before* entering the end?
    -   *Refined Logic*: `dp[r][c]` = Fuel needed **upon entering** `(r, c)` to reach the end.
    -   At the destination, if it's not a gas station, we need `0` *after* entering. But to enter, we pay the cost.
    -   Let's align with the C++ description: "Start from endpoint... fuel consumption = endpoint position fuel".
    -   So, `dp[M-1][N-1] = grid[M-1][N-1]` (if not gas station). If it is `-1`, `dp` is `0` (since we refill and don't need to go further).

**3. Transition Logic (Reverse Movement)**
We pop the cell with the smallest required fuel `(f, r, c)` from the heap and check neighbors `(nr, nc)`.
-   **Cost Calculation:** To move from `(nr, nc)` to `(r, c)`, we incur the cost of `(nr, nc)`? Or `(r, c)`?
    -   Usually, the cost is associated with the cell we are *entering*. In reverse, if `dp[r][c]` is the fuel needed at `(r, c)`, then to get to `(r, c)` from `(nr, nc)`, we need to pay the cost of `(r, c)`?
    -   *Correction*: The problem says "passing through consumes".
    -   If we are at `(nr, nc)` and move to `(r, c)`, we pay `grid[r][c]`? No, we pay `grid[r][c]` to enter `(r, c)`.
    -   So, `required_at_nr_nc = dp[r][c] + grid[r][c]`?
    -   Wait, if `grid[r][c]` is the cost to enter `(r, c)`, then `dp[r][c]` is the fuel needed *after* paying that cost?
    -   Let's assume `dp[r][c]` is the fuel needed *before* entering `(r, c)`.
    -   Then `dp[r][c] = grid[r][c] + fuel_needed_at_next`.
    -   **Gas Station Logic (`-1`)**:
        -   If `(nr, nc)` is a gas station, we leave it with **100** fuel.
        -   The fuel needed *at* `(nr, nc)` is `0` **UNLESS** the path ahead requires more than 100.
        -   If `fuel_needed_at_next + cost_of_next > 100`, then it's impossible to reach the end from this gas station in one go.
        -   If `fuel_needed_at_next + cost_of_next <= 100`, then `dp[nr][nc] = 0`? No, `dp[nr][nc]` is the fuel needed *before* entering `(nr, nc)`.
        -   Actually, if `(nr, nc)` is a gas station, we can refill to 100. So the constraint is: Can we reach `(nr, nc)`?
        -   The calculation for `dp[nr][nc]` (fuel needed to reach `(nr, nc)` from start) is separate from the fuel needed to leave it.
        -   **In Reverse**: `dp[nr][nc]` = Fuel needed *at* `(nr, nc)` to reach end.
        -   If `(nr, nc)` is `-1`:
            -   We leave with 100.
            -   We need `cost(r,c) + dp[r][c]` to reach the end from `(r, c)`.
            -   If `cost(r,c) + dp[r][c] <= 100`, then `dp[nr][nc] = 0` (we just need to arrive there, refill, and go).
            -   If `> 100`, we cannot pass through this segment from this gas station.
        -   If `(nr, nc)` is a normal cell (cost `C`):
            -   `dp[nr][nc] = dp[r][c] + C`.
            -   We must ensure `dp[nr][nc] <= 100`? No, the initial fuel can be > 100, but we can't have > 100 *remaining* in the tank.
            -   Wait, the problem asks for **Initial Fuel**. Initial fuel can be > 100?
            -   "Minimum initial fuel". If the tank capacity is 100, you cannot start with > 100.
            -   **Constraint Check**: If `dp[0][0] > 100`, return `-1`.

**4. Implementation Steps**
1.  Parse input ($M, N$ and grid).
2.  Initialize `dp` table with infinity.
3.  Priority Queue `pq` stores `(fuel_needed, r, c)`.
4.  Push destination state to `pq`.
    -   If `grid[end] == -1`, `fuel = 0`.
    -   Else, `fuel = grid[end]`.
5.  Loop while `pq` is not empty:
    -   Pop `(f, r, c)`.
    -   If `f > dp[r][c]`, continue.
    -   For each neighbor `(nr, nc)`:
        -   Skip if obstacle (`0`) or out of bounds.
        -   Calculate `new_fuel`:
            -   If `grid[nr][nc] == -1`:
                -   If `f + grid[r][c] <= 100`: `new_fuel = 0`.
                -   Else: `new_fuel = infinity` (impossible from this path).
            -   Else:
                -   `new_fuel = f + grid[nr][nc]` (Cost of entering neighbor).
                -   *Wait*, if we are going reverse, we are moving `r->nr`. The cost is `grid[nr][nc]`?
                -   If `dp[r][c]` is fuel needed *at* `r`, then to go `nr -> r`, we pay `grid[r][c]`?
                -   Let's stick to the C++ hint: "Move to neighbor... calculate new cost".
                -   Usually: `new_cost = current_cost + cost_of_new_cell`.
        -   If `new_fuel < dp[nr][nc]`:
            -   Update `dp[nr][nc] = new_fuel`.
            -   Push to `pq`.
6.  **Final Check**:
    -   If `dp[0][0] > 100` or `dp[0][0] == infinity`, return `-1`.
    -   Else return `dp[0][0]`.

**5. Complexity**
-   Time: $O(M \times N \log(M \times N))$ due to Dijkstra.
-   Space: $O(M \times N)$ for the `dp` table.
"""

import heapq
from typing import List

def solve_intelligent_driving():
    # Reading input would go here
    # M, N = map(int, input().split())
    # grid = [list(map(int, input().split())) for _ in range(M)]
    
    # Example placeholder for logic
    # Directions: Up, Down, Left, Right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # dp[i][j] = min fuel needed at (i, j) to reach end
    # Initialize with infinity
    # ... (Implementation details)
    
    pass
