"""
题目描述
给定一个非空字符串S,其被N个'-'分隔成N+1的子串,给定正整数K,要求除第一个子串外,其
余的子串每K个字符组成新的子串,并用'-'分隔
对于新组成的每一个子串,如果它含有的小写字母比大写字母多,则将这个子串的所有大写字
母转换为小写字母;反之,如果它含有的大写字母比小写字母多,则将这个子串的所有小写字母
转换为大写字母;大小写字母的数量相等时,不做转换
输入输出
输入
输入为两行,第一行为参数K,第二行为字符串S
输出
输出转换后的字符串


1、将输入的数字k转换为整数,并将输入的字符串ㇽs赋给变量input_str
2、使用'-'作为分隔符,将input_str拆分为列表arr
3、提取arr列表中的第一个元素,并赋值给startStr。这是输入字符串中第一个"之前的部分
4、将arr列表中的其余部分(去掉第一个元素)连接成一个单独的字符串,并赋值给lastStr。这是输
入字符串中第一个"之后的所有部分
5、创建一个空字符串resLastStr用于存储 处理后的字符串
6、将lastStr字符串的每个字符逐个遍历,如果字符在每k个位置(除了开头)处,则在resLastStr中插
入一个一,然后将字符添加到resLastStr中。这样,resLastStr会在每k个位置处具有'
7、创建两个计数器countA和counta,用于分别统计大写字母和小写字母的数量
8、使用正则表达式 匹配大写字母和小写字母的模式regA和rega
9、将resLastStr按照·分隔符拆分为列表resLastStrArr,得到字符串的各个部分
10.遍历resLastStrArr中的每个部分,然后再遍历每个部分中的字符,统计大写字母和小写字母的数
量
11、根据每个部分中大写字母和小写字母的数量,将该部分转换为全大写或全小写
12、将转换后的部分重新放回resLastStrArr列表中
13、将startStr插入到resLastStrArr列表的开头
14、使用'''将resLastStrArr列表中的各个部分连接起来形成最终结果字符串res
15、将res作为函数的返回值
"""

import re

def strFun(k, s):
    # 将k转换为整数
    numk = int(k)
    # 将输入字符串赋给变量input_str（避免使用'str'作为变量名，因为它是一个内置函数）
    input_str = s

    # 使用'-'分隔符将输入字符串拆分为列表
    arr = input_str.split('-')

    # 提取第一个'-'之前的字符串部分
    startStr = arr[0]

    # 将第一个'-'之后的所有部分连接在一起，形成单个字符串
    arr1 = arr[1:]
    lastStr = ''.join(arr1)

    # 准备'resLastStr'字符串，在每个'numk'位置插入'-'
    resLastStr = ""
    for i in range(len(lastStr)):
        if i % numk == 0 and i != 0:
            resLastStr += '-'
        resLastStr += lastStr[i]

    # 初始化大写字母和小写字母的计数器
    countA = 0
    counta = 0

    # 定义用于匹配大写字母和小写字母的正则表达式模式
    regA = re.compile(r'[A-Z]')
    rega = re.compile(r'[a-z]')

    # 使用'-'分隔符将'resLastStr'字符串拆分为列表，得到字符串的各个部分
    resLastStrArr = resLastStr.split('-')

    # 遍历每个字符串部分，计算大写字母和小写字母的出现次数
    for j in range(len(resLastStrArr)):
        for i in range(len(resLastStrArr[j])):
            if regA.match(resLastStrArr[j][i]):
                countA += 1
            if rega.match(resLastStrArr[j][i]):
                counta += 1

        # 根据大写字母和小写字母的计数，将字符串部分转换为大写或小写
        if countA > counta:
            resLastStrArr[j] = resLastStrArr[j].upper()
        elif countA < counta:
            resLastStrArr[j] = resLastStrArr[j].lower()

        # 为下一个字符串部分重置计数器
        countA = 0
        counta = 0

    # 在列表开头插入'startStr'，然后使用'-'将所有部分连接起来形成最终结果
    resLastStrArr.insert(0, startStr)
    res = '-'.join(resLastStrArr)

    return res


print(strFun(12, '12abc-abCABc-4aB@'))
