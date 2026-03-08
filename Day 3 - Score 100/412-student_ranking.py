"""
Here's the translation of the problem:

---

### Problem Description
Xiao Ming becomes a teacher at a school and needs to rank students by their **total score** or **individual subject score**. Can you help him?

---

### Input / Output

**Input:**
- **Line 1:** Two integers — number of students `n` and number of subjects `m`, where `0 < n < 100`, `0 < m < 10`
- **Line 2:** `m` subject names separated by spaces
  - Subject names contain only English letters, max length 10
  - Order corresponds to the scores entered later
  - No duplicate subject names
- **Lines 3 to n+2:** Each line contains a student's name followed by their `m` scores (space-separated)
  - No duplicate student names
  - Names contain only English letters, max length 10
  - Scores are integers from 0–100, matching the order of subjects in Line 2
- **Last line:** The subject name to rank by. If the subject **doesn't exist**, rank by **total score**

**Output:**
- One line of student names sorted by score (descending), separated by spaces
- If scores are tied, sort by **student name in alphabetical order**

---

### Python Thought Process

1. Read student count `n` and subject count `m`
2. Read `m` subject names into a list called `subjects`
3. Read each student's name and scores into a dictionary (name → scores list)
4. Read the ranking subject name into `rankSubject`
5. Check if `rankSubject` exists in `subjects`:
   - If **yes** → get its index
   - If **no** → set index to `-1`
6. Sort the students:
   - If `index != -1` → sort by that subject's score (descending); ties broken alphabetically
   - If `index == -1` → sort by total score (descending); ties broken alphabetically
7. Output the sorted student names joined by spaces
"""


# 读取学生人数n和科目数量m
n, m = map(int, input().split())
# 读取科目名称
subjects = input().split()

# 创建一个空字典，用于存储学生的姓名和对应的成绩
students = {}

# 读取每个学生的姓名和成绩
for _ in range(n):
    data = input().split()
    name = data[0]  # 学生姓名
    scores = list(map(int, data[1:]))  # 学生各科成绩
    students[name] = scores

# 读取用作排名的科目名称
rank_subject = input()

# 判断排名科目是否存在
if rank_subject in subjects:
    # 存在，则根据指定科目的分数进行排序
    index = subjects.index(rank_subject)
    sorted_students = sorted(students.items(), key=lambda x: (-x[1][index], x[0]))
else:
    # 不存在，则根据总分进行排序
    sorted_students = sorted(students.items(), key=lambda x: (-sum(x[1]), x[0]))

# 输出排序后的学生姓名
sorted_names = [student[0] for student in sorted_students]
print(' '.join(sorted_names))

