# Game Grouping Problem - Translation and Solution

## Problem Description
"""
A department is organizing a King of Glory exhibition match with 10 game enthusiasts, divided into two teams of 5 players each. Each participant has a rating representing their skill level. To make the match as exciting as possible, we need to divide the 10 participants into two teams with similar strengths. A team's strength is the sum of its 5 members' ratings.

**Input:** 10 integers representing the game skill ratings of 10 participants

**Output:** 1 integer representing the minimum absolute difference between the two teams' strengths

---

## Solution Approach (Python)

The problem is essentially a **partition problem** where we need to split 10 players into two groups of 5 each, minimizing the difference in total scores.

**Chain of Thought:**

1. Calculate the total sum of all player scores
2. Generate all possible combinations of 5 players for one team
3. For each combination, the other 5 players automatically form the second team
4. Calculate the score difference between the two teams
5. Track and return the minimum difference found

---
"""
## Python Solution

from itertools import combinations

def min_team_difference(scores):
    total_score = sum(scores)
    min_diff = float('inf')
    
    # Generate all combinations of 5 players
    for team1 in combinations(range(10), 5):
        team1_score = sum(scores[i] for i in team1)
        team2_score = total_score - team1_score
        diff = abs(team1_score - team2_score)
        min_diff = min(min_diff, diff)
        
        # Early exit if perfect split found
        if min_diff == 0:
            break
    
    return min_diff

# Read input
scores = list(map(int, input().split()))
print(min_team_difference(scores))



"""
## Example Walkthrough

**Input:** `1 2 3 4 5 6 7 8 9 10`

**Step-by-step:**

1. **Total score:** 1+2+3+4+5+6+7+8+9+10 = 55
2. **Ideal split:** Each team should have 27.5 (impossible with integers)
3. **Best possible:** One team gets 27, other gets 28 (difference = 1)
4. **Example optimal split:**
   - Team 1: {1, 2, 4, 9, 10} → Score = 26
   - Team 2: {3, 5, 6, 7, 8} → Score = 29
   - Difference = |26 - 29| = 3

   Or better:
   - Team 1: {1, 2, 5, 9, 10} → Score = 27
   - Team 2: {3, 4, 6, 7, 8} → Score = 28
   - Difference = |27 - 28| = 1

**Output:** `1`

The algorithm tries all C(10,5) = 252 possible combinations to find the minimum difference.
"""