"""

### Problem Description
Given a 2D array `nums`, for each element `nums[i][j]`, find the **closest** element that has the **same value**. Output the sum of the absolute differences of their row and column coordinates. If there is no such element with the same value, output `-1` for that position.

---

### Input and Output

#### Input
1. The first line is the **number of rows** of the 2D array.
2. The second line is the **number of columns** of the 2D array.
3. The subsequent lines contain the numbers of the array, separated by spaces (filling the 2D array row by row).

#### Output
Return the result as an **array** (matching the dimensions of the input 2D array), where each element is the calculated sum of absolute coordinate differences (or `-1` if no match exists).

# Python Language Approach
1. Read the number of rows and columns from the input and convert them to integers.
2. Create a dictionary `map` to store each value `Q` and the list of its corresponding coordinates.
3. Create a 2D array `nums` to store the input 2D array `Q`.
4. Create a 2D array `res` to store the resulting 2D array.
5. Iterate through the input 2D array, adding each value and its corresponding coordinates to the dictionary `map`.
6. Iterate through the 2D array `nums`, and perform the following operations for each element:
   - If the length of the coordinate list corresponding to this element in `map` is 1, it means there are no other elements with the same value. Set the value at the corresponding position in the result array `res` to `-1`.
   - Otherwise, iterate through the list of coordinates for this value in `map`, calculate the Manhattan distance from the current coordinate to each coordinate in the list, find the minimum distance, and store it in the result array `res`.
7. Add each row of the result array `res` to the result list `resList`.
8. Output the result list `resList`.

---

Would you like me to also provide the full Python code implementation for this problem?


"""


rowStr = input()  # 输入二维数组的行数
columnStr = input()  # 输入二维数组的列数
rowLen = int(rowStr)
columnLen = int(columnStr)

map = {}  # 存储值和对应坐标的字典
nums = [[0] * columnLen for _ in range(rowLen)]  # 存储输入的二维数组
res = [[0] * columnLen for _ in range(rowLen)]  # 存储结果的二维数组

# 先用字典对值进行存放，key为数值，value为对应坐标的列表集合
for i in range(rowLen):
    line = input()
    strings = line.split(" ")
    for j in range(columnLen):
        val = int(strings[j])
        nums[i][j] = val
        index = [i, j]
        map.setdefault(val, []).append(index)

resList = []
for i in range(rowLen):
    numList = []
    for j in range(columnLen):
        val = nums[i][j]
        indexList = map[val]  # 获取值对应的坐标列表
        if len(indexList) == 1:
            res[i][j] = -1  # 如果只有一个坐标，置为-1
        else:
            min_distance = float('inf')
            for indexArr in indexList:
                if indexArr[0] == i and indexArr[1] == j:
                    continue
                distance = abs(indexArr[0] - i) + abs(indexArr[1] - j)
                min_distance = min(distance, min_distance)
            res[i][j] = min_distance  # 计算最小距离并存入结果数组
        numList.append(res[i][j])  # 将结果添加到当前行的列表中
    resList.append(numList)  # 将当前行的列表添加到结果列表中

print(resList)  # 输出结果列表
