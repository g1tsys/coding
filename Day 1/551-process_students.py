"""
# Translation and Explanation: Elective Course Problem

## Problem Description

You have two elective courses, each with some students enrolled. Each student has grades for their courses. You need to find students who are enrolled in **both** elective courses and output them according to these rules:

1. **Group by class**: Class number (first 5 digits of student ID) in ascending order
2. **Within each class**: Sort by total score (sum of both courses) in descending order
3. **If scores are equal**: Sort by student ID in ascending order

### Input Format
- **Line 1**: First course students' data (format: `studentID,score;studentID,score;...`)
- **Line 2**: Second course students' data (same format)
- **Student ID**: 8-digit number (2-digit department + 2-digit year + 1-digit major + 3-digit class number)
- **Score range**: [0, 100]
- **Number of students**: [1, 2000]

### Output Format
- If no common students: output `NULL`
- Otherwise: For each class, output:
  - Class ID (first 5 digits of student ID)
  - Student IDs separated by semicolons (sorted by rules above)


# Example usage
course1 = "01202301,75;01202302,80;01203101,90;01203102,85"
course2 = "01202301,85;01202302,70;01203101,95;01204101,88"

print(solve_elective_courses(course1, course2))


## Example Walkthrough

### Input:

Course 1: 01202301,75;01202302,80;01203101,90;01203102,85
Course 2: 01202301,85;01202302,70;01203101,95;01204101,88


### Step-by-Step Process:

1. **Parse Course 1**:
   - `01202301` → score 75 (class: 01202)
   - `01202302` → score 80 (class: 01202)
   - `01203101` → score 90 (class: 01203)
   - `01203102` → score 85 (class: 01203)

2. **Parse Course 2**:
   - `01202301` → score 85 (class: 01202)
   - `01202302` → score 70 (class: 01202)
   - `01203101` → score 95 (class: 01203)
   - `01204101` → score 88 (class: 01204) ❌ Not in course 1

3. **Find Common Students**:
   - Class 01202: `01202301` (total: 160), `01202302` (total: 150)
   - Class 01203: `01203101` (total: 185)

4. **Sort by Class** (ascending): 01202, 01203

5. **Sort Within Each Class**:
   - Class 01202: `01202301` (160) before `01202302` (150)
   - Class 01203: Only `01203101` (185)

### Output:
01202
01202301;01202302
01203
01203101
"""

# 定义一个函数来处理输入和输出
def process_students():
    # 动态获取用户输入的两行数据
    input1 = input()
    input2 = input()

    # 将输入的学生成绩按照分号分隔并转换成列表
    students_course1 = input1.split(';')
    students_course2 = input2.split(';')

    # 创建两个字典来存储两门选修课的学生成绩
    course1_scores = {}
    course2_scores = {}

    # 遍历第一门选修课的学生成绩，并填充字典course1_scores
    for student in students_course1:
        # 使用逗号分隔学号和成绩
        student_id, score = student.split(',')
        course1_scores[student_id] = int(score)

    # 遍历第二门选修课的学生成绩，并填充字典course2_scores
    for student in students_course2:
        student_id, score = student.split(',')
        course2_scores[student_id] = int(score)

    # 创建一个字典来存储同时选修了两门选修课的学生
    common_students = {}

    # 遍历第一门选修课的学生成绩
    for student_id in course1_scores:
        # 检查这个学生是否也选修了第二门选修课
        if student_id in course2_scores:
            # 获取学生的班级编号（学号的前五位）
            class_id = student_id[:5]
            # 计算两门选修课成绩的总和
            total_score = course1_scores[student_id] + course2_scores[student_id]
            # 将学生信息加入common_students字典
            if class_id not in common_students:
                common_students[class_id] = []
            common_students[class_id].append((student_id, total_score))

    # 如果没有同时选修两门选修课的学生，输出NULL
    if not common_students:
        print("NULL")
        return

    # 按照班级编号进行排序
    sorted_classes = sorted(common_students.keys())

    # 遍历每个班级，按要求格式化输出
    for class_id in sorted_classes:
        print(class_id)
        # 按照成绩总和降序，成绩相同时按照学号升序排序
        sorted_students = sorted(common_students[class_id], key=lambda x: (-x[1], x[0]))
        # 提取排序后的学号并使用分号分隔
        student_ids = [student[0] for student in sorted_students]
        print(';'.join(student_ids))

# 调用函数处理学生数据
process_students()

