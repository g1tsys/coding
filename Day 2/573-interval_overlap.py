"""
### Problem Description
Given a set of line segments on a coordinate axis, where the start and end points of each segment are integers and the length is not 1, find the **minimum number of segments** required to cover all the given segments.

---

### Input and Output

#### Input
- The first line contains an integer `N`, the number of segments (N ≤ 10000).
- The next `N` lines each represent a segment in the format "x, y", where `x` is the start point and `y` is the end point. The values of `x` and `y` are in the range [-10⁵, 10⁵].

#### Output
Output the minimum number of segments required, which is a positive integer.

---

Would you like me to also translate the corresponding solution approach for this problem?

# Python Language Approach
This problem can be transformed into finding the minimum number of segments such that they can cover all the given segments.

1.  **Sorting Strategy**: First, sort all the given segments by their starting point. If two segments have the same starting point, sort them by their ending point. This ensures we always consider the leftmost segments first.
2.  **Greedy Coverage**: Iterate through the sorted segments:
    - If a segment starts after the end of the current coverage, it means a new segment must be selected to cover this one. Increment the count and update the coverage end to this segment's end.
    - If a segment is entirely within the current coverage, it is already covered and can be skipped.
    - If a segment starts before the current coverage end but extends beyond it, it overlaps with the current coverage. We need to find the segment that starts at or before the current coverage start and has the maximum end, update the coverage end to this maximum, and increment the count.

The specific steps are as follows:

1.  Read the number of segments `n`.
2.  Create an empty 2D list `data` to store the start and end points of the segments.
3.  Loop `n` times. For each iteration, read a segment's start point `a` and end point `b`. Sort `a` and `b` and add them to `data`.
4.  Sort the `data` list by the starting point of the segments. If starting points are equal, sort by the ending point.
5.  Initialize `start` to a very small value, `end` to a value smaller than `start`, and the answer `ans` to 0.
6.  Traverse the sorted data. For each segment `[a, b]`:
    - If `a > end`, this segment can cover the previous one. Update `end` to `b` and increment `ans`.
    - If `b <= end`, this segment is already covered, so skip it.
    - If `a < end`, this segment overlaps with the previous coverage. Find the segment with the maximum end point that starts at or before the current coverage start, update `end` to this maximum end point, and increment `ans`.
7.  Output `ans`, which is the minimum number of segments required.

---

Would you like me to also provide the full Python code implementation for this problem?
"""


n = int(input())  # 输入线段的数量
data = []  # 存储线段的起点和终点
for i in range(n):
    a, b = map(int, input().split(','))  # 输入线段的起点和终点
    if a > b:
        a, b = b, a  # 将起点和终点按照从小到大的顺序排序
    data.append([a, b])  # 将起点和终点添加到data中
data.sort(key=lambda x: (x[0], x[1]))  # 对线段进行排序，按照起点升序排列，起点相同的情况下按照终点升序排列

start = -100005  # 初始化起点
end = -100004  # 初始化终点
ans = 0  # 初始化答案，即最少线段数量
for i in range(n):
    if data[i][0] >= end:  # 如果当前线段的起点大于等于终点，说明这个线段可以覆盖住之前的线段
        while i + 1 < n and data[i + 1][0] == data[i][0]:  # 如果下一个线段的起点和当前线段的起点相等，则继续往下找
            i += 1
        end = data[i][1]  # 更新终点为当前线段的终点
        ans += 1  # 答案加1，表示找到了一个线段
        continue
    else:
        if data[i][1] <= end:  # 如果当前线段的终点小于等于终点，说明这个线段已经被之前的线段覆盖了，直接跳过
            continue
        else:
            ma = data[i][1]  # 初始化一个最大值，用来记录当前线段和之后线段的最大终点
            while i + 1 < n and data[i + 1][0] <= end:  # 如果下一个线段的起点小于等于终点，则继续往下找
                ma = max(ma, data[i + 1][1])  # 更新最大值为当前线段和下一个线段终点的较大值
                i += 1
            end = ma  # 更新终点为最大值
            ans += 1  # 答案加1，表示找到了一个线段
print(ans)  # 输出最少线段数量

