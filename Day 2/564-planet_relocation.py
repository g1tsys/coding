"""
### Problem Description
In the year 2XXX, humans began transforming the atmosphere of Mars to make it habitable. Due to technical limitations, the transformation must be done in a localized manner.

We assume the transformation area is an `row × column` grid. Each grid cell can be in one of three states:
- **YES**: Habitable zone
- **NO**: Transformable zone
- **NA**: Dead zone (cannot be transformed, and cannot be judged as a habitable zone; cannot be passed through)

After initialization, the transformable zones (NO) can exist in multiple regions. Each day at noon, every habitable zone (YES) will automatically transform the four adjacent empty zones (up, down, left, right) into habitable zones.

Calculate whether all transformable zones in the given grid can be fully transformed into habitable zones. If yes, return the number of days required for the full transformation. If not, return `-1`.

---

### Input and Output

#### Input
A `row × column` grid, where each cell's value is one of: `YES`, `NO`, or `NA`.

#### Output
- If all transformable zones (NO) can be fully transformed into habitable zones (YES), return the number of days required.
- If it is impossible, return `-1`.

---

Would you like me to also translate the corresponding solution approach for this problem?

# Python Language Approach
1. Read the number of rows and columns of the input grid, and define the offset values for the four directions (up, down, left, right).
2. Create an empty queue `queue` to store the coordinates of habitable zone cells.
3. Traverse the input grid, find all initial habitable zone ("YES") cells, add their coordinates to the queue, and increment a counter `count`.
4. Initialize a variable `days` to record the number of days of transformation.
5. Enter a loop that continues as long as the queue is not empty:
   a. Get the current length `size` of the queue.
   b. Traverse all the habitable zone cells that will spread during the current day:
      - Pop a cell `(x, y)` from the queue.
      - Expand to the four adjacent directions, checking if the adjacent cell is out of bounds or already transformed.
      - If the adjacent cell is within bounds and is a transformable zone ("NO"), change it to a habitable zone ("YES"), add the new habitable zone `(nx, ny)` to the queue, and increment the `count` counter.
   c. Increment the `days` counter.
6. After the BFS completes, traverse the entire grid again. If any cell is still a transformable zone ("NO"), return `-1` to indicate that it is impossible to transform all zones.
7. Return `days - 1`, which represents the number of days required to complete the transformation.

---

Would you like me to also provide the full Python code implementation for this problem?

"""

def mars_atmosphere(grid):
    row = len(grid)  # 获取行数
    column = len(grid[0])  # 获取列数

    # 定义四个方向的偏移量，用于扩散
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    queue = []  # 存储宜居区格子的队列
    count = 0  # 初始宜居区的数量

    # 遍历待改造区域，找到初始宜居区格子并加入队列
    for i in range(row):
        for j in range(column):
            if grid[i][j] == "YES":
                queue.append((i, j))
                count += 1

    days = 0  # 记录扩散的天数

    while queue:
        size = len(queue)

        # 当前扩散天数内的宜居区进行扩散
        for _ in range(size):
            x, y = queue.pop(0)

            # 向四个方向进行扩散
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                # 判断是否越界或已经改造过
                if 0 <= nx < row and 0 <= ny < column and grid[nx][ny] == "NO":
                    grid[nx][ny] = "YES"  # 将可改造区改为宜居区
                    queue.append((nx, ny))  # 加入队列

        days += 1

    # 判断是否成功将所有可改造区改造为宜居区
    for i in range(row):
        for j in range(column):
            if grid[i][j] == "NO":
                return -1

    return days - 1


grid = [
    ["YES", "NO", "NO", "NO"],
    ["NO", "NO", "NO", "NO"],
    ["NO", "NO", "NO", "NO"],
    ["NO", "NO", "NO", "NO"]
]

result = mars_atmosphere(grid)
print(result)  

