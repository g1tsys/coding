"""
题目描述
现代计算机系统中通常存在多级的存储设备,针对海量workload的优化的
存页优先放到快速存储层级,这就需要对内存页进行冷热标記
一种典型的方案是基于内存页的访问频次进行标记,如果统计窗口内访问
则认为是热内存页,否则是冷内存页
对于统计窗口内跟踪到的访存序列和阈值现在需要实现基于频次的冷热标
作为标识。
输入输出
输入
第一行为输入为N表示访存序列的记录条数0<N<=10000
第二行为访存序列,空格分割的N个内存页框号
第三行为热内存的频次阈值T,正整数范围1<T<10000。
输出
第一行输出标记为热内存的内存页个数,如果没有被标记为热内存的,则
如果第一行>0,则接下来按照访问频次降序输出内存页框号号,一行一个,
页框号小的排前面。

1.读取输入,包括访存序列的记录条数N、访存序列page_access_sequence和阈值threshold。
2.使用字典page_access_count统计每个内存页框号的访问次数。
3.筛选出访问次数大于等于阈值的热内存页,并将其存储在列表hot_pages中。hot_pages中的每个
元素是一个元组,包含页框号和访问次数。
4.对hot_pages进行排序,首先按照访问次数降序排列,如果访问次欠数相同,则按照页框号升序排
列。
5.输出热内存页的数量,即hot_pages的长度。
6.如果存在热内存页,依次输出页框号。
"""

# 读取输入
N = int(input())  # 访存序列的记录条数
page_access_sequence = list(map(int, input().split()))  # 访存序列，页框号
threshold = int(input())  # 阈值

# 统计每个内存页框号的访问次数
page_access_count = {}
for page in page_access_sequence:
    if page in page_access_count:
        page_access_count[page] += 1
    else:
        page_access_count[page] = 1

# 筛选出热内存页，并按照访问频次降序和页框号升序排序
hot_pages = [(page, count) for page, count in page_access_count.items() if count >= threshold]
hot_pages.sort(key=lambda x: (-x[1], x[0]))

# 输出热内存页的数量
print(len(hot_pages))

# 如果存在热内存页，输出页框号
for page, _ in hot_pages:
    print(page)
