"""
### Problem Description
After joining the company, your mentor treats you to hot pot. Many ingredients are added to the pot at different times.
Different ingredients require different cooking times to be perfectly cooked. You want to eat as many perfectly cooked ingredients as possible, but your speed is not fast. Let `m` represent your hand speed: after scooping up one ingredient, you must wait at least `m` seconds before you can scoop another (you can only scoop one at a time).
Using the optimal strategy, what is the maximum number of perfectly cooked ingredients you can eat?

---

### Input and Output

**Input:**
- The first line contains two integers `n` and `m`, where `n` is the number of ingredients added to the pot, and `m` is your hand speed (1 < n, m < 1000).
- The next `n` lines each contain two integers `x` and `y`, meaning that an ingredient is added at `x` seconds and takes `y` seconds to cook perfectly (1 < x, y < 1000).

**Output:**
- An integer representing the maximum number of perfectly cooked ingredients you can eat with the optimal strategy.

# Python Language Approach
1. First, read the input values `n` and `m`, which represent the number of dishes and the number of hands (or the speed of serving).
2. Read the serving time and cooking time for each dish, and store them in a list.
3. Sort the list of dishes according to the time when they become perfectly cooked, i.e., sort them by the sum of serving time and cooking time.
4. Initialize the current time to 0, and initialize the count of dishes you can eat to 0.
5. Iterate through the list of dishes, extracting the serving time and cooking time for each dish:
   - If the current time is less than or equal to the time when this dish becomes perfectly cooked, then this dish can be eaten. Increment the count by 1, and update the current time to the time after finishing this dish plus the time `m` required for the next serving.
   - If the current time is greater than the time when this dish becomes perfectly cooked, then this dish is already past its optimal time and cannot be eaten.
6. Return the maximum number of dishes that can be eaten.

---

Would you like me to also translate the corresponding problem description that this approach is based on?
"""

def max_dishes(n, m, dishes):
    # 先按每道菜变得刚好合适的时间进行排序
    # 每道菜的变得刚好合适的时间是下锅时间 x 加上烹饪时间 y
    dishes.sort(key=lambda dish: dish[0] + dish[1])

    # 初始化当前时间为0
    current_time = 0

    # 初始化可以吃到的菜的计数
    count = 0

    # 遍历所有的菜
    for dish in dishes:
        # 取出这道菜的下锅时间
        start_time = dish[0]
        # 取出这道菜的烹饪时间
        duration = dish[1]

        # 计算这道菜变得刚好合适的时间
        ready_time = start_time + duration

        # 如果当前时间小于等于这道菜刚好合适的时间
        if current_time <= ready_time:
            # 说明这道菜可以吃到
            count += 1
            # 更新当前时间为捞完这道菜之后的时间，加上手速限制的时间 m
            current_time = ready_time + m

    # 返回最多可以吃到的菜的数量
    return count

# 读取输入的 n 和 m
n, m = map(int, input().split())
# 读取每道菜的信息（下锅时间和烹饪时间）
dishes = [tuple(map(int, input().split())) for _ in range(n)]

# 调用函数并打印结果
print(max_dishes(n, m, dishes))


