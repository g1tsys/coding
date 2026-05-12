"""
Based on the webpage content provided, here is the extracted problem description and the associated thought process specifically for the **Python** language section.

*Note: The provided text contains the headings for the Python section (🎈 Python 语言 思路 and 🎉 Python 代码) but does not include the actual detailed text or code within those sections. I have reconstructed the **thought process** based on the problem logic described in the "Question Description" and standard algorithms used to solve this specific graph traversal problem in Python.*

### 🎃 Problem Description: Precision Nucleic Acid Testing

**Scenario:**
To achieve precise pandemic prevention and avoid the waste of full-population testing, we need to identify the specific group of people who may be infected. Based on epidemiological data and big data analysis, we know whether there are trajectory intersections (contacts) between individuals in terms of time and space.

**Objective:**
Given a list of confirmed case IDs ($X_1, X_2, \dots, X_n$), identify all individuals who need to undergo nucleic acid testing.
- **Rule:** Anyone reachable from a confirmed case via a chain of contacts needs testing.
- **Exception:** Confirmed cases themselves do not need to be tested again (they are already confirmed).
- **Output:** The total count of people requiring testing.

**Example Chain:**
If A is confirmed, and A contacted B, B contacted C, C contacted D, and D contacted E:
- A is confirmed (no test needed).
- B, C, D, and E are all reachable.
- **Result:** B, C, D, E need testing. Count = 4.

**Input Format:**
1.  **Line 1:** Total number of people $N$.
2.  **Line 2:** Comma-separated list of confirmed case IDs (e.g., `0,2,5`).
3.  **Line 3 to N+2:** An $N \times N$ adjacency matrix where:
    - `0` means no contact.
    - `1` means contact exists.

**Output Format:**
- A single integer representing the number of people needing testing.

---

### 🐍 Python Language: Thought Process & Logic

Since the specific text was missing from the source, here is the logical deduction required to solve this in Python:

**1. Model the Problem as a Graph:**
- The people are **nodes** in a graph.
- The contact matrix represents **edges**. If `matrix[i][j] == 1`, there is an undirected edge between person `i` and person `j`.
- The problem asks for the **Union of Reachable Nodes** from a set of starting nodes (confirmed cases), excluding the starting nodes themselves. This is a classic **Graph Traversal** problem.

**2. Algorithm Selection:**
- **Breadth-First Search (BFS)** or **Depth-First Search (DFS)** are suitable.
- **Why BFS?** It naturally explores layer by layer (direct contacts, then contacts of contacts), which fits the "virus spread" logic well. It also handles cycles (A contacts B, B contacts A) gracefully by using a `visited` set.
- **Alternative:** Union-Find (Disjoint Set Union) could work, but BFS/DFS is more direct for "reachability" from a specific set of sources.

**3. Step-by-Step Execution Plan (Python):**
1.  **Read Input:**
    - Parse $N$.
    - Parse the list of confirmed cases (convert to a set for $O(1)$ lookup).
    - Parse the $N \times N$ matrix.
2.  **Initialize Traversal:**
    - Create a `visited` set to keep track of all people found so far.
    - Add all **confirmed cases** to the `visited` set immediately (they are the starting points).
    - Create a queue (for BFS) and enqueue all confirmed cases.
3.  **Traverse:**
    - While the queue is not empty:
        - Dequeue a person `current`.
        - Iterate through all other people `neighbor` (0 to N-1).
        - If `matrix[current][neighbor] == 1`:
            - If `neighbor` is **not** in `visited`:
                - Add `neighbor` to `visited`.
                - Enqueue `neighbor`.
4.  **Calculate Result:**
    - The `visited` set now contains all confirmed cases PLUS all people they reached.
    - The number of people needing testing = `len(visited) - len(confirmed_cases)`.
    - Alternatively, count how many people were added during the traversal (excluding the initial queue).

**4. Edge Cases to Consider:**
- **No contacts:** If the matrix is all zeros, the result is 0.
- **Disconnected components:** People not connected to any confirmed case are ignored.
- **Self-loops:** The matrix usually has 0 on diagonals, but if 1, the logic holds (already visited).
- **Input Parsing:** The confirmed cases are comma-separated strings; ensure they are converted to integers.

**5. Python Implementation Sketch:**

from collections import deque

def solve():
    # 1. Input Reading
    try:
        line1 = input().strip()
        if not line1: return # Handle empty
        n = int(line1)
        
        line2 = input().strip()
        confirmed_str = line2.split(',')
        confirmed_cases = set(int(x.strip()) for x in confirmed_str)
        
        # 2. Build Graph (Adjacency Matrix)
        matrix = []
        for _ in range(n):
            row = list(map(int, input().strip().split()))
            matrix.append(row)
            
        # 3. BFS Initialization
        visited = set()
        queue = deque()
        
        for case_id in confirmed_cases:
            visited.add(case_id)
            queue.append(case_id)
            
        # 4. BFS Execution
        while queue:
            u = queue.popleft()
            for v in range(n):
                if matrix[u][v] == 1 and v not in visited:
                    visited.add(v)
                    queue.append(v)
        
        # 5. Result Calculation
        # Total reachable includes confirmed cases, so subtract them
        result = len(visited) - len(confirmed_cases)
        print(result)
        
    except EOFError:
        pass

### Summary of the Approach
The core logic is **Graph Reachability**. You treat the contact matrix as an adjacency matrix and perform a **BFS** starting from all confirmed cases simultaneously. The final answer is the count of all unique nodes reached during the BFS, minus the initial set of confirmed cases.

"""


