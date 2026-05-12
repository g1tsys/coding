"""
### Question Extraction

**Problem Title:** Maximum Social Distance (最大社交距离)

**Problem Description:**
During a period requiring social distancing, a company holds a meeting with a row of $N$ seats, numbered from $0$ to $N-1$. Employees enter the meeting room one by one and can leave at any time. The seating rules are as follows:
1. When an employee enters, they must choose the seat that **maximizes the distance** to the nearest occupied seat.
2. If there are multiple seats that satisfy the maximum distance condition, the employee chooses the seat with the **smallest index**.
3. If the row is full, the employee cannot sit.

**Input Format:**
- `seatNum`: An integer representing the total number of seats ($1 \le seatNum \le 500$).
- `seatOrLeave`: An array of integers representing the sequence of employee actions:
  - `1`: An employee enters the room.
  - Negative number (e.g., `-4`): The employee currently sitting at index `4` leaves the room. (Note: The problem states position 0 employees never leave, but the input format implies the negative value indicates the index of the person leaving).

**Output Format:**
- Return the seat index where the **last entering employee** sits.
- If the room is full when the last employee tries to enter, return `-1`.

**Constraints & Rules:**
- Distance is calculated as the minimum distance to any *currently occupied* seat.
- For the first person (no one seated), they typically sit at index 0 (based on the "smallest index" tie-breaker for max distance to boundaries, though the logic usually implies sitting at an endpoint).
- If the room is full, output -1.

---

### Python Thought Process & Solution

Since the provided text only contains headers ("Initialization", "Processing employee entry/exit", etc.) and no actual code or detailed logic, I have reconstructed the thought process and solution based on the problem description provided in the text.

#### Algorithmic Logic

1.  **State Management**:
    - We need to track which seats are occupied. A boolean array or a set of occupied indices is sufficient.
    - We also need to track the *last entered* employee's seat index to return it at the end.

2.  **Handling Entry (`1`)**:
    - **Check Capacity**: If all $N$ seats are occupied, the new employee cannot sit. Record the result as `-1` (or handle the logic such that if the room is full, we stop or return -1 immediately).
    - **Calculate Distances**: Iterate through every empty seat $i$ from $0$ to $N-1$.
        - If seat $i$ is occupied, skip it.
        - If seat $i$ is empty, calculate the distance to the **nearest** occupied seat.
        - *Special Case*: If no one is in the room yet, the distance is effectively infinite (or the distance to the "virtual" walls), so the rule "smallest index" applies, meaning the first person sits at index 0.
    - **Find Best Seat**:
        - Compare the distances of all empty seats.
        - Select the seat with the **maximum distance**.
        - **Tie-breaking**: If multiple seats have the same maximum distance, pick the one with the **smallest index**.
    - **Update State**: Mark the chosen seat as occupied and store its index.

3.  **Handling Exit (Negative Number `-k`)**:
    - The input `-k` means the person at index `k` leaves.
    - Mark seat `k` as empty.

4.  **Final Output**:
    - After processing the entire sequence, return the index of the seat where the **last successful entry** occurred.

#### Python Implementation

```python
def solve_max_social_distance(seatNum, seatOrLeave):
    """
    Simulates the seating process based on the maximum social distance rule.
    
    Args:
        seatNum (int): Total number of seats.
        seatOrLeave (list[int]): Sequence of actions (1 for enter, negative for leave).
        
    Returns:
        int: The seat index of the last entering employee, or -1 if the room was full.
    """
    occupied = [False] * seatNum
    last_seat_index = -1
    
    for action in seatOrLeave:
        if action == 1:
            # Check if the room is full
            if all(occupied):
                # If full, the last person cannot sit. 
                # The problem asks for the seat of the "last entering employee".
                # If they can't sit, we return -1.
                return -1
            
            best_seat = -1
            max_min_dist = -1
            
            # If no one is seated yet, the first person sits at index 0
            if not any(occupied):
                best_seat = 0
            else:
                # Iterate through all seats to find the best one
                for i in range(seatNum):
                    if occupied[i]:
                        continue
                    
                    # Calculate distance to the nearest occupied seat
                    min_dist = float('inf')
                    
                    # Check left side
                    for j in range(i - 1, -1, -1):
                        if occupied[j]:
                            min_dist = min(min_dist, i - j)
                            break
                    
                    # Check right side
                    for j in range(i + 1, seatNum):
                        if occupied[j]:
                            min_dist = min(min_dist, j - i)
                            break
                    
                    # If no one is seated (should be handled by 'any' check above, but for safety)
                    if min_dist == float('inf'):
                        min_dist = i # Distance to 0? Or just treat as infinite. 
                        # Based on rules, if no one is there, we pick 0. 
                        # But we handled the "no one seated" case above.
                        # If the loop runs and no one is seated, this logic is unreachable.
                    
                    # Update best seat
                    # We want MAX of min_dist. 
                    # If tie, pick smallest i (which is naturally handled by strict > comparison)
                    if min_dist > max_min_dist:
                        max_min_dist = min_dist
                        best_seat = i
            
            # Place the person
            occupied[best_seat] = True
            last_seat_index = best_seat
            
        else:
            # Action is negative, e.g., -4 means person at index 4 leaves
            leave_index = abs(action)
            if 0 <= leave_index < seatNum:
                occupied[leave_index] = False
            # Note: Problem says position 0 employees won't leave, but we handle general case.

    return last_seat_index

# Example Usage based on typical logic
# seatNum = 10
# actions = [1, 1, -2, 1] 
# result = solve_max_social_distance(seatNum, actions)
# print(result)
```

### Key Logic Explanation

1.  **Distance Calculation**: For every empty seat, we scan left and right to find the nearest occupied neighbor. The "distance" for that seat is the minimum of the distance to the left neighbor and the right neighbor.
2.  **Maximization**: We compare these "nearest neighbor distances" for all empty seats. The winner is the one with the largest value.
3.  **Tie-Breaking**: By iterating from index `0` to `N-1` and only updating the `best_seat` if the new distance is **strictly greater** (`>`), we automatically satisfy the requirement to pick the smallest index in case of a tie.
4.  **Edge Cases**:
    - **First Person**: The code explicitly checks `if not any(occupied)` to place the first person at `0`.
    - **Full Room**: If `all(occupied)` is true when a `1` comes in, the function returns `-1` immediately as per the requirement.

This approach ensures the simulation strictly follows the "maximum distance to nearest person" rule with the "smallest index" tie-breaker.

"""


