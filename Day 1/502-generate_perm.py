"""
# The K-th Permutation Problem

## Problem Description

Given a parameter `n`, you have `n` integers from 1 to n: 1, 2, 3, ..., n. These n numbers have n! (factorial) possible permutations.

List all permutations in ascending order and number them sequentially.

**Example:** When n=3, all permutations are:
- "123" (1st)
- "132" (2nd)
- "213" (3rd)
- "231" (4th)
- "312" (5th)
- "321" (6th)

Given `n` and `k`, return the k-th permutation.

## Input/Output

**Input:**
- Two lines: first line contains `n`, second line contains `k`
- Range: n ∈ [1, 9], k ∈ [1, n!]

**Output:**
- The permutation at position k

## Solution Hints

### Approach 1: Backtracking (Brute Force)
1. Create a `used` array to track which digits have been used
2. Build permutations recursively, adding one digit at a time
3. Count permutations until reaching the k-th one
4. Return the result when count equals k

### Approach 2: Mathematical/Direct Calculation
1. Generate all permutations systematically
2. Sort them in lexicographic order
3. Return the k-th permutation (index k-1)

### Approach 3: Factorial Number System (Optimal)
1. Use factorial-based indexing to directly compute the k-th permutation
2. At each position, determine which digit should be placed based on (k-1) divided by (n-1)!
3. Remove used digits and continue

## Example Walkthrough

**Input:**
```
n = 3
k = 3
```

**Step-by-step:**

All permutations of [1, 2, 3] in order:
1. "123" ← 1st
2. "132" ← 2nd
3. "213" ← 3rd ✓ (This is our answer)
4. "231" ← 4th
5. "312" ← 5th
6. "321" ← 6th

**Output:** `213`

---

**Another Example:**

**Input:**
```
n = 4
k = 9
```

For n=4, we have 4! = 24 permutations. The 9th permutation would be found by:
- Permutations starting with 1: positions 1-6 (3! = 6 permutations)
- Permutations starting with 2: positions 7-12 (3! = 6 permutations)
  - Position 9 is the 3rd permutation starting with 2
  - That would be "2143"

**Output:** `2143`
"""




def generate_permutations(current, nums, result):
    if len(current) == len(nums):
        result.append(current)
    else:
        for num in nums:
            if num not in current:
                generate_permutations(current + [num], nums, result)

def get_permutation(n, k):
    nums = list(range(1, n + 1))
    permutations = []
    generate_permutations([], nums, permutations)
    permutations.sort()
    return ''.join(map(str, permutations[k - 1]))

# 读取输入
n = int(input())
k = int(input())

# 获取第k个排列
kth_permutation = get_permutation(n, k)

# 输出结果
print(kth_permutation)
