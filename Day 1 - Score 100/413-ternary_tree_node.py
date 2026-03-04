"""
The task is to **compute the height of a ternary search tree** based on a specific insertion rule. Here's the **translation** of the problem and the **Python solution chain of thoughts**, followed by a **walkthrough example** and an **annotated Python solution**.

---

### 🔹 Problem Translation (from Chinese):

You are given a list of integers. Based on the following rules, insert each number into a ternary search tree:

1. If the number is **less than the current node's value minus 500**, insert it into the **left subtree**.
2. If the number is **greater than the current node's value plus 500**, insert it into the **right subtree**.
3. Otherwise, insert it into the **middle subtree**.

After inserting all the numbers, **compute the height of the tree**, where the height of the root node is 1.

---

### 🔹 Python Solution Chain of Thoughts

1. First define a `TreeNode` class to represent nodes of the tree. Each node has a `value` field for the node's numeric value, and three pointers `left`, `middle`, and `right` that point to the roots of the left subtree, middle subtree, and right subtree respectively.
2. Define a recursive function `insert_node` to insert a node into the ternary search tree. The function takes two parameters: the current node `root` and the value to insert `num`. If the current node is empty, this is a leaf position: create and return a new node. If `num` is less than the current node's value minus 500, insert into the left subtree; if `num` is greater than the current node's value plus 500, insert into the right subtree; otherwise insert into the middle subtree.
3. Define a recursive function `height` to compute the tree's height. The function takes one parameter: the current node `root`. If the current node is empty, we have reached the bottom of the tree and return height 0. Otherwise, recursively compute the heights of the left, middle, and right subtrees, and return the maximum of those subtree heights plus 1 (the height of the current node).
4. In the `main` function, first read the number of input values `N`, then create an integer array `nums` of size `N` to store the input numbers.
5. Next, use a loop to read each input number in turn, and call `insert_node` to insert it into the ternary search tree.
6. Finally, call the `height` function to compute the tree's height and print the result.

---

### 🔹 Example Walkthrough

**Input:**
```
5
100 600 1100 1600 2100
```

**Insertion Steps:**

1. Insert **100** → root node.
2. Insert **600**:
   - 600 > 100 + 500 → insert into **right subtree**.
3. Insert **1100**:
   - 1100 > 600 + 500 → insert into **right subtree** of 600.
4. Insert **1600**:
   - 1600 > 1100 + 500 → insert into **right subtree** of 1100.
5. Insert **2100**:
   - 2100 > 1600 + 500 → insert into **right subtree** of 1600.

**Tree structure:**
```
Root: 100
    Right: 600
        Right: 1100
            Right: 1600
                Right: 2100
```

**Height of the tree: 5**

---
"""
### 🔹 Annotated Python Solution

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.middle = None
        self.right = None

def insert_node(root, num):
    if root is None:
        return TreeNode(num)
    
    if num < root.value - 500:
        root.left = insert_node(root.left, num)
    elif num > root.value + 500:
        root.right = insert_node(root.right, num)
    else:
        root.middle = insert_node(root.middle, num)
    
    return root

def height(root):
    if root is None:
        return 0
    # Calculate height of left, middle, and right subtrees
    left_h = height(root.left)
    middle_h = height(root.middle)
    right_h = height(root.right)
    # Return the maximum of the three + 1 for current node
    return max(left_h, middle_h, right_h) + 1

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    
    root = None
    for num in nums:
        root = insert_node(root, num)
    
    print("Height of the tree:", height(root))

if __name__ == "__main__":
    main()


