"""
# Translation of the Question

## Problem Description
100 people stand in a circle, each with a number from 1 to 100. They count off starting from 1. When someone counts to M, they automatically exit the circle, and the next person starts counting from 1 again. This continues until the remaining number of people is less than M.

**Question:** What are the original numbers of the remaining people?

## Input/Output
- **Input:** An integer M
- **Output:** 
  - If M ≤ 1 or M ≥ 100, output "ERROR!"
  - Otherwise, output the original numbers of remaining people in ascending order, separated by commas

## Sample Cases
- **Sample 1:** If M = 3, some people will be eliminated until fewer than 3 remain
- **Sample 2:** (Similar pattern with different M value)

---

# Python Approach (Translated)

1. **Validate input M:** If M ≤ 1 or M ≥ 100, return "ERROR!"
2. **Initialize the list** `people` with numbers from 1 to 100
3. **Set counter** `count` to 0
4. **Loop until** remaining people < M:
   - Increment count for each person
   - When count reaches M, remove that person from the circle
   - Reset count and continue
5. **After loop ends**, the remaining people are the survivors
6. **Sort the remaining numbers** in ascending order
7. **Return the result** as a comma-separated string

---

# Walk-through Example

Let's use **M = 3** with a simplified example of **10 people** (instead of 100):

**Initial:** People = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

**Round 1:**
- Count: 1 (person 1), 2 (person 2), **3 (person 3)** ← **Exits**
- Remaining: [1, 2, 4, 5, 6, 7, 8, 9, 10]

**Round 2:**
- Count: 1 (person 4), 2 (person 5), **3 (person 6)** ← **Exits**
- Remaining: [1, 2, 4, 5, 7, 8, 9, 10]

**Round 3:**
- Count: 1 (person 7), 2 (person 8), **3 (person 9)** ← **Exits**
- Remaining: [1, 2, 4, 5, 7, 8, 10]

**Continue this pattern...**

The process continues until the number of remaining people < M (which is 3).

**Final result:** When only 2 people remain (less than M=3), the algorithm stops and outputs their original numbers in ascending order.

For the actual problem with 100 people and your chosen M value, the same logic applies but with more iterations.
"""

def findLastPerson(M):
    if M <= 1 or M >= 100:
        return "ERROR!"

    people = list(range(1, 101))  # 初始化编号列表，从1到100
    count = 0  # 报数计数器

    while len(people) > M:
        count += 1
        if count == M:
            people.pop(0)  # 该人退出圈圈
            count = 0  # 重置报数计数器
        else:
            last_person = people.pop(0)  # 移除第一个人，并记录其编号
            people.append(last_person)  # 将该人放到列表末尾

    people_str = ', '.join(str(num) for num in people[:-1])  # 将剩余人的编号转换为字符串
    sorted_people_str = ', '.join(sorted(people_str.split(", "), key=int))  # 对剩余人的编号按照数字从小到大排序
    return sorted_people_str


M = int(input())
result = findLastPerson(M)
print(result)


