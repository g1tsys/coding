"""
题目描述!
一个应用启动时，会有多个初始化任务需要执行，并且任务之间有依赖关系，例如A任务依赖B任务，那么必须在B任务执行完成之后，才能开始执行A任务。
现在给出多条任务依赖关系的规则，请输入任务的顺序执行序列，规则采用贪婪策略，即一个任务如果没有依赖的任务，则立刻开始执行，如果同时有多个任务要执行，则根据任务名称字母顺序排序。
例如:B任务依赖A任务，C任务依赖A任务，D任务依赖B任务和C任务，同时，D任务还依赖E任务。那么执行任务的顺序由先到后是:A任务，E任务，B任务，C任务，D任务。这里A和E任务都是没有依赖的，立即执行
输入输出
输入输入参数每个元素都表示任意两个任务之间的依赖关系，输入参数中符号>表示依赖方向，例A->B表示A依赖B，多个依赖之间用单个空格分割
输出
输出为排序后的启动任务列表，多个任务之间用单个空格分割


1.导入必要的库:co11ections模块提供了defauatdict和deque这两个数据结构，分别用于图的邻接表表示和队列操作。
2.定义topological_sort函数:
graph是一个字典，键是节点，值是节点的邻接列表，用于存储图的结构。0
indeeree是一个字典，键是节点，值是节点的入度，用于跟踪每个节点的入度。0
modes是一个集合，用于存储所有出现的节点。03.解析输入并构建图:
。输入的依赖关系是用空格分隔的字符串。
。对每一个依赖关系，用split(-)方法分隔出依赖的两个节点a和b。
。在图中添加一条边b->a，表示a依赖于b。
。增加节点a的入度，并将a和b加入节点集合nodes。4.找到所有入度为零的节点:
。遍历所有节点，筛选出入度为零的节点。
。按字母顺序排序这些节点，并将它们加入队列。5.执行拓扑排序:
。当队列不为空时，取出当前队列中的所有节点，按字母顺序排序。
。清空队列，并将这些节点加入结果列表。
。对于每个节点，遍历其所有邻居节点，将邻居节点的入度减1。
。如果邻居节点的入度变为0，将其加入队列。
6.返回结果:将结果列表转换为以空格分隔的字符串并返回。
"""


from collections import defaultdict, deque

def topological_sort(dependencies):
    graph = defaultdict(list)  # 创建一个默认值为列表的字典，用于存储图的邻接表
    indegree = defaultdict(int)  # 创建一个默认值为0的字典，用于存储每个节点的入度
    nodes = set()  # 创建一个集合，用于存储所有出现的节点

    # 解析输入并构建图
    for dep in dependencies.split():  # 依赖关系由空格分隔
        a, b = dep.split('->')  # 解析每条依赖关系，a依赖于b
        graph[b].append(a)  # 在图中添加边b->a
        indegree[a] += 1  # 增加节点a的入度
        nodes.add(a)  # 将节点a加入集合nodes
        nodes.add(b)  # 将节点b加入集合nodes

    # 找到所有入度为零的节点
    zero_indegree = [node for node in nodes if indegree[node] == 0]  # 筛选入度为零的节点
    zero_indegree.sort()  # 按字母顺序排序
    queue = deque(zero_indegree)  # 使用双端队列存储这些节点

    result = []  # 用于存储最终的拓扑排序结果

    while queue:  # 当队列不为空时
        level_nodes = sorted(queue)  # 当前队列中的节点按字母顺序排序
        queue.clear()  # 清空队列
        for node in level_nodes:  # 遍历当前层级的所有节点
            result.append(node)  # 将节点加入结果列表

            for neighbor in graph[node]:  # 遍历当前节点的所有邻居
                indegree[neighbor] -= 1  # 将邻居节点的入度减1
                if indegree[neighbor] == 0:  # 如果邻居节点的入度变为0
                    queue.append(neighbor)  # 将邻居节点加入队列

    return ' '.join(result)  # 将结果列表转换为字符串输出


input_data = input()  # 读取输入
output = topological_sort(input_data)  # 调用函数计算拓扑排序
print(output)  # 输出结果
