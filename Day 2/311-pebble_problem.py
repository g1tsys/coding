"""
# MELON's Problem - Translation and Solution Approach

## Problem Description

MELON has a pile of beautiful pebbles (quantity n, each with different weights) and wants to give them to S and W. MELON hopes to give both people pebbles with equal total weight. Design a program to help MELON determine if the pebbles can be evenly distributed.

## Input/Output

**Input:**
- Line 1: Number of pebbles n, where 0 < n < 31
- Line 2: Space-separated weights of each pebble: m[0] m[1] ... m[n-1], where 0 < m[k] < 1001

**Output:**
- If equal distribution is possible: output the minimum number of pebbles to remove to make two equal-weight piles
- If not possible: output -1

## Solution Approach (Python)

This is a **subset sum problem** with a twist. The key insights:

1. **Total weight must be even** - if odd, equal split is impossible
2. **Find subsets that sum to half the total** - use dynamic programming
3. **Minimize stones removed** - try removing 0, 1, 2... stones until a valid split exists

```python
def solve(n, weights):
    total = sum(weights)
    
    # Try removing 0, 1, 2... stones
    for remove_count in range(n):
        # Try all combinations of removing 'remove_count' stones
        from itertools import combinations
        
        for removed in combinations(range(n), remove_count):
            remaining = [weights[i] for i in range(n) if i not in removed]
            remaining_sum = sum(remaining)
            
            # Check if remaining can be split equally
            if remaining_sum % 2 == 0:
                target = remaining_sum // 2
                if can_partition(remaining, target):
                    return remove_count
    
    return -1

def can_partition(arr, target):
    # DP to check if subset sum equals target
    dp = [False] * (target + 1)
    dp[0] = True
    
    for num in arr:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]
    
    return dp[target]
```

## Example Walkthrough

**Input:** `n=4, weights=[1, 2, 3, 6]`

1. Total = 12 (even ✓)
2. Try removing 0 stones: Can we split [1,2,3,6] into two groups summing to 6? 
   - Yes! {6} and {1,2,3} both sum to 6
3. **Output: 0** (no stones need to be removed)

**Input:** `n=3, weights=[1, 2, 4]`

1. Total = 7 (odd ✗)
2. Try removing 1 stone: Remove 1 → [2,4], sum=6, target=3 ✓ (can make {2} and {4}? No, but we need equal)
3. Continue checking until finding minimum removals needed

The algorithm systematically tries removing the minimum number of stones until a valid equal partition is found.
"""


def dfs(p, count, temp_sum):
    global min_count

    if temp_sum == avg:
        if min_count > count:
            min_count = count
        return

    if temp_sum > avg or p == num:
        return

    # 包括当前雨花石
    dfs(p + 1, count + 1, temp_sum + nums[p])

    # 不包括当前雨花石
    dfs(p + 1, count, temp_sum)


if __name__ == '__main__':
    num = int(input())  # 输入雨花石个数
    nums = list(map(int, input().split()))  # 输入雨花石重量
    sum_val = sum(nums)  # 计算雨花石总重量
    if sum_val % 2 != 0:  # 如果总重量不是偶数，则无法平均分配
        print(-1)
    else:
        avg = sum_val // 2  # 计算平均重量
        min_count = float('inf')  # 初始化最小数量为无穷大
        dfs(0, 0, 0)  # 开始深度优先搜索
        if min_count != float('inf'):  # 如果找到了符合条件的组合
            print(min_count)
        else:
            print(-1)  # 如果没有找到符合条件的组合，输出-1
