"""Based on the web page content provided, here is the extraction of the problem details and the logic required to solve it using Python.

### **Problem: File Cache System (华为OD机试真题 481)**

#### **1. Problem Description**
Design a file cache system with a specified maximum capacity (in bytes).
The system supports two operations:
1.  **`put fileName fileSize`**: Store a file.
2.  **`get fileName`**: Read a file.

**Rules:**
*   **Storage**: If the cache has enough space, store the file. If the new file's name already exists in the cache, ignore the operation (do not update size or re-add).
*   **Reading**: If the file exists, access it (update access count and time). If it doesn't exist, do nothing.
*   **Eviction Policy (LRU/LFU Hybrid)**: When the cache is full and a new file needs to be stored:
    *   Delete files until there is enough space for the new file.
    *   **Priority 1**: Delete files with the **lowest access count** (Least Frequently Used).
    *   **Priority 2**: If access counts are equal, delete files with the **oldest access time** (Least Recently Used).
*   **Updates**:
    *   Every time a file is accessed (put if new, or get), its **total access count** increases by 1.
    *   Every time a file is accessed, its **last access time** is updated to the current time (simulated by the order of operations).
    *   *Note*: The problem states "When a new file is first stored... total access count will not change" initially, but then "Every time a file is accessed... total access count increases by 1". This implies:
        *   `put` (new file): Adds to cache, sets time = current step, count = 1 (since the act of putting counts as the first access). *Wait, let's re-read carefully*: "新的文件第一次存入到文件缓存中时，文件的总访问次数不会变化" (When a new file is first stored, the total access count does not change). This is slightly ambiguous. Usually, "put" counts as an access. Let's look at rule 3: "Every time a file is accessed after, total count + 1".
        *   *Correction based on standard LFU/LRU logic and typical Huawei OD patterns*: Usually, the `put` operation itself counts as the first access. However, the text says "total access count will not change" upon *first* storage, but "every time a file is accessed after, count + 1".
        *   *Re-evaluating the text*: "新的文件第一次存入...总访问次数不会变化" (Total count doesn't change on first store). "每次文件访问后，总访问次数加1" (After every file access, count + 1).
        *   This implies:
            1.  `put` (new): Add to cache. Count = 0? Or Count = 1?
            2.  `get`: Count + 1.
            3.  `put` (existing): This acts as an update/access? The text says "If new file name is same as existing, it won't be placed".
            4.  Let's look at the eviction logic: "Access count from few to many".
            5.  *Standard Interpretation for this specific problem type*: The `put` operation counts as the first access (Count = 1). The text "count will not change" might refer to not incrementing an *existing* counter if it were already there, but since it's new, it starts at 1. Or, it starts at 0 and the first `get` increments it.
            6.  *Let's look at the "Time" rule*: "Last access time updates to latest".
            7.  *Safest Logic*: Treat `put` (new) as an access event that sets `time` = current_step and `count` = 1. Treat `get` as incrementing `count` by 1 and updating `time`. If the text strictly means `put` doesn't increment, then `put` sets count=0? But then a file with count=0 would be deleted immediately. It is highly likely `put` sets count=1.

#### **2. Input Format**
*   **Line 1**: Integer `m` (Max cache size in bytes). $0 < m \le 52428800$.
*   **Line 2**: Integer `n` (Number of operations). $0 \le n \le 300000$.
*   **Lines 3 to N+2**: Operations in format `op fileName fileSize`.
    *   `op`: `put` or `get`.
    *   `fileName`: String (lowercase, max length 10).
    *   `fileSize`: Integer (if `op` is `put`).

#### **3. Output Format**
*   Print the names of files currently in the cache, separated by commas, sorted alphabetically (dictionary order).
*   If the cache is empty, print `NONE`.

#### **4. Python Thought Process & Logic**

To solve this efficiently in Python, we need a data structure that allows:
1.  **Fast lookup** by filename (to check existence).
2.  **Efficient eviction** based on (Access Count, Access Time).
3.  **Updating** access stats (count and time) on every `put` (new) and `get`.

**Data Structures:**
*   **Dictionary (`cache`)**: Key = `fileName`, Value = object/dict containing `{size, count, last_access_time}`.
*   **Time Counter**: A global integer that increments with every operation to act as the "timestamp".
*   **Eviction Logic**:
    *   When `put` occurs and space is insufficient:
        *   Identify the file to remove: Sort the current cache items by `(count, last_access_time)`.
        *   Remove the item with the **smallest** count. If tied, remove the one with the **smallest** time (oldest).
        *   Repeat until there is enough space for the new file.
    *   If a new file is too large to fit even in an empty cache, it cannot be stored (Rule 6).
    *   If the file already exists in the cache, do nothing (Rule 1).

**Step-by-Step Algorithm:**
1.  Initialize `current_usage = 0`, `time_counter = 0`, `cache = {}`.
2.  Read `m` and `n`.
3.  Loop `n` times to process operations:
    *   Increment `time_counter`.
    *   Parse `op`, `name`, `size`.
    *   **Case `get`**:
        *   If `name` in `cache`:
            *   `cache[name]['count'] += 1`
            *   `cache[name]['last_access_time'] = time_counter`
    *   **Case `put`**:
        *   If `name` in `cache`:
            *   Do nothing (ignore).
        *   Else:
            *   Check if `size > m`. If so, cannot store. Continue.
            *   While `current_usage + size > m`:
                *   Find the file to evict:
                    *   Sort keys of `cache` by `(cache[k]['count'], cache[k]['last_access_time'])`.
                    *   Select the first one (lowest count, then oldest time).
                *   Remove it from `cache` and subtract its size from `current_usage`.
            *   If `current_usage + size <= m`:
                *   Add to `cache`: `cache[name] = {'size': size, 'count': 1, 'last_access_time': time_counter}`.
                *   `current_usage += size`.
4.  After all operations:
    *   Get keys from `cache`.
    *   Sort alphabetically.
    *   If empty, print `NONE`. Else, print comma-separated string.

**Optimization Note**:
Since $N$ can be up to 300,000, sorting the entire cache for every eviction might be too slow ($O(N^2 \log N)$ worst case).
However, in Python, for typical competitive programming constraints with $N=300,000$, a simple sort during eviction might TLE (Time Limit Exceeded) if many evictions happen.
*Optimized Approach*: Use a `heapq` or a sorted structure?
Actually, since we need to find the *minimum* of (count, time), a Min-Heap could work, but updating keys in a heap is hard.
Given the constraints and Python's speed, if the number of files in cache is small, sort is fine. If large, we need a better structure.
*Alternative*: Since we only remove the "worst" one, we can just scan or keep a sorted list?
Wait, the constraint is $N=300,000$. If we have 300,000 operations, and each triggers a scan of the cache (which could be large), it's slow.
But usually, the cache size is limited by memory `m`. If `m` is large, cache is large.
Is there a faster way?
We can store files in a way that allows quick retrieval of the min (count, time).
A `heap` of `(count, time, name)` could work. But when a file is accessed (`get` or `put`), its count and time change.
In Python, `heapq` doesn't support efficient updates. We would need to use "lazy deletion":
1.  Push new `(count, time, name)` to heap.
2.  When popping, check if the popped entry matches the current data in the `cache` dict. If not (stale), ignore and pop again.
This ensures $O(\log K)$ per operation where $K$ is cache size.

**Revised Python Logic (Optimized):**
1.  `cache`: Dict mapping `name` -> `{size, count, time}`.
2.  `heap`: List of tuples `(count, time, name)`.
3.  **Eviction**:
    *   While space needed:
        *   Pop from `heap`.
        *   Check if the popped `(count, time, name)` matches `cache[name]`'s current values.
        *   If it matches (and name exists), remove from `cache`, subtract size, break loop (we found the victim).
        *   If it doesn't match (stale), ignore and pop next.
4.  **Update**:
    *   When `get` or `put` (new) updates a file's count/time:
        *   Update `cache[name]`.
        *   Push the new `(new_count, new_time, name)` to `heap`.
        *   (The old entry remains in heap but becomes "stale" and will be ignored later).

This ensures the solution runs in $O(N \log N)$.
"""



