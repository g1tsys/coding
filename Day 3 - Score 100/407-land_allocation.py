"""
题目描述
从前有个村庄,村民们喜欢在各种田地上插上小旗子,旗子上标识了各种不同的数字,某天全体
村民决定将覆盖相同数字的最小矩阵形的土地的分配给为木村里做出巨大贡献的村民,请问:此次
分配土地,做出贡献的村民中最大会分配多大面积?
输入输出
输入
第一行输入m和n,m代表村子的土地的长,n代表土地的宽宽
第二开始输入地图上的具体标识
输出
输出要分配的土地面积,包含相桐数字旗子的最小矩阵中的的最大面积


1.首先,创建一个空字典flags来存储每个数字旗子的最小矩阵边力界。
2.使用两个嵌套的循环遍历地图的每个位置,其中i表示行数,j表示列数。
3.在每个位置上,检查当前位置的标识是否为0。如果不为0,说E明该位置有旗子。
4.检查该旗子是否在字典flags中已存在。如果不存在,说明这是是该旗子第一次出现,需要初始化
其边界。
将旗子标识作为字典flags的键,创建一个新的字典作为其值。过这个新字典包含四个键值
对,分别为min_x、max_x、min_y、max_y,初始值为当前位置置的行数 i 和列数j
5.如果旗子在字典flags中已存在,说明这不是该旗子第一次出现见,需要更新旗子的边界。
。检查当前位置的行数i和列数j是否小于旗子在字典flags中的的对应值,如果是,则更新最
小边界;如果不是,则更新最大边界。
6.完成遍历后,字典flags中存储了每个数字旗子的最小矩阵边界界。
7.创建一个变量max_area并初始化为0,用于记录最大面积。
8.使用items()方法遍历字典flags中的每一对键值对,其中键为为旗子的标识,值为该旗子的最小
矩阵边界。
9.对于每个旗子,计算其最小覆盖矩阵的面积,并将其与max_areea比较,更新max_area为较大的
值。
。最小覆盖矩阵的面积等于(max_x-min_x+1)*(max_y-miny+1),即横坐标范围乘以
纵坐标范围。
10.完成遍历后,
max_area记录了所有旗子中最大的面积。
11.返回max_area作为结果。
"""

def calculate_largest_area(m, n, grid):
    # 创建一个字典来存储每个数字旗子的最小矩阵边界
    flags = {}
    for i in range(m):
        for j in range(n):
            flag = grid[i][j]
            # 如果当前位置有旗子
            if flag != 0:
                # 如果旗子是第一次出现，初始化其边界
                if flag not in flags:
                    flags[flag] = {'min_x': i, 'max_x': i, 'min_y': j, 'max_y': j}
                else:
                    # 更新旗子的边界
                    flags[flag]['min_x'] = min(flags[flag]['min_x'], i)
                    flags[flag]['max_x'] = max(flags[flag]['max_x'], i)
                    flags[flag]['min_y'] = min(flags[flag]['min_y'], j)
                    flags[flag]['max_y'] = max(flags[flag]['max_y'], j)

    # 遍历所有旗子，计算它们的最小覆盖矩阵面积，并找到最大值
    max_area = 0
    for flag, coords in flags.items():
        area = (coords['max_x'] - coords['min_x'] + 1) * (coords['max_y'] - coords['min_y'] + 1)
        max_area = max(max_area, area)

    # 如果没有旗子，则返回0
    return max_area

# 读取输入数据
m, n = map(int, input().split())
grid = []
for _ in range(m):
    row = list(map(int, input().split()))
    grid.append(row)

# 计算要分配的土地面积并输出
result = calculate_largest_area(m, n, grid)
print(result)


