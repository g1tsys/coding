"""The text you provided contains the problem description and C++ and Java approaches, but the **Python** section is incomplete—it lists "思路" (thought process) and "代码" (code) headers but leaves the content empty.

Based on the problem description and the logic provided in the C++ and Java sections, here is the reconstructed **Python** thought process and the corresponding code implementation:

### 🐍 Python Language Thought Process

1.  **Input Parsing**:
    *   Read the number of edges `N`.
    *   If `N` is 0, the result is trivially no start/end nodes (or handle as specific edge case).
    *   Read the subsequent line containing `2N` integers. Parse them into pairs to form edges `(start, end)`.

2.  **Graph Construction & Degree Calculation**:
    *   Create a graph structure (e.g., an adjacency list using `defaultdict(list)`).
    *   Simultaneously, track the **in-degree** (number of incoming edges) and **out-degree** (number of outgoing edges) for every node using dictionaries.
    *   Store all unique nodes encountered in a set.

3.  **Cycle Detection (DFS)**:
    *   The problem explicitly states: "If the graph contains a ring, return [-1]".
    *   Implement a standard **Depth First Search (DFS)** with a recursion stack (or color marking: White=unvisited, Gray=visiting, Black=visited).
    *   If a "Gray" node is encountered during traversal, a cycle exists.
    *   Perform this check starting from every unvisited node to ensure the entire component is checked.

4.  **Identify Head and Tail Nodes**:
    *   **Head Node (Start)**: The node with an **in-degree of 0**.
        *   If there are multiple nodes with in-degree 0, or none, it implies a cycle or a disconnected structure that violates the single-source assumption. Return `[-1]`.
    *   **Tail Node (End)**: The node with an **out-degree of 0**.
        *   If there are multiple nodes with out-degree 0, keep all of them (as per "multiple tail nodes" allowance).
        *   If there are no nodes with out-degree 0, it implies a cycle (every node has an outgoing edge). Return `[-1]`.

5.  **Final Output**:
    *   If the head node is unique and no cycles are found:
        *   Sort the tail nodes in **descending order**.
        *   Output the head node followed by the sorted tail nodes.
    *   If any condition fails (multiple heads, cycle detected, no tails), output `-1`.

---

### 🐍 Python Code Implementation

```python
import sys
from collections import defaultdict

def solve():
    # Read N (number of edges)
    try:
        line1 = sys.stdin.readline().strip()
        if not line1:
            return
        n = int(line1)
        
        if n == 0:
            # No edges means no start or end nodes in a connected graph context
            # Based on problem logic, likely return -1 or handle as empty
            # Assuming standard OJ behavior: if no nodes defined, no path exists.
            # But strictly: In-degree 0 and Out-degree 0 condition fails.
            print(-1)
            return

        line2 = sys.stdin.readline().strip()
        if not line2:
            return
            
        values = list(map(int, line2.split()))
        if len(values) != 2 * n:
            return # Invalid input
            
    except ValueError:
        return

    # 1. Build Graph and Calculate Degrees
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)
    all_nodes = set()
    
    for i in range(n):
        u = values[2 * i]
        v = values[2 * i + 1]
        
        graph[u].append(v)
        all_nodes.add(u)
        all_nodes.add(v)
        
        out_degree[u] += 1
        in_degree[v] += 1

    # Ensure all nodes have entries in degree maps even if 0
    for node in all_nodes:
        if node not in in_degree:
            in_degree[node] = 0
        if node not in out_degree:
            out_degree[node] = 0

    # 2. Cycle Detection using DFS
    # Colors: 0 = White (unvisited), 1 = Gray (visiting), 2 = Black (visited)
    color = {node: 0 for node in all_nodes}
    has_cycle = False

    def dfs(node):
        nonlocal has_cycle
        color[node] = 1 # Mark as visiting
        
        for neighbor in graph[node]:
            if color[neighbor] == 1:
                # Found a back edge, cycle detected
                has_cycle = True
                return
            if color[neighbor] == 0:
                dfs(neighbor)
                if has_cycle:
                    return
        
        color[node] = 2 # Mark as visited

    for node in all_nodes:
        if color[node] == 0:
            dfs(node)
            if has_cycle:
                break

    if has_cycle:
        print("-1")
        return

    # 3. Find Head and Tail
    head_nodes = [node for node in all_nodes if in_degree[node] == 0]
    tail_nodes = [node for node in all_nodes if out_degree[node] == 0]

    # Logic Check:
    # "题目给的用例会是一个首节点，但可能存在多个尾节点"
    # "入度为0是首节点... 如果有多个起始节点或终止节点... 返回-1"
    # Note: The problem description says "If multiple start nodes... return -1".
    # But for tails, it says "output multiple tails in descending order".
    
    if len(head_nodes) != 1:
        print("-1")
        return
    
    if len(tail_nodes) == 0:
        print("-1")
        return

    # Sort tail nodes in descending order
    tail_nodes.sort(reverse=True)
    
    result = [head_nodes[0]] + tail_nodes
    print(*(result))

if __name__ == "__main__":
    solve()
```

### Key Logic Notes
- **Cycle Handling**: The DFS strictly checks for back-edges (Gray node encountered) to detect cycles. If found, it immediately prints `-1`.
- **Head Node Constraint**: The problem states "If there are multiple start nodes... return -1". The code enforces `len(head_nodes) == 1`.
- **Tail Node Constraint**: The problem allows multiple tail nodes but requires them sorted **descending**.
- **Edge Cases**: Handles `N=0` and disconnected components (though a valid path usually implies a single connected component in these specific OJ problems).

The text you provided contains the problem description and C++ and Java approaches, but the **Python** section is incomplete—it lists "思路" (thought process) and "代码" (code) headers but leaves the content empty.

Based on the problem description and the logic provided in the C++ and Java sections, here is the reconstructed **Python** thought process and the corresponding code implementation:

### 🐍 Python Language Thought Process

1.  **Input Parsing**:
    *   Read the number of edges `N`.
    *   If `N` is 0, the result is trivially no start/end nodes (or handle as specific edge case).
    *   Read the subsequent line containing `2N` integers. Parse them into pairs to form edges `(start, end)`.

2.  **Graph Construction & Degree Calculation**:
    *   Create a graph structure (e.g., an adjacency list using `defaultdict(list)`).
    *   Simultaneously, track the **in-degree** (number of incoming edges) and **out-degree** (number of outgoing edges) for every node using dictionaries.
    *   Store all unique nodes encountered in a set.

3.  **Cycle Detection (DFS)**:
    *   The problem explicitly states: "If the graph contains a ring, return [-1]".
    *   Implement a standard **Depth First Search (DFS)** with a recursion stack (or color marking: White=unvisited, Gray=visiting, Black=visited).
    *   If a "Gray" node is encountered during traversal, a cycle exists.
    *   Perform this check starting from every unvisited node to ensure the entire component is checked.

4.  **Identify Head and Tail Nodes**:
    *   **Head Node (Start)**: The node with an **in-degree of 0**.
        *   If there are multiple nodes with in-degree 0, or none, it implies a cycle or a disconnected structure that violates the single-source assumption. Return `[-1]`.
    *   **Tail Node (End)**: The node with an **out-degree of 0**.
        *   If there are multiple nodes with out-degree 0, keep all of them (as per "multiple tail nodes" allowance).
        *   If there are no nodes with out-degree 0, it implies a cycle (every node has an outgoing edge). Return `[-1]`.

5.  **Final Output**:
    *   If the head node is unique and no cycles are found:
        *   Sort the tail nodes in **descending order**.
        *   Output the head node followed by the sorted tail nodes.
    *   If any condition fails (multiple heads, cycle detected, no tails), output `-1`.

---

### 🐍 Python Code Implementation


"""
import sys
from collections import defaultdict

