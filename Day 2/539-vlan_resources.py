"""

### Problem Description
VLAN is a technology for logically dividing a local area network. To identify different VLANs, the concept of VLAN ID (an integer between 1 and 4094) is introduced.

A VLAN ID resource pool (referred to as the VLAN resource pool) is defined as follows: consecutive VLANs in the pool are represented by `start VLAN-end VLAN`, while non-consecutive VLANs are represented by a single integer. All VLANs are connected by English commas (`,`).

Now there is a VLAN resource pool, and a business needs to apply for a VLAN from the pool. You need to output the resource pool after removing the applied VLAN from the original VLAN resource pool.

---

### Input and Output

**Input:**
- The first line is the VLAN resource pool in string format.
- The second line is the VLAN to be applied for. The value range of the VLAN is an integer between [1, 4094].

**Output:**
- Output the VLAN resource pool in string format after removing the applied VLAN from the input resource pool. The output must follow the format described in the problem description and be sorted in ascending order of VLAN.
- If the applied VLAN is not in the original VLAN resource pool, output the original VLAN resource pool after sorting it in ascending order.

---

Would you like me to also translate the corresponding solution approach for this problem?

# Python Language Approach
1. Read the input VLAN resource pool and the VLAN ID requested by the business.
2. Split the VLAN resource pool into a list using commas as delimiters.
3. Create an empty result list to store the final VLAN resource pool.
4. Iterate through each VLAN resource in the pool:
   - If the resource is a range (e.g., `1-5`), add all VLAN IDs within that range to the result list.
   - If the resource is a single integer, add it directly to the result list.
5. Sort the result list in ascending order.
6. Check if the requested VLAN ID is in the result list:
   - If it is present, remove the VLAN ID from the result list.
   - If it is not present, output the result list directly.
7. Convert the result list into a string in the required output format:
   - Iterate through the result list to find consecutive VLAN ID ranges.
   - Output the VLANs according to the range rules.
   - Do not add a trailing comma after the last element.
8. Output the final VLAN resource pool.

---

Would you like me to also provide the full Python code implementation for this problem?
"""

def remove_requested_vlan(vlan_pool, requested_vlan):
    # 将输入的VL AN资源池按照逗号拆分成一个列表
    vlan_list = vlan_pool.split(',')
    # 用于存放最终结果的列表
    result = []

    # 遍历每个VL AN资源
    for vlan_range in vlan_list:
        # 如果资源是一个范围（如1-5），则拆分为开始VL AN和结束VL AN
        if '-' in vlan_range:
            start_vlan, end_vlan = map(int, vlan_range.split('-'))
            # 将范围内的所有VL AN加入结果列表
            result.extend(range(start_vlan, end_vlan + 1))
        else:
            # 如果资源是单个整数，则直接加入结果列表
            result.append(int(vlan_range))

    # 将结果列表进行排序
    result.sort()

    # 检查业务要申请的VL AN是否在原资源池内
    if requested_vlan in result:
        # 如果在资源池内，则从结果列表中移除该VL AN
        result.remove(requested_vlan)

    # 将结果列表转换为输出格式的字符串
    output = ''
    i = 0
    while i < len(result):
        start_vlan = result[i]
        # 查找连续的VL AN范围
        while i + 1 < len(result) and result[i + 1] == result[i] + 1:
            i += 1
        end_vlan = result[i]

        # 根据范围情况输出
        if start_vlan == end_vlan:
            output += str(start_vlan)
        else:
            output += f"{start_vlan}-{end_vlan}"

        # 最后一个元素后不加逗号
        if i < len(result) - 1:
            output += ','

        i += 1

    return output


# 读取输入
vlan_pool_input = input().strip()
requested_vlan_input = int(input().strip())

# 调用函数得到结果
output_result = remove_requested_vlan(vlan_pool_input, requested_vlan_input)

# 输出结果
print(output_result)
