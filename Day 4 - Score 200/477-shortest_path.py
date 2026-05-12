"""Based on the text provided, here is the extracted problem details and the Python approach for the "Intersection Minimum Time" problem.

### **Problem Statement**
The city grid is structured like a chessboard where every block has equal distance.
- **Travel Time:** It takes `timePerRoad` to traverse one street segment.
- **Traffic Lights:** Each intersection (cell in the matrix) has a traffic light with a specific cycle period `T` (`lights[row][col]`).
- **Rules:**
  - **Straight or Left Turn:** Requires waiting for `T` time (the full cycle of the traffic light at the *current* intersection) before proceeding.
  - **Right Turn:** No waiting required.
  - **Start/End:** The traffic lights at the starting and ending intersections do **not** count towards the waiting time; you can leave/enter from any direction.
  - **Movement:** You can move Up, Down, Left, or Right. You cannot go outside the grid or jump intersections.

**Goal:** Calculate the minimum time to travel from a starting intersection `(rowStart, colStart)` to a destination `(rowEnd, colEnd)`.

---

### **Input Format**
1.  **Line 1:** Two integers `n` and `m` (rows and columns), separated by a space.
2.  **Lines 2 to n+1:** The traffic light matrix. Each line contains `m` integers representing the cycle `T` for that intersection, separated by spaces.
3.  **Line n+2:** One integer `timePerRoad`.
4.  **Line n+3:** Two integers `rowStart` and `colStart` (start coordinates).
5.  **Line n+4:** Two integers `rowEnd` and `colEnd` (end coordinates).

### **Output Format**
- A single integer representing the **minimum time** required to travel between the start and end intersections.

---

### **Python Thought Process & Algorithm**

The problem is a shortest-path problem on a grid with state-dependent edge weights. Since the cost to move depends on the **direction you arrived from** (to determine if you are turning left, going straight, or turning right), a simple 2D BFS/Dijkstra is insufficient. We need to track the **state** as `(row, col, direction)`.

#### **1. State Definition**
We define the state as `min_time[row][col][direction]`, where:
- `row`, `col`: The current intersection coordinates.
- `direction`: The direction the vehicle is currently facing (0: Up, 1: Right, 2: Down, 3: Left). This is crucial because moving from `(r, c)` to a neighbor depends on whether the new move is a straight, left, or right turn relative to the current direction.

#### **2. Initialization**
- Create a 3D array `min_time` of size `n x m x 4`, initialized to infinity (`float('inf')`) to represent unvisited states.
- Define the 4 directions:
  - Up: `(-1, 0)`
  - Right: `(0, 1)`
  - Down: `(1, 0)`
  - Left: `(0, -1)`
- Since the start point has no waiting time and can be approached from any direction, initialize `min_time[rowStart][colStart][0..3] = 0`.
- Push all four initial states `(rowStart, colStart, direction, time=0)` into a priority queue (for Dijkstra) or a queue (for 0-1 BFS if weights were uniform, but here weights vary, so Dijkstra is safer).

#### **3. Search Algorithm (Dijkstra's Algorithm)**
Use a priority queue to always expand the path with the current minimum time.

1.  **Pop State:** Extract `(r, c, current_dir, current_time)` with the smallest `current_time`.
2.  **Check Destination:** If `(r, c)` is `(rowEnd, colEnd)`, we can potentially update the global minimum, but we must continue because a path arriving from a different direction might be faster to reach the end (though usually, the first time we pop the destination in Dijkstra with non-negative weights is optimal, we check all 4 directions at the end).
3.  **Explore Neighbors:** Iterate through all 4 possible next moves (`next_dir`).
    - Calculate `next_r`, `next_c`.
    - **Boundary Check:** Ensure `0 <= next_r < n` and `0 <= next_c < m`.
    - **Calculate Wait Time:**
      - If `next_dir` is the same as `current_dir`: **Straight** -> Wait `T` (where `T = lights[r][c]`).
      - If `next_dir` is a 90-degree counter-clockwise turn: **Left** -> Wait `T`.
      - If `next_dir` is a 90-degree clockwise turn: **Right** -> Wait `0`.
      - *Note: The problem states "Straight and Left need to wait T". Right does not.*
    - **Calculate New Time:** `new_time = current_time + wait_time + timePerRoad`.
4.  **Relaxation:**
    - If `new_time < min_time[next_r][next_c][next_dir]`:
      - Update `min_time[next_r][next_c][next_dir] = new_time`.
      - Push `(next_r, next_c, next_dir, new_time)` to the priority queue.

#### **4. Final Result**
After the queue is empty, the answer is the minimum value among `min_time[rowEnd][colEnd][0]`, `min_time[rowEnd][colEnd][1]`, `min_time[rowEnd][colEnd][2]`, and `min_time[rowEnd][colEnd][3]`.

#### **Key Logic for Turn Detection**
To determine if a move is Straight, Left, or Right:
- Let `dirs = [(-1,0), (0,1), (1,0), (0,-1)]` (Up, Right, Down, Left).
- If `current_dir` is index `i` and `next_dir` is index `j`:
  - **Straight:** `i == j`
  - **Right Turn:** `(i + 1) % 4 == j` (e.g., Up -> Right)
  - **Left Turn:** `(i - 1) % 4 == j` (e.g., Up -> Left)
  - **U-Turn:** Not allowed in this grid context (usually), or treated as two steps.

"""



