"""
Problem: Happy Weekend (欢乐的周末)
Problem Description Xiaohua and Xiaowei are good friends planning to meet for dinner on the weekend. They have selected multiple potential dining locations on a map. However, due to natural terrain and obstacles, some locations might be unreachable. The goal is to determine how many dining locations are accessible to both Xiaohua and Xiaowei.

Input Format

The first line contains two integers, m and n, representing the length (rows) and width (columns) of the map.
The following m lines contain the map data, where each cell has a specific value:
0: Open road (passable).
1: Obstacle (impassable).
2: Starting position of a person (Xiaohua or Xiaowei). There are exactly two such positions in the map.
3: A selected dining location (passable).
Output Format

A single integer representing the count of dining locations (value 3) that both individuals can reach.
No trailing spaces at the end of the line.
Example Logic The problem essentially requires checking the connectivity of the grid. Since the map is static and obstacles are fixed, we need to perform a traversal (like BFS or DFS) starting from Xiaohua's position to mark all reachable cells, and then do the same for Xiaowei. Finally, we check which cells marked as dining spots (3) are present in both reachability sets.

Python Solution Approach
The core strategy involves Depth-First Search (DFS) or Breadth-First Search (BFS).

Parse Input: Read the dimensions m and n, then read the grid.
Locate Start Points:
Iterate through the grid to find the coordinates of the two people (cells with value 2). Let's call them start1 and start2. 3. Traverse for Person 1: Perform a DFS/BFS starting from start1 to mark all reachable cells in a visited1 set or 2D array. 4. Traverse for Person 2: Perform a DFS/BFS starting from start2 to mark all reachable cells in a visited2 set or 2D array. - Note: Both traversals treat 0 and 3 as passable, and 1 as blocked. 5. Count Common Spots: Iterate through the grid again. If a cell contains 3 (dining spot) and is present in both visited1 and visited2, increment the counter. 6. Output: Print the final count.

Python Code Implementation
Here is the complete Python solution using DFS:

Iterate through the grid to find the coordinates of the two people (cells with value `2`). Let's call them `start1` and `start2`.
3.  **Traverse for Person 1**: Perform a DFS/BFS starting from `start1` to mark all reachable cells in a `visited1` set or 2D array.
4.  **Traverse for Person 2**: Perform a DFS/BFS starting from `start2` to mark all reachable cells in a `visited2` set or 2D array.
    - *Note*: Both traversals treat `0` and `3` as passable, and `1` as blocked.
5.  **Count Common Spots**: Iterate through the grid again. If a cell contains `3` (dining spot) and is present in **both** `visited1` and `visited2`, increment the counter.
6.  **Output**: Print the final count.

### Python Code Implementation

Here is the complete Python solution using DFS:

```python
import sys

# Increase recursion depth just in case the map is large
sys.setrecursionlimit(100000)

def solve():
    # Read m and n
    try:
        line1 = sys.stdin.readline().split()
        if not line1:
            return
        m, n = map(int, line1)
        
        grid = []
        for _ in range(m):
            row = list(map(int, sys.stdin.readline().split()))
            grid.append(row)
    except ValueError:
        return

    # Find start positions (value 2)
    starts = []
    for r in range(m):
        for c in range(n):
            if grid[r][c] == 2:
                starts.append((r, c))
    
    if len(starts) != 2:
        # According to problem description, there are exactly 2 start points
        # Handle error case gracefully if needed
        print(0)
        return

    start1, start2 = starts

    # Helper function for DFS
    def dfs(start_pos, visited, grid, m, n):
        stack = [start_pos]
        visited[start_pos] = True
        
        # Directions: Up, Down, Left, Right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while stack:
            r, c = stack.pop()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check boundaries
                if 0 <= nr < m and 0 <= nc < n:
                    # Check if not visited and not an obstacle (1)
                    # We can walk on 0 (road), 2 (start), and 3 (dining spot)
                    if not visited[nr][nc] and grid[nr][nc] != 1:
                        visited[nr][nc] = True
                        stack.append((nr, nc))

    # Initialize visited arrays
    visited1 = [[False] * n for _ in range(m)]
    visited2 = [[False] * n for _ in range(m)]

    # Run DFS for both people
    dfs(start1, visited1, grid, m, n)
    dfs(start2, visited2, grid, m, n)

    # Count common dining spots (value 3)
    count = 0
    for r in range(m):
        for c in range(n):
            if grid[r][c] == 3 and visited1[r][c] and visited2[r][c]:
                count += 1

    print(count)

if __name__ == "__main__":
    solve()
```

### Key Considerations
- **Obstacle Handling**: The code strictly checks `grid[nr][nc] != 1` to ensure obstacles are not traversed.
- **Reachability**: Both `0` (road) and `3` (dining spot) are treated as passable terrain.
- **Efficiency**: The time complexity is $O(m \times n)$ because each cell is visited at most a constant number of times (once for each person's traversal). This is efficient enough for typical competitive programming constraints.
- **Recursion Limit**: While the solution uses an iterative stack-based DFS to avoid recursion depth issues, `sys.setrecursionlimit` is included as a safeguard if a recursive implementation were preferred. The iterative approach shown above is generally safer for large grids.

"""


def count_common_meeting_spots(m, n, grid):
    # 创建两个二维列表，分别用于记录小华和小为访问过的位置
    visited_xiaohua = [[False for _ in range(n)] for _ in range(m)]
    visited_xiaowei = [[False for _ in range(n)] for _ in range(m)]
    # 创建一个变量count，用于记录两者都能到达的聚餐地点数量
    count = 0

    # 找到小华和小为的初始位置
    xiaohua_pos = None
    xiaowei_pos = None
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                if xiaohua_pos is None:
                    xiaohua_pos = (i, j)
                else:
                    xiaowei_pos = (i, j)
                    break

    # 分别从小华和小为的位置开始进行深度优先搜索
    dfs(xiaohua_pos[0], xiaohua_pos[1], m, n, grid, visited_xiaohua)
    dfs(xiaowei_pos[0], xiaowei_pos[1], m, n, grid, visited_xiaowei)

    # 统计两者都能到达的聚餐地点数量
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 3 and visited_xiaohua[i][j] and visited_xiaowei[i][j]:
                count += 1

    return count


def dfs(row, col, m, n, grid, visited):
    # 检查当前位置是否越界或已经访问过
    if row < 0 or row >= m or col < 0 or col >= n or visited[row][col]:
        return

    # 检查当前位置是否为障碍物
    if grid[row][col] == 1:
        return

    # 标记当前位置为已访问
    visited[row][col] = True

    # 递归搜索上、下、左、右四个方向的相邻位置
    dfs(row - 1, col, m, n, grid, visited)  # 上方位置
    dfs(row + 1, col, m, n, grid, visited)  # 下方位置
    dfs(row, col - 1, m, n, grid, visited)  # 左方位置
    dfs(row, col + 1, m, n, grid, visited)  # 右方位置


# 读取输入的地图信息
m, n = map(int, input().split())
grid = []
for _ in range(m):
    row = list(map(int, input().split()))
    grid.append(row)

# 调用函数计算两者都能到达的聚餐地点数量
result = count_common_meeting_spots(m, n, grid)

# 输出结果
print(result)

