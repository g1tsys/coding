"""
### Problem Description
There is a simple memory pool where memory is classified by **grain size**. Each grain size has a certain number of available memory resources. Users will submit a series of memory allocation requests, and you need to allocate resources from the pool as required, returning a list of allocation results (success or failure).

#### Allocation Rules:
1. The allocated memory must be **greater than or equal to** the requested memory size. If memory meeting the demand exists, it **must** be allocated. Allocation prioritizes **smaller grain sizes**, and memory resources **cannot be split** for use.
2. Allocation follows the **order of requests**: earlier requests are processed first. If available memory is allocated successfully, the result for that request is `true`.
3. If no available memory meets the requirements, the result for that request is `false`.

---

### Input and Output

#### Input
The input consists of two strings:
1. **First line (Memory pool resource list)**: Contains information about all memory grain sizes, separated by commas (`,`). Each grain size entry is split by a colon (`:`): the part before the colon is the **grain size** (memory size), and the part after is the **quantity** of available resources for that size.
2. **Second line (Request list)**: Lists the memory sizes requested by users, separated by commas (`,`).

#### Output
A list representing the allocation results of the memory pool (in the order of the input requests), where each element is either `true` (success) or `false` (failure).


# Python Language Approach
1. First, read the input memory pool resource list and the request list.
2. Parse the memory pool resource list into a dictionary (or map), where the keys are the memory grain sizes and the values are the available quantities.
3. Create a result list to record the allocation outcome for each request.
4. For each request, iterate through each memory grain size in the memory pool resource list.
5. If a memory grain size is found that is greater than or equal to the requested memory size and has an available quantity greater than 0, allocate this grain to the request and decrement the available quantity of that grain size by 1.
6. If no available memory can be allocated for the request, mark the request as failed.
7. Record the allocation result for each request in the result list.
8. Output the result list.

---

Would you like me to also provide the full Python code implementation for this problem?

"""



# 获取输入
cache_list = dict(tuple(map(int, cache.split(':'))) for cache in input().split(','))
task_list = list(map(int, input().split(',')))

# 记录结果
res = []
flag = True

for task_elem in task_list:
    flag = False
    for cache_elem in cache_list.items():
        # 当有可分配的内存时，将内存分配出去
        if cache_elem[0] >= task_elem and cache_elem[1] > 0:
            # 覆盖原有的值
            cache_list[cache_elem[0]] = cache_elem[1] - 1
            flag = True
            break
    res.append(str(flag))

# 输出结果
print(','.join(res))

