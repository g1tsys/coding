"""
Here's a **translation** of the question and a **walkthrough** of the Python logic for solving the problem:

---

### 📌 Question Translation:

A company uses a string to record employee attendance. The string contains entries like:

- `absent`: Absent
- `late`: Late
- `leaveearly`: Early leave
- `present`: Present

The goal is to determine whether the employee qualifies for an attendance award based on the following rules:

1. The number of `absent`, `late`, or `leaveearly` entries must not exceed **1**.
2. There should be **no consecutive** `late` or `leaveearly` entries.
3. In **any 7 consecutive entries**, the number of `absent`, `late`, or `leaveearly` entries must not exceed **3**.

---

### 🐍 Python Language Thought Process:

To solve this problem in Python, we can follow these steps:

1. **Input Parsing**: Read the input string and split it into a list of attendance entries.
2. **Rule 1 Check**: Count the number of `absent`, `late`, and `leaveearly` entries. If the count exceeds 1, return `False`.
3. **Rule 2 Check**: Iterate through the list and ensure that there are no two consecutive `late` or `leaveearly` entries.
4. **Rule 3 Check**: Use a sliding window of size 7 to check each group of 7 consecutive entries. For each group, count the number of `absent`, `late`, or `leaveearly` entries. If any group exceeds 3, return `False`.
5. **Final Decision**: If all rules are satisfied, return `True`.

---

### 🧪 Example Walkthrough:

**Input**: `"present present absent present present leaveearly present absent"`

**Step-by-step**:

1. **Split into list**:
   ```python
   attendance = ["present", "present", "absent", "present", "present", "leaveearly", "present", "absent"]
   ```

2. **Rule 1 Check**:
   - Count of `absent`, `late`, or `leaveearly`: 2 (`absent` and `leaveearly`)
   - This is **not more than 1**, so **proceed**.

3. **Rule 2 Check**:
   - No two consecutive `late` or `leaveearly` entries. ✅

4. **Rule 3 Check**:
   - Check each group of 7 entries:
     - Group 1: `["present", "present", "absent", "present", "present", "leaveearly", "present"]` → 2 invalid entries ✅
     - Group 2: `["present", "absent", "present", "present", "leaveearly", "present", "absent"]` → 3 invalid entries ✅
   - All groups are valid. ✅

5. **Final Output**: `"true"`

---
"""


def check_attendance(records, now):
    cnt = 0
    if now < 7:  # 如果考勤记录少于7次
        for i in range(now + 1):  # 遍历当前记录之前的所有记录
            if records[i] in ["absent", "late", "leaveearly"]:
                cnt += 1  # 计算缺勤、迟到和早退的次数
    else:  # 如果考勤记录多于7次
        for i in range(now - 6, now + 1):  # 遍历最近7次的记录
            if records[i] in ["absent", "late", "leaveearly"]:
                cnt += 1  # 计算缺勤、迟到和早退的次数
    return cnt <= 3  # 如果缺勤、迟到和早退的次数不超过3次，则返回True

def main():
    cnt = int(input())  # 输入考勤记录的数量
    records = []
    for _ in range(cnt):  # 读取每一条考勤记录
        records.append(input().strip())  # 去除每条记录的首尾空格并添加到列表中

    result = []  # 用于存储每条记录的结果

    for record in records:  # 遍历每条考勤记录
        if not record:  # 如果记录为空，则跳过
            break

        split = record.split()  # 将记录按照空格分割成单词列表
        absent_cnt = 0  # 缺勤次数计数
        last_last_or_early = -1  # 上一次迟到或早退的索引
        flag = False  # 标记是否已经判定当前记录不符合条件

        for j in range(len(split)):  # 遍历记录中的每个单词
            if split[j] == "absent":
                absent_cnt += 1  # 增加缺勤次数
                if absent_cnt >= 2:  # 如果缺勤次数达到2次
                    result.append("false")  # 当前记录不符合条件
                    flag = True  # 设置标记
                    break  # 结束当前记录的检查
            elif split[j] in ["late", "leaveearly"]:
                if last_last_or_early == -1:  # 如果是第一次发现迟到或早退
                    last_last_or_early = j  # 记录索引
                else:
                    if j - last_last_or_early == 1:  # 如果连续迟到或早退
                        result.append("false")  # 当前记录不符合条件
                        flag = True  # 设置标记
                        break  # 结束当前记录的检查
                    else:
                        last_last_or_early = j  # 更新最后一次迟到或早退的索引
            if not check_attendance(split, j):  # 检查最近7次记录是否符合条件
                result.append("false")  # 当前记录不符合条件
                flag = True  # 设置标记
                break  # 结束当前记录的检查

        if not flag:  # 如果未发现任何不符合条件的情况
            result.append("true")  # 当前记录符合条件

    print(" ".join(result))  # 输出所有记录的结果

if __name__ == "__main__":
    main()  # 调用主函数


