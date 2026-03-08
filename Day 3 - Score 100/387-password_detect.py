'''
给定用户密码输入流input,输入流中字符'<表示退格,可以清除前一个输入的字符,请你编写程序,输出最终得到
的密码字符,并判断密码是否满足如下的密码安全要求。
密码安全要求如下:
1、密码长度>=8;
2、密码至少需要包含1个大写字母;
3、密码至少需要包含1个小写字母;
密码至少需要包含1个数字;
5、密码至少需要包含1个字母和数字以外的非空白特殊字符;
注意空串退格后仍然为空串,且用户输入的字符串不包含'<'宇符和空白字符;
输入输出
输入
用一行字符串表示输入的用户数据,输入的字符串中<'字符标示识退格,用户输入的字符串不包含空白字符,例如:
ABC<c89%000<

输出
输出经过程序处理后,输出的实际密码字符串,并输出改密码字符串是否满足密码安全要求。两者间由','分隔,例
如:ABc89%00,true

Python 语言思路
1、思路是先定义一个函数is_valid_password来检查密码是否满足密码安全要求。函数中使用了一些内置函数和列表推导
式来判断密码中是否包含大写字母、小写字母、数字和特殊字符,并检查密码长度是否大于等于8。
2、然后定义了另一个函数process input来处理输入流。1函数中创建了一个空列表password用于构建最终的密码。遍历输
入流中的字符,如果遇到退格符号且密码列表中有字符,则移除最后一个字符;否则,将字符添加到密码列表中。
3、最后,将密码列表转换成字符串final_password,并调用is_valid_password函数来检查最终的密码是否满足密码安全
要求。将最终的密码和是否满足密码安全要求的结果转换成字符串,并返回
'''


def is_valid_password(password):
    # 检查密码是否满足以下条件：
    has_upper = any(c.isupper() for c in password)  # 至少包含一个大写字母
    has_lower = any(c.islower() for c in password)  # 至少包含一个小写字母
    has_digit = any(c.isdigit() for c in password)  # 至少包含一个数字
    has_special = any(not c.isalnum() for c in password)  # 至少包含一个特殊字符
    is_long = len(password) >= 8  # 密码长度至少为8
    
    # 必须满足所有条件
    return all([has_upper, has_lower, has_digit, has_special, is_long])

def process_input(input_stream):
    password = []  # 用于构建最终密码的列表
    for char in input_stream:
        if char == '<':
            # 如果遇到退格符号且密码列表中有字符，则移除最后一个字符
            if password:
                password.pop()
        else:
            # 否则，将字符添加到密码列表中
            password.append(char)
    
    # 将密码列表转换成字符串
    final_password = ''.join(password)
    # 检查最终的密码是否满足安全要求
    valid = is_valid_password(final_password)
    # 返回最终的密码以及它是否满足密码安全要求（转换成小写的'true'或'false'）
    return f"{final_password},{str(valid).lower()}"

# 示例使用
input_data = "ABC<c89%000<"
output = process_input(input_data)
print(output)
