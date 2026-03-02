"""
### Problem Description
Sheep, wolves, and a farmer are at the riverbank. If the number of sheep is greater than the number of wolves when the farmer is away, the wolves will attack the sheep and the farmer will suffer a loss. The farmer has a boat with a fixed capacity that can carry a fixed number of animals.

The task is to find the **minimum number of trips** required to safely transport all sheep and wolves to the opposite bank without any losses.

Only the farmer's trips **to the opposite bank** are counted. During return trips, the farmer does not transport any sheep or wolves.

Note: The wolves will not attack the sheep if the farmer is present, or if the number of sheep is not greater than the number of wolves when the farmer is away.

---

### Input and Output

**Input:**
The first line contains three integers `M`, `N`, and `X`, which represent the number of sheep, the number of wolves, and the capacity of the boat, respectively.

**Output:**
Output the minimum number of trips required to safely transport all sheep and wolves to the opposite bank. If it is impossible to meet the conditions, output `0`.

---

Would you like me to also translate the corresponding solution approach for this problem?

# Python Language Approach
1.  Define a recursive function `getTransportTime` to represent the minimum number of trips required to transport animals under the current state. The function parameters include the number of sheep `m0` and wolves `n0` on the current bank, the boat capacity `x`, the number of sheep `m1` and wolves `n1` on the opposite bank, the number of trips already made `times`, and the current minimum number of trips `minTimes`.
2.  First, check if a single trip can transport all animals (i.e., if `x >= m0 + n0`). If so, return `times + 1` as the final result, indicating that only one more trip is needed.
3.  Otherwise, we try to select a certain number of sheep and wolves from the current bank to board the boat and proceed to the next level of recursion. The iteration range for the number of sheep is from 0 to `min(m0, x)`, and for the wolves, it is from 0 to `min(n0, x - 1)`.
4.  For each selection, we need to check if two conditions are met:
    *   After departure, the remaining animals on the original bank must be safe: either there are no sheep left, or the number of sheep is not greater than the number of wolves.
    *   The opposite bank must also meet the same condition: the number of sheep on the boat must not exceed the number of wolves.
5.  If both conditions are satisfied, perform a recursive call to `getTransportTime`, update the parameters to the new state after selecting the sheep and wolves, and pass `times + 1` as the number of trips for the recursive call.
6.  After the recursive call returns, update the minimum number of trips `minTimes` by comparing it with the number of trips returned, and keep the smaller value.
7.  Finally, return `minTimes` as the result.

---

Do you want me to also provide the full Python code implementation for this problem?
"""

def getTransportTime(m0, n0, x, m1, n1, times, minTimes):
    # 若可以一次性运走，结束了
    if x >= m0 + n0:
        return times + 1

    # 尝试运一部分狼一部分羊
    # 要上船的羊数量不可以超过岸上数量、也不可以超过船的容量
    for i in range(min(m0, x) + 1):
        # 要上船的狼的数量不可以超过岸上数量、也不可以超过船装了羊后的剩余的容量
        for j in range(min(n0, x - i) + 1):
            # 不可以不运
            if i + j == 0:
                continue
            # 船离岸后，原来这岸，要么没有羊，要么羊比狼多，才可以运；对岸也要检查，不考虑回程带动物
            if (m0 - i == 0 or m0 - i > n0 - j) and (m1 + i == 0 or m1 + i > n1 + j):
                # 运一次
                result = getTransportTime(m0 - i, n0 - j, x, m1 + i, n1 + j, times + 1, minTimes)
                # 如果获取了结果，和minTimes比较，但是不结束，继续检查
                if result < minTimes and result != 0:
                    minTimes = result

    return minTimes


# 主函数
def main():
    # 读取输入
    str_input = input()
    strs = str_input.split(" ")

    m0 = int(strs[0])  # 羊
    n0 = int(strs[1])  # 狼
    x = int(strs[2])  # 船
    m1 = 0
    n1 = 0

    # 初始化最少运输次数为无穷大
    minTimes = float('inf')

    result = getTransportTime(m0, n0, x, m1, n1, 0, minTimes)

    # 如果步数等于初始化数字，那么代表没找到运输方法
    if result == float('inf'):
        print(0)
    else:
        print(result)


# 调用主函数
if __name__ == "__main__":
    main()


