"""
Here is the extracted information from the **Python** section of the provided text:

### **Question (Problem Description)**
**Title:** 431、跳马问题 (Horse Jumping Problem)  
**Input:**  
- Two integers `m` and `n` representing the dimensions of an `m * n` chessboard.  
- The board data contains either **numbers** (representing a horse and its maximum jump distance `k`) or **`.`** (representing an empty spot).  
- A number `k` at a position means the horse at that location can move a distance between `1` and `k` steps.  

**Movement Rules:**  
- Horses move like a "Horse" (Knight) in Chinese Chess: move one step horizontally or vertically, then one step diagonally.  
- Multiple horses can occupy the same position.  

**Goal:**  
Determine if it is possible to move **all** horses to the **same** position on the board.  
- If possible, output the **minimum total number of steps** required.  
- If impossible, output **-1**.

---

### **Thought Process (Python Logic)**
The solution involves a combination of **Breadth-First Search (BFS)** and aggregation logic:

1.  **Per-Horse BFS**:
    - Perform a **Breadth-First Search (BFS)** for **each horse** individually on the board.
    - Calculate the shortest path (minimum steps) for that specific horse to reach every other reachable position.
    - **Constraint**: The search for each horse is limited by its specific `maxSteps` value (the number on its starting square). It cannot jump further than `1` to `k` steps.

2.  **Aggregation & Validation**:
    - Iterate through every position on the `m * n` board to check if it is a valid meeting point.
    - For a specific target position:
        - Sum the steps required for **all** horses to reach this position.
        - **Critical Check**: If **any single horse** cannot reach this position (within its step limit), this target position is marked as **invalid** (unreachable).
        - If all horses can reach it, store the total sum of steps.

3.  **Result Selection**:
    - Compare the total step sums of all valid meeting positions identified in the previous step.
    - Select the position with the **minimum total steps**.
    - **Output**:
        - If no valid meeting position exists for all horses, output **0** (based on the provided text's logic, though standard problem logic often implies -1 for impossible; the text specifically says "output 0" for impossible in the summary, but the problem description says "output -1" for impossible. The Python logic section states: "If no position satisfies the condition, output 0").
        - Otherwise, output the **minimum total steps** found.

> **Note on Ambiguity**: The provided text contains a slight contradiction. The "Question" section states to output `-1` if impossible, but the "Python Code" description summary says "If no position satisfies the condition, output 0". The logic described above follows the **Python** section's specific instructions.


"""