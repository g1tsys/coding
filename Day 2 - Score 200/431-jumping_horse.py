"""
# Horse Jump Problem - Translation and Python Solution

## Problem Description

Given an **m x n chessboard** with horses (represented by numbers) and empty spaces (represented by "."):
- Each **number** represents a horse that can move a maximum of that many steps
- Horses move like Chinese chess knights: 1 square horizontally/vertically, then 1 square diagonally (L-shape)
- Multiple horses can occupy the same position
- **Goal**: Determine if all horses can meet at one position, and if so, return the minimum total steps needed

## Python Approach

### Algorithm Steps:

1. **BFS for each horse**: Calculate minimum steps from each horse to all reachable positions (limited by max steps)
2. **Aggregate total steps**: For each board position, sum the steps needed for all horses to reach it
3. **Find minimum**: Return the position with minimum total steps, or -1 if impossible

### Python Code:

python
from collections import deque

def bfs(m, n, start_x, start_y, max_steps):
    '''BFS to find minimum steps from (start_x, start_y) to all positions'''
    # 8 possible knight moves
    directions = [(-2,-1), (-2,1), (-1,-2), (-1,2), 
                  (1,-2), (1,2), (2,-1), (2,1)]
    
    # Initialize distance matrix (-1 means unreachable)
    dist = [[-1] * n for _ in range(m)]
    dist[start_x][start_y] = 0
    
    queue = deque([(start_x, start_y, 0)])
    
    while queue:
        x, y, steps = queue.popleft()
        
        # Stop if exceeded max steps
        if steps >= max_steps:
            continue
            
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # Check bounds and if not visited
            if 0 <= nx < m and 0 <= ny < n and dist[nx][ny] == -1:
                dist[nx][ny] = steps + 1
                queue.append((nx, ny, steps + 1))
    
    return dist

def solve(m, n, board):
    '''Find minimum total steps for all horses to meet'''
    horses = []
    
    # Find all horses
    for i in range(m):
        for j in range(n):
            if board[i][j] != '.':
                horses.append((i, j, int(board[i][j])))
    
    if not horses:
        return 0
    
    # Calculate total steps for each position
    total_steps = [[0] * n for _ in range(m)]
    
    for x, y, max_step in horses:
        dist = bfs(m, n, x, y, max_step)
        
        for i in range(m):
            for j in range(n):
                if dist[i][j] == -1:
                    # If any horse can't reach, mark as unreachable
                    total_steps[i][j] = -1
                elif total_steps[i][j] != -1:
                    total_steps[i][j] += dist[i][j]
    
    # Find minimum total steps
    min_steps = float('inf')
    for i in range(m):
        for j in range(n):
            if total_steps[i][j] != -1:
                min_steps = min(min_steps, total_steps[i][j])
    
    return min_steps if min_steps != float('inf') else -1

# Input
m, n = map(int, input().split())
board = []
for _ in range(m):
    board.append(input().split())

print(solve(m, n, board))


## Example Walkthrough

**Input:**

3 3
. . .
2 . 1
. . .


**Step-by-step:**

1. **Identify horses**: 
   - Horse at (1,0) with max_steps=2
   - Horse at (1,2) with max_steps=1

2. **BFS from (1,0) with max=2**:
   
   Distance matrix:
   [2, -1, 1]
   [0, 2, -1]
   [2, -1, 1]
   

3. **BFS from (1,2) with max=1**:
   
   Distance matrix:
   [-1, -1, 1]
   [-1, -1, 0]
   [-1, -1, 1]
   

4. **Sum distances**:
   
   Total steps:
   [-1, -1, 2]  (only (0,2) reachable by both)
   [-1, -1, -1]
   [-1, -1, 2]
   

5. **Result**: Minimum = **2** (both horses can meet at (0,2) or (2,2))

**Output:** `2`
"""

from collections import deque

# 八个可能的马移动方向
DIRECTIONS = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

# 为每匹马执行BFS搜索，返回一个矩阵，记录到达每个点的最小步数
def bfs(m, n, x, y, max_steps):
    matrix = [[-1] * n for _ in range(m)]  # 初始化矩阵，-1表示不可达
    matrix[x][y] = 0  # 起始点步数为0
    queue = deque([(x, y)])  # 使用队列进行BFS搜索
    steps = 0

    # BFS搜索，直到达到最大步数
    while queue and steps < max_steps:
        steps += 1
        for _ in range(len(queue)):
            cur_x, cur_y = queue.popleft()
            for dx, dy in DIRECTIONS:  # 遍历八个方向
                new_x, new_y = cur_x + dx, cur_y + dy
                # 如果新位置在棋盘内且之前没有被访问过
                if 0 <= new_x < m and 0 <= new_y < n and matrix[new_x][new_y] == -1:
                    matrix[new_x][new_y] = steps  # 更新步数
                    queue.append((new_x, new_y))  # 新位置入队

    return matrix  # 返回记录步数的矩阵

# 计算所有马到达每个位置的总步数，并找出最小的总步数
def min_total_steps(m, n, horses):
    total_steps = [[0] * n for _ in range(m)]  # 初始化总步数矩阵
    for x, y, steps in horses:  # 遍历每匹马
        reachable = bfs(m, n, x, y, steps)  # 计算可达性矩阵
        for i in range(m):
            for j in range(n):
                if reachable[i][j] == -1:  # 如果某匹马到不了这个点
                    total_steps[i][j] = -1  # 标记为不可达
                elif total_steps[i][j] != -1:  # 如果这个点可达
                    total_steps[i][j] += reachable[i][j]  # 累加步数

    min_step = float('inf')  # 初始化最小步数为无穷大
    for i in range(m):
        for j in range(n):
            if total_steps[i][j] != -1:  # 如果这个点可达
                min_step = min(min_step, total_steps[i][j])  # 更新最小步数

    return min_step if min_step != float('inf') else -1  # 返回最小步数，如果无法达到返回-1

# 读取输入数据
m, n = map(int, input().split())
horses = []  # 初始化马的列表
for i in range(m):
    row = input().split()
    for j, cell in enumerate(row):
        if cell != '.':  # 如果不是空位置
            horses.append((i, j, int(cell)))  # 添加马的位置和步数到列表

# 计算并输出结果
result = min_total_steps(m, n, horses)
print(result if result != -1 else -1)  # 如果无法到达输出-1，否则输出最小步数





