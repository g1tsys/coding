"""
# Weekend Mountain Climbing Problem - Translation and Analysis

## Problem Description

Xiaoming plans to go mountain climbing on the weekend. The terrain is represented by:
- **0**: flat ground
- **1-9**: mountain heights

**Constraints:**
- Xiaoming can only climb or descend by a height difference of **k or less** per move
- Can only move **one grid at a time** (up, down, left, right)
- Starts from the **top-left corner (0,0)**

## Input/Output Format

**Input:**
- First line: `m n k` (space-separated) - representing an m×n 2D mountain map, where k is the maximum height difference per move
- Next m lines: the mountain map (n values per line, space-separated)

**Output:**
- The **highest peak** Xiaoming can reach and the **shortest number of steps** to reach it (space-separated)
- If there are multiple peaks of the same height, output the one with fewer steps
- If no peak is reachable, return `0 0`

## Python Solution Approach

**Algorithm: BFS (Breadth-First Search)**

1. **Use BFS** to explore all reachable positions from (0,0)
2. **Track visited cells** to avoid revisiting
3. **Check height difference** constraint (≤ k) before moving
4. **Record the maximum height** and minimum steps to reach it
5. **Update result** when finding a higher peak or same height with fewer steps

## Example Walkthrough

Let's say we have:

Input:
3 3 1
0 1 2
1 2 3
2 3 4

m=3, n=3, k=1 (max height difference = 1)
Map:
0 1 2
1 2 3
2 3 4


**Step-by-step:**
- Start at (0,0), height=0, steps=0
- Can move to (0,1) height=1 (diff=1 ✓) or (1,0) height=1 (diff=1 ✓)
- From (0,1), can reach (0,2) height=2 (diff=1 ✓)
- Continue BFS, tracking max height and min steps
- Eventually reach height=4 at position (2,2)

**Output:** `4 6` (highest peak is 4, reached in 6 steps)

## Python Code Structure

from collections import deque

def solve(m, n, k, grid):
    # BFS initialization
    queue = deque([(0, 0, 0)])  # (row, col, steps)
    visited = [[False] * n for _ in range(m)]
    visited[0][0] = True
    
    max_height = grid[0][0]
    min_steps = 0
    
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    
    while queue:
        r, c, steps = queue.popleft()
        current_height = grid[r][c]
        
        # Update result if found higher peak or same height with fewer steps
        if current_height > max_height or (current_height == max_height and steps < min_steps):
            max_height = current_height
            min_steps = steps
        
        # Explore neighbors
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                height_diff = abs(grid[nr][nc] - current_height)
                if height_diff <= k:
                    visited[nr][nc] = True
                    queue.append((nr, nc, steps + 1))
    
    return max_height, min_steps


"""



# 导入队列模块，用于实现广度优先搜索(BFS)



from collections import deque

def main():
    # 读取标准输入数据
    import sys
    input = sys.stdin.read().split()
    idx = 0
    
    # 读取地图的行数m、列数n和最大高度差k
    m = int(input[idx])
    idx += 1
    n = int(input[idx])
    idx += 1
    k = int(input[idx])
    idx += 1
    
    # 读取山地高度矩阵
    matrix = []
    for _ in range(m):
        # 读取一行数据并转换为整数列表
        row = list(map(int, input[idx:idx + n]))
        matrix.append(row)
        idx += n
    
    # 初始化最高峰高度为起点(0,0)的高度
    max_height = matrix[0][0]
    # 初始化到达最高峰的最短步数为0
    min_steps = 0
    
    # 创建访问标记矩阵，记录已访问的位置
    visited = [[False for _ in range(n)] for _ in range(m)]
    # 创建BFS队列，存储待访问的位置和步数
    q = deque()
    # 将起点(0,0)加入队列，步数为0
    q.append((0, 0, 0))
    # 标记起点为已访问
    visited[0][0] = True
    
    # 定义四个移动方向：上、下、左、右
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 开始BFS遍历
    while q:
        # 取出队列中的第一个位置和步数
        x, y, steps = q.popleft()
        # 获取当前位置的高度
        current_height = matrix[x][y]
        
        # 更新最高峰和最短步数
        if current_height > max_height:
            # 如果找到更高的山峰，更新最高峰和步数
            max_height = current_height
            min_steps = steps
        elif current_height == max_height:
            # 如果高度相同，保留更小的步数
            if steps < min_steps:
                min_steps = steps
        
        # 遍历四个方向
        for dx, dy in directions:
            # 计算新位置的坐标
            nx = x + dx
            ny = y + dy
            # 检查新位置是否在地图范围内且未被访问
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                # 获取新位置的高度
                next_height = matrix[nx][ny]
                # 检查高度差是否在允许范围内
                if abs(next_height - current_height) <= k:
                    # 标记新位置为已访问
                    visited[nx][ny] = True
                    # 将新位置和步数+1加入队列
                    q.append((nx, ny, steps + 1))
    
    # 检查是否有可以爬的山峰（最高峰是否高于起点）
    if max_height > matrix[0][0]:
        # 输出最高峰高度和最短步数
        print(max_height, min_steps)
    else:
        # 没有可爬的山峰，输出0 0
        print(0, 0)

if __name__ == "__main__":
    main()
