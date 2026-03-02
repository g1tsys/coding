
"""
Problem Description
There is a robot that can be placed at any position in an M x N grid. Each grid cell contains an integer number. The robot can move between adjacent grid cells if the absolute difference between their integer numbers is less than or equal to 1.
Question: Find the maximum number of grid cells that the robot can reach starting from any single position.
Note: The top-left corner of the grid has coordinates (0, 0), and the bottom-right corner has coordinates (m-1, n-1). The robot can only move to adjacent grid cells in the four directions: up, down, left, and right.
Input and Output
Input:
The first line contains two integers, M and N, where M is the number of rows in the grid and N is the number of columns.
The next M lines each contain N integers, which represent the values in the grid. The values are separated by single spaces, with no leading or trailing spaces on any line.
Constraints: M, N, k are integers, where 1 ≤ M, N ≤ 150 and 0 ≤ k ≤ 50.
Output:
Print one line containing a single integer, which is the number of grid cells in the largest connected movable region. The output should have no leading or trailing spaces.


1. First, we define two functions: max_grid_area and dfs.
The max_grid_area function is used to calculate the number of grid points corresponding to the maximum movable range of the robot. It takes a two-dimensional grid as input.
In the max_grid_area function, we first obtain the number of rows m and columns n of the grid.
2. Then, we create a two-dimensional array visited of the same size as the grid to record the visited grids.
3. Next, we iterate over each position in the grid as the starting point. If the position has not been visited, we call the dfs function to perform Depth-First Search (DFS) and obtain the number of grid points in the movable area starting from the current point.
In the dfs function, we first mark the current grid as visited and initialize the count of grid points in the movable area to 1.
4. Then, we define the offsets for the four directions: up, down, left, and right.
Using Depth-First Search, we judge whether the adjacent grid in each direction meets the condition (the absolute value of the difference in numbers is less than 1). If the condition is met, we recursively call the dfs function to continue the search.
5. Finally, return the number of grid points in the movable area.
The max_grid_area function returns the number of grid points in the largest movable area among all starting points, which is the desired result.
"""

def max_grid_area(grid):
    m = len(grid)  # 网格的行数
    n = len(grid[0])  # 网格的列数

    max_area = 0  # 最大活动区域的网格点数目

    # 创建一个与网格大小相同的二维数组，用于记录已访问的网格
    visited = [[False] * n for _ in range(m)]

    # 遍历网格的每个位置作为起点
    for i in range(m):
        for j in range(n):
            if not visited[i][j]:
                area = dfs(grid, i, j, visited)  # 深度优先搜索计算当前起点的活动区域的网格点数目
                max_area = max(max_area, area)  # 更新最大活动区域的网格点数目

    return max_area


def dfs(grid, i, j, visited):
    m, n = len(grid), len(grid[0])
    area = 1  # 活动区域的网格点数目，初始为1
    visited[i][j] = True  # 将当前网格标记为已访问

    # 定义上下左右四个方向的偏移量
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    # 深度优先搜索
    for dx, dy in directions:
        nx, ny = i + dx, j + dy
        if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and abs(grid[nx][ny] - grid[i][j]) <= 1:
            # 如果相邻网格满足条件（编号差值的绝对值小于等于1），则继续搜索
            area += dfs(grid, nx, ny, visited)

    return area


# 读取输入
m, n = map(int, input().split())
grid = []
for _ in range(m):
    row = list(map(int, input().split()))
    grid.append(row)

# 计算最大活动区域的网格点数目
max_area = max_grid_area(grid)

# 输出结果
print(max_area)


