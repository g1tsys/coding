
"""
# Python Problem Translation & Solution

### 题目 (Problem)
Given two integer arrays `array1` and `array2` sorted in ascending order, you need to select **k pairs** of elements (one from each array) such that the sum of all selected elements is minimized.

**Note:** Two pairs are considered identical if they correspond to the same indices in both arrays.

### 输入输出 (Input/Output)

**Input:**
- Line 1: Array `array1` with size as first number, followed by elements
- Line 2: Array `array2` with size as first number, followed by elements
- Line 3: Integer `k` (number of pairs to select)

**Constraints:**
- 0 < size ≤ 100
- 0 < array1[i], array2[i] ≤ 1000
- 0 < k ≤ array1.size() × array2.size()

**Output:**
- Minimum sum of all selected elements from k pairs

### Python 思路 (Thought Process)

1. Initialize an empty list `pairs` to store sums of element pairs
2. Use nested loops to iterate through each element in `array1` and `array2`
3. Calculate the sum of each pair (num1 + num2) and add it to `pairs`
4. Sort the `pairs` list in ascending order
5. Select the first k elements from the sorted list
6. Sum these k elements and return the result

"""

# 定义函数minSumPairs，接受三个参数：arr1为整数数组1，arr2为整数数组2，k为要求的最小和对数
def minSumPairs(arr1, arr2, k):
    pairs = []  # 创建一个空列表用于存储所有的和对
    for num1 in arr1:  # 遍历数组arr1中的每个元素
        for num2 in arr2:  # 遍历数组arr2中的每个元素
            pairs.append(num1 + num2)  # 将arr1和arr2中的元素相加得到和，并添加到和对列表中

    pairs.sort()  # 对和对列表进行排序
    sum = 0  # 初始化sum为0，用于存储最小的k个和对的和
    for i in range(k):  # 遍历前k个和对
        sum += pairs[i]  # 将每个和对的和累加到sum中

    return sum  # 返回最小的k个和对的和

# 读取输入
size1, *arr1 = map(int, input().split())  # 读取整数数组1的大小和数组元素
size2, *arr2 = map(int, input().split())  # 读取整数数组2的大小和数组元素
k = int(input())  # 读取最小和对数

result = minSumPairs(arr1, arr2, k)  # 调用minSumPairs函数计算最小的k个和对的和
print(result)  # 输出结果


