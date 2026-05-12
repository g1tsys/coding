"""
### Python Question Summary
**Problem Title:** 433. The Courier's Dilemma (Huawei OD Exam Question)

**Task:**
Design the shortest path for a courier to deliver packages to $n$ customers and return to the starting depot.
- **Constraints:**
  - Must visit every customer at least once.
  - Order of delivery is flexible.
  - The depot and customers can be visited multiple times.
  - Paths exist from the depot to every customer.
  - Paths between customers may not exist (must go through the depot if no direct link).
- **Input:**
  - $n$ (number of customers) and $m$ (number of direct customer-to-customer links).
  - $n$ lines: `customer_id` `depot_distance`.
  - $m$ lines: `customer_id_1` `customer_id_2` `distance`.
- **Output:**
  - The total minimum distance to visit all customers and return to the depot.
  - Output `-1` if no valid path exists.
- **Limits:** $0 < n \le 10$, $0 \le m \le 10$.

---

### Python Thought Process & Solution Logic

Based on the provided text, here is the step-by-step reasoning for the Python solution:

1.  **Graph Construction**:
    - Treat the **depot** as node `0`.
    - Treat each **customer** as a node based on their ID.
    - Initialize a distance matrix (adjacency matrix) where `distance[i][j]` represents the direct distance between node `i` and node `j`.
    - Initialize all `distance[i][j]` to infinity (`INF`), except `distance[i][i] = 0`.

2.  **Populate Direct Distances**:
    - **Depot to Customer**: Read the $n$ lines of input. For each customer $C$ with distance $D$ from the depot, set `distance[depot][C] = distance[C][depot] = D`.
    - **Customer to Customer**: Read the $m$ lines of input. For each pair $(C1, C2)$ with distance $D$, set `distance[C1][C2] = distance[C2][C1] = D`.

3.  **Compute All-Pairs Shortest Paths (Floyd-Warshall)**:
    - Since customers can visit the depot multiple times, the shortest path between two customers might not be a direct edge but a path *through* the depot.
    - Apply the **Floyd-Warshall algorithm** to update the distance matrix. This ensures `distance[i][j]` holds the true shortest path between any two nodes $i$ and $j$, potentially via the depot.
    - *Logic*: Iterate $k$ (intermediate node), then $i$, then $j$. Update: `distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])`.

4.  **Find Optimal Delivery Order (Backtracking/Permutations)**:
    - Since $n$ is small ($n \le 10$), we can check all possible permutations of customer visits.
    - **Goal**: Find a permutation $[p_1, p_2, ..., p_n]$ such that the total path cost is minimized:
      $$ \text{Total Cost} = \text{dist}(\text{depot}, p_1) + \text{dist}(p_1, p_2) + ... + \text{dist}(p_{n-1}, p_n) + \text{dist}(p_n, \text{depot}) $$
    - **Algorithm**:
      - Generate all permutations of the customer IDs.
      - For each permutation, sum the distances using the pre-computed shortest path matrix.
      - Track the minimum total distance found.

5.  **Result Handling**:
    - If the minimum distance remains `INF` (meaning some node is unreachable), output `-1`.
    - Otherwise, output the calculated minimum distance.

```text
Key Python Implementation Steps:
1. Read n, m.
2. Map customer IDs to a list of visited nodes.
3. Initialize distance matrix with INF.
4. Fill depot connections and given customer connections.
5. Run Floyd-Warshall to fill in indirect paths (via depot).
6. Use itertools.permutations to try all delivery orders.
7. Calculate total distance for each order and find the minimum.
8. Return -1 if min_distance is still INF, else return min_distance.
```

"""


# 算法复杂度在面对多数量的时候较高,大家可以自己优化下

# Floyd-Warshall 算法用于计算图中所有点对之间的最短路径
def floyd_warshall(graph, id_to_index, n):
    # 初始化距离矩阵，所有距离初始值设为无穷大
    distance = [[float('inf')] * n for _ in range(n)]
    # 对于图中每个点，其到自身的距离为0
    for i in range(n):
        distance[i][i] = 0
    # 根据输入的图关系，初始化距离矩阵
    for (i, j), dist in graph.items():
        i_idx, j_idx = id_to_index[i], id_to_index[j]
        distance[i_idx][j_idx] = dist

    # Floyd-Warshall 算法主体，三重循环更新所有点对之间的最短路径
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # 如果通过中间点k的路径更短，则更新i到j的最短距离
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    return distance

# 根据输入的客户信息和客户之间的距离信息，找出完成快递任务的最短路径
def find_shortest_path(n, m, station_to_customers, customers_to_customers):
    graph = {}  # 存储节点之间的距离
    id_to_index = {0: 0}  # 将客户ID映射到索引，投递站的索引为0
    index = 1  # 客户的索引从1开始

    # 处理投递站到客户之间的距离
    for cust_id, dist in station_to_customers:
        if cust_id not in id_to_index:
            id_to_index[cust_id] = index
            index += 1
        graph[(0, cust_id)] = dist
        graph[(cust_id, 0)] = dist

    # 处理客户之间的距离
    for cust1, cust2, dist in customers_to_customers:
        if cust1 not in id_to_index:
            id_to_index[cust1] = index
            index += 1
        if cust2 not in id_to_index:
            id_to_index[cust2] = index
            index += 1
        graph[(cust1, cust2)] = dist
        graph[(cust2, cust1)] = dist

    # 使用Floyd-Warshall算法计算所有点对之间的最短路径
    distance = floyd_warshall(graph, id_to_index, index)

    # 获取所有客户的索引
    all_customers = [id_to_index[cust_id] for cust_id, _ in station_to_customers]
    min_distance = float('inf')  # 初始化最短路径长度为无穷大

    # 遍历所有客户的排列组合，寻找最短路径
    from itertools import permutations
    for perm in permutations(all_customers):
        curr_distance = distance[0][perm[0]]  # 从投递站到第一个客户的距离
        for i in range(len(perm) - 1):
            curr_distance += distance[perm[i]][perm[i + 1]]  # 客户之间的距离
        curr_distance += distance[perm[-1]][0]  # 从最后一个客户返回投递站的距离

        min_distance = min(min_distance, curr_distance)  # 更新最短路径长度

    # 如果找到了有效的最短路径，则返回其长度；否则返回-1
    return min_distance if min_distance != float('inf') else -1

# 从输入中读取客户数n和客户间距离数m
n, m = map(int, input().split())
station_to_customers = []  # 存储投递站到客户之间的距离
for _ in range(n):
    cust_id, dist = map(int, input().split())
    station_to_customers.append((cust_id, dist))

customers_to_customers = []  # 存储客户之间的距离
for _ in range(m):
    cust1, cust2, dist = map(int, input().split())
    customers_to_customers.append((cust1, cust2, dist))

# 计算最短路径距离
shortest_distance = find_shortest_path(n, m, station_to_customers, customers_to_customers)
print(shortest_distance)  # 输出最短路径距离

