"""
# Problem Translation and Solution

## Problem Description

Given an input string containing only English letters (a-z, A-Z) and parentheses ( ):

**Rules:**
- Parentheses are always paired and never nested
- Letters inside the same parentheses are **equivalent** to each other
- Equivalence is **transitive**: if a≡b and b≡c, then a≡c
- Uppercase and lowercase of the same letter are **equivalent** (e.g., A≡a)
- Empty parentheses are allowed

**Task:** Simplify the string by:
1. Keep only characters **outside** parentheses (in original order)
2. Replace each character with its **lexicographically smallest** equivalent character
3. Output "0" if the result is empty

## Example Walkthrough

**Input:** `"never(dont)live(run)up(f)()"`

**Step 1: Extract equivalence groups**
- `(dont)` → {d, o, n, t}
- `(run)` → {r, u, n}
- `(f)` → {f}
- `()` → empty

**Step 2: Merge groups (transitive property)**
- Both groups contain 'n', so merge: {d, o, n, t, r, u}
- {f} remains separate

**Step 3: Find smallest equivalent for each group**
- {d, o, n, t, r, u} → smallest is 'd'
- {f} → smallest is 'f'

**Step 4: Process characters outside parentheses**
- Original: `n e v e r l i v e u p`
- Replace: n→d, e→e, v→v, r→d, u→d, p→p
- Result: `"devedgivedp"`

## Python Solution

```python
def simplify_string(s):
    # Union-Find (Disjoint Set) implementation
    parent = {}
    
    def find(x):
        if x not in parent:
            parent[x] = x
        if parent[x] != x:
            parent[x] = find(parent[x])  # Path compression
        return parent[x]
    
    def union(x, y):
        root_x, root_y = find(x), find(y)
        # Union by lexicographical order (smaller becomes parent)
        if root_x < root_y:
            parent[root_y] = root_x
        else:
            parent[root_x] = root_y
    
    # Parse the string
    outside_chars = []  # Characters outside parentheses
    inside_paren = False
    temp_group = []
    
    for char in s:
        if char == '(':
            inside_paren = True
            temp_group = []
        elif char == ')':
            inside_paren = False
            # Merge all characters in this group
            if temp_group:
                for i in range(len(temp_group) - 1):
                    union(temp_group[i], temp_group[i + 1])
                    # Also union uppercase/lowercase
                    union(temp_group[i].lower(), temp_group[i].upper())
        elif
"""



def find(x, fa, mnum):
    # 查找根节点
    if x != fa[x]:
        fa[x] = find(fa[x], fa, min(mnum, fa[x]))
    fa[x] = min(mnum, fa[x])
    return fa[x]

def unionSet(x, y, fa):
    # 合并集合
    x_fa = find(x, fa, fa[x])
    y_fa = find(y, fa, fa[y])

    if x_fa != y_fa:
        fa[max(x_fa, y_fa)] = min(x_fa, y_fa)

    return fa

def main():
    fa = [i for i in range(150)]  # 并查集初始化
    is_visited = [0] * 150  # 记录是否访问过
    s = input()  # 输入字符串
    q1 = []  # 存储未被括号包含的字符
    q2 = []  # 存储括号内的字符

    for c in s:
        if c == '(':
            temp = 1  # 记录进入括号内的标志
        elif c == ')':
            temp = 0  # 标志离开括号内
            if q2:
                i = ord(q2[0])

            while q2:
                fa = unionSet(i, ord(q2[0]), fa)  # 合并集合
                is_visited[ord(q2[0])] = 1  # 标记已访问

                if ord(q2[0]) >= ord('a'):
                    if is_visited[ord(q2[0]) - ord('a') + ord('A')] == 1:
                        fa = unionSet(ord(q2[0]) - ord('a') + ord('A'), ord(q2[0]), fa)  # 大写字母和小写字母等效
                else:
                    if is_visited[ord(q2[0]) + ord('a') - ord('A')] == 1:
                        fa = unionSet(ord(q2[0]) + ord('a') - ord('A'), ord(q2[0]), fa)  # 小写字母和大写字母等效

                q2.pop(0)

        elif temp == 0:
            q1.append(c)  # 括号外的字符加入q1列表
        else:
            q2.append(c)  # 括号内的字符加入q2列表

    if not q1:
        print(0)  # 如果q1为空，则输出0

    for char in q1:
        print(chr(find(ord(char), fa, ord(char))), end='')  # 输出每个字符的等效字符

if __name__ == "__main__":
    main()

