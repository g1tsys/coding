"""
Based on the web page content, this appears to be a **coding problem about separating students from two classes**. Here's my interpretation:

## Problem Summary

**Scenario:** Students from two kindergarten classes got mixed up while lining up. Each student knows whether they're in the same class as the student directly in front of them.

**Task:** Separate the students back into their two classes.

**Input Format:**
- Student IDs (integers in range 0-999) paired with flags
- Flag 'Y' = same class as previous student
- Flag 'N' = different class from previous student

**Output Format:**
- Two lines, each containing student IDs from one class
- IDs must be sorted in ascending order
- If only one class exists, the second line is empty
- Print "ERROR" for invalid input

## Example Walkthrough

Let's say we have input: `1 N 2 Y 3 N 4 Y`

**Step-by-step:**
1. Student 1: First student → Class A
2. Student 2 (Y): Same as student 1 → Class A
3. Student 3 (N): Different from student 2 → Class B
4. Student 4 (Y): Same as student 3 → Class B

**Output:**
1 2
3 4


## Approach Hints

1. **Parse input** - validate student IDs are in valid range
2. **Track classes** - use the Y/N flags to assign students to classes
3. **Sort each class** - arrange IDs in ascending order
4. **Format output** - print two lines with sorted IDs

The key insight is treating this as a **grouping problem** where consecutive Y flags keep students in the same group, and N flags switch groups.

"""

def sort_students():
    # 从用户那里获取输入
    input_string = input()

    # 将输入字符串按空格分割，以便处理每个学生的信息
    parts = input_string.split()

    # 初始化两个列表，分别存储两个班的学生编号
    class1 = []
    class2 = []

    # 遍历输入的每部分，检查输入的合法性
    for part in parts:
        id_part, class_part = part.split('/')
        if not id_part.isdigit() or class_part not in ['Y', 'N']:
            print("ERROR")
            return

    # 当前班级变量，开始时未定义
    current_class = None
    for part in parts:
        # 分割每部分为学生编号和是否同班的标志
        student_id, same_class = part.split('/')
        student_id = int(student_id)

        # 检查学生编号是否在有效范围内
        if not 0 < student_id <= 999:
            print("ERROR")
            return

        # 如果标志为'N'，表示当前学生与前一个学生不同班
        if same_class == 'N':
            # 切换当前处理的班级列表
            if current_class is None or current_class == class2:
                current_class = class1
            else:
                current_class = class2
        # 将学生编号添加到当前班级列表中
        current_class.append(student_id)

    # 对每个班的学生编号进行排序，并打印结果
    # 使用map函数将整数列表转换为字符串列表，然后用' '.join将它们连接为一个字符串
    print(' '.join(map(str, sorted(class1))))
    print(' '.join(map(str, sorted(class2))))


# 调用函数，实现动态输入和处理
sort_students()



