"""
题目描述
某个产品当前迭代周期内有N个特性(F1，F2....FN)需要进行覆盖测试，每个特性都被评估了对应的优先级，特性使用其ID作为下标进行标识
设计了M个测试用例(T1，T2....TM)，每个测试用例对应一个覆盖特性的集合，测试用例使用其ID作为下标进行标识，测试用例的优先级定义为其覆盖的特性的优先级之和
在开展测试之前，需要制定测试用例的执行顺序，规则为:优先级大的用例先执行，如果存在优先级相同的用例，用例D小的先执行。
前入输出
输入
第一行输入为N和M
1、N表示特性的数量，0<N<=100
2、M表示测试用例的数量，0≤M=100
之后N行表示特性ID=1到特性ID=N的优先级，再接下来M行表示测试用例ID=1到测试用例ID=M关联的特性的ID的列表
按照执行顺序(优先级从大到小)输出测试用例的ID，每行一个ID，测试用例覆盖的ID不重复
1.读取特性数量N和测试用例数量M。
2.创建一个列表feature_priorities用于保存特性的优先级，索引10不使用。
3.读取特性的优先级，并将其添加到feature_priorities列表中。
4.创建一个列表test_cases用于保存测试用例的信息。
5.循环M次，读取每个测试用例覆盖的特性列表。
。读取每个测试用例覆盖的特性列表，并将其转换为整数列表covered_features。。计算测试用例的优先级，即其覆盖的特性的优先级之和。使用列表推导式和特性的优先级列表feature__priorities，计算covered_features中特性的优先级之和，并将结果赋值给priority.
。将测试用例的ID和优先级作为一个元组，添加到test_cases列表中。使用元组(tuple)表示测试用例的ID和优先级，即(test_case_id,priority)。
6.使用lambda函数作为排序的键值，根据测试用例的优先级和ID进行排序，先按优先级降序排序，然后按ID升序排序。使用sorted0函数，传入test_cases列表和一个lambda函数作为key参数，lambda函数的返回值为一个元组，元组的第一个元素为测试用例的优先级的负数(以实现降序排序)，第二个元素为测试用例的ID。
7.遍历排序后的测试用例例表，输出测试用例的ID。使用for循环遍历sorted_testcases列表，并使用printQ函数输出每个测试用例的ID，即test_case[0]。
。 test_case[0]表示元组(test_case_id,priority)的第一个元素，即测试用例的ID。
"""


# 读取特性数量N和测试用例数量M
N, M = map(int, input().split())

# 读取特性优先级，并保存到一个列表中，索引0不使用
feature_priorities = [0] + [int(input()) for _ in range(N)]

# 初始化测试用例的优先级列表
test_cases = []

# 读取测试用例信息，并计算每个测试用例的优先级
for i in range(1, M+1):
    # 读取每个测试用例覆盖的特性列表
    covered_features = list(map(int, input().split()))
    # 计算测试用例的优先级，即其覆盖的特性的优先级之和
    priority = sum(feature_priorities[feature_id] for feature_id in covered_features)
    # 将测试用例的ID和优先级作为一个元组加入到测试用例列表中
    test_cases.append((i, priority))

# 根据优先级和ID进行排序，先按优先级降序排序，然后按ID升序排序
# 这里使用lambda函数来指定排序的键值
sorted_test_cases = sorted(test_cases, key=lambda x: (-x[1], x[0]))

# 输出排序后的测试用例ID
for test_case in sorted_test_cases:
    print(test_case[0])
