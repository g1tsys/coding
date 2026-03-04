"""
After subscribing to this column, you will unlock the online OJ problem-solving permission.
Column introduction: A summary of the latest Huawei OD machine test questions, with solutions in five languages: C++, Java, Python, C, and JS. The idea analysis for each question is very detailed, and online OJ evaluation and problem-solving are supported!!!! After subscription, you will obtain permissions, with added diagrammatic ideas, problem explanations, multiple sample tests, more than 100 words of reference analysis for ideas, and continuous updates. The code is for learning reference only.
Question bank learning: Real questions for Huawei OD technical interview coding.
Question
Question description
There is a row of parking spaces in the parking lot, where 0 represents no car parked and 1 represents a car parked. There is at least one car parked in the parking spaces and at least one empty space with no car parked.
To prevent scratches, it is necessary to find a parking space for the parking person such that the distance to the nearest vehicle from the parking person's car is maximized. Return the maximum distance at this time.
Input and output
Input
1. A string of parking identifiers separated by half-width commas, where the parking identifiers are 0 or 1, 0 is an empty space, and 1 is a parked car.
2. There are at most 100 parking spaces.
Output
Output an integer recording the maximum distance.

1. First, split the input parking sign string by commas and convert it into a list of integers.
2. Initialize two lists, left_distance and right_distance, to record the distance from each position to the nearest car on the left and the nearest car on the right, respectively.
3. Traverse the parking spaces from left to right. If there is a car at the current position, the distance to itself is 0; otherwise, the distance to the nearest car on the left is equal to the distance of the left position plus 1.
4. Traverse the parking spaces from right to left. If there is a car at the current position, the distance to itself is 0; otherwise, the distance to the nearest car on the right is equal to the distance of the right position plus 1.
5. Traverse each parking space to find the maximum value among the minimum values P of the distances from each empty space to the nearest vehicle.
6. Return the maximum distance.


"""

class Student:
    def __init__(self, height, weight, id):
        self.height = height
        self.weight = weight
        self.id = id

def main():
    # 读取学生数量
    n = int(input())

    # 读取身高序列
    heights = list(map(int, input().split()))

    # 读取体重序列
    weights = list(map(int, input().split()))

    # 创建学生对象列表，并与身高、体重和编号对应
    students = []
    for i in range(n):
        students.append(Student(heights[i], weights[i], i + 1))

    # 对学生对象列表进行排序
    students.sort(key=lambda x: (x.height, x.weight, x.id))

    # 输出排序后的学生编号
    for student in students:
        print(student.id, end=' ')

if __name__ == "__main__":
    main()
