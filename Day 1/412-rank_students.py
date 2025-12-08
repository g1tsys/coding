# Student Ranking Problem - Translation and Solution

## Problem Description
"""
A teacher needs to rank students by their total score or individual subject scores. 

**Input Format:**
- Line 1: Two integers `n` (number of students, 0 < n < 100) and `m` (number of subjects, 0 < m < 10)
- Line 2: `m` subject names separated by spaces (only English letters, max 10 chars each, no duplicates)
- Next n lines: Each contains a student name followed by `m` scores (0-100) corresponding to the subjects
- Last line: Subject name to rank by (if doesn't exist, rank by total score)

**Output Format:**
- Student names sorted by the specified criteria, space-separated
- If scores are equal, sort by student name alphabetically

## Solution Approach (Python)

**Chain of Thought:**

1. **Parse input data**: Read student count, subject count, and subject names
2. **Store student data**: Use a dictionary to map student names to their score lists
3. **Identify ranking criterion**: Check if the specified subject exists; if not, use total score
4. **Sort students**: 
   - Primary key: Score (descending - higher scores first)
   - Secondary key: Name (ascending - alphabetical order)
5. **Output results**: Print sorted student names

## Example Walkthrough

**Input:**
```
3 2
Math English
Alice 85 90
Bob 90 85
Charlie 85 85
Math
```

**Step-by-step execution:**

1. **Read n=3, m=2**: We have 3 students and 2 subjects
2. **Read subjects**: ["Math", "English"]
3. **Read student data**:
   - Alice: [85, 90] (Math: 85, English: 90)
   - Bob: [90, 85] (Math: 90, English: 85)
   - Charlie: [85, 85] (Math: 85, English: 85)
4. **Ranking subject**: "Math" (exists at index 0)
5. **Sorting by Math scores**:
   - Bob: 90 (highest Math score)
   - Alice: 85 (tied with Charlie, but "Alice" comes before "Charlie" alphabetically)
   - Charlie: 85
6. **Output**: `Bob Alice Charlie`

**Alternative scenario** - If ranking subject was "Science" (doesn't exist):
- Would rank by total score instead:
  - Alice: 175 total
  - Bob: 175 total (tied, but "Alice" < "Bob" alphabetically)
  - Charlie: 170 total
- Output would be: `Alice Bob Charlie`

## Annotated Solution
"""
# Define the main function to solve the problem

def solve():
    # Read the first line: n (number of students) and m (number of subjects)
    # map(int, ...) converts string inputs to integers
    # input().split() splits the input line by spaces
    n, m = map(int, input().split())
    
    # Read the second line: subject names
    # split() divides the line into a list of subject names
    subjects = input().split()
    
    # Create an empty dictionary to store student data
    # Key: student name (string), Value: list of scores (list of integers)
    students = {}
    
    # Loop n times to read each student's data
    for _ in range(n):
        # Read one line and split it into parts
        # First part is name, remaining parts are scores
        data = input().split()
        
        # Extract the student's name (first element)
        name = data[0]
        
        # Extract the scores (all elements after the first)
        # map(int, ...) converts string scores to integers
        # list() converts the map object to a list
        scores = list(map(int, data[1:]))
        
        # Store the student's name and scores in the dictionary
        students[name] = scores
    
    # Read the subject name to rank by
    # strip() removes any leading/trailing whitespace
    rank_subject = input().strip()
    
    # Check if the ranking subject exists in the subjects list
    if rank_subject in subjects:
        # If it exists, find its index position (0-based)
        subject_index = subjects.index(rank_subject)
    else:
        # If it doesn't exist, set index to -1 (flag for total score ranking)
        subject_index = -1
    
    # Sort the students based on the ranking criterion
    if subject_index == -1:
        # Rank by total score (subject doesn't exist)
        # sorted() sorts the dictionary items (name-scores pairs)
        # key=lambda x: ... defines the sorting criteria
        # -sum(x[1]): negative sum for descending order (higher scores first)
        # x[0]: student name for ascending alphabetical order (tie-breaker)
        sorted_students = sorted(students.items(), 
                                key=lambda x: (-sum(x[1]), x[0]))
    else:
        # Rank by specific subject score
        # -x[1][subject_index]: negative score at subject_index for descending order
        # x[0]: student name for ascending alphabetical order (tie-breaker)
        sorted_students = sorted(students.items(), 
                                key=lambda x: (-x[1][subject_index], x[0]))
    
    # Create the output string
    # List comprehension extracts just the names from sorted_students
    # ' '.join() combines the names with spaces between them
    result = ' '.join([name for name, _ in sorted_students])
    
    # Print the final result
    print(result)

# Call the solve function to execute the program
solve()

