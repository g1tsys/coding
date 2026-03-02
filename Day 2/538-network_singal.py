"""

### Problem Description
A network signal gradually attenuates as it propagates and cannot pass through obstacles. In this scenario, we need to calculate the network signal value at a specific location.

**Note**: The network signal can pass through empty spaces.

- A 2D array `array[m][n]` represents a grid-based map:
  - `array[i][j] = 0`: The grid at row `i`, column `j` is an empty space.
  - `array[i][j] = x` (where `x` is a positive integer): The grid at row `i`, column `j` is the signal source, with an initial signal strength of `x`.
  - `array[i][j] = -1`: The grid at row `i`, column `j` is an obstacle.

There is exactly one signal source, and there can be zero or more obstacles. The network signal attenuates by 1 when propagating to any adjacent grid (up, down, left, right).

You are required to calculate and output the network signal value at the specified location.

---

### Input and Output

#### Input
The input consists of three lines:
1. The first line contains two integers `m` and `n`, indicating that the input is an `m x n` array.
2. The second line is a sequence of `m * n` space-separated integers. The first `n` integers represent the first row, the next `n` represent the second row, and so on. The corresponding value of each grid indicates whether it is an empty space, a signal source, or an obstacle.
3. The third line contains two integers `i` and `j`, representing the coordinates `array[i][j]` for which the network signal value needs to be calculated.

**Note**: Both `i` and `j` start from 0, meaning the first row is row 0.

**Example:**
```
6 5
0 0 0 -1 0 0 0 0 0 0 0 0 -1 4 0 0 0 0 0 0 0 0 0 0 -1 0 0 0 0 0
1 4
```
This represents the following map:
```
0  0  0 -1  0
0  0  0  0  0
0  0 -1  4  0
0  0  0  0  0
0  0  0  0 -1
0  0  0  0  0
```

#### Output
Output the network signal value at the corresponding location. If the network signal never reaches the grid, output `0`.
If a grid can be reached via multiple paths with different attenuation levels, the **larger** signal value is taken as its signal strength.

---

Would you like me to also translate the corresponding solution approach for this problem?

# Python Language Approach
1. Read the number of rows and columns of the input grid, as well as the grid data.
2. Create a 2D grid map (`mp`) and a 2D grid (`ans`) to store the network signal values of each position.
3. Iterate through the input grid data to populate the grid map and record the coordinates of the signal source.
4. Read the coordinates of the position for which the network signal value needs to be calculated.
5. Create a double-ended queue (`deque`) and add the coordinates of the signal source to the queue.
6. Initialize the network signal value of the signal source's position to its initial signal strength in the `ans` grid.
7. Define the offset values for the four directions: up, down, left, and right.
8. Implement the Breadth-First Search (BFS) algorithm:
   - Dequeue the current position `(nowx, nowy)`.
   - Iterate over the four adjacent positions `(nx, ny)` of the current position:
     - Check if the adjacent position is within the valid grid range, is not an obstacle, has a current network signal value greater than 0, and the signal value of the adjacent position in the `ans` grid is 0.
     - Update the signal value of the adjacent position in the `ans` grid to the signal value of the current position minus 1, and enqueue the adjacent position for the next round of search.
9. After the BFS is completed, output the network signal value of the specified position `(a, b)` from the `ans` grid.


"""



from collections import deque

# 输入网格的行数和列数
n, m = map(int, input().split())

# 输入网格的数据
arr = [int(x) for x in input().split()]

# 创建一个空的网格地图
mp = [[0 for _ in range(m)] for _ in range(n)]

# 创建一个用于存储网络信号值的网格
ans = [[0 for _ in range(m)] for _ in range(n)]

now = 0
x, y = 0, 0

# 根据输入的数据填充网格地图和确定信号源的位置
for i in range(n):
    for j in range(m):
        mp[i][j] = arr[now]
        if arr[now] > 0:
            x, y = i, j
        now += 1

# 输入需要计算网络信号值的位置
a, b = map(int, input().split())

q = deque()
q.append((x, y))
ans[x][y] = mp[x][y]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 使用广度优先搜索计算网络信号值
while q:
    nowx, nowy = q.popleft()
    for i in range(4):
        nx = dx[i] + nowx
        ny = dy[i] + nowy
        if nx >= 0 and nx < n and ny >= 0 and ny < m and mp[nx][ny] != -1 and ans[nowx][nowy] > 0 and ans[nx][ny] == 0:
            ans[nx][ny] = ans[nowx][nowy] - 1
            q.append((nx, ny))

# 输出计算得到的网络信号值
print(ans[a][b])


