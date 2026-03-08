"""
**题目问题：**  
在跳房子游戏中，给定一个步数数组 `steps` 和房子总格数 `count`，需找出**两个不同回合**的步数组合（不可重复使用同一元素），使其和等于 `count`，并返回**索引和最小**的组合（保持原数组顺序）。

---

**输入输出样本：**

> **样例1**  
> 输入：  
> `steps = [1, 2, 3, 4]`  
> `count = 5`  
> 输出：  
> `[1, 4]`  
> *说明：1+4=5，索引和=0+3=3，是所有满足条件中最小的。*

> **样例2**  
> 输入：  
> `steps = [2, 7, 11, 15]`  
> `count = 9`  
> 输出：  
> `[2, 7]`  
> *说明：2+7=9，索引和=0+1=1，唯一且最小。*

---

```text
Python 语言思路

1. 创建一个空的结果列表 results，用于存储已找到的步数组合及其索引之和。
2. 使用双重循环遍历数组中所有可能的两步组合。外层循环控制第一个步数的索引，内层循环控制第二个步数的索引，并确保不重复使用相同的步数。
3. 在循环内部，检查当前步数组合是否满足要求，即判断 steps[i] + steps[j] 是否等于 count。
4. 如果满足要求，将组合及其索引和添加到结果列表 results 中。使用元组来存储组合和索引之和，即 results.append((steps[i], steps[j], i + j))。索引从 1 开始计数，所以需要加 2。
5. 循环结束后，如果结果列表 results 不为空，说明存在满足条件的组合。
6. 在 results 中找到索引和最小的步数组合，即 min(results, key=lambda x: x[2])，min_sum_index = min(results, key=lambda x: x[2])。
7. 返回索引和最小的步数组合，即 min_sum_index[0], min_sum_index[1]。
8. 如果结果列表 results 为空，说明没有满足条件的组合，返回空列表。

"""
Python 代码
def find_min_steps_combination(steps, count):
    # 存储已找到的步数组合及其索引之和
    results = []
    for i in range(len(steps)):
        for j in range(i + 1, len(steps)):  # 确保不重复使用相同的步数
            # 检查当前步数组合是否满足要求
            if steps[i] + steps[j] == count:
                # 添加组合及其索引和（索引从1开始，所以加2）
                results.append((steps[i], steps[j], i + j + 2))
    # 如果没有找到满足条件的组合，返回空列表
    if not results:
        return []
    # 找到索引和最小的组合
    min_sum_index = min(results, key=lambda x: x[2])
    # 返回步数组合
    return [min_sum_index[0], min_sum_index[1]]
