def create_spiral_matrix(n, m):
    # 计算每行需要的数字个数，列数尽可能少
    cols = (n + m - 1) // m
    # 初始化矩阵，填充为0
    matrix = [[0] * cols for _ in range(m)]
    
    # 当前要填入的数字
    num = 1
    # 顺时针螺旋填充的四个方向: 右下左上
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # 当前的方向索引
    direction_idx = 0
    # 当前位置
    row, col = 0, 0
    # 循环填入数字直到n
    while num <= n:
        # 填入数字
        matrix[row][col] = num
        num += 1
        # 计算下一个位置
        next_row = row + directions[direction_idx][0]
        next_col = col + directions[direction_idx][1]
        # 检查下一个位置是否越界或者已经填入数字
        if (0 <= next_row < m and 0 <= next_col < cols and matrix[next_row][next_col] == 0):
            # 更新位置
            row, col = next_row, next_col
        else:
            # 改变方向
            direction_idx = (direction_idx + 1) % 4
            # 更新位置
            row += directions[direction_idx][0]
            col += directions[direction_idx][1]
    
    # 输出矩阵，未填充的位置用*表示
    for i in range(m):
        for j in range(cols):
            if matrix[i][j] == 0:
                print('*', end=' ')
            else:
                print(matrix[i][j], end=' ')
        print()  # 每行输出后换行

# 读取输入
n, m = map(int, input().split())
# 生成并输出矩阵
create_spiral_matrix(n, m)
