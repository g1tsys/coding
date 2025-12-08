"""
# IPv4 Address to Integer Conversion Problem

## Problem Translation

You have a virtual IPv4 address consisting of 4 sections separated by `#`, where each section ranges from 0-255. The address needs to be converted to a 32-bit integer.

**Constraints:**
- First section: 1-128
- Other sections: 0-255
- Format: `(1~128)#(0~255)#(0~255)#(0~255)`
- Return "invalid IP" for illegal addresses

**Examples:**
- `128#0#255#255` → `2147549183` (0x8000FFFF)
- `1#0#0#0` → `16777216` (0x01000000)

## Python Thought Process

### Step-by-Step Approach:

1. **Split the input** by `#` delimiter to get 4 sections
2. **Validate structure**: Check if exactly 4 sections exist
3. **Validate each section**:
   - No leading zeros (except "0" itself)
   - First section: 1 ≤ value ≤ 128
   - Other sections: 0 ≤ value ≤ 255
4. **Convert to 32-bit integer**: Use bit shifting
   - Each section occupies 8 bits
   - Formula: `(sec1 << 24) | (sec2 << 16) | (sec3 << 8) | sec4`

### Example Walkthrough

**Input:** `128#0#255#255`


Step 1: Split by '#'
sections = ['128', '0', '255', '255']

Step 2: Validate count
len(sections) == 4 ✓

Step 3: Validate each section
- '128': No leading zero, 1 ≤ 128 ≤ 128 ✓
- '0': Valid, 0 ≤ 0 ≤ 255 ✓
- '255': No leading zero, 0 ≤ 255 ≤ 255 ✓
- '255': No leading zero, 0 ≤ 255 ≤ 255 ✓

Step 4: Convert to integer
ip_int = 0
ip_int = (0 << 8) | 128 = 128
ip_int = (128 << 8) | 0 = 32768
ip_int = (32768 << 8) | 255 = 8388863
ip_int = (8388863 << 8) | 255 = 2147549183

Result: 2147549183


**Test Cases:**
- `128#0#255#255` → `2147549183` ✓
- `1#0#0#0` → `16777216` ✓
- `0#0#0#0` → `invalid IP` (first section < 1)
- `129#0#0#0` → `invalid IP` (first section > 128)
- `1#256#0#0` → `invalid IP` (section > 255)
- `01#0#0#0` → `invalid IP` (leading zero)
"""

def convert_ipv4(ipv4_str):
    sections = ipv4_str.split("#")  # 拆分IPv4地址字符串为4个小节
    if len(sections) != 4:  # 如果小节数量不等于4，则为非法IPv4地址
        return "invalid IP"

    try:
        ip_int = 0
        for index, section in enumerate(sections):
            if not section.isdigit() or (index == 0 and not (1 <= int(section) <= 128)) or not (0 <= int(section) <= 255) or (section[0] == '0' and section != "0"):
                return "invalid IP"  # 验证小节的有效性
            section_int = int(section)  # 将小节转换为整数
            ip_int = (ip_int << 8) | section_int  # 将每个小节的整数值进行位操作拼接成32位整数
        return str(ip_int)  # 返回转换后的32位整数值
    except ValueError:
        return "invalid IP"  # 如果转换过程中出现非数字字符，则为非法IPv4地址


ipv4_str = input()  # 输入虚拟IPv4地址
result = convert_ipv4(ipv4_str)  # 转换为32位整数或特定字符
print(result)  # 输出结果

