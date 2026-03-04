"""
Problem Description
Given two character sets: one is the full character set, and the other is the occupied character set. Characters in the occupied character set can no longer be used.
It is required to output the remaining available character set.
Input and Output Q
Input
1. The input string must contain @. The part before @ is the full character set, and the part after @ is the occupied character set.
2. The characters in the occupied character set must be from the full character set.
3. Characters in the character set are separated by English commas.
4. Each character is expressed in the form of "character + number" separated by an English colon. For example, a:1 represents one 'a' character.
5. Only English letters are considered as characters, and case is distinguished.
6. Numbers are positive integers not exceeding 100.
7. The @ symbol still exists even if no characters are occupied.
8. For example: a:3,b:5,c:2@
Output
1. Output the available character set.
2. Different output character sets are separated by line breaks.
3. Note that the order of output characters must be consistent with the input order.
4. Do not output b:3,a:2,c:2.
5. If a certain character is completely occupied, it does not need to be output.
Sample 1
java
Al writes code
Copy
Input
a:3,b:5,c:2@a:1,b:2
2
3
Output
a:2,b:3,c:2
5
6
Explanation:
8
9
The full character set is three a's, five b's, and two c's.
Expand

1. First, define a function parse_character_set to parse a character set string into a dictionary. This function takes a string as a parameter in the format "a:3,b:5,c:2" and returns a dictionary in the format {'a':3, 'b':5, 'c':2}. The specific steps are as follows:
- Initialize an empty dictionary char_dict to store characters and their quantities.
- Split the input string using commas to get a list of each character and its quantity.
- Iterate over each element in the list, split each element using a colon to get two parts: the character and the quantity.
- Convert the quantity to an integer and store it in the dictionary char_dict, with the character as the key and the quantity as the value.
- Return the dictionary char_dict.

2. Define a function calculate_remaining_characters to calculate and return the remaining character set. This function takes an input string as a parameter in the format "full character set@used character set" and returns the string representation of the remaining character set. The specific steps are as follows:
- Split the input string using the @ symbol to get two parts: the full character set and the used character set.
- Call the parse_character_set function respectively to parse the full character set and the used character set into dictionary forms, obtaining the full character set dictionary full_set_dict and the used character set dictionary used_set_dict.
- Iterate over the used character set dictionary used_set_dict. For each character and its quantity, check if the character exists in the full character set dictionary full_set_dict. If it exists, subtract the used quantity from the quantity of the corresponding character in the full character set dictionary.
- If the quantity of a character is 0 or negative, remove that character from the full character set dictionary.
- Construct the string representation of the remaining character set. Use a list comprehension to format each key-value pair in the full character set dictionary into the form "character:quantity" and separate them with commas.
- Return the resulting string.

3. In the main program, first read the input string input_str. Then call the calculate_remaining_characters function, pass input_str as a parameter, and print the returned result.
"""


def parse_character_set(s):

    char_dict = {}  # 初始化一个空字典来存储字符及其数量
    characters = s.split(',')  # 使用逗号分割字符串，得到每个字符及其数量的列表
    for char in characters:
        if char:  # 确保字符串非空
            key, value = char.split(':')  # 分割每个字符及其数量
            char_dict[key] = int(value)  # 转换数量为整型并存入字典
    return char_dict

def calculate_remaining_characters(input_str):

    full_set, used_set = input_str.split('@')  # 分割输入字符串为全量字符集和已占用字符集
    full_set_dict = parse_character_set(full_set)  # 解析全量字符集到字典
    used_set_dict = parse_character_set(used_set)  # 解析已占用字符集到字典

    # 遍历已占用字符集，减去相应的字符数量
    for char, count in used_set_dict.items():
        if char in full_set_dict:  # 确保字符在全量字符集中
            full_set_dict[char] -= count  # 减去已占用的数量
            if full_set_dict[char] <= 0:
                del full_set_dict[char]  # 如果某字符数量为0或负数，则从字典中删除

    # 构建并返回结果字符串
    result = ','.join(f'{char}:{count}' for char, count in full_set_dict.items())
    return result

# 动态输入部分
if __name__ == "__main__":
    input_str = input()
    print(calculate_remaining_characters(input_str))


