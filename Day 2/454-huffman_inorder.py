"""
# Huffman Tree Generation Problem - Translation

## Problem Description

Given an unsorted array of numbers with length n, where each number represents the weight of a binary tree's leaf node, and all values are greater than or equal to 1. Complete a function that generates a Huffman tree based on the input array and outputs the tree using **in-order traversal**.

To ensure consistent in-order traversal output, the following constraints are added:
- In the binary tree nodes, the **left node's weight is less than the right node's weight**
- The **root node's weight equals the sum of left and right node weights**
- When left and right nodes have equal weights, the **left subtree's height should be less than or equal to the right subtree's height**

**Note:** All test cases are guaranteed to be valid and can generate a Huffman tree.

## Background

A Huffman tree (also called optimal binary tree) is a binary tree with the shortest weighted path length. The weighted path length of a tree is the sum of all leaf nodes' weights multiplied by their path length to the root node (if the root is at layer 0, the path length equals the leaf node's layer number).

## Input/Output

**Input:** An array of leaf node weights
- Example: 5 15 40 30 10

**Output:** The in-order traversal of the Huffman tree, with values separated by spaces

## Example

For leaf nodes: 5, 15, 40, 30, 10

The optimal binary tree has a minimum weighted path length of:
- 40  x 1 + 30  x 2 + 15  x 3 + 5  x 4 + 10  x 4 = **205**

The output should be the in-order traversal sequence of this Huffman tree.

### thought processes


# Huffman Tree Implementation Steps

1. **Create a Node Structure**
   - Contains `weight` (the node's weight), `left` (pointer to left child), and `right` (pointer to right child)

2. **Create a Comparison Function**
   - Implement a `Compare` struct for priority queue comparisons
   - First compare node weights
   - If weights are equal, compare subtree heights
   - Use a recursive `getHeight` function to calculate subtree heights

3. **Implement Height Calculation**
   - Create a recursive `getHeight` function
   - Return 0 if the node is empty
   - Otherwise, return 1 plus the maximum of left and right subtree heights

4. **Implement In-Order Traversal**
   - Create an `inorderTraversal` function for binary tree traversal
   - Traverse in order: left subtree → current node → right subtree
   - Store results in a vector

5. **Build the Huffman Tree**
   - Create a `buildHuffmanTree` function that receives leaf node weights as input
   - Initialize a priority queue to select nodes with the smallest weight
   - Traverse the leaf node weight array, create leaf nodes, and add them to the priority queue

6. **Construct Tree Iteratively**
   - Use a while loop until only one node remains in the priority queue
   - In each iteration:
     - Pop the two nodes with smallest weights (left and right children)
     - Create a new parent node
     - Set parent weight as the sum of left and right child weights
     - Add the parent node back to the priority queue

7. **Return Root Node**
   - The final remaining node in the priority queue is the root of the Huffman tree

8. **Main Function - Input**
   - Read the number of leaf nodes `n`
   - Create an array of size `n` and read leaf node weights

9. **Build and Traverse**
   - Call `buildHuffmanTree` to construct the tree
   - Assign the returned root node to a variable

10. **Output Results**
    - Create an empty vector for in-order traversal results
    - Call `inorderTraversal` function and store results in the vector
    - Output the traversal results with spaces between elements


    

    Let's walk through an example with the leaf node weights: **5, 15, 40, 30, 10**

### Step 1: Initialize Priority Queue
Create leaf nodes for each weight and add them to the priority queue:
- Nodes: 5, 15, 40, 30, 10

### Step 2: Build Huffman Tree
While there is more than one node in the priority queue:

#### First Iteration:
- Pop 5 and 10 (smallest weights)
- Create a new node with weight = 5 + 10 = 15
- Add this new node to the priority queue

Priority queue now contains: 15, 15, 30, 40

#### Second Iteration:
- Pop 15 (from original leaf nodes) and 15 (newly created node)
- Create a new node with weight = 15 + 15 = 30
- Add this new node to the priority queue

Priority queue now contains: 30, 30, 40

#### Third Iteration:
- Pop 30 (from original leaf nodes) and 30 (newly created node)
- Create a new node with weight = 30 + 30 = 60
- Add this new node to the priority queue

Priority queue now contains: 40, 60

#### Fourth Iteration:
- Pop 40 and 60
- Create a new node with weight = 40 + 60 = 100
- Add this new node to the priority queue

Priority queue now contains: 100

### Step 3: In-Order Traversal
The final Huffman tree has the following in-order traversal:
- Traverse left subtree → current node → right subtree
- Result: **10, 5, 15, 30, 40**

### Final Output

10 5 15 30 40

"""



import heapq

# 定义树的节点类
class TreeNode:
    def __init__(self, value, left=None, right=None): # pyright: ignore[reportMissingParameterType]
        # 节点的初始化方法，包含值、左子节点和右子节点
        self.value = value
        self.left = left # pyright: ignore[reportUnknownMemberType]
        self.right = right # pyright: ignore[reportUnknownMemberType]

    # 为了让节点可以在 heapq（优先队列）中比较，我们定义比较方法
    def __lt__(self, other):
        return self.value < other.value

# 构建哈夫曼树的函数
def build_huffman_tree(nodes):
    # 使用堆初始化优先队列
    heapq.heapify(nodes)

    # 当队列中的节点数大于1时，进行合并
    while len(nodes) > 1:
        # 取出两个最小的节点
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)

        # 创建新的内部节点，左节点权值小于右节点权值
        if left.value == right.value:
            # 当两个节点权值相等时，如果两个节点都没有子节点或者左子树高度不大于右子树高度
            # 则左子节点在左，否则左子节点在右
            if (not left.left and not right.left) or (height(left) <= height(right)):
                internal_node = TreeNode(left.value + right.value, left, right)
            else:
                internal_node = TreeNode(left.value + right.value, right, left)
        elif left.value < right.value:
            internal_node = TreeNode(left.value + right.value, left, right)
        else:
            internal_node = TreeNode(left.value + right.value, right, left)

        # 把新的内部节点放入优先队列
        heapq.heappush(nodes, internal_node)

    # 返回队列中的最后一个节点，即哈夫曼树的根节点
    return nodes[0]

# 计算树的高度
def height(node):
    if not node or (not node.left and not node.right):
        return 0
    return 1 + max(height(node.left), height(node.right))

# 中序遍历函数
def inorder_traversal(node, result):
    if node:
        inorder_traversal(node.left, result)
        result.append(node.value)
        inorder_traversal(node.right, result)

# 主函数，接受数字数组，构建哈夫曼树，并返回中序遍历结果
def huffman_inorder(values):
    # 将每个值转换为一个树节点
    nodes = [TreeNode(value) for value in values]

    # 构建哈夫曼树
    root = build_huffman_tree(nodes)

    # 进行中序遍历并收集结果
    result = []
    inorder_traversal(root, result)
    return result

# 接收动态输入
n = int(input("叶子节点的长度: "))  # 读取数组长度
values_input = input("叶子节点: ")  # 读取数组元素
values = list(map(int, values_input.split()))  # 将输入的字符串转换为整数列表

# 检查输入的数字个数是否与声明的长度一致
if len(values) != n:
    print("错误")
else:
    # 构建哈夫曼树并进行中序遍历
    inorder_result = huffman_inorder(values) # pyright: ignore[reportUnknownVariableType]
    print(" ".join(map(str, inorder_result))) # pyright: ignore[reportUnknownArgumentType]
