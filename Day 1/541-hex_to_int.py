"""
# TLV Parsing Problem - Translation and Explanation

## Problem Description

**TLV encoding** follows the format `[Tag Length Value]`:
- **Tag**: Identifies a data element (1 byte, unique in the stream)
- **Length**: Size of the Value field (2 bytes, **little-endian**)
- **Value**: The actual data (variable length)

Given a TLV-encoded stream and a target Tag, output the corresponding Value in hexadecimal.

**Constraints:**
- Input uses uppercase hex characters only
- Output must also use uppercase hex characters
- Maximum stream length: 50,000 bytes

## Input/Output Format

**Input:**
- Line 1: Target tag (hex string)
- Line 2: Hex byte stream (space-separated)

**Output:**
- The Value corresponding to the target tag (hex string, space-separated bytes)

## Python Solution Approach

### Key Steps:
1. **Parse Input**: Split the byte stream into individual hex bytes
2. **Iterate Through Stream**: 
   - Read current Tag (1 byte)
   - Read Length (2 bytes, little-endian)
   - Convert little-endian length to integer
   - Extract Value (length bytes)
3. **Match Tag**: If current tag matches target, return the value
4. **Skip to Next**: If no match, move index forward by 1 + 2 + length bytes

# Read input
target_tag = input().strip()
byte_stream = input().strip()

# Parse and output
result = parse_tlv(target_tag, byte_stream)
print(result)


## Example Walkthrough

**Input:**

31
31 01 00 32 32 02 00 33 34


**Step-by-step:**

1. **First TLV Entry:**
   - Tag = `31` (matches target!)
   - Length bytes = `01 00` (little-endian)
   - Length = 0x01 + 0x00 × 256 = **1**
   - Value = `32` (1 byte)
   - **Match found!** Return `32`

**Output:** `32`

---

**Another Example:**

33
31 02 00 AA BB 33 03 00 11 22 33


**Step-by-step:**

1. **First TLV:** Tag=`31`, Length=2, Value=`AA BB` → Skip
2. **Second TLV:** Tag=`33` (matches!), Length=3, Value=`11 22 33`

**Output:** `11 22 33`

### Key Points:
- **Little-endian**: Low byte first, then high byte
- **Length calculation**: `length = low_byte + high_byte × 256`
- **Index management**: Always skip Tag(1) + Length(2) + Value(length) bytes
"""




def hex_to_int(hex):
    return int(hex, 16)

tag = input("Enter the tag: ")  # 输入信元的 Tag
byte_stream = input("Enter the byte stream: ")  # 输入字节流

byte_tokens = byte_stream.strip().split(" ")  # 将字节流拆分成字符串数组
byte_count = len(byte_tokens)  # 字节的个数
value = []  # 存储解码后的 value
length = 0  # 信元 value 的长度

i = 0
while i < byte_count:
    length = hex_to_int(byte_tokens[i + 2]) * 256 + hex_to_int(byte_tokens[i + 1])  # 根据小端序合并字节得到 Length 的值
    if hex_to_int(byte_tokens[i]) == hex_to_int(tag):  # 如果当前字节的 Tag 和输入的 Tag 相同
        for j in range(length):
            value.append(byte_tokens[i + 3 + j])  # 提取后续的 Length 个字节作为 Value
        break
    i += (length + 3)

result = " ".join(value)  # 将 value 转换为字符串，并使用空格分隔元素
print(result)  # 输出解码后的值
