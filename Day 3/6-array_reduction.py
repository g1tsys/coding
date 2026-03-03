"""
Here's the translation of the **question** and **Python thought process**:

---

### Problem Description

Given a disordered array, remove all duplicate elements so that each element appears only once, then sort by **frequency (high to low)**. Elements with the same frequency are sorted by their **first appearance order**.

**Input:** An array
**Output:** The deduplicated and sorted array

---

### Python Thought Process

1. Define a function `remove_duplicates_and_sort` that accepts an array as input.
2. Create a dictionary `frequency` to record each element's **occurrence count** and **index of first appearance**.
3. Use `enumerate` to iterate over the input array, getting each element's value `num` and index `index`.
4. If `num` **already exists** in `frequency`, increment its count.
5. If `num` **does not exist** in `frequency`, initialize its count to `1` and record its first appearance index.
6. Use `sorted` on the dictionary keys with a **lambda function** that returns a tuple, sorting by:
   - Occurrence count in **descending order**
   - First appearance index in **ascending order**
7. Return the sorted element list.
8. Read user input via `input()`, split by commas using `.split(',')`, convert to integers using `map(int, ...)`.
9. Call `remove_duplicates_and_sort` and output the result as a **comma-separated string**.
"""

def remove_duplicates_and_sort(arr):
    # 创建一个字典来记录每个元素的出现次数和第一次出现的索引
    frequency = {}
    for index, num in enumerate(arr):
        if num in frequency:
            # 如果元素已经在字典中，增加其出现次数
            frequency[num][0] += 1
        else:
            # 如果元素不在字典中，初始化其出现次数为1，并记录其第一次出现的索引
            frequency[num] = [1, index]
    
    # 按照出现次数从高到低排序，如果次数相同则按照第一次出现的顺序排序
    sorted_elements = sorted(frequency.keys(), key=lambda x: (-frequency[x][0], frequency[x][1]))
    
    return sorted_elements


input_str = input("")
input_array = list(map(int, input_str.split(',')))

# 调用函数并输出结果
output_array = remove_duplicates_and_sort(input_array)
print(','.join(map(str, output_array)))  # 输出按要求的格式


