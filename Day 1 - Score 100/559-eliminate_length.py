"""
# Translation: "Match Elimination Game" Problem

## Problem Description
**Game Rules:** Given a string containing only English letters, if two adjacent letters are the same, they can be eliminated. Repeatedly perform elimination operations on the string until no more eliminations are possible. Output the length of the final remaining string.

**Input:** 
- Original string `str`, containing only uppercase and lowercase English letters
- Letter case is sensitive
- String length ≤ 100

**Output:** 
- Length of the final string after the game ends

**Note:** If input contains non-English letters, return 0 (invalid input).

---

## Solution Approach

### Algorithm (Stack-based)

1. **Create an empty stack**
2. **Iterate through each character** in the input string:
   - **Validate:** Check if character is an English letter (a-z, A-Z). If not, return 0
   - **Elimination check:** If stack is not empty AND top of stack equals current character:
     - **Pop** the top element (elimination occurs)
   - **Otherwise:** Push current character onto stack
3. **Return** the size of the stack (length of final string)

### Key Insight
The stack naturally handles the "adjacent elimination" rule because:
- When we find a match with the stack top, we eliminate both
- This may expose a new pair that can be eliminated (cascading effect)

---

## Example Walkthrough

### Example 1: `"abba"`

| Step | Character | Stack State | Action |
|------|-----------|-------------|--------|
| 0 | - | `[]` | Initialize |
| 1 | 'a' | `['a']` | Push (stack empty) |
| 2 | 'b' | `['a', 'b']` | Push (top='a' ≠ 'b') |
| 3 | 'b' | `['a']` | Pop (top='b' = 'b') ✓ |
| 4 | 'a' | `[]` | Pop (top='a' = 'a') ✓ |

**Final Result:** Stack is empty → Length = **0**

---

### Example 2: `"aabbcc"`

| Step | Character | Stack State | Action |
|------|-----------|-------------|--------|
| 0 | - | `[]` | Initialize |
| 1 | 'a' | `['a']` | Push |
| 2 | 'a' | `[]` | Pop (match) ✓ |
| 3 | 'b' | `['b']` | Push |
| 4 | 'b' | `[]` | Pop (match) ✓ |
| 5 | 'c' | `['c']` | Push |
| 6 | 'c' | `[]` | Pop (match) ✓ |

**Final Result:** Stack is empty → Length = **0**

---

### Example 3: `"abccba"` (Cascading elimination)

| Step | Character | Stack State | Action |
|------|-----------|-------------|--------|
| 0 | - | `[]` | Initialize |
| 1 | 'a' | `['a']` | Push |
| 2 | 'b' | `['a', 'b']` | Push |
| 3 | 'c' | `['a', 'b', 'c']` | Push |
| 4 | 'c' | `['a', 'b']` | Pop (match) ✓ |
| 5 | 'b' | `['a']` | Pop (match) ✓ |
| 6 | 'a' | `[]` | Pop (match) ✓ |

**Final Result:** Stack is empty → Length = **0**

---

### Example 4: `"aabccd"` (Partial elimination)

| Step | Character | Stack State | Action |
|------|-----------|-------------|--------|
| 0 | - | `[]` | Initialize |
| 1 | 'a' | `['a']` | Push |
| 2 | 'a' | `[]` | Pop (match) ✓ |
| 3 | 'b' | `['b']` | Push |
| 4 | 'c' | `['b', 'c']` | Push |
| 5 | 'c' | `['b']` | Pop (match) ✓ |
| 6 | 'd' | `['b', 'd']` | Push |

**Final Result:** Stack = `['b', 'd']` → Length = **2**

---

## Time & Space Complexity
- **Time:** O(n) - single pass through string
- **Space:** O(n) - worst case, no eliminations occur
"""

def eliminate_length(s):
    stack = []  # 创建一个空栈

    for c in s:
        # 判断字符是否为大小写英文字母
        if not c.isalpha():
            return 0

        if stack and stack[-1] == c:
            stack.pop()  # 栈顶字母与当前字母相同，进行消除
        else:
            stack.append(c)  # 入栈

    return len(stack)  # 返回最终字符串长度


# 从输入中读取原始字符串
s = input()

# 计算最终字符串长度
length = eliminate_length(s)

# 输出最终字符串长度
print(length)