# 定义一个类Main来处理整个流调任务
class Main:
    # 初始化函数
    def __init__(self, contactMatrix):
        self.peopleCount = len(contactMatrix)  # 总人数
        self.visited = [False] * self.peopleCount  # 标记每个人是否已被访问，避免重复计算
        self.infectedSet = set()  # 存储可能被感染的人员编号集合
        self.contactMatrix = contactMatrix  # 存储所有人员之间的接触矩阵

    # 深度优先搜索函数
    def depthFirstSearch(self, person):
        self.visited[person] = True  # 标记当前人员已访问
        for i in range(self.peopleCount):  # 遍历与当前人员有接触的所有人
            # 如果当前人员与i号人员有接触，并且i号人员尚未被访问
            if self.contactMatrix[person][i] == 1 and not self.visited[i]:
                self.infectedSet.add(i)  # 将i号人员加入可能被感染的人员集合中
                self.depthFirstSearch(i)  # 对i号人员进行深度优先搜索

    # 统计需要进行核酸检测的人数的函数
    def countInfectedPeople(self, initialCases):
        for initialCase in initialCases:  # 遍历每个确诊病例
            if not self.visited[initialCase]:
                self.depthFirstSearch(initialCase)  # 对未被访问的确诊病例进行深度优先搜索

        # 计算最终需要做核酸检测的人数
        initialSet = set(initialCases)  # 将确诊病例编号转换成集合
        self.infectedSet -= initialSet  # 从可能被感染的人员集合中排除确诊病例自身
        return len(self.infectedSet)  # 返回最终需要进行核酸检测的人数

# 读入总人数
peopleCount = int(input())
# 读入确诊病例人员编号，并转换成整数列表
initialCases = list(map(int, input().split(',')))

# 读入接触矩阵
contactMatrix = []
for _ in range(peopleCount):
    row = list(map(int, input().split(',')))
    contactMatrix.append(row)

# 创建Main类的实例，传入接触矩阵
infectionTracking = Main(contactMatrix)
# 调用实例方法，传入确诊病例编号，获取需要进行核酸检测的人数
result = infectionTracking.countInfectedPeople(initialCases)
# 输出需要进行核酸检测的人数
print(result)


