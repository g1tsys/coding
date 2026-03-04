"""
题目描述
主管期望你来实现英文输入法单词联想功能。
需求如下:
依据用户输入的单词前缀,从已输入的英文语句中联想出用户想输入的单词,按字典序输出联想到的单
词序列,如果联想不到,请输出用户输入的单词前缀。
注意:
1、英文单词联想时,区分大小写
2、缩略形式如"don't",判定为两个单词,"don"和"t"
3、输出的单词序列,不能有重复单词,只能是英文单词,不能有标点符号
输入输出区
输入
输入为两行。
首行输入一段由英文单词word和标点符号组成的语句str;
接下来一行为一个英文单词前缀pre。
0<wordlength() <= 20
0< str.length <= 10000
0<pre <= 20
输出
输出符合要求的单词序列或单词前缀,存在多个时,单词之间以单个空格分割

1.使用正则表达式将句子中的单词分割出来,并正确处理缩略形式。将句子中的单词提取出来并存储在一个
列表中。
2.将缩略词分割成两个单词。如果单词中含有撇号('),则将其分割成两个单词。例如,"don't"被分割
成"don"和"t"。
3.使用集合来存储唯一的单词。将提取出的单词存储在一个集合中,以去除重复的单词。
4.使用列表推导式找到所有以前缀开始的单词,注意区分大小写。遍历集合中的单词,找到所有以给定前缀
开头的单词,并存储在一个列表中。
5.如果有联想到的单词,则按字典序输出,否则输出前缀。如果找到到了以前缀开头的单词,则将这些单词按
字典序排序,并使用空格将它们连接起来作为输出。否则,否则,输出给定的前缀。

Problem Description
The supervisor expects you to implement the word association function of the English input method.
Requirements are as follows:
Based on the word prefix entered by the user, associate the word that the user wants to input from the already entered English sentences, output the associated word sequence in lexicographical order. If no association can be made, please output the word prefix entered by the user.
Notes:
1. When associating English words, case is distinguished.
2. Contractions such as "don't" are judged as two words, "don" and "t".
3. The output word sequence must not contain duplicate words, must only be English words, and must not contain punctuation marks.

Input and Output Area
Input
The input consists of two lines.
The first line inputs a sentence str composed of English words and punctuation marks;
The next line is an English word prefix pre.
0 < word length() <= 20
0 < str.length <= 10000
0 < pre length <= 20

Output
Output the qualified word sequence or word prefix. When there are multiple words, they are separated by a single space.

1. Use regular expressions to split the words in a sentence, and properly handle contractions. Extract the words from the sentence and store them in a list.
2. Split contractions into two words. If a word contains an apostrophe ('), split it into two words. For example, "don't" is split into "don" and "t".
3. Use a set to store unique words. Store the extracted words in a set to remove duplicate words.
4. Use a list comprehension to find all words that start with a given prefix, paying attention to case sensitivity. Iterate through the words in the set, find all words that start with the given prefix, and store them in a list.
5. If there are associated words, output them in lexicographical order; otherwise, output the prefix. If words starting with the prefix are found, sort these words in lexicographical order and concatenate them with spaces as the output. Otherwise, output the given prefix.
"""


import re


def word_suggestion(sentence, prefix):
    # 使用正则表达式将句子中的单词分割出来，并正确处理缩略形式
    # 注意：缩略形式如 "don't" 被视为两个单词 "don" 和 "t"
    words = re.findall(r'\b\w+(?:\'\w+)?\b', sentence)

    # 将缩略词分割成两个单词
    split_words = []
    for word in words:
        if "'" in word:
            split_words.extend(word.split("'"))
        else:
            split_words.append(word)

    # 使用集合来存储唯一的单词
    unique_words = set(split_words)

    # 使用列表推导式找到所有以前缀开始的单词，注意区分大小写
    suggested_words = sorted(word for word in unique_words if word.startswith(prefix))

    # 如果有联想到的单词，则按字典序输出，否则输出前缀
    return ' '.join(suggested_words) if suggested_words else prefix


# 读取两行输入
sentence = input().strip()
prefix = input().strip()

# 输出联想到的单词序列或单词前缀
print(word_suggestion(sentence, prefix))


