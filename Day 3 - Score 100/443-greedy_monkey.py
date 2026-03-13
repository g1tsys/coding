"""
·题目描述
一只贪吃的猴子，来到一个果园，发现许多串香蕉排成一行，每串香蕉上有若干根香蕉。每串香蕉的根数由数组numbers给出。猴子获取香蕉，每次都只能从行的开头或者未尾获取，并且只能获取N次，求猴子最多能获取多少根香蕉.
输入输出 a
输入
第一行为数组numbers的长度第二行为数组numbers的值每个数字通过空格分开第三行输入为N，表示获取的次数
输出
能获取的最大数值

输入
7
1 2 2 7 3 6 1
3

输出
10

输入
3
1 2 3
3

输出
6

说明
全部获取所有的香蕉，因此最终根数为1+2+3 = 6

输入
4
4 2 2 3
2

输出
7

说明
第一次获取香蕉为行的开头，第二次获取为行的末尾，因此最终根数为4+3 =7


1、首先，通过 sum(numbers)计算出所有香蕉的总数，将其保存在变量 total 中。
2、然后，通过 len(numbers)-N计算出窗口的大小，即每次获取香蕉后剩余的香蕉数量。
3、接下来，使用 sum(numbers[:window_size])计算出初始窗口的香蕉数量，并将其保存在变量window sum 中。
4、然后，使用变量 window _sum 保存当前窗口的香蕉数量，并使用变量min_window_sum 保存最小窗口的香蕉数量。
5、通过循环，从窗口的右侧移动窗口，更新窗口的香蕉数量，并更新最小窗口的香蕉数量
6、最后，通过 total - min_window sum 计算出猴子能够获取的最大香蕉数量，并将其作为函数的返回值。
7、在 main 函数中，首先通过 int(input())获取数组 Q numbers 的长度，并将其保存在变量length 中。
8、然后，通过 list(map(int，input().split()))获取数组 numbers 的值，并将其保存在变量numbers 中。
9、接下来，通过 int(input())获取获取次数 N
10、最后，调用 max_banana函数，将数组 numbers 和获取次数N作为参数传入，并将返回结果打印翰出。
"""

def max_banana(numbers, N):
    total = sum(numbers)  # 计算香蕉的总数
    window_size = len(numbers) - N  # 窗口的大小，即每次获取香蕉后剩余的香蕉数量
    window_sum = sum(numbers[:window_size])  # 初始窗口的香蕉数量

    min_window_sum = window_sum  # 最小窗口的香蕉数量

    # 从窗口的右侧移动窗口，更新窗口的香蕉数量，并更新最小窗口的香蕉数量
    for i in range(window_size, len(numbers)):
        window_sum = window_sum - numbers[i-window_size] + numbers[i]
        min_window_sum = min(min_window_sum, window_sum)

    # 返回总数减去最小窗口和，即猴子可以拿到的最大香蕉数
    return total - min_window_sum


if __name__ == "__main__":
    length = int(input())  # 输入数组numbers的长度
    numbers = list(map(int, input().split()))  # 输入数组numbers的值
    N = int(input())  # 输入获取的次数
    print(max_banana(numbers, N))

