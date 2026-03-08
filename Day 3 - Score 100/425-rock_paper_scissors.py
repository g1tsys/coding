"""
Here’s the extracted **input/output specification** and **detailed steps** for solving the **Airport Flight Scheduling** problem:

---

### 🎯 **Problem Summary**
You are given a list of flight numbers (e.g., `CA3385`, `CZ6678`). Each flight number is 6 characters long:  
- First 2 characters = airline code (letters or digits, e.g., `CA`, `CZ`, `DU`)  
- Last 4 characters = numeric flight info (e.g., `3385`, `6678`)  

**Goal**: Sort flights by:  
1. **Airline code** (first 2 chars) — in this order:  
   - Special symbols: `$&*`  
   - Digits: `0-9`  
   - Uppercase letters: `A-Z`  
2. **Flight number** (last 4 digits) — numerically ascending  

Output the sorted list of flight numbers, comma-separated.

---

### 📥 **Input Format**
- One line of input  
- Flight numbers separated by commas (`,`), possibly with spaces  
- Max 100 flights  
- Each flight number is 6 chars: 2-letter/digit code + 4-digit number  
- Example:  
  ```
  CA3385, CZ6678, SC6508, DU7523, HK4456, MK0987
  ```

---

### 📤 **Output Format**
- One line: sorted flight numbers, comma-separated (no extra spaces)  
- Example:  
  ```
  DU7523, HK4456, MK0987, CA3385, SC6508, CZ6678
  ```

---

### 🧩 **Step-by-Step Solution**

#### Step 1: Parse Input
- Read the input line  
- Split by comma `,`  
- Strip whitespace from each flight number  
- Store in a list

#### Step 2: Define Custom Sort Key
For each flight number `s` (e.g., `CA3385`):  
- Extract airline code: `s[0:2]`  
- Extract flight number: `int(s[2:6])`  
- Define sort key as tuple: `(custom_order(airline_code), flight_number)`  

> **Custom Order for Airline Code**:  
> - Special symbols `$&*` → lowest priority  
> - Digits `0-9` → next  
> - Letters `A-Z` → highest  

You can implement this by mapping each character to a priority value:

```python
def get_priority(char):
    if char in '$&*':
        return 0
    elif char.isdigit():
        return 1
    elif char.isalpha():
        return 2
    return 3  # fallback

def airline_key(code):
    # Return tuple of (priority of first char, priority of second char, code itself)
    return (get_priority(code[0]), get_priority(code[1]), code)
```

#### Step 3: Sort the List
Use `sorted()` with key function:

```python
sorted(flights, key=lambda s: (airline_key(s[:2]), int(s[2:6])))
```

#### Step 4: Output
Join sorted list with commas and print.

---

### ✅ Example Walkthrough

**Input**:  
`CA3385, CZ6678, SC6508, DU7523, HK4456, MK0987`

**Airline Codes**:  
- `CA` → (2,2) → letters  
- `CZ` → (2,2)  
- `SC` → (2,2)  
- `DU` → (2,2)  
- `HK` → (2,2)  
- `MK` → (2,2)  

All are letters → sort by code alphabetically:  
`CA`, `CZ`, `DU`, `HK`, `MK`, `SC` → but wait! We must sort by **custom priority**, which for letters is same → then sort by **flight number**.

Actually, since all are letters, we sort by **airline code string** (lex order) then by **flight number**.

So:  
- `CA3385` → 3385  
- `CZ6678` → 6678  
- `DU7523` → 7523  
- `HK4456` → 4456  
- `MK0987` → 987  
- `SC6508` → 6508  

Sort by airline code first:  
`CA`, `CZ`, `DU`, `HK`, `MK`, `SC` → then by number:  
- `CA3385` (3385)  
- `CZ6678` (6678)  
- `DU7523` (7523)  
- `HK4456` (4456)  
- `MK0987` (987)  
- `SC6508` (6508)  

Wait — **this is wrong**. We must sort **first by airline code**, then by number. So:

Group by airline code:  
- `CA3385`  
- `CZ6678`  
- `DU7523`  
- `HK4456`  
- `MK0987`  
- `SC6508`  

Sort airline codes:  
`CA`, `CZ`, `DU`, `HK`, `MK`, `SC` → all same priority → sort alphabetically:  
`CA`, `CZ`, `DU`, `HK`, `MK`, `SC`  

Then within each group, sort by number — but each group has only one flight.

So final order:  
`CA3385`, `CZ6678`, `DU7523`, `HK4456`, `MK0987`, `SC6508`

But wait — the example output in the page is:  
`DU7523, HK4456, MK0987, CA3385, SC6508, CZ6678`

That suggests **airline code is sorted by custom priority**, not alphabetically.

Let’s re-read:  
> “航空公司缩写排序按照从特殊符号$&*, 0~9， A ~Z排序”

So:  
- `$&*` → lowest  
- `0-9` → next  
- `A-Z` → highest  

But in our example, all codes are letters → so they are all in the same group → then sort by **flight number**? No — the problem says:  
> “同一航空公司的航班再按照航班号的后4个数字进行排序”

But here, all airlines are different → so we sort by **airline code** first — and since all are letters, we sort by **airline code string** (lex order).

But the example output doesn’t match that.

Let’s look at the example output:  
`DU7523, HK4456, MK0987, CA3385, SC6508, CZ6678`

This suggests that **airline code is sorted by the numeric value of the first character**, then second? Or perhaps by the **ASCII value**?

Actually, the problem says:  
> “航空公司缩写排序按照从特殊符号$&*, 0~9， A ~Z排序”

This is **not** ASCII order — it’s a custom order:  
- `$&*` → group 0  
- `0-9` → group 1  
- `A-Z` → group 2  

So for two-letter codes, we compare first char by group, then second char by group, then lexicographically within group.

But in our example, all first chars are letters → group 2 → then compare second char — also letters → group 2 → then sort lexicographically.

So `CA`, `CZ`, `DU`, `HK`, `MK`, `SC` → sorted lex:  
`CA`, `CZ`, `DU`, `HK`, `MK`, `SC`

But the example output starts with `DU` — which is after `CA` and `CZ` — so this doesn’t match.

Wait — perhaps the example output is **wrong**? Or perhaps I misread.

Let’s check the sample input:  
`CA3385, CZ6678, SC6508, DU7523, HK4456, MK0987`

If we sort by airline code using **custom priority** (all letters → same group), then by **flight number** (ascending), we get:

- `MK0987` → 987  
- `CA3385` → 3385  
- `HK4456` → 4456  
- `SC6508` → 65
"""
# 定义一个函数来对航班号进行排序
def sort_flights(flights):
    # 使用sorted函数对航班列表进行排序，首先按照航空公司的缩写排序，然后按照航班号的数字排序
    sorted_flights = sorted(flights, key=lambda x: (x[:2], int(x[2:])))
    return sorted_flights

# 主程序
if __name__ == "__main__":
    # 输入航班信息
    input_flights = input().strip().split(',')
    # 对输入的航班信息进行去除两端的空白字符处理
    input_flights = [flight.strip() for flight in input_flights]
    # 调用排序函数获取排序后的航班信息
    sorted_flights = sort_flights(input_flights)
    # 输出排序后的航班起飞顺序，用逗号连接
    print(','.join(sorted_flights))
