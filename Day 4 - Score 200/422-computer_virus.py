"""
### Extracted Content from Python Section

**Question**
A local area network contains computers labeled from 0 to N-1. When a computer gets infected, it spreads the virus to adjacent computers over time. The time it takes for an infection to spread from one computer to an adjacent one is given.
You are given an array `times` where each element `path[i] = {i, j, t}` represents an edge from computer `i` to computer `j` with a weight `t` (the time required for the infection to travel between them).

**Goal:** Determine the minimum time required for the virus to infect **all** computers in the network starting from a single infected computer.
- If all computers get infected, return the maximum time taken to reach any computer (i.e., the time when the last computer gets infected).
- If it is impossible to infect all computers (some remain isolated), return `-1`.

**Input Format:**
- First line: `N` (number of computers).
- Second line: Number of network connections.
- Following lines (implied): Details of connections `i, j, t`.

**Output Format:**
- An integer representing the minimum time to infect all computers, or `-1`.

---

**Python Language Thought Process**
1.  **Graph Construction:**
    - Represent the network as a graph using an adjacency list.
    - For each computer `i`, create a list to store outgoing connections.
    - Each connection stores the target computer `j` and the time weight `w`.

2.  **Initialization:**
    - Create a `dist` array to track the infection time for each computer.
    - Initialize all distances to infinity (`float('inf')`), representing that they are initially uninfected.
    - Select a starting computer (implied to be any specific node, often node 0 or the first provided in context, but the logic applies to finding the "center" or checking from a specific start).
    - Set the distance of the starting computer to `0` (it is infected at time 0).

3.  **Priority Queue (Min-Heap):**
    - Use a min-heap (priority queue) to efficiently retrieve the computer with the shortest current infection time.
    - Push the starting computer and time `0` into the heap: `(0, start_node)`.

4.  **Dijkstra's Algorithm Loop:**
    - While the heap is not empty:
        - Pop the element with the smallest time: `(current_time, u)`.
        - **Check for redundancy:** If `current_time` is greater than the known shortest time `dist[u]`, skip this entry (a shorter path was already found).
        - **Explore Neighbors:** Iterate through all adjacent computers `v` of `u`.
        - **Relaxation:** Calculate the new time to infect `v` as `new_time = current_time + weight(u, v)`.
        - **Update:** If `new_time` is shorter than the current `dist[v]`:
            - Update `dist[v] = new_time`.
            - Push `(new_time, v)` into the heap.

5.  **Final Verification:**
    - After the heap is empty, check the `dist` array.
    - If any computer still has a distance of infinity, it means it was unreachable. Return `-1`.
    - If all computers are reachable, the answer is the **maximum value** in the `dist` array (the time when the last computer gets infected).


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
