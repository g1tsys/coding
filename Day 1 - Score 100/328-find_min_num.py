"""This problem asks you to find the smallest number in an array of consecutive positive numbers with one or more numbers broken up and shuffled in to a string made out of this array of numbers. So we need to recover the string back to its original order and find the smallest after this.
The inputs are the shuffled string and an integer representing the length or the number  of consecutive positive numbers in the original array. 



Input
98011211 5


Output
8

Here the 10 got broken into 1 and 0 and shuffled in to the string. So the original array is [8,9,10,11,12] and the smallest number is 8.

from collections import Counter

def find_min_num(shuffled_str, n):
    # Try different starting numbers
    for start in range(1, 1001):  # Max number is 1000
        # Generate n consecutive numbers starting from 'start'
        expected_nums = [str(start + i) for i in range(n)]
        expected_str = ''.join(expected_nums)
        
        # Check if the shuffled string has the same characters
        if Counter(shuffled_str) == Counter(expected_str):
            return start  # This is the minimum number
    
    return None

if __name__ == "__main__":
    shuffled_str, n = input().split()
    n = int(n)
    result = find_min_num(shuffled_str, n)
    if result is not None:
        print(result)
    else:
        print("No valid reconstruction found.")

so this is like a cheat way to not need to find the original array but find the smallest in the string that matches the start without repeat because of consecutive gives away sort of a small hint that this array wont be repeated so any repeating char that doesn't have a number follow consecutively renders the starting point not the right one am i on the right track?

**YES! You're exactly right!** 🎯

You've understood the clever insight perfectly:

## Why this "cheat" works:

1. **Consecutive numbers are unique** - If we have [8,9,10,11,12], we can't have another 8 or 9 in the sequence
2. **Character frequency is a fingerprint** - "89101112" has a unique mix of digits that only THIS sequence produces
3. **We don't need to unscramble** - Just check if the scrambled string COULD have come from a specific sequence

## Your insight about repetition:

You're spot on! For example:
- If we try start=1, n=5: [1,2,3,4,5] → "12345"
- Count: 1x1, 2x1, 3x1, 4x1, 5x1
- But "98011211" has: 9x1, 8x1, 0x1, **1x4**, 2x2
- **Mismatch!** The '1' appears 4 times, but [1,2,3,4,5] only has one '1'

When we try start=8:
- [8,9,10,11,12] → "89101112"  
- Count: 8x1, 9x1, 1x4, 0x1, 2x2
- **Perfect match!** ✓

## So the algorithm is:

```
For each possible start:
    Build consecutive sequence
    Does character count match? 
        → YES = Found it! (and it's the smallest since we start from 1)
        → NO = Keep trying
```

You've grasped the **key optimization**: We bypass the hard problem (unscrambling) by using the constraint (consecutive = unique character signature)! 🧠

"""


# a more elegant version 

from collections import Counter

def find_min_num(shuffled_str, n):
    char_count = Counter(shuffled_str)
    str_len = len(shuffled_str)
    
    # Estimate the range based on average digit length
    avg_digits = str_len / n
    if avg_digits < 1.5:
        max_start = 10
    elif avg_digits < 2.5:
        max_start = 100
    else:
        max_start = 1000
    
    def can_form_sequence(start, remaining_count, count):
        """Check if we can form n consecutive numbers starting from 'start'"""
        if count == n:
            # Check if we used all characters
            return all(v == 0 for v in remaining_count.values())
        
        current_num = start + count
        num_str = str(current_num)
        
        # Try to use this number's digits
        temp_count = remaining_count.copy()
        for digit in num_str:
            if temp_count.get(digit, 0) <= 0:
                return False  # Can't form this number
            temp_count[digit] -= 1
        
        # Recurse to next number
        return can_form_sequence(start, temp_count, count + 1)
    
    # Try each starting number
    for start in range(1, max_start + 1):
        if can_form_sequence(start, char_count.copy(), 0):
            return start
    
    return None

if __name__ == "__main__":
    shuffled_str, n = input().split()
    n = int(n)
    result = find_min_num(shuffled_str, n)
    if result is not None:
        print(result)
    else:
        print("No valid reconstruction found.")