def solve():
    # Read N (number of edges)
    try:
        line1 = sys.stdin.readline().strip()
        if not line1:
            return
        n = int(line1)
        
        if n == 0:
            # No edges means no start or end nodes in a connected graph context
            # Based on problem logic, likely return -1 or handle as empty
            # Assuming standard OJ behavior: if no nodes defined, no path exists.
            # But strictly: In-degree 0 and Out-degree 0 condition fails.
            print(-1)
            return

        line2 = sys.stdin.readline().strip()
        if not line2:
            return
            
        values = list(map(int, line2.split()))
        if len(values) != 2 * n:
            return # Invalid input
            
    except ValueError:
        return

    # 1. Build Graph and Calculate Degrees
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)
    all_nodes = set()
    
    for i in range(n):
        u = values[2 * i]
        v = values[2 * i + 1]
        
        graph[u].append(v)
        all_nodes.add(u)
        all_nodes.add(v)
        
        out_degree[u] += 1
        in_degree[v] += 1

    # Ensure all nodes have entries in degree maps even if 0
    for node in all_nodes:
        if node not in in_degree:
            in_degree[node] = 0
        if node not in out_degree:
            out_degree[node] = 0

    # 2. Cycle Detection using DFS
    # Colors: 0 = White (unvisited), 1 = Gray (visiting), 2 = Black (visited)
    color = {node: 0 for node in all_nodes}
    has_cycle = False

    def dfs(node):
        nonlocal has_cycle
        color[node] = 1 # Mark as visiting
        
        for neighbor in graph[node]:
            if color[neighbor] == 1:
                # Found a back edge, cycle detected
                has_cycle = True
                return
            if color[neighbor] == 0:
                dfs(neighbor)
                if has_cycle:
                    return
        
        color[node] = 2 # Mark as visited

    for node in all_nodes:
        if color[node] == 0:
            dfs(node)
            if has_cycle:
                break

    if has_cycle:
        print("-1")
        return

    # 3. Find Head and Tail
    head_nodes = [node for node in all_nodes if in_degree[node] == 0]
    tail_nodes = [node for node in all_nodes if out_degree[node] == 0]

    # Logic Check:
    # "题目给的用例会是一个首节点，但可能存在多个尾节点"
    # "入度为0是首节点... 如果有多个起始节点或终止节点... 返回-1"
    # Note: The problem description says "If multiple start nodes... return -1".
    # But for tails, it says "output multiple tails in descending order".
    
    if len(head_nodes) != 1:
        print("-1")
        return
    
    if len(tail_nodes) == 0:
        print("-1")
        return

    # Sort tail nodes in descending order
    tail_nodes.sort(reverse=True)
    
    result = [head_nodes[0]] + tail_nodes
    print(*(result))

if __name__ == "__main__":
    solve()
