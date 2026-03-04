"""
题目描述
橱窗里有一排宝石,不同的宝石对应不同的价格,宝石的价格标记为gems[i],0<=i<n,n=gems.length,宝石可同
时出售0个或多个,如果同时出售多个,则要求出售的宝石编号连续
例如客户最大购买宝石个数为m,购买的宝石编号必须为gems[i],gems[i+1]...gems [i+m-1] (0<=i<n, m<=п)
假设你当前拥有总面值为value的钱,请问最多能购买到多少个当宝石,如无法购买宝石,则返回0
输入输出
输入
第一行输入n,参数类型为int,取值范围:[0,10的6次方],表示橱窗中宝石的总数量
之后n行分别表示从第0个到第n-1个宝石的价格,即gems[0]到gems[n-1]的价格
之后一行输入V,表示你拥有的钱。
输出
输出表示最大可购买的宝石数量。

初始状态:
gems = [8, 4, 6, 3, 1, 6, 7]
value = 10
left = 0
right=0
total = 0
[8,4,6,3,1,6,7]
left
right
total = 0
第一步:移动right指针
[8,4,6,3,1,6,7]
left
right
total = 8
第二步:移动right指针
[8, 4, 6, 3, 1, 6, 7]
left
right
total=12(超过value,需要移动left指针)
第三步:移动left指针,减少total
[8, 4, 6, 3, 1, 6,7]
left
right
total = 4
第四步:再次移动right指针
[8, 4, 6, 3, 1, 6,7]
left
right
total=10(等于value,是一个候选的最大购买数量)
...(继续这个过程,直到right到达数组末尾)
M
CSDN @KJJK

1.初始化两个指针left和right,都指向宝石数组的起始位置。
2.用一个变量total来记录当前窗口内宝石的总价值,初始化为0
3.向右移动right指针,每次移动后将新包含的宝石价格加到 totcal中
4.当total超过value时,从total中减去left指向的宝石的价格,并将left向右移动。
5.在每次移动right指针的过程中,记录并更新能够购买的最大宝石数量。
6.当right指针到达数组末尾时,结束循环,并输出能够购买的量最大宝石数量。
"""
def max_gems(gems, value):
    left = 0
    total = 0
    max_gems_count = 0
    for right in range(len(gems)):
        total += gems[right]
        while total > value:
            total -= gems[left]
            left += 1
        max_gems_count = max(max_gems_count, right - left + 1)
    return max_gems_count

# 输入处理
n = int(input().strip())
gems = [int(input().strip()) for _ in range(n)]
value = int(input().strip())

# 输出最多能购买的宝石数量
print(max_gems(gems, value))