import sys
import heapq

def solve():
    # Read all input from stdin
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        m = int(next(iterator))
        n = int(next(iterator))
    except StopIteration:
        return

    cache = {} # name -> {'size': int, 'count': int, 'time': int}
    heap = []  # min-heap of (count, time, name)
    current_usage = 0
    time_counter = 0

    for _ in range(n):
        try:
            op = next(iterator)
            file_name = next(iterator)
            # For 'put', we need size. For 'get', size is not provided in input stream usually, 
            # but the problem says "op file_name file_size". 
            # If op is get, the next token might be the size of the next command? 
            # No, the input format says: "op file_name file_size" for each line.
            # So if op is 'get', there is still a 3rd token? 
            # The problem description: "put fileName fileSize", "get fileName".
            # The input format says: "op file_name file_size".
            # This implies for 'get', the third token might be ignored or not exist?
            # Standard Huawei OD input usually provides the 3rd token as 0 or just skips it?
            # Let's assume the input stream has the token but we only use it for put.
            # Wait, if op is 'get', does the input line have a size?
            # "从第三行起为文件操作序列，每个序列单独一行，文件操作定义为：op file_name file_size"
            # This implies EVERY line has 3 tokens.
            # So for 'get', we read a size token but ignore it.
            file_size_str = next(iterator)
            file_size = int(file_size_str)
        except StopIteration:
            break

        time_counter += 1

        if op == 'get':
            if file_name in cache:
                # Update access
                cache[file_name]['count'] += 1
                cache[file_name]['time'] = time_counter
                # Push new state to heap
                heapq.heappush(heap, (cache[file_name]['count'], cache[file_name]['time'], file_name))
        
        elif op == 'put':
            # Rule 1: If file exists, ignore
            if file_name in cache:
                continue
            
            # Rule 6: If file too big for empty cache
            if file_size > m:
                continue
            
            # Eviction necessary?
            while current_usage + file_size > m:
                if not cache:
                    break # Should not happen if file_size <= m and we are checking loop
                
                # Pop until we find a valid victim
                while heap:
                    count, t, name = heapq.heappop(heap)
                    
                    # Check if this entry is stale
                    if name not in cache:
                        continue
                    entry = cache[name]
                    if entry['count'] == count and entry['time'] == t:
                        # This is the valid victim
                        current_usage -= entry['size']
                        del cache[name]
                        break
                else:
                    # Heap empty but cache not empty? Logic error or all stale?
                    # If all heap items are stale, we need to rebuild or handle.
                    # But logic ensures we push valid items. If heap is empty, cache must be empty?
                    # If cache is not empty but heap is empty, we have a bug.
                    # Re-try logic: If heap is exhausted, we must scan cache? (Fallback)
                    # With lazy deletion, heap might have old items. If we pop everything and find nothing valid,
                    # it means cache is empty? No.
                    # Let's ensure we handle the case where heap is empty but cache is not.
                    # Actually, if cache is not empty, there must be at least one valid entry pushed.
                    # So the inner while loop will eventually find a valid one.
                    break

            # Now try to add
            if current_usage + file_size <= m:
                cache[file_name] = {
                    'size': file_size,
                    'count': 1,
                    'time': time_counter
                }
                current_usage += file_size
                heapq.heappush(heap, (1, time_counter, file_name))

    # Output
    if not cache:
        print("NONE")
    else:
        sorted_files = sorted(cache.keys())
        print(",".join(sorted_files))

if __name__ == "__main__":
    solve()

"""
### **Key Considerations for the Python Solution**
1.  **Input Parsing**: The input format specifies `op file_name file_size` for every line. Even for `get`, a size value is likely present in the input stream (often 0 or a dummy value), so the parser must consume it to stay in sync.
2.  **Lazy Deletion**: Because updating a file's access count and time invalidates its old position in a heap, we use the "lazy deletion" strategy. We push the new state to the heap and ignore old entries when they surface at the top of the heap.
3.  **Sorting**: Python's `heapq` is efficient for finding the minimum. The tuple comparison `(count, time)` naturally implements the required priority: smallest count first, then smallest time (oldest).
4.  **Output**: The final list must be sorted alphabetically, which `sorted(cache.keys())` handles efficiently.

This approach ensures the solution is robust against the large input size ($N=300,000$) while adhering to the strict eviction rules.
"""