import heapq
import sys

def solve():
    # Read all input from stdin
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        
        lights = []
        for _ in range(n):
            row = []
            for _ in range(m):
                row.append(int(next(iterator)))
            lights.append(row)
            
        timePerRoad = int(next(iterator))
        rowStart = int(next(iterator))
        colStart = int(next(iterator))
        rowEnd = int(next(iterator))
        colEnd = int(next(iterator))
    except StopIteration:
        return

    # Directions: Up, Right, Down, Left
    # Corresponding changes in (row, col)
    # Index 0: Up, 1: Right, 2: Down, 3: Left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    # min_time[r][c][dir] stores the minimum time to reach (r,c) facing 'dir'
    # Initialize with infinity
    INF = float('inf')
    min_time = [[[INF] * 4 for _ in range(m)] for _ in range(n)]
    
    # Priority Queue: (time, r, c, dir)
    pq = []
    
    # Start point: Can enter from any direction with 0 cost (lights don't count at start)
    # We push all 4 directions as starting states
    for d in range(4):
        min_time[rowStart][colStart][d] = 0
        heapq.heappush(pq, (0, rowStart, colStart, d))
        
    while pq:
        curr_time, r, c, curr_dir = heapq.heappop(pq)
        
        # If we found a shorter path to this state already, skip
        if curr_time > min_time[r][c][curr_dir]:
            continue
        
        # Check if we reached the destination
        if r == rowEnd and c == colEnd:
            # We don't break immediately because we might find a faster path 
            # arriving from a different direction, but Dijkstra guarantees 
            # the first time we pop the destination (any direction) is optimal 
            # IF we treat destination as a sink. 
            # However, to be safe and follow the "min of 4 directions" logic:
            pass
            
        # Explore neighbors
        for next_dir in range(4):
            dr, dc = directions[next_dir]
            nr, nc = r + dr, c + dc
            
            # Check boundaries
            if 0 <= nr < n and 0 <= nc < m:
                # Determine wait time
                wait_time = 0
                
                # Determine relationship between current_dir and next_dir
                # Straight: same index
                # Right: (curr + 1) % 4
                # Left: (curr - 1) % 4
                
                if next_dir == curr_dir:
                    # Straight
                    wait_time = lights[r][c]
                elif (curr_dir + 1) % 4 == next_dir:
                    # Right Turn (No wait)
                    wait_time = 0
                elif (curr_dir - 1) % 4 == next_dir:
                    # Left Turn
                    wait_time = lights[r][c]
                else:
                    # U-turn (180 degrees) - Usually not allowed or treated as 2 moves.
                    # In grid problems like this, direct 180 is often invalid or 
                    # equivalent to Left+Left. Assuming direct 180 is invalid or 
                    # we just don't process it to save space.
                    # If allowed, logic would be: wait_time = lights[r][c] (Left + Left?)
                    # Based on "Straight and Left need to wait", U-turn isn't explicitly mentioned.
                    # We'll skip 180 turns as they are inefficient in this context.
                    continue
                
                new_time = curr_time + wait_time + timePerRoad
                
                if new_time < min_time[nr][nc][next_dir]:
                    min_time[nr][nc][next_dir] = new_time
                    heapq.heappush(pq, (new_time, nr, nc, next_dir))
    
    # Result is the minimum time to reach the end in any direction
    result = min(min_time[rowEnd][colEnd])
    print(result)

if __name__ == "__main__":
    solve()
