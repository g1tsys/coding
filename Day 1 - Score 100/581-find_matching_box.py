"""
The question involves identifying a box (from a list of boxes) that contains a string matching a given password `K`. The password `K` is a string of **ascending, non-repeating lowercase letters**. Each box has a string `s`, and we need to extract all the **letters** (ignoring case) from `s`, sort them in **ascending order**, and check if the resulting string matches `K`. If it does, return the **box number** (1-based index). If no box matches, return `-1`.

---

### 🐍 Python Language Thought Process

1. **Extract letters** from each string `s` in the boxes, ignoring case.
2. **Sort** the extracted letters in ascending order.
3. **Compare** the sorted string with the given password `K`.
4. **Return the box number** if there's a match. If no match is found, return `-1`.

---

### 📌 Example Walkthrough

#### Input:

Key: "abc"
Boxes: ["Abc", "aBcD", "xyz", "aBc", "AbCDefg"]


#### Steps:
1. **Box 1** (`"Abc"`): Extract letters → `['A', 'b', 'c']` → lowercase → `['a', 'b', 'c']` → sorted → `"abc"` → **Matches**.
2. **Box 2** (`"aBcD"`): Extract letters → `['a', 'B', 'c', 'D']` → lowercase → `['a', 'b', 'c', 'd']` → sorted → `"abcd"` → **No match**.
3. **Box 3** (`"xyz"`): Sorted → `"xyz"` → **No match**.
4. **Box 4** (`"aBc"`): Sorted → `"abc"` → **Matches**.
5. **Box 5** (`"AbCDefg"`): Sorted → `"abcdefg"` → **No match**.

#### Output:
Since **Box 1** is the **first** match, return `1`.


"""




def find_matching_box(key, boxes):
    """
    :param key: 密码字符串，由小写字母组成且按升序排列
    :param boxes: 箱子列表，每个元素是一个字符串
    :return: 返回符合条件的箱子编号，如果没有符合的返回-1
    """
    # 确保密码为升序且无重复的小写字母
    key = ''.join(sorted(set(key)))  # 对key中的字符去重并排序

    # 遍历每一个箱子的字符串
    for i, box in enumerate(boxes, start=1):  # 使用enumerate从1开始编号
        # 提取当前字符串中的所有字母字符，并将其转换为小写
        letters = [char.lower() for char in box if char.isalpha()]

        # 对提取的字母列表去重排序后转换为字符串
        password = ''.join(sorted(set(letters)))

        # 严格检查生成的密码是否与key完全匹配
        if password == key and len(letters) == len(key):  # 限制生成密码的长度必须匹配
            return i

    # 如果遍历完所有箱子都没有找到符合条件的，返回-1
    return -1

# 获取输入
key = input().strip()  # 使用strip去除输入字符串两端的空格
boxes = input().strip().split()  # 使用split分隔字符串为列表

# 调用函数并打印结果
result = find_matching_box(key, boxes)
print(result)

