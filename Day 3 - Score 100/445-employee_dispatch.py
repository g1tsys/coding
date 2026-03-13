"""
·题目措述
某公司部门需要派遣员工去国外做项目，现在，代号为x的国家和代号为y的国家分别需要cnbx名和cnty名员工，部门每个员工有一个员工号(1，2，3..)，工号连续，从1开始
部长派遣员工的规则:
1、从[1，w中选择员工派遣出去
2、编号为x的倍数的员工不能去x国;编号为y的倍数的员工不能去y国
问题:找到最小的k，使得可以将编号在[1，K中的员工分配给x国和y国，且满足x国和y国的需
求
宁输入输出 Q
输入
四个整数x，y;cnbx;cnty;(2<=x<y<=30000;x和y一定是质数;1<=cntx;cnty<10^9;cnbx+cnty<=10^9)
输出
满足条件的最小的k

输入
2 3 3 1

输出
5

说明:
输入说明:
2-表示国家代号2
3-表示国家代号3
3-表示国家2需要3个人
1-表示国家3需要1个人

输入
2 3 1 1

输出
2

输入
2 5 100000000 100000000

输出
222222222

输入
3 13 500000000 500000000

输出
1026315789     //这个为正常情况下K取Long.MAX_VALUE的输出

1000000001     //这个为100%通过率的输出，K取的1e9

输入
3 1 5 7

输出
9223372036854775808     //这个为正常情况下K取Long.MAX_VALUE的输出

1000000001     //这个为100%通过率的输出，K取的1e9

Python四语言思路
1.确定搜索范围: 首先，我们需要确定一个搜索范围。由于要派遣的员工数量不能小于两个国家需求的总和，所以搜索范围的下限是cntX+cntY。而搜索范围的上限可以选择一个足够大的数，如1e9.
2.二分查找: 使用二分查找算法来逐步缩小搜索范围，直到找到满足条件的最小的k值。每次选代中，我们计算中间值mid，并计算在范围[1,mid]内不能去特定国家的员工数量。
3.计算实际需求和可派遣员工数: 对于中间值mid，我们需要计算两个国家的实际需求以及在这个范围内可派遣的员工数。然后，根据不能去某个国家的员工数量，计算出实际需要派遣的员工数0
4.调整搜索范围: 如果实际需要派遣的员工数量小于等于可派遣的员工数，说明这个范围内的员工数量可以满足需求，我们就将搜索范围缩小到左半部分;否则，我们将搜索范围缩小到右半部分。
5.找到最小k值: 当搜索范围缩小到左右指针相遇时，此时的左指针就是满足条件的最小的k值,
"""

//此代码设置k为1e9的范围
def calculate_unavailable_workers(k, divisor):
    """
    计算在给定的员工范围[1, k]中，不能去特定国家（编号为divisor的倍数）的员工数。
    """
    return k // divisor  # 返回不能去特定国家的员工数，即员工号为divisor的倍数的数量


def calculate_needs(cnt, unavailable, common_unavailable):
    """
    计算还需要为某国分配的员工数，减去因特定规则（如是某数的倍数）而不能去的员工数。
    """
    return max(0, cnt - (unavailable - common_unavailable))  # 返回某国还需要的员工数，考虑了特定规则下不能去的员工数


def find_minimum_k(x, y, cntX, cntY):
    """
    使用二分查找算法找出满足所有条件的最小k值。
    """
    left, right = cntX + cntY, 1e9  # 设置搜索的初始范围

    while left <= right:
        mid = (left + right) // 2  # 中间值
        cantGoX = calculate_unavailable_workers(mid, x)  # 不能去x国的员工数
        cantGoY = calculate_unavailable_workers(mid, y)  # 不能去y国的员工数
        cantGoBoth = calculate_unavailable_workers(mid, x * y)  # 同时不能去x国和y国的员工数

        actualNeedX = calculate_needs(cntX, cantGoY, cantGoBoth)  # x国实际需要的员工数
        actualNeedY = calculate_needs(cntY, cantGoX, cantGoBoth)  # y国实际需要的员工数
        available = mid - cantGoX - cantGoY + cantGoBoth  # 可以派遣的员工数

        if actualNeedX + actualNeedY <= available:  # 如果满足条件
            right = mid - 1  # 缩小搜索范围
        else:
            left = mid + 1  # 扩大搜索范围

    return int(left)  # 返回最小满足条件的k值


def main():
    # 接收输入
    x, y, cntX, cntY = map(int, input().split())

    # 输出最小满足条件的k值
    print(find_minimum_k(x, y, cntX, cntY))


if __name__ == "__main__":
    main()

