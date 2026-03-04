"""
# Log Collection System - Maximum Points on First Report

## Problem Translation

**Description:**
A log collection system generates logs line by line, with each line being one entry. The system reports logs in batches with the following rules:

1. **+1 point** for each log successfully reported
2. **-1 point** for each log delayed by 1 second
3. **Must report immediately** when accumulated logs reach 100 entries

Given a sequence of logs generated over time, calculate the maximum points achievable on the first report.

**Input:**
- A sequence of log counts T1, T2, ..., Tn generated at each second
- Where 1 ≤ n ≤ 1000, 0 ≤ Ti ≤ 100

**Output:**
- Maximum points achievable on first report

---

## Python Solution Approach

**Key Insights:**

1. **Score Calculation:** If we report at second `i`:
   - Gain: `total_logs` points (one per log)
   - Loss: Each log waits from when it was generated until second `i`
   - Net score = `total_logs - accumulated_wait_time`

2. **Wait Time Tracking:** A log generated at second `j` and reported at second `i` waits `(i - j)` seconds

3. **Strategy:** Try reporting at each possible second and find maximum score

```python
def max_score_first_report(logs):
    n = len(logs)
    max_score = float('-inf')
    
    total_logs = 0      # Accumulated logs
    wait_penalty = 0    # Accumulated wait time penalty
    
    for i in range(n):
        total_logs += logs[i]
        
        # Calculate score if we report now
        # Score = total_logs (gain) - wait_penalty (loss)
        current_score = total_logs - wait_penalty
        max_score = max(max_score, current_score)
        
        # If we reach 100 logs, must report immediately
        if total_logs >= 100:
            break
        
        # If we don't report, all current logs wait 1 more second
        wait_penalty += total_logs
    
    return max_score

# Read input
logs = list(map(int, input().split()))
print(max_score_first_report(logs))
```

---

## Example Walkthrough

**Example Input:** `1 98 1`

**Step-by-step:**

| Second | New Logs | Total Logs | Wait Penalty | Score if Report Now | Action |
|--------|----------|------------|--------------|---------------------|---------|
| 0 | 1 | 1 | 0 | 1 - 0 = **1** | Continue |
| 1 | 98 | 99 | 1 | 99 - 1 = **98** | Continue |
| 2 | 1 | 100 | 99 + 99 = 198 | 100 - 198 = **-98** | Must report (≥100) |

**Analysis:**
- Second 0: 1 log, no wait → score = 1
- Second 1: 99 total logs, 1 log waited 1 sec → score = 99 - 1 = 98 ✓ **Best**
- Second 2: 100 logs (forced report), all previous logs waited → score = -98

**Output:** `98`

---

**Another Example:** `10 10 10 10 10`

| Second | Logs | Total | Wait | Score | Max |
|--------|------|-------|------|-------|-----|
| 0 | 10 | 10 | 0 | 10 | 10 |
| 1 | 10 | 20 | 10 | 10 | 10 |
| 2 | 10 | 30 | 30 | 0 | 10 |
| 3 | 10 | 40 | 60 | -20 | 10 |
| 4 | 10 | 50 | 100 | -50 | 10 |

**Output:** `10` (report at second 0 or 1)
"""

logs = list(map(int, input().split()))  # 输入日志序列

# 记录到当前秒的总条数
sum = 0

# 记录到当前秒之前的总条数
# 每一轮都会减一次
pre_sum = 0

# 记录到当前秒首次上报要减去的分数
n_score = 0

# 记录到首次上报的最大得分
max_score = 0

for i in range(len(logs)):
    pre_sum = sum
    sum += logs[i]
    # 还有个100条的限制
    if sum >= 100:
        sum = 100
        n_score += pre_sum
        max_score = max(max_score, sum - n_score)
        break
    n_score += pre_sum
    max_score = max(max_score, sum - n_score)

print(max_score)
