'''
题目描述
提取字符串中的最长合法简单数学表达式,字符串长度最长的,并计算表达式的值。如果没有,则返回0
简单数学表达式只能包含以下内容:0-9数字,符号+*/
说明:
1、所有数字,计算结果都不超过long
2、如果有多个长度-样的,请返回第一个表达式的结果
3、数学表达式,必须是最长的,合法的
4、操作符不能连续出现,如+--+1不合法的
输入输出Q
输入
第一行为输入字符串
输出
最长数学表达式的结果

1.首先,定义一个空栈stack、一个变量num(用于记录当前数文字)和一个变量sign(用于记录当前的操作符,默认
为"+")。
2.定义一个集合operators,包含合法的操作符"+*"。
3.为了简化计算过程,我们在表达式末尾添加一个额外的操作符"+"+"
4.遍历字符串中的每个字符,执行以下操作:
。如果字符是数字,则将其转换为整数,并累加到num上。
。如果字符是操作符,则根据sign的值进行相应的操作:
如果sign是"+",则将num入栈。
·如果sign是"-",则将-num入栈。
·如果sign是"*",则将num与栈顶元素相乘,并将结果替换钱顶元素。
·将num重置为0,并将sign更新为当前操作符。
5.最后,计算找中所有元素的和,即为最长合法简单数学表达式的结果。
接下来是找到最长合法简单数学表达式Q的过程:
1.初始化变量max_length为0,max_expr为空字符串。
2.定义一个合法字符集valid chars,包含数字和合法的操作符。
3.使用两个指针start和end,分别指向当前表达式的起点和结结束位置
4.外层循环,遍历字符串中的每个字符作为表达式的起点。
5.内层循环,从起点开始向后遍历,寻找合法字符并记录结束立置。
6.内层循环结束后,判断当前表达式是否为合法表达式。
。首先,将表达式中的"-"替换为"+"。
。然后,统计表达式中的"+"的数量,如果数量大于0,表示是合合法表达式
7.如果是合法表达式且长度大于之前的最长表达式,更新最长寿表达式和长度。
8.外层循环结束后,根据最长表达式计算结果,并返回结果。
'''

def evaluate(expression):
    # 如果表达式为空，则直接返回0
    if not expression:
        return 0
    # 初始化栈、当前数字和当前符号
    stack, num, sign = [], 0, "+"
    # 定义操作符集合
    operators = set("+-*")
    # 在表达式末尾添加一个"+"，以方便处理最后一个数字
    expression += "+"
    for char in expression:
        if char.isdigit():
            # 累积数字
            num = num * 10 + int(char)
        elif char in operators:
            # 根据前一个符号进行计算，并将结果放入栈中
            if sign == "+":
                stack.append(num)
            elif sign == "-":
                stack.append(-num)
            elif sign == "*":
                # 乘法直接作用于栈顶元素
                if stack:
                    stack[-1] = stack[-1] * num
                else:
                    # 如果表达式以"*"开始，视作乘以1
                    stack.append(num)
            # 重置当前数字，并更新当前符号
            num, sign = 0, char
    # 将栈中所有数字相加得到结果
    return sum(stack)

def find_longest_valid_expression(s):
    max_length = 0
    max_expr = ""
    # 定义合法字符集合
    valid_chars = set("1234567890+-*")

    start = 0
    while start < len(s):
        end = start
        # 找到一个可能的表达式
        while end < len(s) and s[end] in valid_chars:
            end += 1
        # 回退并找到最长的合法表达式
        while end > start:
            if s[start:end].lstrip("-").replace("-", "+").replace("*", "+").count("+") > 0:
                length = end - start
                if length > max_length:
                    max_length = length
                    max_expr = s[start:end]
                break
            end -= 1
        start += 1

    # 如果找到了合法的表达式，则计算其结果，否则返回0
    if max_expr:
        return evaluate(max_expr)
    else:
        return 0

# 输入输出部分
input_str = input().strip()
print(find_longest_valid_expression(input_str))
