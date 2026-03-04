"""
Here's the extracted and translated content from the screenshot and webpage:

---

### **Problem Statement (Translated)**

**Title**: Attendance Information

**Description**:  
A company uses a string to represent employee attendance records:
- `absent`: Absent
- `late`: Late
- `leaveearly`: Left early
- `present`: Present (on time)

Determine if the employee qualifies for an attendance award based on the following conditions:
1. No more than **one absence**.
2. **No consecutive** late or early departures.
3. In **any consecutive 7 attendance records**, no more than **3** absences, late arrivals, or early departures.

---

### **Input/Output**

**Input**:  
A string of attendance records (length < 10,000, ≥ 1 record).  
Example:  
```
2
present present absent present present leaveearly present absent
```

**Output**:  
- `"true"` if the employee qualifies for the award.  
- `"false"` otherwise.  
Example output for the above input:  
```
true
false
```

---

### **Python Logic (Translated from Screenshot)**

1. Split the input attendance string into individual elements (each representing one attendance record).
2. Iterate through each element and maintain:
   - `absentCnt`: Count of absences (initialized to 0).
   - `lastLateOrEarly`: Position of the last late/early departure (initialized to -1).
   - `flag`: Boolean to track if award conditions are already violated (initialized to `False`).
3. For each element:
   - If it’s `absent`: Increment `absentCnt`. If `absentCnt > 2`, output `"false"` and set `flag = True` to break the loop.
   - If it’s `late` or `leaveearly`:
     - If `lastLateOrEarly == -1` (first occurrence), update `lastLateOrEarly` to current position.
     - Else, if current position is **consecutive** to `lastLateOrEarly` (difference = 1), output `"false"` and set `flag = True` to break.
     - Else, update `lastLateOrEarly` to current position.
   - Check if the last 7 records violate condition #3 (call `judge7C` function). If violated, output `"false"` and break.
4. If no violations found, output `"true"`.
5. Store results in a list and output as space-separated string.

---

Let me know if you’d like the full code implementation in Python, C++, or Java!
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


