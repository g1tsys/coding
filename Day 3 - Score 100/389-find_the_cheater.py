"""
题目描述
公司组织了一次考试,在结果出来之后想看一下有没有人作弊,但是员工太多了,所以需要对员工进行筛选,再确
认是不是真的作弊,现在有如下规则:找到分数差最小的员工ID对(p1,p2)列表,p1<p2
输入输出 区
输入
员工ID和考试分数
输出
分数差最小的员工ID对(p1,p2)列表,每一行集合内的员工ID按顺序排列,多行结果也以员工ID对中p1大小升序排列
(p1相同就按p2升序)

# 解题步骤思路（清晰易懂版）
我把这道题的解题逻辑拆成**6个核心步骤**，每一步都对应代码的作用，你一看就能理解：

## 步骤1：读取输入数据
- 先输入员工总人数
- 循环读取每一行的**员工ID**和**考试分数**
- 把所有员工信息存成列表：`[(ID1, 分数1), (ID2, 分数2), ...]`

## 步骤2：按分数从小到大排序
- 对员工列表**只按照分数排序**，ID不参与排序
- 目的：让分数接近的员工挨在一起，方便计算最小差值
  ✅ 排序后：分数从小到大，相邻两个员工的分数差一定是最小候选值

## 步骤3：计算最小分数差
- 遍历排序后的列表，只计算**相邻两个员工**的分数差
- 记录下所有差值里**最小的那个值**（min_diff）

## 步骤4：分两种情况找符合条件的ID对
### 情况A：最小差值 = 0（分数完全相同）
- 把所有**分数一样**的员工分到同一组
- 对每组员工ID先从小到大排序
- 生成所有满足 `p1 < p2` 的组合（比如ID [1,3,5] → (1,3)(1,5)(3,5)）

### 情况B：最小差值 > 0（分数不同）
- 只看排序后**相邻**的员工对
- 筛选出分数差 = 最小差值的对
- 把每对ID整理成 `(小ID, 大ID)` 格式

## 步骤5：对结果排序（满足题目输出要求）
- 所有ID对按照规则排序：
  1. 先按第一个ID（p1）升序
  2. p1相同，按第二个ID（p2）升序

## 步骤6：输出结果
- 逐行打印每一对符合条件的员工ID

---

# 极简总结（核心逻辑）
1. **排序分数** → 让相近分数挨在一起
2. **算最小差** → 找到最小的分数差距
3. **找对应对** → 分数相同全组合，不同只看相邻
4. **排序输出** → 按ID规则打印

这个思路完全贴合题目要求，也是最高效、最不容易出错的解法。
"""

# 读取输入的员工数量
n = int(input())

# 初始化一个列表来存储员工的信息，每个元素是(id, score)的元组
employees = []

# 读取每个员工的ID和分数
for _ in range(n):
    parts = input().split()
    employee_id = int(parts[0])
    score = int(parts[1])
    employees.append((employee_id, score))

# 按分数排序，便于计算相邻差值
employees.sort(key=lambda x: x[1])

# 初始化最小差值为一个很大的数
min_diff = float('inf')
# 存储所有分数差等于最小差值的员工对
result_pairs = []

# 遍历所有相邻员工，计算分数差并更新最小差值
for i in range(len(employees) - 1):
    current_diff = employees[i+1][1] - employees[i][1]
    if current_diff < min_diff:
        min_diff = current_diff

# 如果最小差值为0，说明存在多个分数相同的员工，需要输出所有组合
if min_diff == 0:
    # 找出所有分数相同的员工组
    from collections import defaultdict
    score_groups = defaultdict(list)
    for emp_id, score in employees:
        score_groups[score].append(emp_id)
    
    # 对每个分数相同的组，生成所有可能的p1 < p2的组合
    for group in score_groups.values():
        group_sorted = sorted(group)
        for i in range(len(group_sorted)):
            for j in range(i + 1, len(group_sorted)):
                result_pairs.append((group_sorted[i], group_sorted[j]))
else:
    # 如果最小差值不为0，只考虑相邻员工对
    for i in range(len(employees) - 1):
        current_diff = employees[i+1][1] - employees[i][1]
        if current_diff == min_diff:
            pair = (min(employees[i][0], employees[i+1][0]), max(employees[i][0], employees[i+1][0]))
            result_pairs.append(pair)

# 对结果列表按p1升序、p2升序排序
result_pairs.sort()

# 输出结果
for pair in result_pairs:
    print(pair[0], pair[1])

