"""Based on the text provided from the web page, here is the extracted question and the associated thought process specifically for the **Python** programming language section.

### **Question**
**Title:** Spiral Digital Matrix (螺旋数字矩阵)
**Context:** During isolation, Xiao Ming invented a way to write numbers. Given a total count of numbers `n` and a number of rows `m` (where `0 < n <= 999`, `0 < m <= 999`), write numbers starting from 1 at the top-left corner, filling in a spiral pattern (clockwise, moving inward) up to `n`, forming an `m`-row matrix.

**Constraints:**
1. Every row must have the same number of elements.
2. The number of columns should be as few as possible.
3. When filling, prioritize filling the outer layers first.
4. If there are not enough numbers to fill the matrix, use a single `*` to occupy the remaining spots.

**Input:**
Two integers separated by a space: `n` and `m`.

**Output:**
The unique matrix that meets the requirements.

---

### **Thought Process (Python Logic)**

Although the text omits the detailed step-by-step narrative for Python (it jumps from "Python Language Thought" directly to "Python Code"), the logic is explicitly defined in the **C++ section** and applies universally to the Python implementation as follows:

1.  **Calculate Matrix Dimensions:**
    *   Determine the number of columns (`cols`) required. Since every row must have the same number of elements and columns should be minimized, calculate `cols` based on `n` and `m` such that `m * cols >= n`.
    *   Formula: `cols = (n + m - 1) // m` (integer division to round up).

2.  **Initialize the Matrix:**
    *   Create an `m x cols` matrix (list of lists in Python).
    *   Initialize all cells with `0` (as a placeholder for empty spots before filling).

3.  **Define Movement Directions:**
    *   Set up a direction array representing the four clockwise directions: **Right** `(0, 1)`, **Down** `(1, 0)`, **Left** `(0, -1)`, **Up** `(-1, 0)`.
    *   Initialize a direction index `direction_idx = 0` to start moving Right.

4.  **Spiral Traversal & Filling:**
    *   Start at the top-left corner: `row = 0`, `col = 0`.
    *   Loop from `num = 1` to `n`:
        *   Assign the current number `num` to `matrix[row][col]`.
        *   Calculate the *next* position `next_row`, `next_col` based on the current direction.
        *   **Boundary Check:** Check if the next position is out of bounds (outside the `m x cols` grid) OR if the cell is already filled (not `0`).
        *   **Turn:** If the next position is invalid, rotate the direction index: `direction_idx = (direction_idx + 1) % 4`.
        *   Update `row` and `col` to the new valid position.

5.  **Output Formatting:**
    *   Iterate through the matrix row by row.
    *   If a cell contains `0`, print `*`.
    *   Otherwise, print the number.
    *   Ensure each row is printed on a new line.

"""


# Conceptual Python structure based on the logic above
def solve_spiral_matrix(n, m):
    # 1. Calculate columns
    cols = (n + m - 1) // m
    
    # 2. Initialize matrix with 0
    matrix = [[0] * cols for _ in range(m)]
    
    # 3. Directions: Right, Down, Left, Up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dir_idx = 0
    row, col = 0, 0
    
    # 4. Fill spiral
    for num in range(1, n + 1):
        matrix[row][col] = num
        
        # Calculate next position
        next_row = row + directions[dir_idx][0]
        next_col = col + directions[dir_idx][1]
        
        # Check bounds and if cell is already filled
        if (not (0 <= next_row < m and 0 <= next_col < cols)) or matrix[next_row][next_col] != 0:
            # Change direction
            dir_idx = (dir_idx + 1) % 4
            next_row = row + directions[dir_idx][0]
            next_col = col + directions[dir_idx][1]
            
        row, col = next_row, next_col

    # 5. Output
    for r in matrix:
        print(" ".join(str(x) if x != 0 else "*" for x in r))