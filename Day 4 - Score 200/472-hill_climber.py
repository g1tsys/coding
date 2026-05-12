"""Based on the text provided, here are the extracted details specifically for the **Python** section. Please note that while the text includes section headers for "Thought Process" and "Python Code," the actual content under these specific Python headers was not fully detailed in the provided snippet (the content appears to be truncated or represented by placeholders like "🎉 Python code" without the actual code block following it).

### **Question (题目)**
*   **Description**: You are given a 1D array representing a map where indices are horizontal positions and values are relative altitudes (0 represents ground).
*   **Goal**: Determine how many peaks in the map can be climbed safely and returned to ground without the climber's stamina dropping to zero.
*   **Stamina Logic**:
    *   Climbing up consumes stamina based on the height difference multiplied by 2 (upward slope cost).
    *   Climbing down consumes stamina based on the height difference (downward slope cost).
    *   A peak is valid if the total stamina required for a round trip (starting from ground 0, reaching the peak, and returning to ground 0) is strictly less than the climber's available stamina.
    *   *Note*: The example logic suggests the cost calculation might vary slightly depending on the specific path taken (e.g., $1 \times 2 + 1 \times 2 + 2 \times 2$ for ascent, $2 \times 1 + 1 \times 1 + 1 \times 1$ for descent).

### **Input**
1.  **Line 1**: A 1D array representing the map (e.g., `[0,1,2,4,3,1,0,0,1,2,3,1,2,1,0]`).
2.  **Line 2**: An integer representing the climber's total stamina.

### **Output**
*   An integer representing the count of peaks that can be safely climbed and returned from, given the stamina constraint.

### **Thought Process (Python Approach)**
*Since the specific Python algorithm steps were not explicitly detailed in the text snippet, the logical process derived from the problem description is:*

1.  **Parse Input**:
    *   Read the array string and convert it to a list of integers.
    *   Read the stamina integer.
2.  **Identify Peaks**:
    *   Iterate through the array to find "local maxima."
    *   A peak is a position where the height is strictly greater than its immediate neighbors.
    *   Boundary conditions: The first or last element can be a peak if it's higher than its single neighbor (though the problem implies climbing from "ground" which is often index 0, the text mentions peaks can be at boundaries if higher than adjacent).
3.  **Calculate Stamina Cost for Each Peak**:
    *   For each identified peak, calculate the cost to reach it from a valid ground starting point (index 0 or any index with height 0).
    *   **Ascent Cost**: Sum of `(height_difference * 2)` for each step upward.
    *   **Descent Cost**: Sum of `(height_difference * 1)` for each step downward.
    *   **Total Cost**: Ascent Cost + Descent Cost.
    *   *Optimization Note*: The text implies the climber can start from *any* ground position (0) to reach the peak if it's the most efficient route, or specifically from index 0. The example shows `0 -> 3 -> 0`.
4.  **Filter Valid Peaks**:
    *   Check if `Total Cost < Stamina`.
    *   If yes, increment the count.
5.  **Output Result**:
    *   Print the final count of valid peaks.

### **Python Code (Reference)**
*The provided text mentions a section for "Python Code" but does not contain the actual code implementation. The placeholder `🎉 Python代码` indicates where the code should be, but it is missing from the snippet.*

**Search for the actual code or logic implementation:**
"""
# 注意攀登者体力必须要大于 上山、下山体力消耗之和
# 定义一个函数，接受地图和攀登者的体力作为参数
def can_climb_peaks(altitude_map, stamina):
    n = len(altitude_map)  # 获取地图长度
    peaks = []  # 初始化一个列表，用于存储所有的山峰位置

    # 遍历地图，找出所有的山峰
    for i in range(n):
        # 判断当前位置是否为山峰：在数组边界且高于相邻位置，或在数组中间且高于两侧
        if (i == 0 and altitude_map[i] > altitude_map[i + 1]) or \
                (i == n - 1 and altitude_map[i] > altitude_map[i - 1]) or  \
                (0 < i < n - 1 and altitude_map[i] > altitude_map[i - 1] and altitude_map[i] > altitude_map[i + 1]):
            peaks.append(i)  # 将山峰位置加入到列表中

    climbable_count = 0  # 初始化可攀登山峰的数量

    # 遍历所有山峰，判断每座山峰是否可攀登
    for peak in peaks:

        left_ground = right_ground = None  # 初始化最近的左右地面位置

        # 向左遍历找到最近的地面位置
        for i in range(peak, -1, -1):
            if altitude_map[i] == 0:
                left_ground = i
                break

        # 向右遍历找到最近的地面位置
        for i in range(peak, n):
            if altitude_map[i] == 0:
                right_ground = i
                break

        # 定义一个计算从一点到另一点的体力消耗的函数
        def calculate_cost(start, end):
            if start is None or end is None:
                return float('inf')  # 如果起点或终点不存在，返回无穷大
            cost = 0  # 初始化消耗的体力
            # 计算上山和下山的体力消耗
            if start < end:  # 如果是向右移动
                for i in range(start, end):
                    if altitude_map[i + 1] > altitude_map[i]:  # 上山
                        cost += 2 * (altitude_map[i + 1] - altitude_map[i])
                    else:  # 下山
                        cost += (altitude_map[i] - altitude_map[i + 1])
            else:  # 如果是向左移动
                for i in range(start, end, -1):
                    if altitude_map[i - 1] > altitude_map[i]:  # 上山
                        cost += 2 * (altitude_map[i - 1] - altitude_map[i])
                    else:  # 下山
                        cost += (altitude_map[i] - altitude_map[i - 1])
            return cost  # 返回总体力消耗

        # 计算从最近的左侧地面到山峰再返回的总体力消耗
        total_cost_to_left = calculate_cost(left_ground, peak) + calculate_cost(peak, left_ground)
        # 计算从最近的右侧地面到山峰再返回的总体力消耗
        total_cost_to_right = calculate_cost(right_ground, peak) + calculate_cost(peak, right_ground)

        # 如果左侧或右侧的返回路径的体力消耗小于攀登者的体力，则认为该山峰可攀登
        if (left_ground is not None and total_cost_to_left < stamina) or \
                (right_ground is not None and total_cost_to_right < stamina):
            climbable_count += 1  # 可攀登的山峰数量加一

    return climbable_count  # 返回可攀登的山峰数量

input_map = list(map(int, input().split(',')))  # 读取地图，转换为整数列表
input_stamina = int(input()) 
print(can_climb_peaks(input_map, input_stamina))


