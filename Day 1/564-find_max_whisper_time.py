# Binary Tree "Whisper Propagation" Problem

## Problem Translation
"""
You're given a binary tree where each node has a person standing on it. The number at each node represents the **time cost** to pass a whisper from the parent node to that node.

Initially, the person at the root node has a whisper to pass to everyone else. Find the **total time** needed for all nodes in the binary tree to receive the whisper.

**Input:** A binary tree representation  
**Output:** The time required for all nodes to receive the whisper

---

## Solution Approach (Based on Python Section)

### Method 1: Track Maximum Path Sum
The key insight is that the whisper propagates along all paths simultaneously. The bottleneck is the **longest path** from root to any leaf.

**Algorithm:**
1. Recursively traverse the tree from the root
2. Accumulate the time cost along each path
3. For each node, explore both left and right subtrees
4. Return the maximum cumulative time among all paths

### Method 2: Collect All Paths
1. Generate all root-to-leaf paths
2. Calculate the sum for each path
3. Return the maximum sum

"""

## Python Solution
def find_max_whisper_time(nodes, index=0, current_sum=0):
    """
    Calculate maximum time for whisper to reach all nodes
    
    Args:
        nodes: List representation of binary tree
        index: Current node index in array
        current_sum: Accumulated time to reach current node
    
    Returns:
        Maximum time needed for whisper propagation
    """
    # Base case: out of bounds or empty node
    if index >= len(nodes) or nodes[index] == -1:
        return current_sum
    
    # Add current node's time cost
    current_sum += nodes[index]
    
    # Recursively calculate for left and right subtrees
    left_time = find_max_whisper_time(nodes, 2 * index + 1, current_sum)
    right_time = find_max_whisper_time(nodes, 2 * index + 2, current_sum)
    
    # Return maximum time (longest path)
    return max(left_time, right_time)

# Example usage
nodes = list(map(int, input().split()))
print(find_max_whisper_time(nodes))



"""
## Example Walkthrough

**Input:** `0 1 2 3 4 -1 -1`

This represents a binary tree (array format):
```
        0
       / \
      1   2
     / \
    3   4


**Step-by-step execution:**

1. **Start at root (index 0, value=0):**
   - current_sum = 0
   - Explore left child (index 1)

2. **Node at index 1 (value=1):**
   - current_sum = 0 + 1 = 1
   - Explore left child (index 3)

3. **Node at index 3 (value=3):**
   - current_sum = 1 + 3 = 4
   - No valid children → return 4

4. **Back to index 1, explore right child (index 4, value=4):**
   - current_sum = 1 + 4 = 5
   - No valid children → return 5

5. **Back to root, explore right child (index 2, value=2):**
   - current_sum = 0 + 2 = 2
   - No valid children → return 2

6. **Compare all paths:**
   - Path to node 3: 0→1→3 = 4
   - Path to node 4: 0→1→4 = 5 ✓ (maximum)
   - Path to node 2: 0→2 = 2

**Output:** `5`

The whisper takes 5 time units to reach all nodes (limited by the longest path).
"""