def conference_seat_distance(seat_num, seat_or_leave):
    # 初始化会议室座位数组，0表示空座，1表示有人
    seats = [0] * seat_num

    seat_index = -1  # 最后一个员工坐的位置

    for order in seat_or_leave:
        if order < 0:  # 处理员工离开情况
            seats[-order] = 0  # 将对应位置设为空
        else:  # 处理员工进入情况
            max_distance = -1
            chosen_seat = -1

            # 寻找最优座位
            for i in range(seat_num):
                if seats[i] == 0:
                    left = i
                    while i < seat_num and seats[i] == 0:
                        i += 1
                    right = i - 1

                    if left == 0 or right == seat_num - 1:
                        distance = right - left + 1
                    else:
                        distance = (right - left + 2) // 2

                    if distance > max_distance:
                        max_distance = distance
                        chosen_seat = left if left == 0 else right if right == seat_num - 1 else left + (right - left) // 2

            if chosen_seat != -1:
                seats[chosen_seat] = 1  # 标记该座位已被占用
                seat_index = chosen_seat
            else:
                seat_index = -1  # 无法安排座位

    return seat_index  # 返回最后一个员工坐的位置


# 读取输入
seat_num = int(input())
seat_or_leave = list(map(int, input().strip()[1:-1].split(',')))

# 计算并输出最后进来的员工所坐的位置
ans = conference_seat_distance(seat_num, seat_or_leave)
print(ans)
