"""
Based on the web page text provided, here is the extracted problem details and the logical thought process for solving the "Wonderland" problem using Python.

Note: The original text mentions code exists but does not explicitly write out the step-by-step logic text or the full code in the snippet provided. The thought process below is derived from the standard algorithmic approach required to solve this specific "minimum cost for tickets" dynamic programming problem, which matches the problem description perfectly.

### Problem Statement: Wonderland

**Description:**
You need to calculate the minimum cost for a person (Xiao Wang) to visit a theme park called Wonderland on specific days within a year. There are 4 types of passes available:
1.  **1-day pass** (valid for 1 day)
2.  **3-day pass** (valid for 3 consecutive days)
3.  **7-day pass** (valid for 7 consecutive days)
4.  **30-day pass** (valid for 30 consecutive days)

The costs for these passes are given in an array `costs`.
The days Xiao Wang plans to visit are given in a sorted array `days`.
If a pass is bought on day $d$, it covers visits from day $d$ to $d + \text{duration} - 1$.

**Goal:** Find the minimum total cost to cover all days in the `days` array.

---

### Input & Output

**Input:**
*   `costs`: A list of 4 integers representing the price of [1-day, 3-day, 7-day, 30-day] passes.
*   `days`: A sorted list of integers (1 to 365) representing the specific days Xiao Wang will visit.

**Output:**
*   An integer representing the **minimum cost** required.

**Example Logic:**
*   If `costs = [2, 7, 15, 30]` and `days = [1, 4, 6, 7, 8, 20]`:
    *   Buying individual tickets for every day might be expensive.
    *   Buying a 7-day pass on day 1 might cover days 1, 4, 6, 7, 8.
    *   The algorithm must find the optimal combination.

---

### Python Thought Process & Algorithm

This is a classic **Dynamic Programming (DP)** problem. The core idea is to calculate the minimum cost to cover travel up to a specific day $i$.

**Key Concepts:**
1.  **State Definition:** Let `dp[i]` be the minimum cost to cover all travel days up to day $i$ (where $i$ ranges from 0 to 365).
2.  **Base Case:** `dp[0] = 0` (Cost to cover 0 days is 0).
3.  **Transitions:**
    *   If day $i$ is **not** in the `days` list, then no new pass is needed for today. The cost is the same as yesterday: `dp[i] = dp[i-1]`.
    *   If day $i$ **is** in the `days` list, we must have bought a pass that covers this day. We have 4 choices corresponding to the 4 pass types. We take the minimum of these options:
        *   **1-day pass:** Cost is `costs[0] + dp[i-1]` (assuming $i-1 \ge 0$).
        *   **3-day pass:** Cost is `costs[1] + dp[i-3]` (assuming $i-3 \ge 0$, else just `costs[1]`).
        *   **7-day pass:** Cost is `costs[2] + dp[i-7]`.
        *   **30-day pass:** Cost is `costs[3] + dp[i-30]`.
    *   Formula: `dp[i] = min(dp[max(0, i-1)] + costs[0], dp[max(0, i-3)] + costs[1], dp[max(0, i-7)] + costs[2], dp[max(0, i-30)] + costs[3])`

**Optimization Note:**
Since `days` can be sparse (e.g., only day 1 and day 365), iterating 365 times is efficient enough. We can use a set for `days` for $O(1)$ lookups.

---
"""
### Python Code Solution

