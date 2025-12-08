"""
The problem is as follows:

### **Problem Description**
A group of geese is flying south, and a string is given that represents the sounds heard by tourists on the ground. Your task is to determine the **minimum number of geese** that could have made these sounds.

### **Rules**
- Each goose emits the full sound **"quack"** in sequence. That is, the characters **'q'**, **'u'**, **'a'**, **'c'**, **'k'** must appear in that specific order to count as a complete "quack" from one goose.
- If a string contains characters other than **'q'**, **'u'**, **'a'**, **'c'**, **'k'**, return **-1**.
- If no complete "quack" is found in the string, return **-1**.

### **Example**
Let’s walk through an example.

#### **Input:**
```
"ququackcak"
```

#### **Step-by-step Walkthrough:**
1. We need to identify all complete "quack" sequences in the string.
2. The string is: **q u q u a c k c a k**
3. We can break it down:
   - First "quack" is formed from positions: **q (0)**, **u (1)**, **a (4)**, **c (5)**, **k (6)**.
   - Second "quack" is formed from positions: **q (2)**, **u (3)**, **a (7)**, **c (8)**, **k (9)**.
4. So, the total number of geese is **2**.

#### **Output:**
```
2
```

### **Key Idea**
- Track the positions of each character in the string.
- For each "q", find the next "u", then "a", then "c", then "k" in order.
- If all five characters are found in order for a goose, count it and continue.

Let me know if you'd like the code implementation for this problem.

"""


def result(quacks):
    q = []  # 用来记录字符"q"的位置
    u, a, c = 0, 0, 0  # 分别记录字符"u", "a", "c"的数量
    rans = []  # 用来存储符合要求的大雁叫声的起始和结束位置
    for i in range(len(quacks)):
        char = quacks[i]
        if char == "q":
            q.append(i)  # 将字符"q"的位置添加到q列表中
        elif char == "u":
            if u + 1 <= len(q):
                u += 1  # 如果字符"u"的数量小于等于q的长度，则字符"u"符合要求
        elif char == "a":
            if a + 1 <= u:
                a += 1  # 如果字符"a"的数量小于等于字符"u"的数量，则字符"a"符合要求
        elif char == "c":
            if c + 1 <= a:
                c += 1  # 如果字符"c"的数量小于等于字符"a"的数量，则字符"c"符合要求
        elif char == "k":
            if c >= 1:
                rans.append([q.pop(0), i])  # 如果字符"c"的数量大于等于1，则找到一只大雁，将其起始和结束位置添加到rans中
                u -= 1  # 匹配到一只大雁后，将字符"u", "a", "c"的数量减1
                a -= 1
                c -= 1
        else:
            return -1  # 如果字符串中的字符不是"q", "u", "a", "c", "k"中的一个，则返回-1
    if len(rans) == 0:
        return -1  # 如果没有找到一只大雁，则返回-1
    ans = 1
    for i in range(len(rans)):
        cnt = 1
        for j in range(i+1, len(rans)):
            if rans[i][1] >= rans[j][0]:
                cnt += 1  # 统计在同一时间内叫声的大雁数量
        ans = max(ans, cnt)  # 更新最大的大雁数量
    return ans

quacks = input("大雁叫声: ")
print(result(quacks))

