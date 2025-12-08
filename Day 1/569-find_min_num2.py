"""
> **Question Translation:**  
Given an integer array, select 3 elements from it to form the smallest possible number and output it. If the array length is less than 3, use all the elements to form the smallest number.

---

> **Python Thought Process Translation:**  
1. First, we import the `permutations` function from the `itertools` module, which is used to generate all possible permutations of the array.  
2. Define a function `find_min_number` that takes an array as input and returns the smallest number formed from it.  
3. Inside the function, sort the array to ensure we start with the smallest elements.  
4. Use `permutations` to generate all possible permutations of the first three elements.  
5. Initialize `min_num` as a very large number (`float('inf')`) to compare and update the minimum value.  
6. Iterate over all the permutations, convert each permutation into a number, and compare it with the current minimum.  
7. Finally, return the smallest number as a string.

---

> **Example Walkthrough:**  
Let's take the input array: `[1, 2, 3, 4, 5]`  
- Step 1: Sort the array → `[1, 2, 3, 4, 5]`  
- Step 2: Generate all permutations of the first three elements → `(1, 2, 3)`, `(1, 3, 2)`, `(2, 1, 3)`, etc.  
- Step 3: Convert each permutation to a number (e.g., `123`, `132`, `213`)  
- Step 4: Find the smallest number → `123`  

Thus, the final output is: **123**.
"""
from itertools import permutations

def find_min_number(nums):
    nums.sort()  # 对数组进行排序
    permutations_list = list(permutations(nums[:3]))  # 取前三个元素的全排列
    min_num = float('inf')  # 初始化最小数字为正无穷大
    for perm in permutations_list:
        num = int(''.join(map(str, perm)))  # 将排列转换为数字
        min_num = min(min_num, num)  # 更新最小数字
    return str(min_num)

# 输入处理
input_str = input().strip()
nums = list(map(int, input_str.split(',')))

# 输出最小数字
min_number = find_min_number(nums)
print(min_number)
