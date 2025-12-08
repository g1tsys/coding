"""
# Problem Translation and Analysis

## Problem Description

A company's software training team is organizing a daily check-in learning activity for new employees. After one month (30 days), they want to identify the top performers based on check-in frequency.

**Requirements:**
- Find the top 5 employees with the most check-ins
- Tiebreaker rules (in order):
  1. Higher check-in count ranks higher
  2. If counts are equal, earlier first check-in date ranks higher
  3. If both are equal, smaller employee ID ranks higher

## Input Format
- Line 1: Number of employees N (range [1,100]), with IDs from 0 to N-1
- Line 2: 30 integers representing the number of employees who checked in each day
- Next 30 lines: Employee IDs who checked in each day (no duplicates per day)

## Output Format
- Top 5 employee IDs separated by spaces (or fewer if less than 5 employees participated)

## Solution Approach

**Key Steps:**
1. **Track check-in data** for each employee:
   - Total check-in count
   - First check-in day (for tiebreaker)
   - Employee ID

2. **Process daily records**:
   - Read each day's check-ins
   - Increment count for each employee
   - Record first appearance day if not already recorded

3. **Sort employees** using the three-level criteria:
   - Primary: Check-in count (descending)
   - Secondary: First check-in day (ascending)
   - Tertiary: Employee ID (ascending)

4. **Output** the top 5 (or fewer) employee IDs

## Example Walkthrough

**Sample Input:**
```
5
3 2 2 1 3 ...
0 1 2
0 3
1 2
...
```

**Process:**
- Employee 0: Checked in days 1, 5, 10 → count=3, first_day=1
- Employee 1: Checked in days 1, 3, 7 → count=3, first_day=1
- Employee 2: Checked in days 1, 3 → count=2, first_day=1
- Employee 3: Checked in days 2, 8 → count=2, first_day=2

**Sorting:**
1. Employees 0 and 1 both have 3 check-ins and started day 1 → ID 0 ranks first
2. Employee 2 started day 1, Employee 3 started day 2 → Employee 2 ranks higher

**Output:** `0 1 2 3 4` (assuming employee 4 also participated)

This is a classic ranking problem combining frequency counting with multi-level sorting criteria.
"""

# 读取新员工数量和每天打卡员工数量
n = int(input())
card_counts = list(map(int, input().split()))

# 创建字典来存储每个员工的打卡次数和最早参与打卡的时间
employee_dict = {}

# 遍历每天的打卡记录
for i in range(30):
    card_list = list(map(int, input().split()))

    # 更新每个员工的打卡次数和最早参与打卡的时间
    for employee_id in card_list:
        if employee_id in employee_dict:
            employee_dict[employee_id][0] += 1  # 打卡次数加一
            employee_dict[employee_id][1] = min(employee_dict[employee_id][1], i)  # 更新最早参与打卡的时间
        else:
            employee_dict[employee_id] = [1, i]  # 新员工，打卡次数为1，参与时间为当前时间

# 根据打卡次数、参与时间和员工编号进行排序
sorted_employee = sorted(employee_dict.items(), key=lambda x: (-x[1][0], x[1][1], x[0]))

# 提取前五名员工的编号
top5 = [x[0] for x in sorted_employee[:5]]

# 输出结果
print(' '.join(map(str, top5)))


