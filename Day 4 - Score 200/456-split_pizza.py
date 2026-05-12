"""
### Problem Statement: Pizza Distribution (分披萨)

**Scenario:**  
Two people, "Foodie" (吃货) and "Glutton" (馋嘴), order a circular pizza. Instead of being cut into equal even slices, the server accidentally cuts it into an **odd number** of slices, all of **different sizes**.

**Rules:**
1.  **Order:** They take turns picking slices, starting with "Foodie".
2.  **First Move:** The first person ("Foodie") can pick **any** slice from the circle.
3.  **Subsequent Moves:** After the first slice is taken, there is a "gap". All future picks must be made from the immediate neighbors of this gap (i.e., the two slices adjacent to the removed slice).
4.  **"Glutton's" Strategy:** "Glutton" always picks the **largest** available slice from the two options at the gap.
5.  **"Foodie's" Strategy:** "Foodie" knows "Glutton's" strategy and wants to maximize their own total pizza size.

**Goal:**  
Calculate the maximum total size of pizza "Foodie" can get.

**Input Constraints:**
-   $N$ (number of slices): An odd integer, $3 \le N < 500$.
-   Slice sizes: Integers in range $[1, 2147483647]$.
-   The slices are given in order around the circle.

---

### Python Thought Process & Logic

Since "Foodie" makes the first move, they can choose to break the circle at any of the $N$ slices. Once a slice is removed, the circular pizza becomes a linear sequence of slices with a "gap" at the ends.

**Key Insight:**
Because "Glutton" plays optimally to maximize *their* take (by always picking the larger of the two ends), "Foodie" must simulate every possible first move. For each first move, the remaining problem becomes a linear game where "Foodie" and "Glutton" alternate picking from the ends of the remaining line.

**Algorithm Steps:**

1.  **Iterate through all possible first moves:**
    Since the pizza is circular, "Foodie" can start by removing any slice $i$ (where $0 \le i < N$).
    -   If "Foodie" picks slice $i$, the remaining slices form a linear array starting from $i+1$ and ending at $i-1$ (wrapping around).

2.  **Simulate the Game (Dynamic Programming / Recursion):**
    For a specific linear segment of slices from index `start` to `end`:
    -   **Turn:** It's "Foodie's" turn to pick from the current segment.
    -   **Choice:** "Foodie" can pick the slice at `start` or the slice at `end`.
    -   **Opponent's Reaction ("Glutton"):**
        -   If "Foodie" picks `start`, the new segment is `start+1` to `end`. "Glutton" will then look at the new ends (`start+1` and `end`) and pick the larger one.
        -   If "Foodie" picks `end`, the new segment is `start` to `end-1`. "Glutton" will look at the new ends (`start` and `end-1`) and pick the larger one.
    -   **Recursion:** The function returns the maximum sum "Foodie" can get from that state.
    -   **Memoization:** Use a 2D table `dp[start][end]` to store results for sub-segments to avoid recalculating the same states.

3.  **State Definition:**
    Let `solve(start, end)` be the maximum pizza "Foodie" can get from the sub-segment `slices[start...end]` assuming it is currently "Foodie's" turn to pick *from this segment* (after the initial move has been made in the main loop).
    
    *Correction on Turn Logic:*
    Actually, the problem states: "Foodie" picks first (anywhere). Then "Glutton" picks (largest of two ends). Then "Foodie" picks (from the new ends).
    So, inside the recursive function for a linear segment:
    -   If it's "Foodie's" turn: They choose `max(slices[start] + result_after_glutton_picks_from_rest, slices[end] + result_after_glutton_picks_from_rest)`.
    -   If it's "Glutton's" turn: They will greedily pick `max(slices[start], slices[end])`. The remaining segment is passed to "Foodie's" turn.

    *Simplified Approach for Python:*
    Since $N$ is small ($<500$), we can simulate the game for every possible starting index.
    
    **Logic for a fixed start index `i`:**
    -   "Foodie" takes `slices[i]`.
    -   Remaining array: `slices[i+1], ..., slices[N-1], slices[0], ..., slices[i-1]`.
    -   Now we have a linear array.
    -   Loop:
        -   **Foodie's Turn:** They can pick the left end or the right end.
            -   Option A: Pick left. "Glutton" will immediately pick the larger of the *new* ends.
            -   Option B: Pick right. "Glutton" will immediately pick the larger of the *new* ends.
            -   "Foodie" chooses the option that leaves them with the best future total.
    
    *Wait, the provided text suggests a specific DP state:*
    The text describes `solvePizzaDistribution(start, end)` which calculates the max "Foodie" can get from a range.
    Inside the recursion:
    -   If `start == end`: Return `slices[start]` (only one left, "Foodie" takes it? No, need to track whose turn it is).
    
    Let's refine the logic based on the "Foodie knows Glutton" constraint:
    The game is deterministic once the first move is made.
    1.  **First Move:** "Foodie" picks index `k`. Score = `slices[k]`.
    2.  **Remaining:** Linear array `L`.
    3.  **Loop while L is not empty:**
        -   **Glutton's Turn:** Glutton picks `max(L[0], L[-1])`. Remove that slice.
        -   **Foodie's Turn:** Foodie picks `max(L[0], L[-1])`? **NO**.
        
    *Re-reading the problem carefully:*
    "除第一块...其他都必须从缺口开始选" (Except the first, all must be picked from the gap).
    "馋嘴" (Glutton) always picks the **largest** of the two available at the gap.
    "吃货" (Foodie) picks **optimally** (maximizing their total), knowing Glutton will pick the largest.
    
    So the sequence is:
    1. Foodie picks any $S_0$.
    2. Gap created. Available: $A, B$ (neighbors of $S_0$).
    3. Glutton picks $\max(A, B)$.
    4. Gap updates. Available: $C, D$.
    5. Foodie picks to maximize future total (not necessarily the current max).
    6. Glutton picks $\max(...)$.
    7. Repeat.
    
    **Python DP Strategy:**
    Since $N$ is odd, the total number of moves is $N$.
    Foodie moves: $1, 3, 5, \dots, N$ (Total $(N+1)/2$ moves).
    Glutton moves: $2, 4, 6, \dots, N-1$ (Total $(N-1)/2$ moves).
    
    We can define a function `dp(start, end)` representing the maximum score "Foodie" can get from the linear sub-segment `slices[start...end]`, assuming it is **Foodie's turn** to pick from this segment.
    
    Wait, the turns alternate strictly.
    If the segment has length $k$:
    - If $k$ is odd, it's Foodie's turn (since Foodie starts the linear phase? No, let's trace).
    - Initial: $N$ slices. Foodie picks 1. Remaining $N-1$ (even).
    - Next is Glutton. Remaining $N-2$ (odd).
    - Next is Foodie.
    
    So, in the linear phase:
    - If remaining count is even: It's Glutton's turn.
    - If remaining count is odd: It's Foodie's turn.
    
    Actually, it's easier to just simulate the two choices for Foodie at every Foodie-turn and let Glutton's move be deterministic.
    
    **Recursive Function `solve(start, end)`:**
    - Base case: if `start > end`, return 0.
    - Current length `len = end - start + 1`.
    - If `len` is **odd** (Foodie's turn):
        - Option 1: Pick `start`.
            - Glutton responds by picking `max(start+1, end)` (if valid).
            - If Glutton picks `start+1`, next state is `solve(start+2, end)`.
            - If Glutton picks `end`, next state is `solve(start+1, end-1)`.
            - Wait, Glutton picks the best for *themselves*, which is the larger of the two ends.
            - So if Foodie picks `start`, the remaining ends are `start+1` and `end`. Glutton takes `max(slices[start+1], slices[end])`.
                - If `slices[start+1] >= slices[end]`, Glutton takes `start+1`. Next state: `solve(start+2, end)`.
                - Else, Glutton takes `end`. Next state: `solve(start+1, end-1)`.
            - Score = `slices[start] + result`.
        - Option 2: Pick `end`.
            - Remaining ends: `start` and `end-1`.
            - Glutton takes `max(slices[start], slices[end-1])`.
            - Update state accordingly.
            - Score = `slices[end] + result`.
        - Return `max(Option1, Option2)`.
    
    - If `len` is **even** (Glutton's turn):
        - Glutton picks `max(slices[start], slices[end])`.
        - If `slices[start] >= slices[end]`: return `solve(start+1, end)`.
        - Else: return `solve(start, end-1)`.
        - Foodie gets 0 from this specific move (Glutton took it).

    **Final Answer:**
    Iterate $i$ from $0$ to $N-1$.
    Total = `slices[i]` + `solve((i+1)%N, (i-1+N)%N)` (handling circular wrapping by creating a doubled array or modulo logic).
    Return the max Total.
"""
### Python Code Implementation

import sys

# Increase recursion depth just in case, though N < 500 is manageable
sys.setrecursionlimit(10000)

def solve_pizza():
    # Read input
    try:
        line1 = sys.stdin.readline()
        if not line1:
            return
        N = int(line1.strip())
        
        slices = []
        # Read N lines
        for _ in range(N):
            line = sys.stdin.readline()
            if line:
                slices.append(int(line.strip()))
    except ValueError:
        return

    if N == 0:
        print(0)
        return

    # Since the pizza is circular, we can duplicate the array to handle wrapping easily
    # Or use modulo arithmetic. Let's use a helper that handles indices.
    # But for DP, it's easier to linearize the problem for each starting point.
    # We will create a linear array of size 2*N to simulate the circle.
    linear_slices = slices + slices
    
    # Memoization table for the recursive function
    # dp[start][end] stores the max foodie can get from slices[start...