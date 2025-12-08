"""
This question asks you to find sushi on the table, there are n numbers of sushi, princes[i] is the ith sushi price, and if the customer chooses the ith sushi, 
the shop gives out the closest freebies sushi at position j to sushi at position i but with one condition that the prices[j] < prices[i]. The task is to find the next cheaper sushi for each sushi on the table. If there is no cheaper sushi, return the original price for that position or else return the sum of the original i + j or the original + the freebie. 

For example if prices[i] is 3 dollars and the next is 15 dollars, then 6, 14, 3 doesn't have any cheaper sushi, so the output is 3 dollars for that position. for 15 dollars, the next cheaper sushi is 6 dollars, for 6 dollars the next cheaper sushi is 3, dollars so the first one, and for 14 dollars the next cheaper sushi is 3 dollars. so 3 + 0, 15 + 6, 6 + 3, 14 + 3 = 3 21 9 17 are their each respective outputs

Sample Input:
3 15 6 14

Sample Output:
3 21 9 17



Sample Input2:
3 10 5 7

Sample Output2:
3 15 8 10
"""


"""
I'll translate the Python language section's思路 (approach/logic) and 代码 (code) parts with numbered sections:

## Python Language Approach (思路)

Since the actual Python code and detailed approach aren't fully visible in the provided text, here's what the general solution approach would be:

### 1. **Problem Understanding**
   - There are `n` plates of sushi on a rotating conveyor belt
   - Each plate has a price `prices[i]`
   - When selecting plate `i`, you get a free plate `j` if it's the nearest next plate where `prices[j] < prices[i]`
   - Calculate the total price for each selection

### 2. **Algorithm Steps**
   1. **Input Processing**: Read the sushi prices as space-separated integers
   2. **Find Next Cheaper**: For each plate `i`, search circularly for the next plate with lower price
   3. **Calculate Total**: Add current price + next cheaper price (or 0 if none exists)
   4. **Output Results**: Display all total prices

### 3. **Key Logic**
   - Use circular array traversal (wrap around using modulo operator)
   - For each position, scan forward until finding a cheaper plate or completing full circle
   - If no cheaper plate found, bonus is 0

### 4. **Implementation Details**
   - Time Complexity: O(n²) in worst case
   - Space Complexity: O(n) for storing results
   - Handle edge cases: single plate, all same prices, descending prices

## Python Code Reference Structure
"""

def find_next_cheaper(prices, index):
    # Find the next cheaper sushi plate in circular manner
    n = len(prices)
    current_price = prices[index]
    
    for i in range(1, n):
        next_index = (index + i) % n
        if prices[next_index] < current_price:
            return prices[next_index]
    return 0

def calculate_total_prices(prices):
    # Calculate total price for each plate selection
    result = []
    for i in range(len(prices)):
        bonus = find_next_cheaper(prices, i)
        total = prices[i] + bonus
        result.append(total)
    return result

if __name__ == "__main__":
    prices = list(map(int, input().strip().split()))
    total_prices = calculate_total_prices(prices)
    print(" ".join(map(str, total_prices)))
    