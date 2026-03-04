"""
The problem requires finding the **minimum number of swaps** needed to group all integers in an array that are **less than K** together, **adjacent** to each other (but their exact position in the array does not matter, only that they are grouped).

### Python Language Thought Process:

1. **Count the number of elements less than K** in the array. Let's call this `count`.
2. **Find the maximum number of consecutive elements less than K** in the array. This is the largest window of such elements that are already grouped.
3. **The minimum number of swaps needed** is the difference between the total number of such elements and the size of the largest such window. That is:  
   `minimum_swaps = count - max_consecutive_count`

### Example Walkthrough:

Let’s take an example:

- Input array: `[3, 1, 2, 4, 5]`
- Input K: `3`

**Step 1:** Count the number of elements less than `3`:  
`[1, 2]` → count = 2

**Step 2:** Find the maximum number of consecutive elements less than `3`:  
In the array, the sequence `[1, 2]` is the largest such group → max_consecutive_count = 2

**Step 3:** Minimum swaps = `2 - 2 = 0`

So, **no swaps** are needed since the elements less than `K` are already grouped together.

"""

def min_swaps_to_group_less_than_k(arr, k):
    # 统计小于K的元素个数
    count = sum(1 for num in arr if num < k)

    # 如果count为0，说明没有小于K的元素，不需要交换
    if count == 0:
        return 0

    # 初始化窗口中大于等于K的元素个数
    bad = sum(1 for num in arr[:count] if num >= k)

    # 初始化最小交换次数为当前窗口中大于等于K的元素个数
    min_swaps = bad

    # 滑动窗口遍历数组
    for i in range(len(arr) - count):
        # 移出窗口的元素
        if arr[i] >= k:
            bad -= 1
        
        # 加入窗口的元素
        if arr[i + count] >= k:
            bad += 1

        # 更新最小交换次数
        min_swaps = min(min_swaps, bad)

    return min_swaps

# 输入数据
arr = list(map(int, input().split()))
k = int(input())

# 计算并输出最少交换次数
print(min_swaps_to_group_less_than_k(arr, k))

