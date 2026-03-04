"""
# Matrix Matching Problem - Translated and Organized

## Problem Description

Given an **N x M matrix** (where N ≤ M), select **N numbers** such that no two numbers are in the same row or column. Find the **minimum value** among all possible K-th largest numbers from these selections.

## Constraints

- 1 ≤ K ≤ N ≤ M ≤ 150
- Each selection must have exactly N numbers
- No two numbers can share the same row or column

## Input Format


N M K
[N x M matrix elements]


## Output

The minimum value of the K-th largest number across all valid combinations.

---

## Algorithm Steps

1. **Define `can_choose(matrix, mid, k)`** - Checks if N numbers can be selected where the K-th largest ≤ mid using depth-first search
2. **Initialize matching arrays** - Create a column matching array `match[]` (initialized to -1) to track row-column assignments
3. **Define `dfs(row, vis, match, limit)`** - Recursive function to find valid column matches for current row
4. **Column traversal logic** - For each column `col`:
   - If `matrix[row][col] ≤ limit` and column not visited
   - Mark column as visited
   - If column unmatched OR can rematch recursively → assign to current row
5. **Count valid matches** - Track number of successfully matched rows in variable `valid`
6. **Iterate through rows** - Call `dfs()` for each row, increment `valid` on success
7. **Return feasibility** - Check if `valid ≥ k` (at least K rows matched)
8. **Define `find_min_kth_element(matrix, k)`** - Main function to find the answer
9. **Extract and sort elements** - Get all unique matrix elements into sorted list `elements[]`
10. **Binary search initialization** - Set `low = 0`, `high = len(elements) - 1`
11. **Calculate midpoint** - `mid = (low + high) // 2`
12. **Check feasibility** - Call `can_choose(matrix, elements[mid], n-k+1)`
    - If valid: update `best = elements[mid]`, set `high = mid - 1`
    - If invalid: set `low = mid + 1`
13. **Iterate until convergence** - Repeat steps 11-12 until `low > high`
14. **Return result** - Output the final `best` value

15. **Main execution** - Read input, call `find_min_kth_element()`, print result

---

## Example Walkthrough

**Input:**
3 4 2
9 3 4 5
1 2 8 6
4 5 6 7


**Step-by-step:**

1. **Matrix:** 3 x 4, need to select 3 numbers (one per row, different columns), find minimum of 2nd largest

2. **Possible selections:**
   - [9, 2, 4] → sorted: [2, 4, 9] → 2nd largest = **4**
   - [9, 2, 5] → sorted: [2, 5, 9] → 2nd largest = **5**
   - [9, 8, 4] → sorted: [4, 8, 9] → 2nd largest = **8**
   - [3, 1, 6] → sorted: [1, 3, 6] → 2nd largest = **3**
   - ... (many more combinations)

3. **Binary search on unique elements:** [1, 2, 3, 4, 5, 6, 7, 8, 9]

4. **Test mid values:**
   - Test if we can select 3 numbers where 2nd largest ≤ 4
   - Use bipartite matching to verify feasibility
   - If yes, try smaller values; if no, try larger

5. **Result:** The minimum 2nd largest value across all valid selections

**Output:** `4` (or the actual minimum found)

---

This problem combines **bipartite matching** (Hungarian algorithm) with **binary search** to efficiently find the optimal answer without enumerating all combinations.
"""



# 检查是否能选出n个数，其中第k大的数不大于mid
def can_choose(matrix, mid, k):
    n = len(matrix)  # 矩阵行数
    m = len(matrix[0])  # 矩阵列数

    # 深度优先搜索用于查找是否存在满足条件的匹配
    def dfs(row, vis, match, limit):
        for col in range(m):  # 遍历列
            # 若当前元素小于等于限制值且该列未被访问
            if matrix[row][col] <= limit and not vis[col]:
                vis[col] = True  # 标记列为已访问
                # 若该列未匹配或可通过递归重新匹配其它行
                if match[col] == -1 or dfs(match[col], vis, match, limit):
                    match[col] = row  # 匹配该列到当前行
                    return True
        return False

    match = [-1] * m  # 列匹配数组，-1表示未匹配
    valid = 0  # 有效匹配的行数
    for row in range(n):  # 对每一行执行
        vis = [False] * m  # 访问标记数组
        if dfs(row, vis, match, mid):
            valid += 1  # 若成功匹配一行，则增加计数

    return valid >= k  # 返回是否至少有k行能被匹配

# 寻找矩阵中第K大的最小值
def find_min_kth_element(matrix, k):
    n, m = len(matrix), len(matrix[0])  # 矩阵的行数和列数
    elements = sorted(set(elem for row in matrix for elem in row))  # 提取矩阵中所有不重复元素并排序

    low, high = 0, len(elements) - 1  # 二分查找的上下界
    best = float('inf')  # 记录找到的最小值

    while low <= high:  # 二分查找
        mid = (low + high) // 2  # 中点
        # 检查是否存在一个组合，其中第k大的数为elements[mid]
        if can_choose(matrix, elements[mid], n - k + 1):
            best = elements[mid]  # 更新最佳结果
            high = mid - 1  # 缩小上界
        else:
            low = mid + 1  # 增大下界

    return best  # 返回最终结果


# 输入
n, m, k = map(int, input().split())  # 读取n, m, k
matrix = [list(map(int, input().split())) for _ in range(n)]  # 读取矩阵

# 处理并输出结果
result = find_min_kth_element(matrix, k)  # 调用函数计算结果
print(result)  # 输出结果
