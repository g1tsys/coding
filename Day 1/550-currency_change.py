"""
# Currency Conversion Problem

## Problem Description

You have a ledger with multiple entries of foreign currency amounts that need to be converted to Chinese Yuan cents (fen) and summed up.
Each line records one amount with its currency unit in the format: number + unit. It could be just yuan/dollars, just cents, or a combination of both.

**Conversion rates between major units and minor units (all 1:100):**
- 1 CNY = 100 fen
- 1 HKD = 100 cents  
- 1 JPY = 100 sen
- 1 EUR = 100 eurocents
- 1 GBP = 100 pence

**Exchange rates to CNY:**
- 100 CNY = 1825 JPY = 123 HKD = 14 EUR = 12 GBP

**Task:** Convert all currencies to CNY fen, sum them up, and output only the integer part (discard decimals).

## Input/Output

**Input:**
- First line: N (number of records, 0 < N < 100)
- Next N lines: each contains one currency amount (only one currency type per line)

**Output:**
- Integer sum in CNY fen (no decimals, no units)

---

## Python Solution Approach

### Key Steps:

1. **Parse each line** to extract the numeric value and currency unit
2. **Convert to base unit** (fen, cents, sen, etc.) if needed
3. **Convert to CNY fen** using exchange rates
4. **Sum all amounts** and output the integer part

### Conversion Logic:

```python
def convert_to_cny_fen(amount, unit):
    # Exchange rates (how much CNY fen = 1 unit)
    rates = {
        'CNY': 100,      # 1 CNY = 100 fen
        'fen': 1,        # 1 fen = 1 fen
        'JPY': 100/18.25,  # 100 CNY = 1825 JPY
        'sen': 1/18.25,
        'HKD': 100/1.23,   # 100 CNY = 123 HKD
        'cents': 1/1.23,
        'EUR': 100/0.14,   # 100 CNY = 14 EUR
        'eurocents': 1/0.14,
        'GBP': 100/0.12,   # 100 CNY = 12 GBP
        'pence': 1/0.12
    }
    return amount * rates[unit]
```

---

## Example Walkthrough

**Input:**
```
3
100CNY
20HKD50cents
100JPY
```

**Step-by-step calculation:**

1. **Line 1: "100CNY"**
   - Amount: 100 CNY
   - Convert: 100 × 100 = **10,000 fen**

2. **Line 2: "20HKD50cents"**
   - First part: 20 HKD = 20 × (100/1.23) = 1,626.02 fen
   - Second part: 50 cents = 50 × (1/1.23) = 40.65 fen
   - Total: **1,666.67 fen**

3. **Line 3: "100JPY"**
   - Amount: 100 JPY
   - Convert: 100 × (100/18.25) = **547.95 fen**

**Sum:** 10,000 + 1,666.67 + 547.95 = 12,214.62 fen

**Output:** `12214` (integer part only)

---


This solution parses each currency entry, converts it to CNY fen using the appropriate exchange rate, sums everything up, and outputs the integer result.

"""


def get(s, y, x):
    sum = 0
    f = float(s[y:x])
    if s[x] == 'C':
        sum += f
    elif s[x] == 'f':
        sum += f / 100
    elif s[x] == 'E':
        sum += f / 0.14  # 100:14
    elif s[x] == 'e':
        sum += f / 0.14 / 100
    elif s[x] == 'G':
        sum += f / 0.12  # 100:12
    elif s[x] == 'p':
        sum += f / 0.12 / 100
    elif s[x] == 'J':
        sum += f / 18.25  # 100:1825
    elif s[x] == 's':
        sum += f / 18.25 / 100
    elif s[x] == 'H':
        sum += f / 1.23  # 100:123
    elif s[x] == 'c':
        sum += f / 1.23 / 100

    return sum


n = int(input())  # 读取记录数
sum = 0

while n > 0:
    s = input()  # 读取一行记录
    x = 0
    while s[x].isdigit() or s[x] == '.':  # 找到金额的结束位置
        x += 1
    y = x
    while y < len(s) and (s[y].isalpha() or s[y].isupper()):  # 找到单位的结束位置
        y += 1

    if y == len(s):  # 单位结束位置等于字符串长度，说明只有一个货币金额
        sum += get(s, 0, x)
    else:  # 否则，有两个货币金额需要转换并累加
        sum += get(s, 0, x)
        x = y
        while s[x].isdigit() or s[x] == '.':  # 找到第二个金额的结束位置
            x += 1
        sum += get(s, y, x)

    n -= 1

ans = int(sum * 100)  # 将金额乘以100并转换为整数
print(ans)  # 输出最终的金额

