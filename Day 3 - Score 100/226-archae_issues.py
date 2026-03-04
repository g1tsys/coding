"""
题目抽述
有一个考古学家发现一个石碑,但是很可惜,发现时其已经断成多段,原地发现n个断口整
石碑碎片,为了破解石碑内容,考古学家希望有程序能帮忙十算复原后的石碑文字组合数,
帮忙吗?
输入输出
输入
第一行输入n,n表示石碑碎片的个数
第二行依次输入石碑碎片上的文字内容s,共有n组
输出
输出石碑文字的组合(按照升序排列),行未无多余空格

Python语言 思路
1.dfs函数是核心,它通过递归方式搜索所有可能的排列组合。它接受四个参数:element
片的内容列表),path(当前路径上的元素列表),visited(标记元素是否被访问过的
表),results(保存结果的列表)。
2.在dfs函数中,首先检查当前路径是否包含了所有的碎片(限即路径长度是否等于碎片总
果是,则将当前路径转换为字符串,并检查是否已经在结果列表中。如果不在,则将其添
果列表中,并返回。
3.如果路径长度不足以包含所有碎片,则遍历未被访问过的碎片,逐个尝试将其添加到路径
添加之前,需要检查当前元素是否与前一个元素相同,并且前一个元素未被访问过,以避
重复的排列。
4.如果添加当前元素后,路径长度仍不足以包含所有碎片,则递归调用dfs函数,继续向
5.当递归完成后,需要进行回溯操作,即将当前元素从路径中移除,并将其标记为未访问,
续的排列组合生成。
6.find_combinations函数用于初始化访问标记列表,并调用dfs 函数来寻找所有可能的抖
合。
7.最后,在main函数中,读取输入,调用find_combinations函数,然后打印所有生成的
"""
# 定义深度优先搜索函数，用于生成不重复的组合
def dfs(elements, path, visited, results):
    # 如果路径长度等于元素总数，说明找到了一种组合
    if len(path) == len(elements):
        result = ''.join(path)  # 将路径中的元素连接成字符串
        if result not in results:  # 检查结果是否唯一
            results.append(result)  # 如果唯一，则添加到结果列表中
        return  # 返回上一层递归
    
    # 遍历所有元素，尝试每种可能的组合
    for i, elem in enumerate(elements):
        # 如果当前元素未被访问过
        if not visited[i]:
            # 如果当前元素与前一个元素相同，并且前一个元素未被访问过，则跳过，避免重复
            if i > 0 and elements[i] == elements[i - 1] and not visited[i - 1]:
                continue
            visited[i] = True  # 标记当前元素为已访问
            path.append(elem)  # 将当前元素添加到路径中
            dfs(elements, path, visited, results)  # 递归搜索下一层
            path.pop()  # 回溯，移除路径中的最后一个元素
            visited[i] = False  # 取消当前元素的访问标记，以便重用

# 定义寻找所有组合的函数
def find_combinations(pieces):
    visited = [False] * len(pieces)  # 初始化访问标记列表
    results = []  # 初始化结果列表
    dfs(sorted(pieces), [], visited, results)  # 调用dfs函数，传入排序后的碎片
    return results  # 返回结果列表

def main():
    n = int(input().strip())  # 读取碎片数量
    pieces = input().strip().split()  # 读取碎片内容
    combinations = find_combinations(pieces)  # 获取所有不重复的组合
    for comb in combinations:
        print(comb)  # 打印每一种组合

if __name__ == "__main__":
    main()  
