"""

> The following is a translation of the question, hints, and a walkthrough example based on the provided web content.

---

### 🎃 Question Description (Translated)

Implement an integer encoding method such that the smaller the number to be encoded, the fewer bytes it occupies.

**Encoding Rules:**

1. Encode 7 bits at a time. The low 7 bits of each byte are used to store the two's complement of the number to be encoded.
2. The highest bit of the byte indicates whether there are more bytes to follow. Set to `1` if there are more bytes, and `0` if it is the last byte.
3. Use **little-endian** encoding (the lower bits and lower bytes are placed at lower addresses).
4. Output the encoded result in hexadecimal character format, with lowercase letters converted to uppercase.

---

### 🎃 Input and Output (Translated)

- **Input:** A string representing a **non-negative integer**.
- **Output:** A string representing the hexadecimal code stream of the encoded integer.

---

### 🎈 Example Walkthrough (Python)

Let's take the number **123** as an example.

#### Step 1: Convert the input to an integer
num = int("123")


#### Step 2: Encode the number using the rules
- Break the number into 7-bit chunks.
- For each chunk:
  - Take the 7 least significant bits.
  - If more chunks remain, set the 8th bit (MSB) to `1`.
  - Otherwise, set it to `0`.

Let's break down **123** (binary: `01111011`).

- First chunk: `01111011` (7 bits) → `0b1111011` = `123` in decimal.
- Since this is the only chunk, the MSB is set to `0`.

So the encoded byte is: `0b01111011` = `123` in decimal.

#### Step 3: Convert the encoded bytes to hexadecimal
- Convert each byte to a 2-character hexadecimal string.
- Convert lowercase letters to uppercase.

The byte `123` in hexadecimal is `7B`.

---

### 🎉 Final Output

7B



### 🎈  Language Thought Process (Translated)

1. **First, convert the input string into an integer type.**  
   This allows us to work with the number mathematically.

2. **Create an empty list `encoded_bytes` to store the encoded bytes.**  
   This will be used to collect the encoded bytes as we process the number.

3. **Enter a loop that continues until the number becomes 0.**  
   In each iteration:
   - Extract the **lowest 7 bits** of the number using a bitwise AND operation with `0b01111111` (i.e., `127` in decimal).
   - Right shift the number by 7 bits to process the next part of the number.
   - If the number is **not zero** (i.e., more bytes are needed), set the **8th bit (MSB)** of the current byte to `1` using a bitwise OR operation with `0b10000000` (i.e., `128` in decimal).
   - Append the encoded byte to the `encoded_bytes` list.

4. **Convert the encoded bytes into a hexadecimal string.**
   - Create an empty string `encoded_hex` to store the final result.
   - For each byte in `encoded_bytes`, convert it into a two-character hexadecimal representation.
   - Use bitwise operations to extract the **high 4 bits** and **low 4 bits** of the byte.
   - Map each 4-bit value to its corresponding hexadecimal character using the string `"0123456789ABCDEF"`.
   - Append the characters to the `encoded_hex` string.

5. **Return the final hexadecimal string as the result.**

---

### 🎉 Example Walkthrough (Revisited)

Let's walk through the **number 123** again using the above logic:

1. **Convert input string "123" to integer:**
   
   num = int("123")
   

2. **Encode the number into bytes:**
   - **Step 1:** Extract the lowest 7 bits: `123 & 0b01111111 = 123` (since `123 < 128`).
   - **Step 2:** Right shift the number: `123 >> 7 = 0`.
   - **Step 3:** Since the number is now `0`, the MSB is set to `0`.
   - **Encoded byte:** `123` in decimal = `0b01111011` = `7B` in hexadecimal.

3. **Convert byte to hexadecimal:**
   - The byte `123` is converted to the hexadecimal string `"7B"`.

4. **Final output:**
7B
"""



def encode_integer(num):
    num = int(num)
    encoded_bytes = []

    while True:
        byte = num & 0b01111111  # 取当前数字的最低7位
        num >>= 7  # 右移7位，以处理下一个字节

        if num != 0:
            byte |= 0b10000000  # 如果还有更多字节，将当前字节的最高位置1

        encoded_bytes.append(byte)  # 将编码后的字节添加到列表中

        if num == 0:
            break

    encoded_hex = ''.join(format(byte, '02X') for byte in encoded_bytes)  # 将字节列表转换为16进制字符串

    return encoded_hex


input_num = input()  # 获取输入的非负整数
encoded_hex = encode_integer(input_num)  # 编码整数
print(encoded_hex)  # 输出16进制码流

