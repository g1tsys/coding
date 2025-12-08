"""
# Translation of Problem and Python Approach

## Problem Description

A DevOps engineer has collected n log entries from a product line. The logs need to be sorted by timestamp in chronological order. The log time format is H:M:S.N where:

- **H** = hours (0-23)
- **M** = minutes (0-59)
- **S** = seconds (0-59)
- **N** = milliseconds (0-999)

**Important:** Times may not be zero-padded. For example, `01:01:01.001` could be written as `1:1:1.1`.

### Input
- First line: integer n (number of logs, 1 ≤ n ≤ 100,000)
- Next n lines: timestamps in H:M:S.N format

### Output
- Timestamps sorted in ascending order
- If two timestamps represent the same time, maintain their original input order (stable sort)

---

## Python Approach

### Thought Process

1. **Define `parse_time` function**: Parse a time string into hours, minutes, seconds, and milliseconds, returning a dictionary with this information
2. **Define `compare_logs` function**: Compare two logs to determine their chronological order
3. **Read input**: Get the number of log entries (n)
4. **Process logs**: Loop through each timestamp, parse it using `parse_time`, and store the parsed log in a list
5. **Sort logs**: Use Python's `sorted()` function with a custom comparison key to sort by time while maintaining input order for equal times
6. **Output results**: Iterate through the sorted list and print timestamps in order

---

## Example Walkthrough

### Sample Input

3
1:2:3.4
1:2:3.400
0:59:59.999


### Step-by-Step Execution

**Step 1: Parse each timestamp**
- `"1:2:3.4"` → `{h: 1, m: 2, s: 3, ms: 4}` → Total: 3,723,004 ms
- `"1:2:3.400"` → `{h: 1, m: 2, s: 3, ms: 400}` → Total: 3,723,400 ms
- `"0:59:59.999"` → `{h: 0, m: 59, s: 59, ms: 999}` → Total: 3,599,999 ms

**Step 2: Convert to milliseconds for comparison**
- Log 1: (1×3600 + 2×60 + 3)×1000 + 4 = 3,723,004 ms
- Log 2: (1×3600 + 2×60 + 3)×1000 + 400 = 3,723,400 ms
- Log 3: (0×3600 + 59×60 + 59)×1000 + 999 = 3,599,999 ms

**Step 3: Sort by total milliseconds**
- 3,599,999 ms → `"0:59:59.999"`
- 3,723,004 ms → `"1:2:3.4"`
- 3,723,400 ms → `"1:2:3.400"`

### Output

0:59:59.999
1:2:3.4
1:2:3.400


**Note:** Even though `1:2:3.4` and `1:2:3.400` look similar, they represent different times (4ms vs 400ms), so they're sorted accordingly. If they were identical, the original input order would be preserved.

"""




def parse_time(time_string, index):
    # 将时间字符串按冒号和点号进行分割
    parts = time_string.split(':') + time_string.split('.')
    h, m, s, ms = 0, 0, 0, 0

    # 解析小时、分钟、秒钟部分
    if len(parts) >= 3:
        try:
            h = int(parts[0])
            m = int(parts[1])
            s = int(parts[2])
        except ValueError:
            pass

    # 解析毫秒部分
    if len(parts) == 4:
        try:
            ms = int(parts[3])
        except ValueError:
            pass

    # 返回包含解析结果的字典
    return {
        'time_string': time_string,
        'hour': h,
        'minute': m,
        'second': s,
        'millisecond': ms,
        'index': index
    }


def compare_logs(log_a, log_b):
    # 按照时间顺序比较两个日志
    if log_a['hour'] != log_b['hour']:
        return log_a['hour'] - log_b['hour']
    if log_a['minute'] != log_b['minute']:
        return log_a['minute'] - log_b['minute']
    if log_a['second'] != log_b['second']:
        return log_a['second'] - log_b['second']
    if log_a['millisecond'] != log_b['millisecond']:
        return log_a['millisecond'] - log_b['millisecond']
    return log_a['index'] - log_b['index']


n = int(input())
logs = []

# 读取日志并解析时间
for i in range(n):
    time_string = input().strip()
    log = parse_time(time_string, i)
    logs.append(log)

# 按照时间顺序对日志进行排序
sorted_logs = sorted(logs, key=lambda log: (log['hour'], log['minute'], log['second'], log['millisecond'], log['index']))

# 输出排序后的日志时间字符串
for log in sorted_logs:
    print(log['time_string'])
