"""
### Problem Description
Xiao Hua and Xiao Wei are good friends who have agreed to have dinner together on the weekend.

They communicated via their phones and selected multiple potential dining spots on a map (some are unreachable due to natural terrain). Find the number of dining spots that **both** Xiao Hua and Xiao Wei can reach.

---

### Input and Output

#### Input
1. The first line contains two integers `m` and `n`, representing the length and width of the map, respectively.
2. Starting from the second line, the map information is entered. The map contains:
   - `0`: A passable road.
   - `1`: An obstacle (only `1` represents an obstacle).
   - `2`: The starting position of Xiao Hua or Xiao Wei (the map will have exactly two such positions, which are not obstacles).
   - `3`: A selected dining spot (not an obstacle).

#### Output
Output the number of dining spots that can be reached by both people, with no trailing spaces.

---

Would you like me to also translate the corresponding solution approach for this problem?
# Python Language Approach
1. First, create two 2D boolean arrays `visited_xiaohua` and `visited_xiaowei` to record the positions visited by Xiao Hua and Xiao Wei, initialized to `False`.
2. Find the starting positions of Xiao Hua and Xiao Wei. Traverse the entire map; when the number `2` is encountered, record the coordinates, setting `xiaohua_pos` for one and `xiaowei_pos` for the other.
3. Next, use a `dfs` function to perform a depth-first search. First, check if the current position is out of bounds or has already been visited. If so, return. Then check if the current position is an obstacle. If it is, return. If the current position is passable, mark it as visited.
4. In the `dfs` function, recursively search the adjacent positions in the four directions (up, down, left, right). For each adjacent position, call the `dfs` function.
5. After completing the depth-first searches for both, count the number of dining spots reachable by both. Traverse the entire map; if the current position is a dining spot (number `3`) and has been visited by both Xiao Hua and Xiao Wei, increment the counter `count` by 1.
6. Return the counter `count`, which is the number of dining spots reachable by both.

Finally, call the `count_common_meeting_spots` function, passing in the input map information as a parameter, and then print the calculated result.

---

Would you like me to also provide the full Python code implementation for this problem?

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

