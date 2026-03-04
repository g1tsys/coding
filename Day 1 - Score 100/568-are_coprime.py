"""
# Translation and Explanation
## Problem Description

**Pythagorean Triplet Tuples**
If 3 positive integers (a, b, c) satisfy the relationship a² + b² = c², they are called Pythagorean numbers (the famous 3-4-5 triangle).
To explore the patterns of Pythagorean numbers, we define that if the Pythagorean numbers (a, b, c) are pairwise coprime (meaning a and b, a and c, b and c are all coprime with no common divisors), then it's a **Pythagorean triplet tuple**. For example, (3, 4, 5) is a Pythagorean triplet tuple, but (6, 8, 10) is not.
Find all Pythagorean triplet tuples within the given range [N, M].

## Input/Output

**Input:**
- Starting range N, where 1 ≤ N ≤ 10000
- Ending range M, where N < M ≤ 10000

**Output:**
1. Ensure a < b < c, output format: "a b c"
2. Sort multiple triplets by a ascending, then b ascending, then c ascending
3. If no triplets found in the range, output "NA"

## Python Thought Process Explanation

### Step 1: Check if Two Numbers are Coprime
python
def are_coprime(a, b):

- Uses the **Euclidean algorithm** (greatest common divisor method)
- Repeatedly divides and takes remainder until one number becomes 0
- If GCD = 1, the numbers are coprime (share no common factors)

### Step 2: Find All Pythagorean Triplets
python
def find_pythagorean_triplets(N, M):

- **Nested loops**: Iterate through all possible pairs (a, b) where N ≤ a < b < M
- For each pair, calculate c² = a² + b²
- Take the square root to get c
- **Three conditions must be met:**
  1. c² equals the calculated sum (perfect square check)
  2. c is within range (c ≤ M)
  3. All three numbers are pairwise coprime

### Step 3: Sort and Output
- If no triplets found → output "NA"
- Otherwise, sort by (a, b, c) in ascending order
- Output each triplet on a new line

## Example Walkthrough

**Input:** N = 1, M = 20

### Iteration Process:

**When a = 3, b = 4:**
- c² = 3² + 4² = 9 + 16 = 25
- c = √25 = 5 ✓
- Check: 5² = 25? Yes ✓
- Check: 5 ≤ 20? Yes ✓
- Check coprime:
  - GCD(3, 4) = 1 ✓
  - GCD(3, 5) = 1 ✓
  - GCD(4, 5) = 1 ✓
- **Result: (3, 4, 5) is valid**

**When a = 5, b = 12:**
- c² = 5² + 12² = 25 + 144 = 169
- c = √169 = 13 ✓
- Check: 13² = 169? Yes ✓
- Check: 13 ≤ 20? Yes ✓
- Check coprime:
  - GCD(5, 12) = 1 ✓
  - GCD(5, 13) = 1 ✓
  - GCD(12, 13) = 1 ✓
- **Result: (5, 12, 13) is valid**

**When a = 6, b = 8:**
- c² = 6² + 8² = 36 + 64 = 100
- c = √100 = 10 ✓
- Check coprime:
  - GCD(6, 8) = 2 ✗ (not coprime!)
- **Result: (6, 8, 10) is rejected**

**When a = 8, b = 15:**
- c² = 8² + 15² = 64 + 225 = 289
- c = √289 = 17 ✓
- Check: 17 ≤ 20? Yes ✓
- Check coprime: All pairs have GCD = 1 ✓
- **Result: (8, 15, 17) is valid**

### Final Output:
3 4 5
5 12 13
8 15 17


The key insight is that we're looking for **primitive Pythagorean triples** - those where the three numbers share no common factor, making them the fundamental building blocks of all Pythagorean relationships.

"""

def are_coprime(a, b):
    """
    判断两个数是否互质（没有公约数）
    """
    while b != 0:
        a, b = b, a % b
    return a == 1


def find_pythagorean_triplets(N, M):
    """
    寻找范围[N, M]内的勾股数元组
    """
    triplets = []
    for a in range(N, M):
        for b in range(a + 1, M):
            c_square = a**2 + b**2
            c = int(c_square**0.5)
            if c**2 == c_square and are_coprime(a, b) and are_coprime(a, c) and are_coprime(b, c):
                triplets.append((a, b, c))
    return triplets


N = int(input())
M = int(input())

triplets = find_pythagorean_triplets(N, M)

if len(triplets) == 0:
    print("NA")
else:
    triplets.sort()  # 按要求排序
    for triplet in triplets:
        print(*triplet)


