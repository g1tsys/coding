"""
Here is the extracted information from the web page, focusing on the Python programming section, structured for clarity.

### **Problem Statement**

**Title:** Parent-Child Game (Huawei OD Machine Test Question 452)

**Description:**
In a 2D grid map of size $N \times N$, a baby and a mother are placed at random positions. Each cell contains a certain number of candies, and some cells contain obstacles.
*   **Goal:** The mother must reach the baby's position in the **shortest possible time** (1 unit of time per step).
*   **Constraint:** While taking the shortest path, the mother must collect the **maximum number of candies** possible.
*   **Movement:** Up, down, left, right. Cannot move through obstacles.
*   **Grid Values:**
    *   `-3`: Mother's start position.
    *   `-2`: Baby's position (target).
    *   `-1`: Obstacle (cannot pass).
    *   `>= 0`: Number of candies (0 means no candy, but passable).

**Input Format:**
1.  First line: An integer $N$ (size of the matrix).
2.  Next $N$ lines: Each line contains $N$ integers representing the grid values.

**Output Format:**
*   A single integer representing the maximum candies collected on a shortest path.
*   No trailing spaces.

**Constraints:**
*   Maximum map size: $50 \times 50$.

---

### **Thought Process (Python Approach)**

The core challenge is a variation of the **Breadth-First Search (BFS)** algorithm. Standard BFS finds the shortest path in an unweighted graph. Here, we need the shortest path *and* the maximum weight (candies) among all shortest paths.

**Key Algorithmic Steps:**

1.  **Initialization:**
    *   Parse the input to find the coordinates of the Mother (`-3`) and the Baby (`-2`).
    *   Initialize a queue for BFS. Each element in the queue needs to store: `(row, col, steps, current_candies)`.
    *   Initialize a way to track the "best state" for each cell. Since we can visit a cell multiple times if it leads to more candies within the *same* shortest distance, we need a 2D array (or dictionary) `max_candies_at_step[row][col]` to store the maximum candies collected to reach that specific cell in the minimum steps found so far. Alternatively, we can store `visited[row][col]` as the minimum steps, and if we reach it again with the same steps but more candies, we update it.

2.  **BFS Execution:**
    *   Push the Mother's starting position into the queue with `steps = 0` and `candies = 0` (or the candy value of the start cell if applicable, though usually start/end logic varies slightly; based on the problem, we collect candies *on the way*, so we likely add the candy value of the cell we step *into*).
    *   While the queue is not empty:
        *   Dequeue the current position `(r, c, steps, candies)`.
        *   **Check Target:** If `(r, c)` is the Baby's position:
            *   If `steps` is less than the recorded shortest time to the baby, update the global `min_steps` and `max_candies`.
            *   If `steps` equals the recorded `min_steps`, update `max_candies` if `current_candies` is higher.
            *   *Note:* Since BFS guarantees we find paths in increasing order of steps, the first time we reach the baby, that is the shortest time. However, there might be multiple paths of that same length. We must continue processing the current "layer" of the BFS to ensure we find the max candies among all paths of that specific length.
        *   **Explore Neighbors:** Iterate through 4 directions (up, down, left, right).
            *   Calculate new coordinates `(nr, nc)`.
            *   **Validity Check:** Ensure `(nr, nc)` is within bounds and not an obstacle (`-1`).
            *   **State Update Logic:**
                *   Calculate `new_steps = steps + 1`.
                *   Calculate `new_candies = candies + grid[nr][nc]` (if the cell has candies).
                *   **Crucial Logic:** Check if we can reach `(nr, nc)` better:
                    *   If `(nr, nc)` has **never been visited**: Mark visited, set best steps, set best candies, and enqueue.
                    *   If `(nr, nc)` was visited with **fewer steps**: Ignore this path (not the shortest).
                    *   If `(nr, nc)` was visited with the **same steps**: Compare `new_candies` with the recorded `best_candies`. If `new_candies` is greater, update the recorded candies and **re-enqueue** this state to propagate the higher candy count to future nodes.
                    *   If `(nr, nc)` was visited with **more steps**: This implies we found a shorter path to this cell previously? No, BFS finds shortest first. If we reached it with more steps, we ignore.

3.  **Result:**
    *   Return the `max_candies` found when reaching the baby's position with the minimum steps.

**Why Standard BFS isn't enough:**
Standard BFS marks a node as "visited" and never visits it again. This works for finding *a* shortest path. But here, we might reach a specific cell via Path A (length 5, 10 candies) and Path B (length 5, 15 candies). We must discard Path A and continue from Path B. Therefore, the "visited" logic must be: `visited[r][c]` stores the minimum steps to reach `(r,c)`, and we allow re-processing if `current_steps == visited[r][c]` AND `current_candies > stored_candies`.

---

### **Python Code Implementation**

```python
import collections

def solve():
    # Read N
    try:
        line1 = input().split()
        if not line1:
            return
        n = int(line1[0])
    except EOFError:
        return

    grid = []
    start_pos = None
    end_pos = None

    # Read Grid and Locate Start/End
    for r in range(n):
        row_data = list(map(int, input().split()))
        grid.append(row_data)
        for c in range(n):
            if grid[r][c] == -3:
                start_pos = (r, c)
                # Treat start position candy as 0 or the value? 
                # Problem says -3 is mom. Usually start cell candy is not collected or is 0.
                # We will assume we collect candies of cells we step INTO.
                # But if the start cell had a value, we might need to add it.
                # Given the input format, -3 replaces the value. So start candy = 0.
                grid[r][c] = 0 
            elif grid[r][c] == -2:
                end_pos = (r, c)
                # Baby position candy? Usually we collect it.
                # We will treat -2 as a passable cell with 0 candy or specific value?
                # Problem says -2 is baby. Let's assume 0 candy at baby pos unless specified.
                # However, logic usually sums the path.
                grid[r][c] = 0

    if not start_pos or not end_pos:
        print(0)
        return

    # Directions: Up, Down, Left, Right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Queue: (r, c, steps, candies)
    queue = collections.deque()
    queue.append((start_pos[0], start_pos[1], 0, 0))
    
    # visited[r][c] = (min_steps, max_candies)
    # Initialize with infinity steps
    visited = [[(float('inf'), -1) for _ in range(n)] for _ in range(n)]
    visited[start_pos[0]][start_pos[1]] = (0, 0)
    
    min_total_steps = float('inf')
    max_candies_on_shortest = -1

    while queue:
        r, c, steps, candies = queue.popleft()

        # If we reached the baby
        if (r, c) == end_pos:
            if steps < min_total_steps:
                min_total_steps = steps
                max_candies_on_shortest = candies
            elif steps == min_total_steps:
                if candies > max_candies_on_shortest:
                    max_candies_on_shortest = candies
            # We do NOT stop here immediately because there might be another path 
            # in the same BFS layer (same steps) with more candies.
            # However, since we process layer by layer, we can just let it run.
            # Optimization: If steps > min_total_steps, we can stop processing this branch?
            # But BFS queue order ensures we process all 'steps' before 'steps+1'.
            continue

        # If current steps already exceed the known shortest path to baby, skip
        # (Optional optimization, but standard BFS handles this naturally)
        if steps >= min_total_steps:
            continue

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            # Check bounds and obstacles
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] != -1:
                new_steps = steps + 1
                # Candy at new position (grid value is >= 0 now)
                new_candies = candies + grid[nr][nc]

                # Check if this path is better
                prev_steps, prev_candies = visited[nr][nc]

                if new_steps < prev_steps:
                    # Found a shorter path to this cell
                    visited[nr][nc] = (new_steps, new_candies)
                    queue.append((nr, nc, new_steps, new_candies))
                elif new_steps == prev_steps and new_candies > prev_candies:
                    # Found a path with same length but more candies
                    visited[nr][nc] = (new_steps, new_candies)
                    queue.append((nr, nc, new_steps, new_candies))

    # Output result
    if max_candies_on_shortest == -1:
        # Should not happen if baby is reachable
        print(0) 
    else:
        print(max_candies_on_shortest)

if __name__ == "__main__":
    solve()
```

### **Key Logic Explanation**

1.  **State Tracking**: The `visited` array doesn't just store a boolean. It stores a tuple `(min_steps, max_candies)`.
2.  **Re-queuing**: If we reach a cell `(nr, nc)` and the `new_steps` equals the `prev_steps` (meaning we found another shortest path to this cell), we check if `new_candies > prev_candies`. If true, we update the record and **add the state back to the queue**. This ensures that the higher candy count propagates to the baby.
3.  **BFS Guarantee**: Since BFS processes nodes layer by layer (by step count), we are guaranteed to find the minimum steps first. The logic handles multiple paths of the *same* minimum length by updating the candy count before moving to the next step layer.


Here is the extraction and translation of the algorithm explanation and sample data from the image.

### **Sample Input**

```text
4
3 2 1 -3
1 -1 1 1
1 1 -1 2
-2 2 1 3
```

**Explanation of Values:**
*   `4`: Size of the matrix ($N=4$).
*   `-3`: Mother's starting position.
*   `-2`: Baby's position.
*   `-1`: Obstacle (cannot pass).
*   `0` or positive integers: Number of candies.

---

### **Algorithm Explanation (Translated)**

To better understand the algorithm, we can explain it using the sample below:

**1. Initialization**
First, we locate the position of the Mother (`-3`) and the Baby (`-2`). Then, we use **Breadth-First Search (BFS)** to explore all possible paths while accumulating the candy count along the route. Since we are looking for the shortest path, we will record the number of steps and the total candies for each step.

The map is initialized as follows (Note: In the visual representation, `-3` and `-2` are treated as passable cells with `0` candies for calculation purposes, while `-1` is marked as `X` for obstacles):

| | Col 0 | Col 1 | Col 2 | Col 3 |
|---|---|---|---|---|
| **Row 0** | 3 | 2 | 1 | **0** (Mom) |
| **Row 1** | 1 | **X** (Obs) | 1 | 1 |
| **Row 2** | 1 | 1 | **X** (Obs) | 2 |
| **Row 3** | **0** (Baby) | 2 | 1 | 3 |

*   **-3**: Represents the Mother's starting position.
*   **-2**: Represents the Baby's position.
*   **X**: Represents an obstacle.

**2. BFS Search Process**
Next, we begin the BFS search:

1.  **Start:** The Mother's initial position is `(0, 3)` (Row 0, Column 3), and the Baby's position is `(3, 0)`. We add the Mother's starting position to the queue.
2.  **Explore:** From the Mother's position, we explore the four directions (Up, Down, Left, Right). We find that only moving **Down** and **Left** are feasible. We add these two positions to the queue and record their respective candy counts and step numbers.
    *   *Note:* Moving Left from `(0,3)` hits an obstacle? No, looking at the grid: `(0,3)` is Mom. Left is `(0,2)` (1 candy). Down is `(1,3)` (1 candy).
3.  **Iterate:** We repeat the process above, gradually exploring all possible paths to reach the Baby, while recording the total candies for each path.
4.  **Check & Update:** When we reach the Baby's position, we check if the current path's step count is the minimum found so far.
    *   If it is **not** the minimum, we discard this path.
    *   If it **is** the minimum, we update the maximum candy count if the current path has more candies than the previous best.
5.  **Result:** Finally, we identify the path among all shortest paths that yields the highest number of candies.

"""


