"""
给定一个mtn的整数阵作为地图，短阵数值为地形高度:中庸行者选择地图中的任意一点作为起点，尝试往上、下、左、右四个相邻格子移动;移动时有如下约束:
1、中庸行者只能上坡或者下坡，不能走到高度相同的点。
2、不允许连续上坡或者连续下坡，需要交替进行;
3、每个位置只能经过一次，不能重复行走;
4、请给出中庸行者在本地图内，能连续移动的最大次数。
输入输出Q
前入一个只包含整数的二维数组
说明:
第一行两个数字，分别为行数和每行的列数后续数据为矩阵地图内容:矩阵边长范围:[1，8:地形高度范围:[0，100000:
前出
一个整数，代表中庸行者在本地图内，能连续移动的最大次数

输入
2 2
1 2
4 3

输出
3

输入
3 3
1 2 4
3 5 7
6 8 9

输出
4


1、首先，定义了一个方向数组Qdirections，其中每个元素表示上、下、左、右四个方向的移动。
2、接下来，定义了一个can_move函数，用于检查是否可以从一个点移动到另一个点。该函数首先判断目标点是否在地图Q范围内，并且未被访问过。然后根据是否上坡或下坡来判断是否可以移动到目标点。
3、然后，定义了一个DFS函数来进行深度Q优先搜索。该函数首先更新最大移动次数。然后标记当前位置为已访问。接着遍历四个方向，对于每个方向，判断是否可以移动到下一个点，如果可以，则递归调用DFS函数。最后，在回溯时取消当前位置的访问标记。

"""

def max_moves(matrix):
    rows, cols = len(matrix), len(matrix[0])
    max_move_count = 0

    # 定义方向数组，分别对应上、下、左、右
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 检查是否可以从一个点移动到另一个点
    def can_move(x, y, nx, ny, going_up):
        if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]:
            if going_up and matrix[nx][ny] > matrix[x][y]:
                return True
            if not going_up and matrix[nx][ny] < matrix[x][y]:
                return True
        return False

    # DFS搜索函数
    def dfs(x, y, move_count, going_up):
        nonlocal max_move_count
        # 更新最大移动次数
        max_move_count = max(max_move_count, move_count)
        # 标记当前位置已经访问
        visited[x][y] = True
        # 遍历四个方向
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if can_move(x, y, nx, ny, going_up):
                # 尝试下一步移动，上坡和下坡交替进行
                dfs(nx, ny, move_count + 1, not going_up)
        # 回溯时取消当前位置的访问标记
        visited[x][y] = False

    # 对每个点进行深度优先搜索
    for i in range(rows):
        for j in range(cols):
            visited = [[False] * cols for _ in range(rows)]
            dfs(i, j, 0, True)  # 尝试上坡移动
            dfs(i, j, 0, False)  # 尝试下坡移动

    return max_move_count

# 读取输入并调用函数
def main():
    m, n = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(m)]
    print(max_moves(matrix))

if __name__ == "__main__":
    main()

