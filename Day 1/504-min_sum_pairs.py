"""
# Translation and Analysis
## Problem Description
Given two integer arrays `array1` and `array2`, both sorted in ascending order. You can pick one element from each array to form a pair. You need to select `k` pairs and calculate the minimum possible sum of all selected elements.
**Note:** Two pairs are considered the same if they correspond to the same indices in both arrays.
## Input/Output Format

**Input:**
- Two lines for `array1` and `array2`, where the first number is the array size (0 < size ≤ 100)
- 0 < array1[i] ≤ 1000
- 0 < array2[i] ≤ 1000
- Next line: positive integer k
- 0 < k ≤ array1.size() × array2.size()

**Output:**
- The minimum sum that satisfies the requirements

## Python Approach (Thought Process)

1. **Initialize an empty list** `pairs` to store the sum of each pair from the two arrays
2. **Nested loop iteration**: For each element `num1` in `array1` and each element `num2` in `array2`, calculate `num1 + num2` and add to `pairs`
3. **Sort the pairs list** in ascending order to get all possible sums sorted
4. **Take the first k elements** from the sorted list and sum them to get the minimum sum
5. **Implementation**: Use two nested loops to traverse both arrays, calculate pair sums, sort the results, and sum the first k elements

## Example Walkthrough

**Input:**
```
3 1 2 3
3 4 5 6
4
```

**Step-by-step:**

1. **Parse input:**
   - array1 = [1, 2, 3]
   - array2 = [4, 5, 6]
   - k = 4

2. **Generate all pairs:**
   - (1,4)=5, (1,5)=6, (1,6)=7
   - (2,4)=6, (2,5)=7, (2,6)=8
   - (3,4)=7, (3,5)=8, (3,6)=9
   - pairs = [5, 6, 7, 6, 7, 8, 7, 8, 9]

3. **Sort pairs:**
   - sorted_pairs = [5, 6, 6, 7, 7, 7, 8, 8, 9]

4. **Sum first k=4 elements:**
   - 5 + 6 + 6 + 7 = **24**

**Output:** 24
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


