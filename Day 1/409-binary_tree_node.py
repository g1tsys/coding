"""
# Translation and Explanation

## Problem Statement

**Title:** Passing Whispers

You are given a binary tree where each node has a person standing on it. The number on each node represents the **time cost** to pass a whisper from the parent node to that node.

Initially, the person at the root node has a whisper to pass to everyone else. Find the **total time** needed for all nodes in the binary tree to receive the whisper.

**Input:** A binary tree representation  
**Output:** The time required for all nodes to receive the whisper

---

## Python Approach - Thought Process

### **Approach 1:**

1. Define a function `speak(nds, index, current_sum)` where:
   - `nds` = list of binary tree nodes
   - `index` = current node index
   - `current_sum` = accumulated sum along current path

2. **Base case:** If index is out of range or current node is empty (value = -1), return the current accumulated sum

3. **Recursive case:** 
   - Add current node's value to `current_sum`
   - Recursively process left child at index `2*index + 1`
   - Recursively process right child at index `2*index + 2`
   - Return the **maximum** of left and right subtree path sums

4. The answer is the maximum path sum from root to any leaf

### **Approach 2:**

1. Define a function `speak(b, a, index, nds)` where:
   - `b` = list storing all complete paths
   - `a` = current path being built
   - `index` = current node index
   - `nds` = binary tree nodes

2. **Base case:** If out of range or node is empty, add current path to `b`

3. **Recursive case:**
   - Append current node value to path `a`
   - Recursively explore left child with a copy of `a`
   - Recursively explore right child with a copy of `a`

4. Calculate sum of each complete path and return the maximum

---

## Example Walkthrough

**Input:** `[0, 2, 3, -1, -1, 4, 5]`

This represents a binary tree (array format):
```
        0
       / \
      2   3
         / \
        4   5
```

**Step-by-step (Approach 1):**

1. Start at root (index 0, value 0): `current_sum = 0`
2. Left child (index 1, value 2): `current_sum = 0 + 2 = 2`
   - Both children are -1, return 2
3. Right child (index 2, value 3): `current_sum = 0 + 3 = 3`
   - Left child (index 5, value 4): `current_sum = 3 + 4 = 7`
   - Right child (index 6, value 5): `current_sum = 3 + 5 = 8`
   - Return max(7, 8) = 8

**Answer:** **8** (the longest path is root → 3 → 5)

The whisper takes 8 time units to reach all nodes because the furthest node requires going through edges with costs 0→3 (3 units) + 3→5 (5 units) = 8 units total.

# python walkthrough translation on web page
# Code Thought Process Reference:
1. Define a function named `speak` with three parameters: `nds` represents the list of binary tree nodes, `index` represents the index of the current node, `current_sum` represents the accumulated sum of the current path.
2. First check if the current node index is out of range or if the current node is an empty node (value is -1). If so, return the accumulated sum of the current path.
3. If the current node is not empty, add the value of the current node to `current_sum`.
4. Recursively process the left subtree of the current node, passing parameters `nds`, `index * 2 + 1`, and `current_sum`, updating the left subtree path sum as `left_sum`.
5. Recursively process the right subtree of the current node, passing parameters `nds`, `index * 2 + 2`, and `current_sum`, updating the right subtree path sum as `right_sum`.
6. Return the maximum value of the left and right subtree path sums.
7. In the `main` function, first read the user input binary tree node list and convert it to an integer list.
8. Call the `speak` function to calculate the maximum path sum and print out the result.
"""

def speak(nds, index=0, current_sum=0):
    # 如果节点索引超出范围或节点值为-1（表示空节点），则返回当前路径的累积和
    if index >= len(nds) or nds[index] == -1:
        return current_sum
    # 累加当前节点的值
    current_sum += nds[index]
    # 递归处理左子树，并更新路径和
    left_sum = speak(nds, index * 2 + 1, current_sum)
    # 递归处理右子树，并更新路径和
    right_sum = speak(nds, index * 2 + 2, current_sum)
    # 返回左右子树路径和的最大值
    return max(left_sum, right_sum)

def main():
    st = input()  # 从用户那里读取输入
    # 将输入字符串分割并转换成整数列表
    nodes = list(map(int, st.split()))
    # 计算最大路径和
    max_value = speak(nodes)
    print(max_value)  # 打印最大路径和

if __name__ == "__main__":
    main()
