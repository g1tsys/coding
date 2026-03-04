"""
Here's the extracted text from the image:

---

**Subscribe to this column to unlock online OJ practice access.**

Column Introduction: The latest Huawei OD machine test list is summarized, using five languages: C++, Java, Python, C language, JS. The thought analysis of each question is very detailed, and supports online OJ review brushing!!!!! Get permissions when you subscribe, new graphic ideas, problem solving, a variety of examples tested, more than 100 words of ideas referenced, constantly updated, code for learning reference only

[Question Bank Learning-Huawei OD Technology Interview Real Questions]

---

### I. Problem Statement

**Problem Description**

Given two integer arrays `array1` and `array2`, with elements sorted in ascending order.

Assume that taking one element from `array1` and one from `array2` can form a pair; now you need to take `k` pairs of elements,

And calculate the minimum sum of all extracted elements.

**Note:**

If two pairs of elements correspond to the same indices in `array1` and `array2`, they are considered the same pair.

---

### Input and Output

**Input**

Input two lines of array `array1`, `array2`; the first number in each line is the size of the array (0 < size <= 100);

0 < `array1[i]` <= 1000  
0 < `array2[i]` <= 1000

The next line contains a positive integer.

0 < k <= `array1.size()` * `array2.size()`

**Output**

Minimum sum that meets the requirements

---

Here's the extracted text from the image:

---

**Python Language Approach**

1. Initialize an empty list `pairs` to store the sum of element pairs  
2. For each element `num1` in `array1` and each element `num2` in `array2`, calculate their sum `num1 + num2` and add the result to `pairs`.  
3. Sort the `pairs` list so that the sum of each element pair is sorted in ascending order  
4. Extract the first `k` pairs and accumulate their sums to obtain the minimum sum.  
5. In the specific implementation, you can use two nested loops to iterate through `array1` and `array2`, calculate the sum of each element pair, sort the `pairs` list, and then take the sum of the first `k` elements.

---

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


