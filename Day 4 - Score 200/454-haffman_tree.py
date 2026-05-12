"""
Based on the webpage content provided, here is the extracted question and the thought process specifically for the **Python** programming language section.

### **Question**

**Task:** Generate a Huffman Tree from an unordered array of integers (representing leaf node weights) and output the tree using **in-order traversal**.

**Constraints & Rules:**
1.  **Input:** An array of $n$ integers, where each value $\ge 1$.
2.  **Tree Construction Rules:**
    *   The left node's weight must be **less than** the right node's weight.
    *   If the left and right node weights are **equal**, the left subtree's height must be **less than or equal to** the right subtree's height.
    *   The root node's weight is the sum of its left and right children.
3.  **Output:** A space-separated string of the in-order traversal of the constructed Huffman Tree.
4.  **Definition:** A Huffman Tree (Optimal Binary Tree) is a binary tree where the weighted path length (sum of leaf weight $\times$ path length from root) is minimized.

**Example:**
*   **Input:** `5 15 40 30 10`
*   **Output:** The in-order traversal array of the resulting tree.
*   **Note:** The minimum weighted path length for this example is 205.

---

### **Python Thought Process & Logic**

The solution relies on using a **Min-Heap** (Priority Queue) to efficiently access the two smallest nodes at any step, which is the core greedy algorithm for building Huffman Trees.

**1. Data Structure Design:**
*   **`TreeNode` Class:** Represents a node in the tree.
    *   Attributes: `value` (weight), `left` (left child), `right` (right child).
    *   **Critical:** Implement the `__lt__` (less than) method. This allows Python's `heapq` module to compare `TreeNode` objects directly based on their `value`. If values are equal, the logic must also consider the **height** to satisfy the problem's specific tie-breaking rule (left height $\le$ right height).

**2. Building the Tree (`build_huffman_tree`):**
*   **Initialization:** Convert the input array of integers into a list of `TreeNode` objects and push them into a min-heap.
*   **Iterative Merging:**
    *   While the heap contains more than one node:
        1.  **Pop** the two nodes with the smallest weights (`node1`, `node2`).
        2.  **Determine Left/Right:**
            *   Compare weights. The smaller weight becomes the **left** child.
            *   If weights are equal, compare their **heights**. The node with the smaller (or equal) height becomes the **left** child.
        3.  **Create New Root:** Create a new internal node with `value = node1.value + node2.value`.
        4.  **Assign Children:** Set the new node's left and right children based on the logic above.
        5.  **Push Back:** Push the new internal node back into the min-heap.
*   **Result:** When the loop ends, the single remaining node in the heap is the **root** of the Huffman Tree.

**3. Calculating Height (`height` function):**
*   Since the tie-breaking rule depends on height, a helper function is needed to calculate the height of any given node recursively:
    *   Height of a leaf is 0 (or 1, depending on definition, but consistency is key).
    *   Height of a node = $1 + \max(\text{height(left)}, \text{height(right)})$.

**4. In-Order Traversal (`inorder_traversal`):**
*   Perform a standard recursive in-order traversal:
    1.  Traverse the **left** subtree.
    2.  Visit the **current** node (append value to result list).
    3.  Traverse the **right** subtree.

**5. Main Execution Flow (`huffman_inorder`):**
*   Receive the input list.
*   Call the builder to get the root.
*   Call the traversal function to get the list of values.
*   Print the list as a space-separated string.

**Key Python Libraries:**
*   `heapq`: For the efficient min-heap operations (`heappush`, `heappop`).

"""


import heapq

# 定义树的节点类
class TreeNode:
    def __init__(self, value, left=None, right=None):
        # 节点的初始化方法，包含值、左子节点和右子节点
        self.value = value
        self.left = left
        self.right = right

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
    inorder_result = huffman_inorder(values)
    print(" ".join(map(str, inorder_result)))
