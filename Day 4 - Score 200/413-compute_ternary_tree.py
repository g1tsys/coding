"""
Based on the text provided, here is the extracted question and the thought process specifically for the Python solution:

### **Question**
**Title:** 【华为OD机试真题】413、计算三叉搜索树的高度

**Description:**
Define the rules for constructing a ternary search tree as follows:
Each node stores a number. When inserting a new number, start from the root node and search downwards until an appropriate empty node is found for insertion.

The search rules are:
1. If the number is **less than** the node's value **minus 500**, insert it into the **left** subtree.
2. If the number is **greater than** the node's value **plus 500**, insert it into the **right** subtree.
3. **Otherwise**, insert it into the **middle** subtree.

Given a series of numbers, insert them into the tree in order according to the rules above, construct the ternary search tree, and finally output the **height** of the tree.

**Input:**
- The first line contains an integer `N` (1 <= N <= 10000), representing the number of elements.
- The second line contains `N` space-separated integers, each in the range [1, 10000].

**Output:**
- Output the height of the tree (the height of the root node is 1).

---

### **Python Thought Process (思路)**

The solution approach involves two main components: defining the tree structure and implementing recursive functions for insertion and height calculation.

1.  **Node Definition**:
    -   Define a `TreeNode` class to represent each node in the tree.
    -   Each node needs to store a `value` and three references: `left`, `middle`, and `right` for the respective subtrees.

2.  **Insertion Logic (`insert_node`)**:
    -   Create a function to insert a number into the tree.
    -   **Base Case**: If the current node is `None`, create a new `TreeNode` with the given number and return it.
    -   **Recursive Step**: Compare the number to be inserted (`num`) with the current node's value (`root.value`):
        -   If `num < root.value - 500`: Recursively insert into the **left** subtree.
        -   If `num > root.value + 500`: Recursively insert into the **right** subtree.
        -   Otherwise (if the number is within the range `[root.value - 500, root.value + 500]`): Recursively insert into the **middle** subtree.
    -   Update the corresponding child pointer of the current node with the result of the recursive call.

3.  **Height Calculation (`height`)**:
    -   Create a function to calculate the height of the tree.
    -   **Base Case**: If the current node is `None`, return `0`.
    -   **Recursive Step**:
        -   Recursively calculate the height of the **left**, **middle**, and **right** subtrees.
        -   Find the **maximum** of these three heights.
        -   Return `max_height + 1` to account for the current node.

4.  **Main Execution**:
    -   Read the input values: the count `N` and the list of numbers.
    -   Initialize the `root` of the tree as `None`.
    -   Iterate through the list of numbers, calling `insert_node` for each to build the tree.
    -   Finally, call the `height` function on the `root` and print the result.
"""
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.middle = None
        self.right = None

def insert_node(root, num):
    """
    插入节点的递归函数
    """
    # 没有根节点，创建新节点
    if root is None:
        return TreeNode(num)
    # 如果插入的数小于当前节点数减去500，插入到左子树
    if num < root.value - 500:
        root.left = insert_node(root.left, num)
    # 如果插入的数大于当前节点数加上500，插入到右子树
    elif num > root.value + 500:
        root.right = insert_node(root.right, num)
    # 否则插入到中子树
    else:
        root.middle = insert_node(root.middle, num)
    return root

def height(root):
    """
    计算树的高度
    """
    # 如果节点为空，高度为0
    if root is None:
        return 0
    # 计算左子树、中子树和右子树的高度
    left_height = height(root.left)
    middle_height = height(root.middle)
    right_height = height(root.right)
    # 树的总高度为最高的子树高度加1（当前节点的高度）
    return max(left_height, middle_height, right_height) + 1

# 输入描述
N = int(input())  # 输入的数的个数
nums = list(map(int, input().split()))  # 输入的数

# 根据规则构造三叉搜索树
root = None
for num in nums:
    root = insert_node(root, num)

# 输出树的高度
print(height(root))


