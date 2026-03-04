"""
# Maximum Profit Problem - Translation and Walkthrough

## Problem Description

A merchant operates a shop with **number** types of goods. Due to warehouse limitations, the maximum quantity that can be held for each item is **item[index]**. The price of each item on each day is **item_price[item_index][day]**. The merchant can buy and sell goods to make a profit. Find the maximum profit the merchant can achieve over **days** days.

**Note:** The same item can be bought and sold repeatedly.

## Input Format

- **Line 1:** Number of goods (number), e.g., 3
- **Line 2:** Number of selling days (days), e.g., 3
- **Line 3:** Maximum holding quantity for each item (space-separated), e.g., 4 5 6
- **Next number lines:** Each line contains days values representing the price of that item on each day

## Output Format

Output the maximum profit the merchant can achieve during this period.

## Solution Approach (Greedy Algorithm)

The key insight is:
1. For each item, calculate the profit by buying low and selling high
2. If tomorrow's price > today's price, buy today and sell tomorrow
3. Multiply the profit by the maximum quantity you can hold for that item
4. Sum up profits from all items

## Example Walkthrough

### Input:
```
3          (3 types of goods)
3          (3 days)
4 5 6      (max quantities: item 0→4, item 1→5, item 2→6)
1 2 3      (item 0 prices: day 0→1, day 1→2, day 2→3)
4 3 2      (item 1 prices: day 0→4, day 1→3, day 2→2)
1 5 3      (item 2 prices: day 0→1, day 1→5, day 2→3)
```

### Step-by-Step Calculation:

**Item 0 (max quantity = 4):**
- Day 0→1: price increases from 1 to 2, profit = 2-1 = 1
- Day 1→2: price increases from 2 to 3, profit = 3-2 = 1
- Total profit per unit = 1 + 1 = 2
- Total profit = 2 x 4 = **8**

**Item 1 (max quantity = 5):**
- Day 0→1: price decreases from 4 to 3, no profit (0)
- Day 1→2: price decreases from 3 to 2, no profit (0)
- Total profit = 0 x 5 = **0**

**Item 2 (max quantity = 6):**
- Day 0→1: price increases from 1 to 5, profit = 5-1 = 4
- Day 1→2: price decreases from 5 to 3, no profit (0)
- Total profit per unit = 4
- Total profit = 4 x 6 = **24**

### Final Answer:
**Maximum Profit = 8 + 0 + 24 = 32**

The greedy strategy works because we can buy and sell on consecutive days, so we capture every profitable price increase while holding the maximum allowed quantity.     


"""


number = int(input())
days = int(input())

items_str = input()
items = list(map(int, items_str.split()))

sum = 0
for i in range(number):
    price_arr_str = input()
    price_arr = list(map(int, price_arr_str.split()))

    max_profit = 0
    # 使用贪心算法计算每件商品的最大利润
    for j in range(1, len(price_arr)):
        cur = price_arr[j]
        pre = price_arr[j - 1]
        # 当天价格减去前一天价格，如果当天利润大于0，则卖出，否则保存
        cur_profit = cur - pre
        max_profit += max(cur_profit, 0)

    sum += max_profit * items[i]

print(sum)


