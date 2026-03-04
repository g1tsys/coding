"""
## Translation

This appears to be a **sliding window algorithm** problem in Chinese. Here's the translation:

### Problem Statement
Given a list `selected_elements` containing `screen_count` sub-arrays, where each sub-array represents elements on a screen.

### Algorithm Description

1. **Initialize** a list `selected_elements` with `screen_count` sub-arrays, each representing elements on a screen.
2. **Initialize** a list `list_indices`, where element values are initially set to 0, used to track the index position of the next element to be selected in each list.
3. **Initialize** a variable `total_selected` to 0, used to record the total number of elements already selected.
4. **Enter a loop**, iterating through each window until all elements in all lists have been selected.
5. **During iteration**, for each window, if the current window has already selected more than half of the elements (window size is large), skip this window.
6. **For each window**, select one element from each input list (if there are unselected elements). Iterate through all input lists and select the next element based on the list's index `list_index`.
7. **If** the current list still has unselected elements, add that element and increment the index for that list.
8. **Update** the index for that list to point to the next element.
9. **Update** the total selected element count.
10. **If** the current window has selected more than half of the elements (window size is large) or elements are exhausted (i.e., selected element count is greater than or equal to window size), then jump out of the inner loop.
11. **If** elements have been selected that exceed half of the window (i.e., selected elements count is greater than window count multiplied by window size), then jump out of the outer loop.
12. **Combine** all selected elements from all windows into a single list and return this list as the result.
13. **Convert** the result to a string, format and partition the list, then print the result.

---

## Example Walkthrough

Let's say we have:
- `screen_count = 3` (3 screens)
- `selected_elements = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]`
- Window size = 2

**Initial state:**
- `list_indices = [0, 0, 0]`
- `total_selected = 0`

**Iteration 1 (Window 1):**
- Select from list 0: element `1` (index becomes 1)
- Select from list 1: element `4` (index becomes 1)
- Select from list 2: element `6` (index becomes 1)
- Window 1 elements: `[1, 4, 6]` (3 elements selected, exceeds window size/2)

**Iteration 2 (Window 2):**
- Select from list 0: element `2` (index becomes 2)
- Select from list 1: element `5` (index becomes 2)
- Select from list 2: element `7` (index becomes 2)
- Window 2 elements: `[2, 5, 7]`

**Continue until all elements are distributed...**

**Final result:** All elements combined and returned as a single list: `[1, 4, 6, 2, 5, 7, 3, 8, 9]`

"""


def select_diverse_elements(screen_count, window_size, element_lists):
    # 创建一个列表，其中包含screen_count个子列表，每个子列表代表一个屏幕上的元素
    selected_elements = [[] for _ in range(screen_count)]
    # 初始化一个列表来跟踪每个输入列表的索引，开始都是0
    list_indices = [0] * len(element_lists)
    # 记录已经选中的元素总数
    total_selected = 0

    # 继续选择元素直到填满所有窗口或所有列表中的元素都已选择
    while total_selected < screen_count * window_size:
        # 遍历每个屏幕
        for screen_index in range(screen_count):
            # 如果当前屏幕已经选择了足够多的元素，则继续下一个屏幕
            if len(selected_elements[screen_index]) >= window_size:
                continue
            # 从每个输入列表中选择一个元素（如果还有未选择的元素）
            for list_index, element_list in enumerate(element_lists):
                # 如果当前列表还有未选择的元素
                if list_indices[list_index] < len(element_list):
                    # 选中当前列表的下一个元素，并将其加入到当前屏幕的列表中
                    selected_elements[screen_index].append(element_list[list_indices[list_index]])
                    # 更新该列表的索引，向前移动一位
                    list_indices[list_index] += 1
                    # 更新总选择元素计数
                    total_selected += 1
                    # 如果当前屏幕已经选择足够多元素或总元素已足够，则不再继续选择
                    if len(selected_elements[screen_index]) >= window_size or total_selected >= screen_count * window_size:
                        break
            # 如果已经选择足够多元素，则不再继续选择
            if total_selected >= screen_count * window_size:
                break

    # 将所有屏幕上选中的元素合并成一个单一的列表
    result = [item for sublist in selected_elements for item in sublist]
    return result

# 下面我们将实际进行输入和输出操作
screen_count = int(input().strip())  # 输入屏幕数量，例如4
window_size = int(input().strip())  # 输入每个屏幕窗口大小，例如7
element_lists = []

# 循环读取剩余的输入行，每行代表一个屏幕上的元素列表
while True:
    try:
        line = input().strip()
        if line == "":  # 如果读取到空行，则停止读取
            break
        # 将读取的行分割成数字，并添加到element_lists中
        element_lists.append(list(map(int, line.split())))
    except EOFError:  # 如果遇到文件结束标志，则停止读取
        break

# 调用函数选择元素，并将结果打印出来
result = select_diverse_elements(screen_count, window_size, element_lists)
print(' '.join(map(str, result)))
