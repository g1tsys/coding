
"""
> **Question Translation:**  
On a straight road, there are N streetlights installed, starting from position 0, with a fixed distance of 100 meters between each. Each streetlight has its own illumination radius. Calculate the total length of the areas that are **not illuminated** between the **first** and **last** streetlight.

---
> **Python Language Thought Process (Translated):**  

1. **Calculate the total road length:**  
   The total length of the road between the first and last streetlight is `(N - 1) * 100` meters.
2. **Determine the illuminated intervals:**  
   For each streetlight, calculate the **start** and **end** of its illumination range. For example, if a streetlight is at position `i * 100` and has a radius `r`, the illuminated range is `[i * 100 - r, i * 100 + r]`.
3. **Sort the intervals:**  
   Sort the intervals by their starting point to prepare for merging overlapping intervals.
4. **Merge overlapping intervals:**  
   Iterate through the intervals and merge overlapping or adjacent intervals into a single continuous interval.
5. **Calculate the total illuminated length:**  
   Sum up the lengths of the merged illuminated intervals.
6. **Calculate the unlit length:**  
   Subtract the total length of the illuminated intervals from the total road length.
7. **Handle edge cases:**  
   If the total illuminated length is greater than or equal to the total road length, the unlit length is `0`.
8. **Return the result:**  
   Return the calculated unlit length as the final result.

---

> **Example Walkthrough (N = 3, Radii = [50, 100, 50]):**  
- **Positions of streetlights:** 0, 100, 200  
- **Illumination ranges:**  
  - Light 1: [-50, 50]  
  - Light 2: [0, 200]  
  - Light 3: [150, 250]  

- **Merged illuminated intervals:** [ -50, 250 ]  
- **Total road length:** (3 - 1) * 100 = 200 meters  
- **Unlit length:** 200 - (250 - (-50)) = 200 - 300 = **-100** → Since negative, it means **the entire road is illuminated**.

"""




def unlit_distance(N, radii):
    # 初始化未照明区域的总长度为公路总长度
    total_length = (N - 1) * 100

    # 初始化被照明区间的起点和终点列表
    intervals = []

    # 对于每个路灯，计算其照明的起点和终点，添加到区间列表中
    for i in range(N):
        # 确保照明的起点不小于公路的起始点
        start = max(0, i * 100 - radii[i])
        # 确保照明的终点不大于公路的终点
        end = min((N - 1) * 100, i * 100 + radii[i])
        intervals.append((start, end))

    # 按照区间的起点排序，以便后续合并区间
    intervals.sort()

    # 初始化当前处理的区间为第一个路灯的区间
    current_start, current_end = intervals[0]

    # 遍历排序后的区间，合并重叠的区间
    for i in range(1, N):
        start, end = intervals[i]
        # 如果下一个区间与当前处理的区间重叠，更新当前区间的终点为二者的较大值
        if start <= current_end:
            current_end = max(current_end, end)
        else:
            # 如果不重叠，说明前一个区间结束，计算其长度并从总长度中减去
            total_length -= (current_end - current_start)
            # 然后更新当前处理的区间为下一个区间
            current_start, current_end = start, end

    # 处理完所有区间后，还需要减去最后一个区间的长度
    total_length -= (current_end - current_start)

    # 返回未照明区域的总长度
    return total_length

N = int(input())
radii = list(map(int, input().split()))

# 调用函数，并输出未照明区域的总长度
print(unlit_distance(N, radii))

