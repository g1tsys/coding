"""
Based on the webpage content provided, here is the extracted problem description and the translated thought process for the Python solution.

### Problem: Channel Allocation (华为OD机试真题)

**Description:**
Algorithm engineer Xiao Ming faces the problem of allocating communication channels to as many users as possible. The rules and conditions are:
1.  **Channel Attribute:** Every channel has an attribute called "order". A channel of order $r$ has a capacity of $2^r$ bits.
2.  **User Requirement:** All users need to transmit the same amount of data: $D$ bits.
3.  **Allocation Rule:** A user can be assigned multiple channels, but each channel can only be assigned to one user.
4.  **Satisfaction Condition:** A user can transmit data only if the sum of the capacities of all channels assigned to them is $\ge D$.

**Goal:** Given a set of channel resources, calculate the maximum number of users that can be served.

**Input Format:**
*   Line 1: An integer $R$ (maximum order), where $0 \le R < 20$.
*   Line 2: $R+1$ integers separated by spaces, representing the quantity $N_i$ of channels for each order $i$ (from 0 to $R$).
*   Line 3: An integer $D$, the data requirement per user, where $0 < D < 1,000,000$.

**Output Format:**
*   A single integer representing the maximum number of users that can transmit data.

---

### Python Implementation Thought Process

The following steps outline the logic used to solve this problem in Python, derived from the strategy described in the source text:

1.  **Initialization and Preprocessing:**
    *   Read the input values: the maximum order $R$, the list of channel counts for each order, and the data requirement $D$.
    *   Calculate the **total capacity** of all available channels. This is done by summing $N_i \times 2^i$ for all orders $i$.
    *   Initialize a counter for the number of served users to 0.
    *   *Purpose:* This allows for a quick check to see if the remaining total capacity is sufficient to serve even a single user.

2.  **Main Loop (Greedy Allocation):**
    *   Enter a loop that continues as long as the **remaining total capacity** is greater than or equal to $D$.
    *   Inside the loop, attempt to allocate channels to a new user until their requirement $D$ is met.

3.  **Prioritize Large Channels:**
    *   To maximize the number of users, the strategy is to satisfy each user's requirement using the **fewest number of channels** possible.
    *   Start iterating from the **largest order** (largest capacity) down to the smallest.
    *   For the current user's remaining need, check if a channel of the current order is available.
    *   If available, and if adding this channel does not exceed the user's specific need (or to minimize waste, assign it if it fits best), assign the channel.
    *   *Refinement:* Ideally, we want to fill the user's quota $D$ as efficiently as possible. The text suggests using large channels first to reduce the count of channels used per user, leaving smaller channels available for others.

4.  **Supplement with Small Channels:**
    *   If after trying all larger channels the user's requirement is still not fully met, switch to using **smaller order channels**.
    *   Iterate from the smallest order upwards to fill the remaining gap.
    *   Continue assigning channels until the sum of capacities for the current user $\ge D$.

5.  **Update Counters:**
    *   Once a user's requirement is satisfied, increment the **served user count**.
    *   Subtract the used channel capacities from the global pool of available channels (update the counts $N_i$ and the total remaining capacity).

6.  **Termination and Output:**
    *   If at any point the remaining total capacity is less than $D$, the loop terminates because no more users can be served.
    *   Print the final count of served users.

**Key Logic Summary:**
The core algorithm is a **greedy approach**. By satisfying each user with the largest possible chunks first, we minimize the "fragmentation" of the channel pool, theoretically leaving enough small channels to satisfy the requirements of subsequent users.
"""

# Conceptual structure based on the thought process

def solve_channel_allocation():
    # 1. Read Input
    # R = int(input())
    # channels = list(map(int, input().split()))
    # D = int(input())
    
    # 2. Preprocessing
    # total_capacity = sum(channels[i] * (2 ** i) for i in range(len(channels)))
    # users_served = 0
    
    # 3. Main Loop
    # while total_capacity >= D:
    #     current_user_need = D
    #     
    #     # 4. Prioritize Large Channels (Greedy)
    #     # Iterate from largest order down to 0
    #     for i in range(R, -1, -1):
    #         if current_user_need <= 0: break
    #         if channels[i] > 0:
    #             capacity_per_channel = 2 ** i
    #             # Calculate how many of this channel we need
    #             count_needed = min(channels[i], (current_user_need + capacity_per_channel - 1) // capacity_per_channel)
    #             
    #             # Assign
    #             channels[i] -= count_needed
    #             current_user_need -= count_needed * capacity_per_channel
    #             total_capacity -= count_needed * capacity_per_channel
    #             
    #     # Note: The logic in the text implies a two-phase fill or a specific greedy fill.
    #     # If the simple greedy from top-down doesn't perfectly align, 
    #     # the text mentions "Supplement with small channels" if needed.
    #     
    #     if current_user_need <= 0:
    #         users_served += 1
    #     else:
    #         # If we ran out of channels but still have need, and total_capacity < D, loop breaks naturally
    #         break
             
    # 5. Output
    # print(users_served)
    pass

