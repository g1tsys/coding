"""
# Tree Structure Query Problem - Translation and Solution

## Problem Description

You are given a tree structure represented by multiple lines showing child-parent relationships. After inputting a node, print all its descendant nodes (all nodes below it in the tree).

**Example tree structure:**
```
西安 陕西     (Xi'an is child of Shaanxi)
陕西 中国     (Shaanxi is child of China)
江西 中国     (Jiangxi is child of China)
中国 亚洲     (China is child of Asia)
泰国 亚洲     (Thailand is child of Asia)
```

## Input/Output Format

**Input:**
- First line: number of relationships (n)
- Next n lines: each contains "child parent" separated by space
- Last line: the query node

**Output:**
- All descendant nodes of the query node, sorted in dictionary order (lexicographically)

**Note:** All node names are unique in the tree.

## Python Solution Approach

**Key Ideas:**
1. Build an adjacency list to store parent → children relationships
2. Use DFS (Depth-First Search) or BFS to find all descendants
3. Sort the results alphabetically

## Python Code

```python
def find_all_descendants(n, relationships, query_node):
    # Build adjacency list: parent -> list of children
    tree = {}
    
    for child, parent in relationships:
        if parent not in tree:
            tree[parent] = []
        tree[parent].append(child)
    
    # Find all descendants using DFS
    descendants = []
    
    def dfs(node):
        if node in tree:
            for child in tree[node]:
                descendants.append(child)
                dfs(child)  # Recursively find descendants
    
    dfs(query_node)
    
    # Sort in dictionary order
    descendants.sort()
    
    return descendants

# Example input
n = 5
relationships = [
    ("西安", "陕西"),
    ("陕西", "中国"),
    ("江西", "中国"),
    ("中国", "亚洲"),
    ("泰国", "亚洲")
]
query_node = "中国"

result = find_all_descendants(n, relationships, query_node)
print("\n".join(result))
```

## Example Walkthrough

**Given tree structure:**
```
        亚洲 (Asia)
       /    \
     中国    泰国
    /   \
  陕西   江西
   |
  西安
```

**Query: "中国" (China)**

**Step-by-step execution:**
"""





# 定义一个函数collect_children，用于收集树中所有下层节点
# 参数tree表示树的字典表示，node表示查询节点
def collect_children(tree, node): # type: ignore
    """收集树中所有下层节点"""
    # 如果查询节点不在树中，则返回空列表
    if node not in tree:
        return []
    # 定义一个空列表用于存储所有下层节点
    children = []
    # 定义一个列表用于存储待访问的节点
    nodes_to_visit = [node] # pyright: ignore[reportUnknownVariableType]
    # 循环直到待访问的节点列表为空
    while nodes_to_visit:
        # 取出待访问的节点列表中的最后一个节点
        current_node = nodes_to_visit.pop() # pyright: ignore[reportUnknownVariableType]
        # 获取当前节点的所有子节点
        current_children = tree.get(current_node, [])
        # 将当前节点的子节点添加到下层节点列表中
        children.extend(current_children)
        # 将当前节点的子节点添加到待访问的节点列表中
        nodes_to_visit.extend(current_children)
    # 返回所有下层节点列表
    return children

# 读取输入行数
num_lines = int(input().strip())

# 构建树的字典表示
tree = {}
for _ in range(num_lines):
    # 读取每行数据，以空格分隔节点和父节点
    child, parent = input().strip().split()
    # 如果父节点已经存在于树中，则将子节点添加到父节点的子节点列表中
    if parent in tree:
        tree[parent].append(child)
    # 否则，创建一个新的父节点，并将子节点添加到子节点列表中
    else:
        tree[parent] = [child]

# 读取查询节点
query_node = input().strip()

# 收集查询节点的所有下层节点
descendants = collect_children(tree, query_node)

# 将下层节点按字典序排序
sorted_descendants = sorted(descendants)

# 打印输出每个下层节点
for descendant in sorted_descendants:
    print(descendant)
