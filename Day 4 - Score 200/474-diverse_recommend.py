"""
Based on the text provided from the Huawei OD exam problem "Recommendation Diversity" (Problem 474, Paper E), here are the extracted details and the solution logic implemented in Python.

### **Question Description**
The goal is to distribute elements from multiple input lists into **N** windows (screens), where each window must contain exactly **K** elements.

**Distribution Strategy:**
1.  **Interleaving:** Elements are picked from the input lists in a round-robin fashion. You pick one element for *each* of the N windows from the first list, then one for each window from the second list, and so on.
2.  **Batching:** In each step, you attempt to take `N` elements from the current list (one for each window).
    *   If the list has enough elements, take the next `N` elements and distribute them sequentially to Window 1, Window 2, ..., Window N.
    *   If the list has fewer than `N` elements remaining, take all remaining elements and fill the first `len(remaining)` windows.
3.  **Termination:** Stop when the total number of elements collected reaches `N * K`.

**Input:**
*   Line 1: `N` (Number of windows, 1-10).
*   Line 2: `K` (Elements per window, 1-100).
*   Subsequent lines: Space-separated integers representing elements in each list. The number of lists is variable (1-10).

**Output:**
*   A single line of space-separated integers.
*   Order: All elements for Window 1, followed by all elements for Window 2, ..., up to Window N.

---

### **Thought Process (Python Logic)**

1.  **Parse Input:** Read `N` and `K`. Then read all remaining lines, splitting them into a list of lists (where each inner list is one source list of elements).
2.  **Initialize Windows:** Create `N` empty lists (or queues) to store the elements for each window.
3.  **Simulate Distribution:**
    *   Maintain a global counter `total_needed = N * K`.
    *   Maintain a pointer `current_count = 0` for how many elements we have placed.
    *   Iterate through the input lists one by one.
    *   For each list, iterate through its elements.
    *   Distribute elements to `windows[0]`, `windows[1]`, ..., `windows[N-1]`, then wrap around to `windows[0]` again if we continue taking from the same list?
    *   *Correction based on problem description:* The problem says "先从第一个列表中为每屏选择一个元素... 再从第二个列表...". This implies a specific round-robin *per list batch*.
    *   **Refined Logic:**
        *   We iterate through the source lists.
        *   For a specific source list, we take elements in chunks of `N`.
        *   Chunk 1: Take up to `N` elements. Assign 1st to Window 0, 2nd to Window 1, ..., Nth to Window N-1.
        *   Chunk 2: Take next `N` elements. Assign 1st to Window 0, etc.
        *   Repeat until the source list is exhausted or we have filled all `N * K` slots.
4.  **Stop Condition:** As soon as `total_count == N * K`, stop processing.
5.  **Format Output:** Flatten the list of windows: `windows[0] + windows[1] + ... + windows[N-1]` and print space-separated.

---

### **Python Code**

```python
import sys

def solve_recommendation_diversity():
    # Read all lines from standard input
    input_data = sys.stdin.read().splitlines()
    
    if not input_data:
        return

    # Parse N and K
    try:
        n = int(input_data[0].strip())
        k = int(input_data[1].strip())
    except (IndexError, ValueError):
        return

    # Total elements needed
    total_needed = n * k
    
    # Initialize windows (list of lists)
    windows = [[] for _ in range(n)]
    
    # Track how many elements we have placed
    current_count = 0
    
    # Process remaining lines as input lists
    # Line indices 2 onwards
    source_lists = []
    for line in input_data[2:]:
        if line.strip():
            # Convert string elements to integers (or keep as strings if output format is flexible)
            # The problem implies integers, but output is space separated string
            elements = list(map(int, line.strip().split()))
            source_lists.append(elements)

    # Distribution Logic
    for source_list in source_lists:
        if current_count >= total_needed:
            break
            
        # We distribute this list in rounds of N
        # Index within the current source list
        idx = 0
        list_len = len(source_list)
        
        while idx < list_len and current_count < total_needed:
            # Determine how many we can take in this round (max N)
            # But also limited by remaining needed
            remaining_needed = total_needed - current_count
            
            # How many items we can take from this list in this batch
            items_to_take = min(n, list_len - idx, remaining_needed)
            
            # Distribute these 'items_to_take' to windows 0, 1, 2...
            for i in range(items_to_take):
                win_idx = i
                # Add element to the specific window
                windows[win_idx].append(source_list[idx + i])
                current_count += 1
                if current_count >= total_needed:
                    break
            
            # Move the index forward by the number of items taken
            idx += items_to_take
            
            # If we filled everything, break outer loop too
            if current_count >= total_needed:
                break

    # Format Output: Window 1 elements, then Window 2, etc.
    result = []
    for w in windows:
        result.extend(w)
    
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    solve_recommendation_diversity()
```

### **Example Walkthrough (Based on Problem Description)**
*   **Input:**
    ```text
    4
    4
    0 1 2 3 4 5 6 7
    10 11 12 13 18 19
    20 21 22 23
    ```
    *(Note: N=4, K=4, Total=16)*

1.  **List 1** (`0..7`):
    *   Take 4 (`0,1,2,3`) -> Win 0, 1, 2, 3. (Count: 4)
    *   Take 4 (`4,5,6,7`) -> Win 0, 1, 2, 3. (Count: 8)
2.  **List 2** (`10..19`):
    *   Take 4 (`10,11,12,13`) -> Win 0, 1, 2, 3. (Count: 12)
    *   Need 4 more. List has `18, 19` left.
    *   Take 2 (`18, 19`) -> Win 0, 1. (Count: 14)
3.  **List 3** (`20..23`):
    *   Need 2 more.
    *   Take 2 (`20, 21`) -> Win 0, 1. (Count: 16) -> **Stop**.

*   **Final Windows:**
    *   Win 0: `0, 4, 10, 18, 20` (Wait, K=4, so only first 4 elements per window? No, the logic in the problem description says "fill the window". If we stop exactly at 16, each window has exactly 4).
    *   Let's re-verify the count:
        *   W0: 0, 4, 10, 18 (4 items)
        *   W1: 1, 5, 11, 19 (4 items)
        *   W2: 2, 6, 12, 20 (4 items) -- Wait, in step 3 we took 20 for W0?
        *   *Correction on Step 3 logic:*
            *   We need 2 items.
            *   Current window pointer starts at 0?
            *   The rule is "from the list, pick for every screen".
            *   If we pick 2 items, they go to Window 0 and Window 1.
            *   So W0 gets 20, W1 gets 21.
            *   W0: 0, 4, 10, 20 (4 items)
            *   W1: 1, 5, 11, 21 (4 items)
            *   W2: 2, 6, 12 (3 items? No, we stopped early).
    *   **Re-reading the problem carefully:** "每个列表的元素尽量均分为 N 份... 如果不够 N 个，也要全部分配完".
    *   The example in the text says:
        *   (1) List 1: 0,1,2,3 -> W1, W2, W3, W4
        *   (2) List 2: 10,11,12,13 -> W1, W2, W3, W4
        *   (3) List 3: 20,21,22,23 -> W1, W2, W3, W4
        *   (4) List 1: 4,5,6,7 -> W1, W2, W3, W4
        *   (5) List 1: 4,5 (Wait, list 1 has 8 items? 0-7. 0,1,2,3 used. 4,5,6,7 used. No items left).
        *   The example text says: "再从第一个列表中选择 4 条 4 5 6 7" (Take 4,5,6,7).
        *   Then "再从第一个列表中选择... 由于数量不足 4 条...". This implies the example text might be describing a scenario with *more* items or a different list size than my manual trace.
        *   **Crucial Logic Check:** The distribution is strictly sequential across windows for every batch of N taken from a list.
        *   If we stop at 16 items, every window must have exactly 4.
        *   My code logic `win_idx = i` inside the `range(items_to_take)` loop assumes we start distributing from Window 0 every time we start a new batch from a list.
        *   **Is that correct?**
            *   "先从第一个列表中为每屏选择一个元素" -> Take N, assign to 0..N-1.
            *   "再从第一个列表中选择..." -> Take next N, assign to 0..N-1.
            *   Yes, the distribution always resets to Window 0 for the start of a new batch from the *same* list or a *new* list?
            *   Actually, the text says "从第一个列表... 再从第二个列表... 再从第一个列表".
            *   It seems the "Round" is defined by the list.
            *   So yes, for every batch of up to N items taken from a list, we fill Windows 0, 1, 2...
            *   This means if we need 2 more items at the end, we give them to Window 0 and Window 1.
            *   This leaves Window 2 and 3 with fewer items? **No**, because the total count is exactly N*K.
            *   If Total = 16, N=4, K=4.
            *   If we give the last 2 to W0 and W1, then W0 and W1 have 5 items?
            *   **Wait**, the problem says "一次性要返回 N 屏数据... 每屏 K 个".
            *   This implies the process stops *exactly* when every window has K items.
            *   So if we are at 14 items (3.5 per window? No, 14 items total).
            *   If we have 14 items distributed, the distribution might be uneven?
            *   Let's re-read the example logic (5) and (6).
            *   (5) Take 2 items -> "放到 窗口1 和 窗口2" (Wait, text says "窗口1 和 窗口2", which are indices 0 and 1).
            *   (6) Take 2 items -> "放到 窗口3 和 窗口4" (Indices 2 and 3).
            *   This implies the distribution continues sequentially across windows regardless of list boundaries?
            *   **Alternative Interpretation:**
                *   We have a global pointer for the window (0 to N-1).
                *   We iterate through lists.
                *   We take an element, put in current window, move window pointer.
                *   If window pointer reaches N, reset to 0.
                *   *But* the text says "先从第一个列表中为每屏选择一个元素" (Pick one for *every* screen from the first list). This implies a block of N.
                *   If the list has 10 items and N=4.
                *   Block 1: Items 0-3 -> W0, W1, W2, W3.
                *   Block 2: Items 4-7 -> W0, W1, W2, W3.
                *   Block 3: Items 8-9 -> W0, W1.
                *   If we stop here, W0 and W1 have 3 items, W2 and W3 have 2.
                *   This violates "每屏 K 个" (Each screen K items) unless the total input guarantees a perfect fill or the process stops *before* the partial block?
                *   **Ah, the example (5) and (6) in the text:**
                    *   (5) "取剩下的 2 条，放到 窗口1 和 窗口2" (Take remaining 2, put in W1 and W2).
                    *   (6) "取 18 19 放到 窗口3 和 窗口4" (Take 18, 19 put in W3 and W4).
                    *   This implies that the "partial block" from List A went to W1, W2. And the "partial block" from List B went to W3, W4.
                    *   This suggests the window pointer **does not reset** to 0 at the start of every list. It continues from where it left off?
                    *   **OR**, it implies that the distribution is strictly:
                        *   List 1: Fill W0, W1, W2, W3 (4 items).
                        *   List 1: Fill W0, W1, W2, W3 (4 items).
                        *   List 1: Fill W0, W1, W2, W3 (4 items).
                        *   List 1: Fill W0, W1 (2 items). -> W0, W1 have 5? No, K=4.
                        *   The example text is slightly confusing without the exact numbers of the full example.
            *   **Let's look at the standard interpretation of "Recommendation Diversity" on Huawei OD:**
                *   The standard algorithm is:
                    1.  Flatten all input lists into a single stream? No, "interleaving" is key.
                    2.  The logic is: Iterate through lists. For each list, iterate through its elements.
                    3.  Assign element `e` to `windows[i]` where `i` is a global counter modulo N?
                    4.  **NO**, the text says "先从第一个列表中为每屏选择一个元素" (Select one for every screen from the first list). This sounds like a block.
                    5.  However, if we look at step (5) and (6) again:
                        *   (5) List 1 remaining 2 items -> W1, W2.
                        *   (6) List 2 remaining 2 items -> W3, W4.
                        *   This implies the window assignment **continued sequentially** across the boundary of the lists.
                        *   If List 1 filled W1, W2, then List 2 started filling W3, W4.
                        *   This implies a **global round-robin** across windows, but the "batch" nature is just how we describe taking from a list.
                        *   **Actually, the most robust logic for this specific problem (Huawei OD 474)** is:
                            *   We have a "current window index" that starts at 0.
                            *   We iterate through each source list.
                            *   For each element in the source list:
                                *   Assign to `windows[current_window_index]`.
                                *   `current_window_index = (current_window_index + 1) % N`.
                                *   Stop if total items == N*K.
                            *   **BUT**, does the text "先从第一个列表中为每屏选择一个元素" contradict this?
                            *   If I have 4 windows and a list of 10 items.
                            *  

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
