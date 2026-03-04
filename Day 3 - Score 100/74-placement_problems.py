"""
题目描述
幼儿园两个班的小朋友在排队时混在了一起,每位小朋友都知道自己是否否与前面一位小朋友同班,请你帮
忙把同班的小朋友找出来。
小朋友的编号是整数,与前一位小朋友同班用Y表示,不同班用N表示
学生序号范围(0,999],如果输入不合法则打印ERROR。
输入输出区
输入
输入为空格分开的小朋友编号和是否同班标志。
输出
输出为两行,每一行记录一个班小朋友的编号,编号用空格分并,直
1、编号需按照升序排列。
2、若只有一个班的小朋友,第二行为空行。

Problem Description
Children from two kindergarten classes got mixed up while lining up. Each child knows whether they are in the same class as the previous child. Please help identify which children are in the same class.

Each child has an integer number. "Y" indicates that the child is in the same class as the previous one, and "N" indicates they are in a different class.

The range of student serial numbers is (0, 999]. If the input is invalid, print "ERROR".

Input and Output
Input
The input consists of children's numbers and their same-class indicators, separated by spaces.

Output
Output two lines, each line records the numbers of children in one class, with the numbers separated by spaces.
1. The numbers must be arranged in ascending order.
2. If there is only one class of children, the second line should be an empty line.

1.通过input()函数获取用户输入的学生编号和是否同班的标志,并将输入的字符串按空格分割为一个列表。
2.初始化两个空列表class1和class2,分别用于存储两个班的学生编号。
3.遍历输入的每个部分,检查输入的合法性。如果学生编号不是一个合法的整数或同班标志不是'Y'或'N',
则打印"ERROR"并返回。
4.初始化一个变量current_class,用于记录当前处理的班级列表默认为None。
5.遍历输入的每个部分,将学生编号和同班标志分割出来,并将学生编号转换为整数。
6.检查学生编号是否在有效范围内,如果不是,则打印"ERROR""并返回。
7.如果同班标志为'N',表示当前学生与前一个学生不同班,切换当前处理的班级列表。
8.将学生编号添加到当前班级列表中。
9.对每个班的学生编号进行排序,并使用map函数将整数列表转换为字符串列表,然后使用"join将它们连
接为一个字符串。
10.打印两个班级的学生编号列表。如果只有一个班级的学生,第二行输出为空行。

Python Language Approach
1. Obtain the student ID and the same-class flag input by the user through the input() function, and split the input string into a list by spaces.
2. Initialize two empty lists, class1 and class2, to store the student IDs of the two classes respectively.
3. Traverse each part of the input to check the validity of the input. If the student ID is not a valid integer or the same-class flag is not 'Y' or 'N', print "ERROR" and return.
4. Initialize a variable current_class to record the current class list being processed, which defaults to None.
5. Traverse each part of the input, split out the student ID and the same-class flag, and convert the student ID to an integer.
6. Check if the student ID is within the valid range. If not, print "ERROR" and return.
7. If the same-class flag is 'N', it means the current student is not in the same class as the previous student, so switch the current class list being processed.
8. Add the student ID to the current class list.
9. Sort the student IDs of each class, use the map function to convert the integer list to a string list, and then use ''.join to connect them into a string.
10. Print the student ID lists of the two classes. If there is only one class of students, output an empty line for the second line.
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





