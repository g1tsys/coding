"""
> Question Translation:  
A company organizes a bike ride on a green island as a team-building activity. They are renting public double-person bicycles, each of which can carry a maximum of two people and has a maximum weight limit of M. Given the weight of each person in the department, determine the **minimum number of double-person bicycles** required.

---

> Python Language Thought Process Translation:  
1. First, read the input values: the maximum weight limit of the bicycle (`m`) and the total number of people (`n`).  
2. Then, read the list of `n` integers representing each person's weight.  
3. Sort the weight list in ascending order.  
4. Initialize a counter variable `count` to 0, which will be used to track the number of bicycles needed.  
5. Use a two-pointer approach: one pointer (`left`) starts at the beginning of the list, and the other (`right`) starts at the end of the list.  
6. In each iteration, check if the sum of the weights at the `left` and `right` pointers is less than or equal to `m`.  
   - If it is, then both people can ride together, so increment the `count` by 1 and move the `left` pointer to the right.  
   - Regardless of the result, move the `right` pointer to the left.  
7. Repeat this process until the `left` pointer is no longer less than or equal to the `right` pointer.  
8. Return the value of `count` as the minimum number of bicycles required.

---

> Example Walkthrough:  
Let’s say the input is:

```
m = 100
n = 5
weights = [60, 70, 80, 90, 100]
```

**Step-by-step process:**

1. Sort the weights: `[60, 70, 80, 90, 100]`  
2. Initialize `left = 0`, `right = 4`, `count = 0`  
3. Check if `60 + 100 = 160 <= 100` → No → Move `right` to 3  
4. Check if `60 + 90 = 150 <= 100` → No → Move `right` to 2  
5. Check if `60 + 80 = 140 <= 100` → No → Move `right` to 1  
6. Check if `60 + 70 = 130 <= 100` → No → Move `right` to 0  
7. Now, `left = 0`, `right = 0` → Loop ends  
8. Result: `count = 0` (No pair can ride together in this case)

If the limit was `m = 150`, the result would be `2` (pairs: 60 + 90 and 70 + 80).

"""


result = 0  # 记录最少需要的双人自行车数量
m, n = map(int, input().split())  # 自行车限重m和部门总人数n
weight = list(map(int, input().split()))  # 每个人的体重列表

# 对weight排序
weight.sort()

# 双游标从左右向中间找相加小于等于m的数
lp = 0  # 左指针
rp = n - 1  # 右指针
while lp <= rp:
    if weight[lp] + weight[rp] <= m:
        lp += 1  # 左指针右移
    rp -= 1  # 右指针左移
    result += 1  # 找到一对骑行者，数量加1

print(result)  # 输出最少需要的双人自行车数量


