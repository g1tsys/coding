"""
# Computer Virus Infection Problem - Translation and Analysis

## 📋 Problem Description

In a local area network, there are many computers labeled from 0 to N-1. Connected computers have different distances, resulting in different infection times (represented by t).
When one computer in the network is infected by a virus, we need to find the **minimum time required** to infect all computers in the network. If some computers cannot be infected, return **-1**.
Given an array where `path[i] = {i, j, t}` means: computer i can infect computer j, and it takes time t.

## 📥 Input/Output

**Input:**
- First line: N (number of computers)
- Second line: Number of network connections
- Following lines: Each contains {source, target, time}

**Output:**
- Minimum time to infect all computers, or -1 if impossible

## 🧠 Python Solution Approach

This is a **shortest path problem** (Dijkstra's algorithm):

1. **Build adjacency list** - Create a graph representation where each node stores its neighbors and infection times
2. **Initialize distances** - Set all distances to infinity, except the starting node (0)
3. **Use priority queue (min-heap)** - Always process the node with shortest infection time
4. **Update neighbors** - For each node, check if going through it provides a shorter path to neighbors
5. **Check completion** - If all nodes are reachable, return max infection time; otherwise return -1

## 💻 Python Code Example


import heapq
from collections import defaultdict

def min_infection_time(n, connections, start=0):
    # Build adjacency list
    graph = defaultdict(list)
    for source, target, time in connections:
        graph[source].append((target, time))
    
    # Initialize distances
    dist = [float('inf')] * n
    dist[start] = 0
    
    # Priority queue: (time, node)
    pq = [(0, start)]
    
    while pq:
        current_time, node = heapq.heappop(pq)
        
        # Skip if we've found a better path
        if current_time > dist[node]:
            continue
        
        # Update neighbors
        for neighbor, infection_time in graph[node]:
            new_time = current_time + infection_time
            if new_time < dist[neighbor]:
                dist[neighbor] = new_time
                heapq.heappush(pq, (new_time, neighbor))
    
    # Check if all computers are infected
    max_time = max(dist)
    return max_time if max_time != float('inf') else -1

# Example usage
n = 4
connections = [
    [0, 1, 1],
    [0, 2, 2],
    [1, 3, 3],
    [2, 3, 1]
]

result = min_infection_time(n, connections)
print(f"Minimum infection time: {result}")
```

## 🔍 Example Walkthrough

**Given:** 4 computers (0, 1, 2, 3), starting from computer 0

**Connections:**
- 0 → 1 (time: 1)
- 0 → 2 (time: 2)
- 1 → 3 (time: 3)
- 2 → 3 (time: 1)

**Step-by-step execution:**

| Step | Queue          | Current | Distances [0,1,2,3] | Action                         |
|------|----------------|---------|---------------------|--------------------------------|
| Init | [(0,0)]        | -       | [0, ∞, ∞, ∞]        | Start at node 0                |
| 1    | [(1,1), (2,2)] | 0       | [0, 1, 2, ∞]        | Infect nodes 1 and 2           |
| 2    | [(2,2), (4,3)] | 1       | [0, 1, 2, 4]        | From node 1, infect node 3     |
| 3    | [(3,3)]        | 2       | [0, 1, 2, **3**]    | From node 2, better path to 3! |
| 4    | []             | 3       | [0, 1, 2, 3]        | Done                           |

**Result:** Maximum time = **3** (all computers infected)

**Why this works:** Computer 0 infects 2 (time 2), then 2 infects 3 (time 1), total = 3. This is faster than 0→1→3 (total = 4).
"""



import heapq


def network_delay_time(times, N, K):
    # 构建图的邻接表表示
    graph = {i: [] for i in range(1, N + 1)}
    for u, v, w in times:
        graph[u].append((v, w))

    # 初始化距离数组，所有的距离初始化为无穷大
    # 将起点的距离初始化为0
    dist = {node: float('inf') for node in range(1, N + 1)}
    dist[K] = 0

    # 使用堆（优先队列）来得到当前最短的感染时间
    heap = [(0, K)]
    while heap:
        time, node = heapq.heappop(heap)

        # 如果当前的时间比已知的感染时间大，那么就不用继续处理
        if time > dist[node]:
            continue

        for v, w in graph[node]:
            # 如果通过当前节点感染相邻节点的时间更短，则更新时间
            if time + w < dist[v]:
                dist[v] = time + w
                heapq.heappush(heap, (dist[v], v))

    # 最后检查是否所有电脑都被感染，如果是，返回最大的感染时间
    max_dist = max(dist.values())
    return max_dist if max_dist < float('inf') else -1


# 读取输入
N = int(input())
connections = int(input())
times = []
for _ in range(connections):
    times.append(list(map(int, input().split())))
K = int(input())

# 计算输出
print(network_delay_time(times, N, K))
