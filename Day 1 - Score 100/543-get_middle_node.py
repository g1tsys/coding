"""
# Single Linked List Middle Node Problem
## Problem Description

Find the middle node value in a singly linked list. If there's an odd number of nodes, take the middle one. If even, take the one slightly to the right of center.

## Input/Output Format

**Input:**
- First line: Head node address and number of nodes n
- Following n lines: Each represents a node in format: `node_address node_value next_node_address` (-1 indicates null pointer)
- Note: The input guarantees no cycles, but may contain nodes not part of the main linked list

**Output:**
- The value of the middle node in the linked list

## Python Solution Approach

1. **Read input**: Get the head node address and total number of nodes
2. **Build node dictionary**: Create a HashMap where keys are node addresses and values are tuples containing (node_value, next_node_address)
3. **Traverse the linked list**: Starting from the head, follow the chain of nodes and store all values in order
4. **Calculate middle index**: For a list of length n, the middle index is `n // 2` (this automatically gives us the right-center node for even-length lists)
5. **Return the middle value**


# Read input
head, n = map(int, input().split())

# Build the nodes dictionary
nodes = {}
for _ in range(n):
    addr, value, next_addr = map(int, input().split())
    nodes[addr] = (value, next_addr)

# Get and print the middle node value
result = get_middle_node(head, nodes)
print(result)
```

## Example Walkthrough

**Example Input:**
```
00010 4
00000 3 00010
00010 5 10001
10001 2 -1
10002 8 -1
```

**Step-by-step execution:**

1. **Parse first line**: `head = 10, n = 4`

2. **Build nodes dictionary**:
   ```
   nodes = {
       0: (3, 10),
       10: (5, 10001),
       10001: (2, -1),
       10002: (8, -1)  # Not part of main chain
   }
   ```

3. **Traverse from head (10)**:
   - Current = 10 → value = 5, next = 10001 → `linked_list = [5]`
   - Current = 10001 → value = 2, next = -1 → `linked_list = [5, 2]`
   - Current = -1 → Stop

4. **Calculate middle**:
   - Length = 2
   - Middle index = 2 // 2 = 1
   - Result = `linked_list[1] = 2`

**Output:** `2`

**Note:** Node at address 0 and 10002 are not traversed because they're not part of the chain starting from head node 10.
"""


def get_middle_node(head, nodes):
    linked_list = []  # 存储所有节点的值

    curr = head  # 初始化当前节点为头节点
    while curr is not None:
        info = nodes[curr]
        linked_list.append(info[0])  # 将当前节点的值存入链表中
        curr = info[1]  # 更新当前节点为下一个节点的地址

    length = len(linked_list)  # 计算链表的长度
    mid_index = length // 2  # 计算中间节点的下标

    return linked_list[mid_index]  # 返回链表中间节点的值


head, n = input().split()
n = int(n)
nodes = {}

# 读取节点信息并存入字典中
for _ in range(n):
    line = input().split()
    addr = line[0]
    val = line[1]
    next_addr = line[2] if line[2] != '-1' else None
    nodes[addr] = (val, next_addr)

result = get_middle_node(head, nodes)
print(result)


