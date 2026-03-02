"""
### Problem Description
To celebrate the 100th anniversary of the founding of the Communist Party of China, a park will hold multiple cultural performances. Many shows start simultaneously, and a person can only watch one show at a time without arriving late or leaving early. Since the venues are in different locations, there must be at least a **15-minute interval** between consecutive shows.

Xiao Ming is an avid fan of the arts and wants to watch as many shows as possible. Given the performance schedule, help Xiao Ming calculate the maximum number of shows he can attend.

---

### Input and Output

#### Input
- The first line contains an integer `N`, representing the number of shows (1 ≤ N ≤ 1000).
- The next `N` lines each contain two integers separated by a space:
  - The first integer `T` is the start time of the show (in minutes, 0 ≤ T ≤ 1440).
  - The second integer `L` is the duration of the show (in minutes, 0 ≤ L ≤ 100).

#### Output
Output the maximum number of shows Xiao Ming can attend.

---

Would you like me to also translate the corresponding solution approach for this problem?

# Python Language Approach
1. Read the number of performances `N` from the input, and create a list `performs` to store the start time and duration of each performance.
2. Use a loop to read the start time and duration of each performance, and add them to the `performs` list as tuples `(start, duration)`.
3. Sort the `performs` list based on the end time of each performance, which is calculated as `start + duration`. This sorting ensures that when selecting performances, we prioritize those that end earlier, leaving more time for subsequent performances.
4. Initialize a counter `count` to 0, which is used to record the number of performances that can be watched.
5. Initialize `last_moment` to 0, representing the time point after the last watched performance.
6. Iterate through each performance. For each performance, check if its start time is greater than or equal to `last_moment`. If so, it means this performance can be watched.
7. If the performance can be watched, increment the counter `count` by 1, and update `last_moment` to the end time of the current performance plus 15 minutes, i.e., `start + duration + 15`, which represents the earliest time when the next watchable performance can start after the current one.
8. Finally, output the value of the counter `count`, which is the maximum number of performances Xiao Ming can watch.

---

Would you like me to also provide the full Python code implementation for this problem?
"""


def main():
    N = int(input())  # 读取演出场数
    performs = []  # 存储演出开始时间和持续时间的列表

    # 读取每场演出的开始时间和持续时间，并添加到performs列表中
    for _ in range(N):
        start, duration = map(int, input().split())
        performs.append((start, duration))

    # 按照表演结束时间对performs列表进行排序
    performs.sort(key=lambda x: x[0] + x[1])

    count = 0  # 计数器，记录能观看的演出场数
    last_moment = 0  # 上一次观看的时刻

    # 遍历每场演出
    for perform in performs:
        if perform[0] >= last_moment:  # 如果演出的开始时间晚于或等于上一场演出的结束时间，可以观看该演出
            count += 1  # 计数器加1
            last_moment = perform[0] + perform[1] + 15  # 更新上一次观看的时刻为当前演出的结束时间加上15分钟

    print(count)  # 输出最多能观看的演出场数


if __name__ == "__main__":
    main()

