"""
# Candy Distribution Problem

## Problem Description

Xiao Ming randomly grabs a handful of candies from a candy box. Each time, Xiao Ming takes out half of the candies to distribute to classmates.
When candies cannot be evenly distributed, Xiao Ming can choose to take one candy from the box (assuming the box has enough candies) or put one candy back.
What is the minimum number of operations (taking out, putting back, and distributing all count as one operation) needed for Xiao Ming to distribute the candies until only one remains?
## Input/Output

**Input:** Number of candies grabbed (<1,000,000,000): 15

**Output:** Minimum operations to reach one candy: 5

## Python Approach & Thought Process

1. **Base Case:** If the current number of candies `m` is 1, we're done. Return the current count.
2. **Even Number:** If `m` is even, we can directly divide by 2. Recursively call with `m // 2` and increment count by 1.
3. **Odd Number:** If `m` is odd, we have two choices:
   - Add 1 candy (making it even), then divide: `dfs(m + 1, count + 1)`
   - Remove 1 candy (making it even), then divide: `dfs(m - 1, count + 1)`
   - Take the minimum of both paths

4. **Optimization:** Use memoization to avoid recalculating the same states.

## Python Code

```python
def dfs(m, count, memo):
    # Base case: only 1 candy left
    if m == 1:
        return count
    
    # Check if already calculated
    if m in memo:
        return memo[m] + count
    
    # If even, divide by 2
    if m % 2 == 0:
        result = dfs(m // 2, count + 1, memo)
    else:
        # If odd, try both adding and subtracting 1
        result = min(
            dfs(m + 1, count + 1, memo),
            dfs(m - 1, count + 1, memo)
        )
    
    # Store in memo (relative to count 0)
    memo[m] = result - count
    return result

# Main
n = int(input())
memo = {}
result = dfs(n, 0, memo)
print(result)
```

## Example Walkthrough (n = 15)

Let's trace through the solution for **15 candies**:

```text
Step 1: Start with 15 (odd)
  → Option A: 15 + 1 = 16
  → Option B: 15 - 1 = 14
  → Choose minimum path

Step 2a: Try 16 (even) - count = 1
  → 16 ÷ 2 = 8

Step 3a: 8 (even) - count = 2
  → 8 ÷ 2 = 4

Step 4a: 4 (even) - count = 3
  → 4 ÷ 2 = 2

Step 5a: 2 (even) - count = 4
  → 2 ÷ 2 = 1 ✓

Path A total: 5 operations

Step 2b: Try 14 (even) - count = 1
  → 14 ÷ 2 = 7

Step 3b: 7 (odd) - count = 2
  → Try 8 or 6, choose minimum...

Path B total: 6 operations

Minimum: 5 operations (Path A)
```

**Operations sequence:** 15 → 16 → 8 → 4 → 2 → 1

**Answer: 5 operations**
"""




def main():
    n = int(input())  # 获取输入的糖果数量n
    res = dfs(n, 0)  # 调用dfs函数计算最少需要的次数
    print(res)  # 输出结果

def dfs(m, count):
    if m == 1:  # 当糖果数量m为1时，递归结束，返回count
        return count
    else:
        if m % 2 == 0:  # 当糖果数量m为偶数时，递归调用dfs函数，糖果数量除以2，count加1
            return dfs(m // 2, count + 1)
        else:  # 当糖果数量m为奇数时，递归调用dfs函数，分别将糖果数量加1和减1，count加1，并取最小值
            return min(dfs(m + 1, count + 1), dfs(m - 1, count + 1))

if __name__ == "__main__":
    main()  # 调用main函数执行程序


