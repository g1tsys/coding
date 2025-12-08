"""Problem Description
Question: Given a string s that forms a circle (head connects to tail), find the length of the longest substring where the characters 'l', 'o', and 'x' all appear an even number of times (including zero).

Input: A string of lowercase letters
Output: An integer representing the maximum length

Chain of thoughts:
1. Since the string is circular, we can simulate this by concatenating the string to itself.
2. We will use a bitmask to track the parity (even or odd) of the counts of 'l', 'o', and 'x'.
3. Each character will correspond to a bit in the bitmask:
   - 'l' -> 1st bit
   - 'o' -> 2nd bit
   - 'x' -> 3rd bit
4. As we traverse the string, we will update the bitmask based on the characters we encounter.
5. We will use a dictionary to store the first occurrence of each bitmask state.
6. If we encounter the same bitmask state again, it means the substring between these two occurrences has even counts of 'l', 'o', and 'x'.
7. We will calculate the length of this substring and update our maximum length if it's greater than the previously recorded maximum.
8. Finally, we will return the maximum length found.
9. We need to ensure that the length of the substring does not exceed the original string length since we are simulating a circular string.
"""


# walk me through the code like i am five years old
def find_longest_even_o(s: str) -> int:
    n = len(s)
    s = s + s  # Duplicate the string to handle circular nature
    state = 0  # This will hold the parity state of 'l', 'o', 'x'
    pos = {0: -1}  # Dictionary to store the first occurrence of each state
    max_length = 0  # Variable to keep track of the maximum length found

    for i in range(2 * n):
        char = s[i]
        # Update the state based on the character
        if char == 'l':
            state ^= 1 << 0  # Toggle the first bit for 'l'
        elif char == 'o':
            state ^= 1 << 1  # Toggle the second bit for 'o'
        elif char == 'x':
            state ^= 1 << 2  # Toggle the third bit for 'x'

        if state in pos:
            length = i - pos[state]  # Calculate the length of the substring
            if length <= n:  # Ensure it doesn't exceed original string length
                max_length = max(max_length, length)  # Update max_length if needed
        else:
            pos[state] = i  # Store the first occurrence of this state

    return max_length  # Return the maximum length found

if __name__ == "__main__":
    s = input().strip()
    # this line reads the input string s and removes any leading or trailing whitespace.
    result = find_longest_even_o(s)
    # this line calls the function find_longest_even_o with the input string s and stores the result in the variable result.
    print(result)
    # this line prints the result, which is the length of the longest substring where 'i', 'o', and 'x' all appear an even number of times.



