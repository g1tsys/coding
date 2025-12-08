"""
The problem involves generating all possible letter combinations from a given string of digits, based on a predefined mapping of digits to letters. Then, we must filter out any combinations that contain all the letters from a given "block" string. Here's a breakdown of the Python approach:

### **Problem Translation**
- Each digit corresponds to a specific set of letters (e.g., 0 → "a", "b", "c").
- Given a string of digits (e.g., "78"), we generate all possible letter combinations based on the digit-letter mapping.
- We are also given a "block" string (e.g., "ux"). Any generated combination that contains **all** the letters in the block string must be excluded.
- Finally, output the valid combinations, separated by commas, with a trailing comma.

### **Python Approach**
1. **Digit to Letters Mapping**:
   - Create a dictionary to map each digit to its corresponding letters.
   ```python
   digit_to_letters = {
       '0': 'abc', '1': 'def', '2': 'ghi', '3': 'jkl',
       '4': 'mno', '5': 'pqr', '6': 'st', '7': 'uv',
       '8': 'wx', '9': 'yz'
   }
   ```

2. **Generate All Combinations**:
   - Use `itertools.product` to generate the Cartesian product of the letters for each digit in the input string.
   ```python
   from itertools import product
   letters_list = [digit_to_letters[digit] for digit in input_digits]
   all_combinations = product(*letters_list)
   ```

3. **Filter Combinations**:
   - For each combination, check if it contains **all** the letters in the block string.
   - Use a set for the block string for quick lookup.
   ```python
   block_set = set(block_string)
   valid_combinations = []
   for combo in all_combinations:
       combo_set = set(combo)
       if not block_set.issubset(combo_set):
           valid_combinations.append(''.join(combo))
   ```

4. **Output the Results**:
   - Join the valid combinations with commas and add a trailing comma.
   ```python
   result = ','.join(valid_combinations) + ','
   print(result)
   ```

### **Example Walkthrough**
**Input**:
- Digit string: `"78"`
- Block string: `"ux"`

**Step 1**: Map digits to letters:
- 7 → "uv"
- 8 → "wx"

**Step 2**: Generate all combinations:
- "uv" × "wx" → "uw", "ux", "vw", "vx"

**Step 3**: Filter out combinations containing both "u" and "x":
- "ux" is excluded (contains both "u" and "x").
- Valid combinations: "uw", "vw", "vx"

**Step 4**: Output:
```
uw,vw,vx,
```

Let me know if you'd like a full code example!
"""


# 导入product模块以用于生成笛卡尔积
from itertools import product

# 定义一个函数来生成符合条件的字母组合
def generate_combinations(number_string, block_string):
    # 建立数字到字母的映射关系字典
    digit_to_letters = {
        '0': ['a', 'b', 'c'],
        '1': ['d', 'e', 'f'],
        '2': ['g', 'h', 'i'],
        '3': ['j', 'k', 'l'],
        '4': ['m', 'n', 'o'],
        '5': ['p', 'q', 'r'],
        '6': ['s', 't'],
        '7': ['u', 'v'],
        '8': ['w', 'x'],
        '9': ['y', 'z']
    }
    
    # 根据输入的数字字符串获取对应的字母列表
    letters_list = [digit_to_letters[digit] for digit in number_string]
    
    # 生成所有可能的字母组合
    all_combinations = product(*letters_list)
    
    # 过滤掉包含屏蔽字符串所有字母的组合
    valid_combinations = []
    for combination in all_combinations:
        # 将组合转换为集合以便于判断
        combination_set = set(combination)
        # 检查屏蔽字符串的字母是否都是当前组合的一部分
        if not all(letter in combination_set for letter in block_string):
            # 如果不是，则将该组合加入有效组合列表
            valid_combinations.append(''.join(combination))
    
    # 返回有效组合并用逗号连接，末尾加上逗号
    return ','.join(valid_combinations) + ','

# 获取输入
number_string = input().strip()
block_string = input().strip()

# 调用函数生成符合条件的组合并输出
output = generate_combinations(number_string, block_string)
print(output)

