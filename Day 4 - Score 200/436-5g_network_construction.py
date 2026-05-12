"""
Based on the text provided, here are the extracted question details and the specific thought process for the Python language section.

### **Question: 5G Network Construction (5G网络建设)**

**Problem Description**
You need to build a 5G network in a city with $N$ selected locations for base stations (numbered 1 to $N$). The goal is to connect these stations using fiber optics to ensure mutual connectivity.
- The cost of laying fiber between different stations varies.
- Some nodes may already have existing fiber connections.
- Connectivity is transitive (if A connects to B, and B connects to C, then A connects to C).

**Input Format**
1.  First line: Integer $N$ (number of stations), where $0 < N \le 20$.
2.  Second line: Integer $M$ (number of potential fiber connections), where $0 < M < N \times (N-1)/2$.
3.  Next $M$ lines: Format `X Y Z P`
    -   `X`, `Y`: Station numbers ($0 < X, Y \le N$, $X \neq Y$).
    -   `Z`: Cost to lay fiber between X and Y ($0 < Z < 100$).
    -   `P`: Connection status ($0$ = not connected, $1$ = already connected).

**Output Format**
-   If a fully connected network is possible: Output the **minimum total construction cost**.
-   If it is impossible to connect all stations: Output **-1**.

---

### **Python Language Thought Process**

**Core Concept: Minimum Spanning Tree (MST)**
The problem asks for the minimum cost to connect all nodes in a graph. This is a classic **Minimum Spanning Tree (MST)** problem. Since some edges (connections) already exist with a cost of 0 to achieve, we need to treat them slightly differently than new construction.

**Algorithm: Kruskal's Algorithm**
The text specifies using **Kruskal's Algorithm**, which is ideal for finding the MST in a weighted, undirected graph.

**Step-by-Step Logic:**

1.  **Problem Analysis**:
    -   We have $N$ nodes and $M$ potential edges.
    -   Some edges are pre-connected (cost effectively 0 for the *new* construction, but they force the nodes to be in the same set immediately).
    -   We need to add new edges with the lowest possible costs to ensure all nodes end up in a single connected component.

2.  **Data Structure: Union-Find (Disjoint Set Union - DSU)**:
    -   To efficiently manage connected components and detect cycles, we use a Union-Find structure.
    -   Each station starts as its own parent.
    -   `find(i)`: Returns the representative (root) of the set containing station `i`.
    -   `union(i, j)`: Merges the sets containing `i` and `j`.

3.  **Processing Existing Connections**:
    -   Iterate through the input list.
    -   If a connection has `P = 1` (already connected), perform `union(X, Y)`.
    -   **Cost**: Add **0** to the total cost, as no new money is spent on these.

4.  **Processing Potential Connections (Kruskal's Step)**:
    -   Filter the input list to keep only edges where `P = 0` (not yet connected).
    -   **Sort** these edges by cost (`Z`) in **ascending order** (greedy approach).
    -   Iterate through the sorted edges:
        -   Check if the two stations (`X` and `Y`) are already in the same set using `find`.
        -   If they are **not** in the same set:
            -   Perform `union(X, Y)`.
            -   Add the cost `Z` to the **total cost**.
        -   If they are already connected, skip the edge (adding it would create a cycle).

5.  **Final Validation**:
    -   After processing all necessary edges, check if all $N$ stations belong to the **same set**.
    -   This can be done by counting the number of unique roots or checking if the number of successful unions equals $N-1$.
    -   **If connected**: Return the calculated `total cost`.
    -   **If not connected**: Return `-1`.

**Key Takeaway**:
The solution combines **Union-Find** for efficient connectivity checks with a **Greedy** strategy (sorting by cost) to ensure the minimum construction expense. Pre-existing links are handled by pre-merging the sets before sorting and selecting new edges.
"""


# 并查集数据结构
class UnionFind:
    def __init__(self, n):
        # 初始化每个节点的父节点为其自身
        self.parent = [i for i in range(n)]

    def find(self, x):
        # 查找节点x的根节点
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # 合并节点x和y所在的集合
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_y] = root_x
            return True
        return False

# 计算连接所有站点的最小成本
def min_cost_to_connect_stations(N, connections):
    uf = UnionFind(N)
    total_cost = 0
    # 首先处理已经存在的连接，不增加额外成本
    for x, y, cost, connected in connections:
        if connected == 1:
            uf.union(x - 1, y - 1)  # 减1是因为并查集中节点索引是从0开始的

    # 对所有未连接的边按成本从低到高排序
    remaining_connections = [c for c in connections if c[3] == 0]
    remaining_connections.sort(key=lambda x: x[2])

    # 使用克鲁斯卡尔算法逐条检查未连接的边
    for x, y, cost, connected in remaining_connections:
        # 如果添加这条边不会造成循环，则添加到MST中
        if uf.union(x - 1, y - 1):
            total_cost += cost

    # 检查是否所有节点都已经连接在同一棵树上
    root = uf.find(0)
    for i in range(1, N):
        if uf.find(i) != root:
            return -1  # 如果有节点未连接，返回-1
    return total_cost

# 读取输入数据
N = int(input())
M = int(input())
connections = []
for _ in range(M):
    x, y, z, p = map(int, input().split())
    connections.append((x, y, z, p))

# 计算最小成本并输出
min_cost = min_cost_to_connect_stations(N, connections)
print(min_cost)
