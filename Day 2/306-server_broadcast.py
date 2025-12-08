'''
# Python Coding Problem - Network Broadcast Algorithm

## Problem Translation

You need to implement an algorithm that calculates the **minimum number of broadcasts** required to reach all servers in a network.

### Algorithm Steps:

1. **Initialize**: Create a connectivity matrix `connectivity_matrix` from input, where `matrix[i][j] == 1` indicates that server i and server j are directly connected.

2. **Create** a `visited` array to track which servers have already been visited. Initially set all values to `False`.

3. **Initialize** the broadcast count `number_of_broadcasts` to 0.

4. **Traverse** all servers. If a server has not been visited yet, perform a Breadth-First Search (BFS) starting from it.

5. **During BFS**: Add the starting server to the queue and mark it as visited. Then for each server in the queue, traverse all servers that may be directly connected to it. If a server has not been visited, add it to the queue and mark it as visited.

6. **When the BFS completes**, a complete connected component is found. At this point, increment the broadcast count by one.

7. **Repeat** steps 4-6 until all servers have been visited.

8. **Output** the final broadcast count, which is the minimum number of broadcasts required.

---

## Python Implementation with Example Walkthrough


from collections import deque

def min_broadcasts(connectivity_matrix):
    """
    Calculate minimum number of broadcasts needed to reach all servers
    """
    n = len(connectivity_matrix)
    visited = [False] * n
    number_of_broadcasts = 0
    
    def bfs(start):
        """Perform BFS from starting server"""
        queue = deque([start])
        visited[start] = True
        
        while queue:
            current = queue.popleft()
            # Check all possible connections
            for neighbor in range(n):
                if connectivity_matrix[current][neighbor] == 1 and not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
    
    # Traverse all servers
    for server in range(n):
        if not visited[server]:
            bfs(server)
            number_of_broadcasts += 1
    
    return number_of_broadcasts

# Example Walkthrough
connectivity_matrix = [
    [1, 1, 0, 0, 0],  # Server 0 connects to 0, 1
    [1, 1, 1, 0, 0],  # Server 1 connects to 0, 1, 2
    [0, 1, 1, 0, 0],  # Server 2 connects to 1, 2
    [0, 0, 0, 1, 1],  # Server 3 connects to 3, 4
    [0, 0, 0, 1, 1]   # Server 4 connects to 3, 4

]

result = min_broadcasts(connectivity_matrix)
print(f"Minimum broadcasts needed: {result}")
```

### Step-by-Step Execution:


Initial State:
- Servers: [0, 1, 2, 3, 4]
- Visited: [False, False, False, False, False]
- Broadcasts: 0

Step 1: Start at Server 0 (not visited)
- BFS from 0: visits 0 → 1 → 2
- Visited: [True, True, True, False, False]
- Broadcasts: 1 (First connected component found)

Step 2: Server 1 (already visited, skip)

Step 3: Server 2 (already visited, skip)

Step 4: Start at Server 3 (not visited)
- BFS from 3: visits 3 → 4
- Visited: [True, True, True, True, True]
- Broadcasts: 2 (Second connected component found)

Step 5: Server 4 (already visited, skip)

Final Result: 2 broadcasts needed
```

### Explanation:
- **Connected Component 1**: Servers {0, 1, 2} are interconnected → needs 1 broadcast
- **Connected Component 2**: Servers {3, 4} are interconnected → needs 1 broadcast
- **Total**: 2 broadcasts to reach all 5 servers

This algorithm finds the number of **disconnected subnetworks** in the server network, where each subnetwork requires one broadcast to reach all its servers.
'''





from collections import deque


def main():
    # 读取第一行输入并按空格分割，然后转换为整数列表
    first_line = input().strip().split()
    n = len(first_line)  # 确定服务器数量n
    first_line = list(map(int, first_line))  # 转换数据类型为整数

    # 初始化连接矩阵，首先添加第一行
    connectivity_matrix = [first_line]

    # 读取剩余的n-1行输入来完成连接矩阵的构建
    for _ in range(n - 1):
        row = list(map(int, input().strip().split()))
        connectivity_matrix.append(row)

    # 创建一个访问状态数组，用于标记每个服务器是否已经被访问过
    visited = [False] * n
    # 初始化广播所需的服务器数量
    number_of_broadcasts = 0

    # 遍历每个服务器，检查其连接状态
    for i in range(n):
        if not visited[i]:  # 如果服务器i未被访问过
            # 使用队列进行广度优先搜索（BFS）
            queue = deque([i])
            visited[i] = True  # 标记服务器i为已访问

            while queue:
                current = queue.popleft()  # 取出当前服务器
                # 遍历所有可能的连接服务器
                for j in range(n):
                    # 如果服务器j与服务器current直接连接且未被访问过
                    if connectivity_matrix[current][j] == 1 and not visited[j]:
                        queue.append(j)  # 将服务器j加入队列
                        visited[j] = True  # 标记服务器j为已访问

            # 完成一个连通分量的搜索后，需要增加一个广播源
            number_of_broadcasts += 1

    # 输出所需的最少广播源数量
    print(number_of_broadcasts)


if __name__ == "__main__":
    main()
