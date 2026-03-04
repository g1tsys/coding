"""
# Problem Translation and Solution
## Problem Description

Given a group of non-negative integers `nums`, rearrange the order of each number (each number cannot be split) to form the largest possible integer.
**Note:** The output result may be very large, so you need to return a string instead of an integer.
---

## Python Approach & Thought Process

### Key Insights:

1. **String Conversion**: Convert all numbers to strings for easier comparison and concatenation.
2. **Custom Sorting**: The core idea is to sort numbers based on which concatenation produces a larger result. For two numbers `a` and `b`, compare `a+b` vs `b+a`. If `a+b > b+a`, then `a` should come before `b`.
3. **Edge Case Handling**: If all numbers are zeros, the result should be "0" instead of "000...".
4. **Concatenation**: After sorting, join all strings together to form the final result.

---

## Example Walkthrough

**Input:** `nums = [3, 30, 34, 5, 9]`

### Step-by-step process:

1. **Convert to strings:** `["3", "30", "34", "5", "9"]`

2. **Custom sorting comparison:**
   - Compare "3" and "30": "330" vs "303" → "330" > "303", so "3" comes first
   - Compare "3" and "34": "334" vs "343" → "343" > "334", so "34" comes first
   - Compare "3" and "5": "35" vs "53" → "53" > "35", so "5" comes first
   - Compare "3" and "9": "39" vs "93" → "93" > "39", so "9" comes first

3. **After sorting:** `["9", "5", "34", "3", "30"]`

4. **Concatenate:** `"9534330"`

**Output:** `"9534330"`

**Time Complexity:** O(n log n) for sorting  
**Space Complexity:** O(n) for storing string representations
"""


from functools import cmp_to_key  # 导入cmp_to_key，用于将比较函数转换为键函数

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]  # 输入类型是一个整型列表
        :rtype: str  # 输出类型是一个字符串
        """
        # 将每个整数转换为字符串
        nums_str = list(map(str, nums))  # 将整数列表转换为字符串列表
        
        # 自定义排序函数，使用lambda表达式
        # cmp_to_key将比较函数转换为键函数
        # lambda x, y: (y + x > x + y) - (y + x < x + y)
        # 如果 y + x > x + y, 则返回1, 表示y应该排在x前面
        # 如果 y + x < x + y, 则返回-1, 表示x应该排在y前面
        # 如果 y + x == x + y, 则返回0, 表示x和y位置不变
        nums_str.sort(key=cmp_to_key(lambda x, y: (y + x > x + y) - (y + x < x + y)))
        
        # 将排序后的字符串列表拼接成一个结果字符串
        result = ''.join(nums_str)  # 使用join将列表中的字符串连接起来
        
        # 处理特殊情况：如果结果的第一个字符是'0'
        # 例如输入[0, 0]，排序后仍然是[0, 0]，结果会是'00'
        # 我们需要将结果转换为'0'
        return '0' if result[0] == '0' else result  # 如果第一个字符是'0'，返回'0'，否则返回结果字符串