"""This is a full walkthrough generated b LEO AI
Here is the **Python solution approach** translated and formatted with **numbered sections** as requested:

---

### 🎈 Python 语言思路

1. **Extend the string**  
   First, we extend the given string `s` to double its length to simulate the circular nature of the string. This allows us to handle the circular condition without explicitly wrapping around.

2. **Define variables**  
   - Define `max_len` to store the maximum length of the valid substring, initialized to 0.
   - Define `status` to track the parity (odd/even) of the counts of 'l', 'o', and 'x' using binary bits. The initial state is 0 (all even).
   - Use a dictionary `status_positions` to record the first occurrence of each `status`. Initially, we set `status_positions[0] = -1`.

3. **Iterate through the extended string**  
   For each character in the extended string:
   - Update the `status` by flipping the corresponding bit if the character is 'l', 'o', or 'x'.
   - If the current `status` has been seen before (i.e., exists in `status_positions`), calculate the length of the substring between the current index and the first occurrence of this `status`. If the length is less than or equal to the original string length `n`, update `max_len` accordingly.
   - If the current `status` is new, record its first occurrence in the dictionary.

4. **Return the result**  
   After processing all characters, return `max_len`, which represents the length of the longest valid substring where 'l', 'o', and 'x' all appear an even number of times.

---

### 🎉 Python 代码

```python
def longestSubstring(s):
    n = len(s)
    extended_s = s + s
    max_len = 0
    status = 0
    status_positions = {0: -1}  # 初始状态0的位置设为-1

    for i in range(len(extended_s)):
        c = extended_s[i]
        if c == 'l':
            status ^= (1 << 0)
        elif c == 'o':
            status ^= (1 << 1)
        elif c == 'x':
            status ^= (1 << 2)

        if status in status_positions:
            curr_len = i - status_positions[status]
            if curr_len <= n:
                max_len = max(max_len, curr_len)
        else:
            status_positions[status] = i

    return max_len
```

---

Let me know if you'd like the same formatting applied to other languages like C++ or Java!



# Bit Manipulation Walkthrough Example

Let me explain how bit manipulation works in this problem using a concrete example.

---

## Example String: `s = "loxlo"`

We're tracking whether 'l', 'o', 'x' appear an **even** or **odd** number of times using 3 bits:

- **Bit 0** (rightmost): tracks 'l' → `001` in binary = `1` in decimal
- **Bit 1** (middle): tracks 'o' → `010` in binary = `2` in decimal  
- **Bit 2** (leftmost): tracks 'x' → `100` in binary = `4` in decimal

**Status = 0 means all three characters appear an even number of times (including 0 times)**

---

## Step-by-Step Walkthrough of bit manipulation

### Initial State
```
status = 0 (binary: 000)
status_positions = {0: -1}
max_len = 0
extended_s = "loxloloxlo" (double the original)
```

---

### **i = 0, char = 'l'**
```
status ^= (1 << 0)  // XOR with 001
status = 0 ^ 1 = 1 (binary: 001)
```
- 'l' appears **1 time** (odd) → bit 0 is ON
- Status `1` is **new**, so record: `status_positions[1] = 0`

---

### **i = 1, char = 'o'**
```
status ^= (1 << 1)  // XOR with 010
status = 1 ^ 2 = 3 (binary: 011)
```
- 'l' appears 1 time (odd) → bit 0 is ON
- 'o' appears **1 time** (odd) → bit 1 is ON
- Status `3` is **new**, so record: `status_positions[3] = 1`

---

### **i = 2, char = 'x'**
```
status ^= (1 << 2)  // XOR with 100
status = 3 ^ 4 = 7 (binary: 111)
```
- All three characters appear **odd** times
- Status `7` is **new**, so record: `status_positions[7] = 2`

---

### **i = 3, char = 'l'**
```
status ^= (1 << 0)  // XOR with 001
status = 7 ^ 1 = 6 (binary: 110)
```
- 'l' appears **2 times** (even) → bit 0 is OFF
- 'o' appears 1 time (odd) → bit 1 is ON
- 'x' appears 1 time (odd) → bit 2 is ON
- Status `6` is **new**, so record: `status_positions[6] = 3`

---

### **i = 4, char = 'o'**
```
status ^= (1 << 1)  // XOR with 010
status = 6 ^ 2 = 4 (binary: 100)
```
- 'l' appears 2 times (even) → bit 0 is OFF
- 'o' appears **2 times** (even) → bit 1 is OFF
- 'x' appears 1 time (odd) → bit 2 is ON
- Status `4` is **new**, so record: `status_positions[4] = 4`

---

### **i = 5, char = 'l'** ✨ **KEY MOMENT**
```
status ^= (1 << 0)  // XOR with 001
status = 4 ^ 1 = 5 (binary: 101)
```
- Status `5` is **new**, so record: `status_positions[5] = 5`

---

### **i = 6, char = 'o'**
```
status ^= (1 << 1)  // XOR with 010
status = 5 ^ 2 = 7 (binary: 111)
```
- Status `7` **already exists** at position 2! 🎯
- Substring from position 3 to 6: `"loxl"` → length = `6 - 2 = 4`
- This substring has all three characters appearing **even** times
- `4 <= 5` (original length), so `max_len = 4`

---

### **i = 7, char = 'x'**
```
status ^= (1 << 2)  // XOR with 100
status = 7 ^ 4 = 3 (binary: 011)
```
- Status `3` **already exists** at position 1! 🎯
- Substring length = `7 - 1 = 6`
- But `6 > 5` (exceeds original length), so **ignore**

---

### **i = 8, char = 'l'**
```
status ^= (1 << 0)  // XOR with 001
status = 3 ^ 1 = 2 (binary: 010)
```
- Status `2` is **new**, so record: `status_positions[2] = 8`

---

### **i = 9, char = 'o'**
```
status ^= (1 << 1)  // XOR with 010
status = 2 ^ 2 = 0 (binary: 000)
```
- Status `0` **already exists** at position -1! 🎯
- Substring length = `9 - (-1) = 10`
- But `10 > 5` (exceeds original length), so **ignore**

---

## Final Result

**`max_len = 4`**

The longest valid circular substring is **"loxl"** (or equivalent rotation) where 'l', 'o', 'x' all appear an even number of times.

---

## Why XOR Works

**XOR (^) flips bits:**
- `0 ^ 1 = 1` (even → odd)
- `1 ^ 1 = 0` (odd → even)

When the **same status appears twice**, it means the substring **between those positions** has all characters appearing an even number of times (the bits flipped back to the same state).

"""