def min_cost_wonderland(costs, days):
    """
    Calculates the minimum cost to cover all travel days.
    
    Args:
    costs: List[int] - [1-day, 3-day, 7-day, 30-day] prices
    days: List[int] - Sorted list of days to travel (1-365)
    
    Returns:
    int - Minimum cost
    """
    # Convert days to a set for O(1) lookup
    travel_days = set(days)
    
    # Get the last day we need to cover
    last_day = days[-1]
    
    # DP array initialization
    # dp[i] represents the min cost to cover all travel days up to day i
    dp = [0] * (last_day + 1)
    
    # Durations corresponding to costs
    durations = [1, 3, 7, 30]
    
    for i in range(1, last_day + 1):
        if i not in travel_days:
            # If today is not a travel day, cost is same as yesterday
            dp[i] = dp[i-1]
        else:
            # If today is a travel day, we calculate the min cost by trying all 4 passes
            # We look back 'duration' days. If index < 0, we use 0 cost for that part.
            min_val = float('inf')
            
            for j in range(4):
                duration = durations[j]
                cost = costs[j]
                
                # Calculate the previous day's cost before this pass starts
                prev_day = i - duration
                if prev_day < 0:
                    prev_cost = 0
                else:
                    prev_cost = dp[prev_day]
                
                total_cost = prev_cost + cost
                if total_cost < min_val:
                    min_val = total_cost
            
            dp[i] = min_val
            
    return dp[last_day]

# Example Usage
if __name__ == "__main__":
    # Sample Input based on typical problem constraints
    # Costs: 1-day=2, 3-day=7, 7-day=15, 30-day=30
    costs = [2, 7, 15, 30]
    days = [1, 4, 6, 7, 8, 20]
    
    result = min_cost_wonderland(costs, days)
    print(f"Minimum cost: {result}")



"""
### Explanation of the Code Logic
1.  **Set Conversion**: `set(days)` allows us to instantly check if a specific day requires a ticket.
2.  **DP Array**: `dp` array size is `last_day + 1`. `dp[i]` stores the optimal cost up to day `i`.
3.  **Iteration**: We loop from day 1 to the last travel day.
    *   If `i` is not a travel day, we simply carry forward the previous cost (`dp[i] = dp[i-1]`).
    *   If `i` is a travel day, we try buying a 1-day, 3-day, 7-day, or 30-day pass *ending* or *starting* such that it covers day `i`.
        *   Buying a 3-day pass on day `i` effectively covers `i-2, i-1, i`. The cost is `costs[1] + dp[i-3]`.
        *   We take the `min` of all these 4 possibilities.
4.  **Result**: The value at `dp[last_day]` is the answer.

This approach ensures we find the global minimum by breaking the problem down into optimal substructures (optimal cost to cover days up to `i-1`, `i-3`, etc.). The time complexity is $O(N)$ where $N$ is the last day in the `days` array (max 365), which is extremely efficient.
"""

def min_cost_for_trip(costs, days):
    # 创建一个dp数组，长度为一年的天数+1，用于记录到达每一天所需的最低消费
    # 初始值设为0，表示没有消费
    dp = [0 for _ in range(days[-1] + 1)]

    # 创建一个集合，包含小王计划游玩的所有日期，方便后面检查某一天是否是游玩日
    day_set = set(days)

    # 遍历一年中的每一天
    for i in range(1, len(dp)):
        # 如果当天不是游玩日，则当天的消费与前一天相同，因为小王没有购票的必要
        if i not in day_set:
            dp[i] = dp[i - 1]
        else:
            # 如果当天是游玩日，则需要计算最低消费
            # 考虑购买一日票的情况，直接在前一天的消费基础上加上一日票的价格
            cost_1d = dp[max(0, i - 1)] + costs[0]
            # 考虑购买三日票的情况，需要查看三天前的消费，再加上三日票的价格
            cost_3d = dp[max(0, i - 3)] + costs[1]
            # 考虑购买周票的情况，需要查看七天前的消费，再加上周票的价格
            cost_7d = dp[max(0, i - 7)] + costs[2]
            # 考虑购买月票的情况，需要查看三十天前的消费，再加上月票的价格
            cost_30d = dp[max(0, i - 30)] + costs[3]

            # 当天的消费等于以上四种情况中的最小值
            dp[i] = min(cost_1d, cost_3d, cost_7d, cost_30d)

    # 返回最后一天的消费，即为完成游玩计划所需的最低消费
    return dp[-1]



# 输入售票价格
costs_input = input()
costs = list(map(int, costs_input.split()))

# 输入小王计划游玩日期数组
days_input = input()
days = list(map(int, days_input.split()))

# 计算并输出最低消费
print(min_cost_for_trip(costs, days))
