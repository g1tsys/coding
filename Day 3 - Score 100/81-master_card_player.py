"""
题目描述
给定一个长度为n的整型数组,表示一个选手在n轮内可选择的牌面分数。选手基于规则选牌,请计算所
有轮结束后其可以获得的最高总分数。
选择规则如下:
1、在每轮里选手可以选择获取该轮牌面,则其总分数加上该轮牌面分数,为其新的总分数。
2、选手也可不选择本轮牌面直接跳到下一轮,此时将当前i总分数还原为3轮前的总分数,若当前轮次小于
等于3(即在第1、2、3轮选择跳过轮次),则总分数置为0。
3、选手的初始总分数为0,且必须依次参每一轮。
输入输出 Q
输入
第一行为一个小写逗号分割的字符串,表示n轮的牌面分数,1<=n<=20.
分数值为整数,-100<=分数值<=100。
不考虑格式问题。
输出
所有轮结束后选手获得的最高总分数。

Given an integer array of length n, which represents the card scores a player can choose from in n rounds. The player selects cards based on the rules; please calculate the maximum total score they can obtain after all rounds.

The selection rules are as follows:
1. In each round, the player can choose to take the card of the current round, and their total score will be increased by the score of this round's card to form the new total score.
2. The player can also choose not to take the current round's card and directly skip to the next round. In this case, the current total score will be reverted to the total score from 3 rounds ago. If the current round number is less than or equal to 3 (i.e., choosing to skip the round in the 1st, 2nd, or 3rd round), the total score will be set to 0.
3. The player's initial total score is 0, and they must participate in each round in sequence.

Input and Output a
Input
The first line is a string separated by lowercase commas, representing the card scores of n rounds, where 1 <= n <= 20.
The score values are integers, ranging from -100 to 100.
Format issues are not considered.
Output
The maximum total score the player can obtain after all rounds.

Python语言 思路
1.输入处理:首先,代码将输入的字符串(由逗号分隔的分数)转换为整数列表。这些整数代表了每一轮中
选手可以获得的分数。
2.初始化动态规划数组:接着,初始化一个动态规划数组dp,其长度为n+1,其中n是输入分数的轮
数。dp[i]用于存储到第1轮结束时可能获得的最高总分数,初始总分分数设为0
3.动态规划逻辑:
对于前3轮(即i<=3的情况),选手可以选择获取该轮的牌面面分数,将总分加上该轮分数;或者
如果该操作导致总分数小于0,则可以选择跳过,将总分数置为00,
。对于第4轮及以后(即1>3的情况),选手除了可以选择获取该轮的牌面分数(并将其加到总分
上)外,还可以选择不获取本轮分数,而是将总分还原为3轮前的的总分数。这里的关键决策是在于选
择"获取当前轮分数加上之前的总分"与"3轮前的总分数"之间的较大者。
4.输出最高分:最终,dp[n]存储的就是所有轮结束后选手可以获得的最高总分数,即为所求的答案。
样例分析
以样例1,-5,-6,4,3,6,-2为例,动态规划 数组Qdp的更新行过程如下:
在前3轮结束时,选手会选择在第一轮获得1分,第二轮和第三轮跳过,分数分别是1,1,1(因为选择跳过
会让分数保持在更高的1分,而不是加上负分或者重置为0)。
从第4轮开始,选手开始有了更多的选择。在第4轮可以获得额外的4分,使得总分达到5分。之后,选手会
选择在第5轮和第6轮获得分数,分别达到8分和14分。在最后一轮,选择跳过(因为添加-2会降低总
分),总分保持为11分。

Python Language Approach

1. Input Processing: First, the code converts the input string (scores separated by commas) into a list of integers. These integers represent the scores a player can obtain in each round.
2. Initialization of Dynamic Programming Array: Next, initialize a dynamic programming array dp with a length of n+1, where n is the number of rounds of the input scores. dp[i] is used to store the maximum total score that can be obtained by the end of the i-th round, with the initial total score set to 0.
3. Dynamic Programming Logic:
For the first 3 rounds (i.e., when i <= 3), the player can choose to take the face value score of the current round and add it to the total score; or if this operation causes the total score to be less than 0, they can choose to skip, setting the total score to 0.
For the 4th round and beyond (i.e., when i > 3), in addition to choosing to take the face value score of the current round (and adding it to the total score), the player can also choose not to take the current round's score and instead revert the total score to the total score from 3 rounds ago. The key decision here is to choose the larger value between "the current round's score plus the previous total score" and "the total score from 3 rounds ago".
4. Output the Highest Score: Finally, dp[n] stores the highest total score the player can obtain after all rounds, which is the desired answer.
Sample Analysis
Taking the sample 1, -5, -6, 4, 3, 6, -2 as an example, the update process of the dynamic programming array dp is as follows:
By the end of the first 3 rounds, the player will choose to get 1 point in the first round and skip the second and third rounds. The scores are 1, 1, 1 respectively (because choosing to skip keeps the score at the higher 1 point instead of adding negative points or resetting to 0).
Starting from the 4th round, the player has more choices. In the 4th round, an additional 4 points can be obtained, making the total score 5 points. After that, the player will choose to get scores in the 5th and 6th rounds, reaching 8 points and 14 points respectively. In the last round, they choose to skip (because adding -2 would reduce the total score), and the total score remains 14 points.
"""


def calculate_max_score(input_scores):
    # 将输入字符串转换为整型数组，这里输入的是一系列用逗号分隔的分数
    scores = list(map(int, input_scores.split(',')))

    # 动态规划，初始化dp数组。dp数组用于存储到每一轮为止可能获得的最高分数。
    n = len(scores)  # n为总轮数
    dp = [0] * (n + 1)  # 初始化一个长度为n+1的列表，初始值为0。dp[i]表示第i轮结束时的最高总分。

    # 遍历每一轮，计算每一轮的最高总分。i表示当前轮数。
    for i in range(1, n + 1):
        # 如果当前轮次小于等于3，则选手可以选择获取该轮牌面分数或将总分数置为0。
        if i <= 3:
            dp[i] = max(dp[i - 1] + scores[i - 1], 0)
        # 如果当前轮次大于3，则选手可以选择获取该轮牌面分数，或还原为3轮前的总分数。
        else:
            dp[i] = max(dp[i - 1] + scores[i - 1], dp[i - 3])

    # 最高总分数即为最后一轮结束后的总分，即dp数组的最后一个元素。
    return dp[n]


input_scores = input()
# 调用函数并打印结果
max_score = calculate_max_score(input_scores)
print(max_score)


