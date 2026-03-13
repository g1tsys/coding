"""
给定一个表达式，求其分数计算结果
表达式的限制如下:
1、所有的输入数字皆为正整数(包括0)
2、仅支持四则运算(±*/)和括号
3、结果为整数或分数，分数必须化为最简格式(比如6，314，718，9017)
4、除数可能为0，如果遇到这种情况，直接输出"ERROR"
5、输入和最终计算结果中的数字都不会超出整型范围
白输入输出 a
输入
字符串格式的表达式，仅支持+*，数字可能超过两位，可能带有空格，没有负数，长度小干200个字符
输出
表达式结果，以最简格式表达
如果结果为整数，那么直接输出整数
如果结果为分数，那么分子分母不可再约分，可以为假分数，不可表达为带分数结果可能是负数，负号放在最前面

1.首先，定义了一个函数 parse_fraction 用于将字符串转换为分数对象。如果无法转换，则返回None.
2.然后，定义了一个函数 simplify_fraction 用于将分数化简为最简形式。如果分母为1，则直接输出分子部分。否则，输出分子和分母之间用"/"连接。
3.接着，定义了一个函数 evaluate 用于求解表达式的值。这个函数使用递归的方式对表达式进行解析和计算。
4.在 evaluate 函数内部，定义了一个辅助函数 next token 用于获取下一个token。
香的一前家国多另外，定义了一个辅助函数 calculate 用于根据操作符计算两个数的结果。
6.factor 函数用于解析括号内的表达式或数字。首先获取一个token，如果是”("，则递归调用expression 函数解析括号内的表达式，并丢弃”)"。如果是数字，则调用 parse fraction 函数将其转换为分数对象。
term 函数用于解析乘除法。首先获取一个因子作为结果，然后循环判断下一个token是否是乘法或除法的操作符，如果是，则获取下一个因子，并根据操作符计算结果。如果除法操作符的右操作数为0，则抛出ZeroDivisionError异常。
expression 函数用于解析加减法。首先获取一个项作为结果，然后循环判断下一个token是否是8加法或减法的操作符，如果是，则获取下一个项，并根据操作符计算结果。
最后，使用正则表达式将输入的表达式分割成tokens。然后调用 evaluate 函数求解表达式的结9.
果，并调用 simplify fraction 函数将结果化简为最简分数形式。
10.如果在计算过程中遇到除数为0的情况，则捕获zeroDivisionError异常，并返回"ERROR"作为结果。
"""

import re
from fractions import Fraction

def compute(expression):
    def parse_fraction(part):
        # 尝试将字符串转换为Fraction对象
        try:
            return Fraction(part)
        except ValueError:
            return None
    
    def simplify_fraction(result):
        # 确保结果为最简分数形式
        if result.denominator == 1:
            return str(result.numerator)
        return f"{result.numerator}/{result.denominator}"

    def evaluate(tokens):
        def next_token():
            # 获取下一个token
            return tokens.pop(0) if tokens else None
        
        def calculate(a, op, b):
            # 根据操作符计算结果
            if op == '+': return a + b
            if op == '-': return a - b
            if op == '*': return a * b
            if op == '/': return a / b
        
        def factor():
            # 解析括号内表达式或数字
            token = next_token()
            if token == '(':
                result = expression()
                next_token()  # 丢弃 ')'
                return result
            return parse_fraction(token)
        
        def term():
            # 解析乘除法
            result = factor()
            while tokens and tokens[0] in ('*', '/'):
                op = next_token()
                right = factor()
                if op == '/' and right == 0:
                    raise ZeroDivisionError
                result = calculate(result, op, right)
            return result
        
        def expression():
            # 解析加减法
            result = term()
            while tokens and tokens[0] in ('+', '-'):
                op = next_token()
                result = calculate(result, op, term())
            return result
        
        return expression()

    # 分割表达式成tokens
    tokens = re.findall(r'\d+|/|\*|\+|\-|\(|\)', expression)
    # 计算结果
    try:
        result = evaluate(tokens)
        return simplify_fraction(result)
    except ZeroDivisionError:
        return "ERROR"

print(compute("1+5*7/8"))  

