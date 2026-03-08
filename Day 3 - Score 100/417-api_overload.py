"""
Here's the extracted **input** and **output** specification from the problem:

---

**Input:**
- First line: `N` (number of access log entries, where `0 < N <= 100`)
- Next `N` lines: Each contains a RESTful API URL (only letters and `/`, max 10 levels, each level max 10 chars)
- Last line: Two values — `L` (target level) and `keyword` (case-sensitive string to search for)

**Output:**
- A single integer: the **frequency** of the exact match of `keyword` at level `L` across all URLs (0 if never appears)

---

> **Note**: Levels are 1-indexed (e.g., in `/A/B/C`, `A` is level 1, `B` is level 2, etc.). Match is **case-sensitive** and **exact**.

The image contains a Python code snippet with comments in Chinese. Here is the extracted and translated content:

---

**Python Code:**

```python
def count_api_frequency(n, api_logs, l, keyword):
    # Initialize frequency count to 0
    count = 0
    # Iterate through each API log
    for api_log in api_logs:
        # Split the API log by '/' to get the levels
        levels = api_log.split('/')
        # Check if the number of levels is greater than or equal to the target level
        if len(levels) >= l:
            # Check if the level at index (l-1) matches the keyword
            if levels[l-1] == keyword:
                # Increment count if there's a match
                count += 1
    # Return the final count
    return count
```

---

**Translated Comments:**

1. First, define a function `count_api_frequency` to count the frequency of API access.
2. In `count_api_frequency`, initialize the count to 0.
3. Iterate through each API log in the list.
4. Split the API log by `/` to get the levels.
5. Check if the number of levels is greater than or equal to the target level.
6. If the level at the target index matches the keyword, increment the count.
7. Return the final count.

---

**Input Parameters:**
- `n`: Number of API logs.
- `api_logs`: List of API log strings.
- `l`: Target level (1-indexed).
- `keyword`: The string to match at the target level.

**Output:**
- The frequency of the exact match of the keyword at the specified level.
"""

def count_api_frequency(n, api_logs, l, keyword):
    """
    统计在给定层级上关键字出现的频次

    :param n: 日志条数
    :param api_logs: RESTful API 访问日志的列表
    :param l: 要查询的层级
    :param keyword: 要查询的关键字
    :return: 关键字在给定层级上出现的频次
    """
    # 初始化频次为0
    frequency = 0

    # 遍历日志列表
    for api in api_logs:
        # 将每条API日志按'/'分割成层级列表
        levels = api.strip().split('/')
        # 如果层级数大于或等于所查询的层级
        if len(levels) > l:
            # 检查对应层级的名称是否与关键字完全匹配
            if levels[l] == keyword:
                # 如果匹配，则频次加1
                frequency += 1

    # 返回最终频次
    return frequency

# 读取输入
N = int(input().strip())  # 日志条数
api_logs = []  # API 日志列表
for _ in range(N):
    api_logs.append(input().strip())  # 添加日志到列表
L, keyword = input().strip().split()  # 读取层级和关键字
L = int(L)  # 将层级转换为整数

# 计算频次并输出结果
frequency = count_api_frequency(N, api_logs, L, keyword)
print(frequency)
