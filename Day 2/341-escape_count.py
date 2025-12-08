"""
# Weekend Mountain Climbing - Complete Translation and Python Solution

## 📋 Problem Translation

**Background:** Xiaoming wants to go mountain climbing on the weekend for exercise.

**Map Representation:**
- `0` = flat ground
- `1-9` = mountain heights

**Movement Rules:**
- Can only move **one grid at a time** (up, down, left, right)
- Height difference between consecutive moves must be **≤ k**
- Starting position: **top-left corner (0, 0)**

**Goal:** Find the highest peak Xiaoming can reach and the shortest path to get there.

---

## 🎯 Input/Output Specification

**Input:**
Line 1: m n k (space-separated)
  - m = number of rows
  - n = number of columns  
  - k = maximum height difference allowed per move
Next m lines: the mountain grid (n integers per line, space-separated)


**Output:**
max_height min_steps (space-separated)
  - max_height = highest reachable peak
  - min_steps = shortest path to that peak
  - If multiple peaks have same height, output the one with fewer steps
  - If no peak is reachable, output: 0 0


---

## 💡 Python Thought Process

### **Algorithm Choice: BFS (Breadth-First Search)**

**Why BFS?**
1. BFS naturally finds the **shortest path** in unweighted graphs
2. We explore level-by-level, guaranteeing minimum steps
3. Perfect for grid traversal problems

### **Key Steps:**

1. **Initialize BFS Queue**
   - Start from (0, 0) with 0 steps
   - Mark starting position as visited

2. **Explore Neighbors**
   - For each position, check 4 directions (up, down, left, right)
   - Validate: within bounds, not visited, height difference ≤ k

3. **Track Maximum**
   - Keep updating the highest reachable peak
   - If same height found, keep the one with fewer steps

4. **Return Result**
   - Output the maximum height and minimum steps

---

## 📝 Complete Python Code

from collections import deque

def weekend_climbing(m, n, k, grid):
    '''
    Find the highest peak reachable and shortest steps to reach it.
    
    Args:
        m: number of rows
        n: number of columns
        k: max height difference allowed
        grid: 2D list representing mountain map
    
    Returns:
        (max_height, min_steps)
    '''

    # BFS initialization
    queue = deque([(0, 0, 0)])  # (row, col, steps)
    visited = [[False] * n for _ in range(m)]
    visited[0][0] = True
    
    # Track the best result
    max_height = grid[0][0]
    min_steps = 0
    
    # Four directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while queue:
        row, col, steps = queue.popleft()
        current_height = grid[row][col]
        
        # Update result if we found a higher peak
        # OR same height with fewer steps
        if current_height > max_height:
            max_height = current_height
            min_steps = steps
        elif current_height == max_height and steps < min_steps:
            min_steps = steps
        
        # Explore all 4 neighbors
        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc
            
            # Check if the new position is valid
            if (0 <= new_row < m and 
                0 <= new_col < n and 
                not visited[new_row][new_col]):
                
                new_height = grid[new_row][new_col]
                height_diff = abs(new_height - current_height)
                
                # Check if height difference is acceptable
                if height_diff <= k:
                    visited[new_row][new_col] = True
                    queue.append((new_row, new_col, steps + 1))
    
    return max_height, min_steps


# Main program
if __name__ == "__main__":
    # Read input
    m, n, k = map(int, input().split())
    grid = []
    for _ in range(m):
        row = list(map(int, input().split()))
        grid.append(row)
    
    # Solve and output
    max_height, min_steps = weekend_climbing(m, n, k, grid)
    print(max_height, min_steps)
```

---

## 🔍 Example Walkthrough

### **Example 1:**

**Input:**

5 4 1
0 1 2 0
1 0 0 0
1 2 1 1
1 3 1 1
0 0 0 9


**Visual Map:**

Grid (5 rows × 4 columns, k=1):
0  1  2  0
1  0  0  0
1  2  1  1
1  3  1  1
0  0  0  9


**Step-by-Step BFS Execution:**

**Step 0:** Start at (0,0), height=0, steps=0

[START] → 0


**Step 1:** From (0,0), explore neighbors
- Right (0,1): height=1, diff=|1-0|=1 ✓ → Add to queue
- Down (1,0): height=1, diff=|1-0|=1 ✓ → Add to queue

**Step 2:** Process (0,1), height=1, steps=1
- Can reach (0,2): height=2, diff=|2-1|=1 ✓

**Step 3:** Process (1,0), height=1, steps=1
- Can reach (2,0): height=1, diff=|1-1|=0 ✓

**Step 4:** Continue BFS...
- From (0,2) reach neighbors with valid height differences
- From (2,0) → (2,1) height=2
- From (2,1) → (3,1) height=3

**Key Path Found:**

(0,0)[0] → (1,0)[1] → (2,0)[1] → (2,1)[2] → (3,1)[3]
Steps: 0 → 1 → 2 → 3 → 4


**Result:**
- Maximum reachable height: **3**
- Minimum steps to reach it: **4**
- Note: Height 9 at (4,3) is **NOT reachable** because no valid path exists

**Output:** `3 4`

---

### **Example 2:**

**Input:**

3 3 2
0 2 4
3 1 5
6 7 8


**Visual Map:**

0  2  4
3  1  5
6  7  8


**BFS Trace:**

1. Start: (0,0), height=0
2. From (0,0): 
   - (0,1) height=2, diff=2 ✓
   - (1,0) height=3, diff=3 ✗ (exceeds k=2)
3. From (0,1):
   - (0,2) height=4, diff=2 ✓
   - (1,1) height=1, diff=1 ✓
4. From (0,2):
   - (1,2) height=5, diff=1 ✓
5. Continue exploring...

**Reachable positions and their steps:**
- (0,0): height=0, steps=0
- (0,1): height=2, steps=1
- (0,2): height=4, steps=2
- (1,1): height=1, steps=2
- (1,2): height=5, steps=3 ← **Maximum!**

**Output:** `5 3`

---

## ⏱️ Complexity Analysis

- **Time Complexity:** O(m × n) - visit each cell at most once
- **Space Complexity:** O(m × n) - for visited array and queue

This solution efficiently finds the optimal answer using BFS! 🎉
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