from collections import deque

# 四个可能的移动方向（上下左右）
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 检查坐标(x, y)是否在地图内且不是障碍物
def is_valid(x, y, n, grid):
    return 0 <= x < n and 0 <= y < n and grid[x][y] != -1

# 定义广度优先搜索函数
def bfs(grid, start, end, n):
    queue = deque()
    # 将妈妈的起始位置加入队列，初始化步数为0，糖果数为0
    queue.append((start[0], start[1], 0, 0))
    visited = set()  # 记录已访问的位置
    visited.add(start)
    max_candies = -1  # 最大糖果数初始化为-1

    while queue:
        x, y, steps, candies = queue.popleft()
        # 如果到达宝宝的位置
        if (x, y) == end:
            # 更新最多糖果数
            max_candies = max(max_candies, candies)
            # 这里我们不继续搜索，因为我们只关心最短路径
            continue

        # 检查四个方向的相邻位置
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # 如果相邻位置有效且未被访问过
            if is_valid(nx, ny, n, grid) and (nx, ny) not in visited:
                visited.add((nx, ny))
                # 如果相邻位置有糖果，更新糖果总数
                new_candies = candies + grid[nx][ny] if grid[nx][ny] >= 0 else candies
                # 将新位置加入队列，步数加1
                queue.append((nx, ny, steps + 1, new_candies))

    return max_candies

# 读取输入
n = int(input())
grid = []
mom = baby = (-1, -1)

# 构建地图并记录妈妈和宝宝的位置
for i in range(n):
    row = list(map(int, input().split()))
    grid.append(row)
    for j, val in enumerate(row):
        if val == -2:  # 宝宝的位置
            baby = (i, j)
        elif val == -3:  # 妈妈的位置
            mom = (i, j)

# 进行广度优先搜索
max_candies = bfs(grid, mom, baby, n)

# 输出最大糖果数
print(max_candies)

