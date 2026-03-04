"""
题目
题目描述
寿司店周年庆,正在举办优惠活动回馈新老客户。
寿司转盘上总共有n盘寿司,prices[i]是第1盘寿司的价格,如果果客户选择了第i盘寿司,寿司店免费赠送客户距离 第
i盘寿司最近的下一盘寿司j,前提是prices[j]<prices[i],如果没有满足条件的j,则不赠送寿司
每个价格的寿司都可无限供应
输入输出
输入
输入的每一个数字代表每盘寿司的价格,每盘寿司的价格之间使用空格分隔
寿司的盘数n范围为:1<=n<=500
每盘寿司的价格price范围为:1<=price<=1000
输出
输出享受优惠后的一组数据,每个值表示客户选择第i盘寿司时实际得到的寿司的总价格

1.遍历价格列表,对于每一盘寿司(第1盘),执行以下步骤。
2.从当前寿司(第1盘)开始,在转盘上向前和向后搜索价格低于当前寿司的寿司。由于是环形,向前搜索时索引会
减小,而向后搜索时索引会增加。我们需要使用取模操作来确保索引不会越界,即(i+d)%n和(i-d+n)%
n。
3.对每个可能的距离d(从1开始直到n-1),我们首先检查索引(i+d)%n的寿司价格是否低于第 i 盘的价格。
如果是,我们找到了向后的最近更便宜的寿司。如果不是,我们再检查索引(i-d+n)%n的寿司价格是否低于
第1盘的价格。如果是,我们找到了向前的最近更便宜的的寿司。
4.一旦找到了价格更低的寿司,我们将第 i盘寿司的价格加上找到的这盘寿司的价格,得到总价格,并将其添加到结
果列表中。如果没有找到价格更低的寿司,则只添加当前寿司的价格
5.遍历完成后,我们得到了一个包含了每一盘寿司享受优就是后的总价格的列表。
"""

def find_next_cheaper(prices, i):
    n = len(prices)
    # 从当前位置向前和向后搜索最近的更便宜的寿司
    for d in range(1, n):
        # 向后查找
        j = (i + d) % n
        if prices[j] < prices[i]:
            return prices[j]
        # 向前查找
        j = (i - d + n) % n
        if prices[j] < prices[i]:
            return prices[j]
    # 如果没有找到，返回0，表示不赠送
    return 0

def calculate_total_prices(prices):
    total_prices = []
    for i in range(len(prices)):
        # 计算第i盘寿司的总价格
        free_sushi_price = find_next_cheaper(prices, i)
        total_price = prices[i] + free_sushi_price
        total_prices.append(total_price)
    return total_prices

# 读取输入
input_prices = input().strip().split()
prices = [int(price) for price in input_prices]

# 计算并输出结果
result = calculate_total_prices(prices)
print(" ".join(map(str, result)))
