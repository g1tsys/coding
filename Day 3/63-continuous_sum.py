"""
题目描述
一个整数可以由连续的自然数之和来表示;给定一个整数,计算真该整数有几种连续自然数之和的表达
式,且打印出每种表达式
输入输出
输入
一个目标整数T(1<=T<=1000)
输出
该整数的所有表达式和表达式的个数。如果有多种表达式,输出出要求为:
1、自然数个数最少的表达式优先输出
2、每个表达式中按自然数递增的顺序输出,具体的格式参见样例。
3、在每个测试数据结束时,输出-行"Result.X",其中X是最终的表达式个数。

Problem Description
An integer can be expressed as the sum of consecutive natural numbers. Given an integer, calculate how many such expressions exist for that integer and print each expression.

Input and Output
Input
A target integer T (1 ≤ T ≤ 1000)

Output
All expressions of the integer and the number of expressions. If there are multiple expressions, the output requirements are:
1. Expressions with the fewest number of natural numbers are output first.
2. Each expression is output in the increasing order of natural numbers; refer to the sample for the specific format.
3. At the end of each test data, output a line "Result: X", where X is the total number of expressions.

Python语言 思路
1、首先,我们需要遍历所有可能的连续自然数序列的长度n。假没当前长度为n,那么序列的第一个数可以取
值从1到×,其中x是满足条件的首项。
2、为了确定首项x,我们可以利用等差数列的求和公式来计算连续读自然数序列的和。根据公式,连续自然数序
列的和等于首项乘以长度n加上长度n减1的和的一半。即:x*n+n*(n-1)/2
3、如果计算得到的连续自然数序列的和等于目标整数T,则找到了一个满足条件的表达式。我们将该表达式添
加到结果中,并增加表达式的计数。
4、最后,按照自然数个数从小到大的顺序输出所有的表达式。
总结来说,该算法Q通过遍历连续自然数序列的长度,并计算首项,来判断是否存在满足条件的连续自然数
序列。如果存在,则将表达式添加到结果中。这样可以找到所有满足条件的连续自然数序列,并输出结果。

Python Language Approach
1. First, we need to iterate through all possible lengths n of consecutive natural number sequences. Assuming the current length is n, the first number of the sequence can take values from 1 to x, where x is the first term that satisfies the condition.
2. To determine the first term x, we can use the sum formula of an arithmetic sequence to calculate the sum of the consecutive natural number sequence. According to the formula, the sum of the consecutive natural number sequence is equal to the first term multiplied by the length n plus half of the sum of (length n minus 1). That is: x*n + n*(n-1)/2
3. If the calculated sum of the consecutive natural number sequence is equal to the target integer T, then a satisfying expression is found. We add this expression to the result and increment the count of expressions.
4. Finally, output all expressions in ascending order of the number of natural numbers.
In summary, this algorithm Q finds all satisfying consecutive natural number sequences by iterating through the lengths of the consecutive natural number sequences, calculating the first term, and determining if there exists a consecutive natural number sequence that meets the condition. If it exists, the expression is added to the result. This way, all satisfying consecutive natural number sequences can be found and the results can be output.

"""
def printExpressions(T):
    count = 0

    for n in range(1, int((2 * T) ** 0.5) + 1):
        # 计算首项
        x = (2 * T - n * (n - 1)) // (2 * n)

        # 如果首项满足条件，输出表达式
        if x * n + n * (n - 1) // 2 == T:
            count += 1
            print(f'{T}=', end='')
            for i in range(n):
                print(x + i, end='')
                if i != n - 1:
                    print('+', end='')
            print()

    print(f'Result:{count}')

T = int(input())
printExpressions(T)



