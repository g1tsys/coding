"""
# Hotel Booking Problem - Translation and Walkthrough

## Problem Description

Xiao Ming is planning a vacation and found various hotels with different prices (array A of length n). His target budget is x yuan. Help him filter out k hotels closest to x yuan (where n≥k>0) and print the hotel prices from low to high.

## Input/Output Format

**Input:**
- First line: n, k, x (number of hotels, number to select, target price)
- Second line: A[0] A[1] A[2]...A[n-1] (hotel prices)

**Output:**
- Print selected hotel prices from low to high

## Python Solution Approach

### Thought Process:

1. **Read Input**: Parse n (total hotels), k (hotels to select), x (target price), and the array A of hotel prices
2. **Calculate Distances**: For each hotel price, calculate its absolute difference from the target price x
3. **Sort by Proximity**: Sort hotels by their distance to x (closest first). If distances are equal, prefer the lower price
4. **Select Top k**: Take the k hotels with smallest distances to x
5. **Sort Result**: Sort the selected k hotels by price (low to high) for output
6. **Print**: Output the final sorted prices

## Example Walkthrough

Let's say we have:
- **Input**: `n=5, k=3, x=100`
- **Hotel prices**: `[80, 120, 90, 150, 95]`

**Step-by-step:**


1. Calculate distances from x=100:
   - 80: |80-100| = 20
   - 120: |120-100| = 20
   - 90: |90-100| = 10
   - 150: |150-100| = 50
   - 95: |95-100| = 5

2. Sort by distance (then by price if tied):
   - 95 (distance: 5)
   - 90 (distance: 10)
   - 80 (distance: 20) ← lower price
   - 120 (distance: 20)
   - 150 (distance: 50)

3. Select top k=3:
   - [95, 90, 80]

4. Sort selected prices low to high:
   - [80, 90, 95]

5. Output: 80 90 95


## Python Code

python
# Read input
n, k, x = map(int, input().split())
prices = list(map(int, input().split()))

# Sort prices by distance to x, then by price itself
sorted_prices = sorted(prices, key=lambda p: (abs(p - x), p))

# Select top k closest hotels
selected = sorted_prices[:k]

# Sort selected hotels by price (low to high)
selected.sort()

# Print result
print(' '.join(map(str, selected)))


**Key Points:**
- The `lambda p: (abs(p - x), p)` sorts by distance first, then by price if distances are equal
- This ensures we get the k closest hotels, preferring cheaper ones when equidistant
- Final sort ensures output is in ascending price order
"""



def filter_hotels(n, k, x, prices):
    # 对酒店价格数组进行排序
    prices.sort()

    # 初始化结果数组
    res = []

    # 寻找差值最小的k个酒店价格
    for _ in range(k):
        min_index = 0  # 记录最小差值的索引
        min_diff = abs(prices[0] - x)  # 初始化最小差值为第一个价格与x的差值

        for j in range(1, n):
            diff = abs(prices[j] - x)  # 计算当前价格与x的差值

            # 如果当前差值更小，则更新最小差值和索引
            if diff < min_diff:
                min_index = j
                min_diff = diff

        res.append(prices[min_index])  # 将差值最小的价格加入结果数组
        prices.pop(min_index)  # 将已选择的酒店价格从数组中移除
        n -= 1  # 数组长度减一

    # 按从低到高顺序打印筛选出的酒店价格
    for price in sorted(res):
        print(price, end=" ")

# 读取输入
n, k, x = map(int, input().split())
prices = list(map(int, input().split()))

# 调用函数并打印结果
filter_hotels(n, k, x, prices)
