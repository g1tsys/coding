""""
# Number Guessing Game - Problem Translation

## Problem Description

One person sets a **4-digit number** as the answer, and another person tries to guess it.

For each guess, the setter provides a hint in the format **XAYB**:
- **X** = number of digits that are correct in both value AND position
- **Y** = number of digits that are correct in value but WRONG position

**Examples:**
- Answer: 8123, Guess: 1052 → Hint: **0A2B**
  - 0 digits correct position (0A)
  - 2 digits correct but wrong position: 1 and 2 (2B)

- Answer: 5637, Guess: 4931 → Hint: **1A0B**
  - 1 digit correct position: 3 (1A)
  - 0 digits correct but wrong position (0B)

Given N guesses and their hints, determine the answer. If the answer is certain, output it; otherwise output **"NA"**.

## Input/Output

**Input:**
- First line: A positive integer N (0 < N < 100)
- Next N lines: Each contains a guessed number and its hint result

**Output:**
- The final answer, or "NA" if uncertain

---

## Example Walkthrough

Let's say we have these guesses:

```text
3
1234 1A1B
5678 0A2B
1357 2A0B
```

**Step-by-step analysis:**

1. **Guess: 1234 → 1A1B**
   - 1 digit is in correct position
   - 1 digit exists but in wrong position

2. **Guess: 5678 → 0A2B**
   - 0 digits in correct position
   - 2 digits exist but in wrong positions

3. **Guess: 1357 → 2A0B**
   - 2 digits in correct positions
   - 0 digits in wrong positions

**Solution approach:**
- Test all numbers from 0000-9999
- For each candidate, check if it produces the same hints for all guesses
- If exactly ONE number satisfies all conditions → that's the answer
- If zero or multiple numbers satisfy → output "NA"

The algorithm counts:
- **Correct position matches** (A value)
- **Correct digit, wrong position matches** (B value) by comparing digit frequencies





"""




def findAnswer(N, guesses):
    possibleAnswers = set()  # 可能的答案集合
    for i in range(10000):
        digits = [int(x) for x in str(i).zfill(4)]  # 将数字i转换为四位数的列表形式
        valid = True  # 判断数字i是否满足所有猜测的条件
        for guess in guesses:
            guessDigits = [int(x) for x in str(guess[0])]  # 将猜测数字guess转换为列表形式
            a = guess[1]  # 位置正确的数字个数
            b = guess[2]  # 数字正确但位置不对的个数
            correct = 0  # 记录数字位置正确的个数
            misplaced = 0  # 记录数字位置不对但数字正确的个数
            digitCount1 = [0] * 10  # 记录数字i中每个数字的个数
            digitCount2 = [0] * 10  # 记录猜测数字guess中每个数字的个数
            for j in range(4):
                if digits[j] == guessDigits[j]:  # 判断数字i和猜测数字guess在相同位置是否相等
                    correct += 1
                else:
                    digitCount1[digits[j]] += 1
                    digitCount2[guessDigits[j]] += 1
            misplaced = sum(min(digitCount1[k], digitCount2[k]) for k in range(10))  # 计算数字位置不对但数字正确的个数
            if a != correct or b != misplaced:  # 判断数字i是否满足当前猜测的条件
                valid = False
                break
        if valid:
            possibleAnswers.add(i)  # 如果数字i满足所有猜测的条件，则将其添加到可能的答案集合中
    if len(possibleAnswers) == 1:
        return str(possibleAnswers.pop()).zfill(4)  # 如果可能的答案集合中只有一个数字，则返回该数字作为答案
    else:
        return "NA"  # 如果可能的答案集合中有多个数字，则无法确定答案，返回NA作为结果

N = int(input())  # 输入猜测次数
guesses = []  # 保存每次猜测和结果的列表
for _ in range(N):
    guess, result = input().split()  # 输入猜测数字和结果
    guesses.append((int(guess), int(result[0]), int(result[2])))  # 将猜测数字和结果添加到列表中
print(findAnswer(N, guesses))  # 调用函数查找答案并输出结果


