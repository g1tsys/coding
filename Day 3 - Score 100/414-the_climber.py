"""
Based on the provided page content, here is the extracted **Question, Input, and Output** section:

---

### 🎃 题目描述 (Problem Description)

给一个数组，判断山峰的个数。数组的每个元素的值代表海拔高度，0代表平地，数值越高，海拔越高。山峰的定义为：当某个位置左右的海拔低于自己的海拔时，这个位置就是山峰。数组的起始和末尾如果符合条件也算山峰。

> *Given an array, count the number of mountain peaks. Each element represents altitude (0 = flat ground; higher value = higher altitude). A mountain peak is defined as a position where both left and right neighbors have lower altitudes. The first and last positions also count as peaks if they meet the condition.*

---

### 🎃 输入输出 (Input/Output)

- **输入 (Input):** 一个整数数组  
  > *An integer array*

- **输出 (Output):** 符合条件的山峰个数  
  > *The count of positions that qualify as mountain peaks*

---

This is the complete question, input, and output information visible in the provided page excerpt.

---

**Python 语言思路**

1. 遍历数组，对于每个位置，判断其是否满足山峰的条件：
   - 判断条件1：是数组的第一个位置（即i==0），或者arr[i]大于arr[i-1]，表示当前位置的海拔高度高于左边的位置。
   - 判断条件2：是数组的最后一个位置（即i==n-1），或者arr[i]大于arr[i+1]，表示当前位置的海拔高度高于右边的位置。

2. 如果当前位置满足山峰的条件，则将山峰个数加一。

3. 返回最终的山峰个数作为函数的输出。

---

**整体思路是通过遍历数组，判断每个位置是否满足山峰的条件，
"""



def countPeaks(arr):
    n = len(arr)
    peaks = 0
    for i in range(n):
        # 判断是否为山峰
        if (i == 0 or arr[i] > arr[i-1]) and (i == n-1 or arr[i] > arr[i+1]):
            peaks += 1
    return peaks

# 示例输入
arr = list(map(int, input().strip().split(',')))
# 调用函数计算山峰个数
result = countPeaks(arr)
# 输出结果
print(result)
