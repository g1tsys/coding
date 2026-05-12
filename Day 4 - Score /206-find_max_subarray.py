"""
Based on the text provided, here is the extracted problem description, the logical thought process for solving it, and the corresponding Python implementation.

### Problem Description

**Title:** Maximum Geometric Mean Subarray
**Source:** Huawei OD Machine Test (2026)

**Task:**
Given an array of $N$ positive numbers, find a contiguous subarray with a length of at least $L$ that has the **maximum geometric mean**.
- The geometric mean of $K$ numbers is the $K$-th root of their product: $\sqrt[K]{x_1 \times x_2 \times \dots \times x_K}$.
- If multiple subarrays have the same maximum geometric mean, choose the one with the **smallest length**.
- If there are still ties, choose the **first** one (smallest starting index).

**Output:**
The starting index (0-based) and the length of the subarray, separated by a space.

**Constraints:**
- $1 \le N \le 100,000$
- $1 \le L \le N$
- $10^{-9} \le \text{numbers}[i] \le 10^9$
- All numbers are positive.

---

### Python Thought Process (Algorithm Analysis)

To solve this efficiently, we must avoid calculating the geometric mean directly for every possible subarray, as that would involve multiplying up to $N$ numbers and taking large roots, leading to **Time Limit Exceeded (TLE)** and **Floating Point Overflow/Underflow** issues.

**Key Insight: Logarithms**
The geometric mean of a subarray $A[i \dots j]$ is:
$$ GM = \sqrt[j-i+1]{\prod_{k=i}^{j} A[k]} $$

Taking the logarithm (base $e$ or 10) of both sides:
$$ \ln(GM) = \frac{1}{j-i+1} \sum_{k=i}^{j} \ln(A[k]) $$

Since the logarithm function is monotonically increasing, **maximizing the Geometric Mean is equivalent to maximizing the Logarithm of the Geometric Mean**.
This transforms the problem from:
1. Multiplying numbers (prone to overflow)
2. Taking $N$-th roots

To:
1. Summing logarithms (stable)
2. Dividing by length (simple arithmetic)

**Algorithm Steps:**

1.  **Preprocessing:**
    - Convert the input array `numbers` into an array of logarithms: `log_nums[i] = log(numbers[i])`.
    - Compute a **Prefix Sum** array `prefix_sum` for `log_nums`.
      - `prefix_sum[i]` stores the sum of logs from index 0 to `i-1`.
      - The sum of logs for a subarray from `i` to `j` (inclusive) is `prefix_sum[j+1] - prefix_sum[i]`.

2.  **Iterate and Find Maximum:**
    - We need to find a subarray starting at `i` with length `len` (where `len >= L`).
    - Since $N$ is up to $10^5$, an $O(N^2)$ approach (checking every subarray) will be too slow. However, the problem constraints and the nature of geometric means often allow for specific optimizations or a sliding window approach if the data has specific properties.
    - *Correction on Complexity:* For the general case of "Maximum Average Subarray with length at least L", a standard $O(N^2)$ check is too slow. However, in competitive programming contexts like Huawei OD, sometimes $N=10^5$ with a simple $O(N)$ or $O(N \log N)$ solution is required.
    - **Optimization Strategy:**
      The problem asks for the **global** maximum geometric mean.
      Let's reconsider the properties. Is it possible to use a sliding window?
      Actually, for "Maximum Average Subarray with length $\ge L$", there is a known binary search on the answer approach that runs in $O(N \log(\text{precision}))$.
      
      **Binary Search Approach:**
      - We want to check if there exists a subarray of length $\ge L$ such that $\frac{\sum \ln(A)}{len} \ge X$.
      - This inequality can be rewritten as: $\sum (\ln(A) - X) \ge 0$.
      - We can transform the array to $B[i] = \ln(A[i]) - X$.
      - The problem becomes: Does there exist a subarray of length $\ge L$ in $B$ with a sum $\ge 0$?
      - This can be solved in $O(N)$ using prefix sums: calculate prefix sums of $B$, and for each $j \ge L$, check if `prefix_sum[j] - min(prefix_sum[0...j-L]) >= 0`.
      
      **Tie-Breaking Logic:**
      The binary search finds the *value* of the maximum mean. To find the specific index and length with tie-breaking rules (smallest length, then first index), we might need a slightly more careful implementation or a final pass.
      
      **Alternative (Simpler for OD context):**
      Often in these specific Huawei OD problems, the constraints or test cases allow for a slightly less complex approach, or the $O(N \log N)$ binary search is the intended solution. Given the "10^-10" precision note, binary search on the answer is the robust mathematical approach.

      **Refined Plan:**
      1. Convert inputs to logs.
      2. Binary Search for the maximum average value `mid`.
         - Range: `min(log_val)` to `max(log_val)`.
         - Check function: Can we find a subarray of length $\ge L$ with average $\ge mid$?
         - Inside check: Calculate `val[i] = log_nums[i] - mid`. Compute prefix sums. Track `min_prefix` seen so far (up to `i-L`). If `current_prefix - min_prefix >= 0`, return True.
      3. Once the max value is found (within precision $10^{-10}$), perform a final pass to find the **exact** subarray that matches this value, adhering to tie-breaking rules (smallest length, then first index).

      *Wait, the tie-breaking rule is specific:* "If multiple subarrays have the same max GM, output the one with smallest length. If still tied, output the first one."
      The binary search gives the value. To get the specific index/length:
      - We can perform the check function one last time with the found maximum value, but instead of just returning True/False, we track the valid subarrays that satisfy the condition $\approx 0$ (within epsilon).
      - Among those, pick the one with minimum length, then minimum start index.

      **Wait, is $O(N^2)$ acceptable?**
      $N=100,000$. $O(N^2)$ is $10^{10}$ operations. Definitely too slow.
      The Binary Search on Answer is $O(N \log(\text{range}/\epsilon))$. This is efficient enough.

**Tie-Breaking Implementation Detail:**
After finding the maximum average `max_avg` via binary search:
1. Iterate through all valid subarrays of length $\ge L$.
2. Calculate their average of logs.
3. If `abs(current_avg - max_avg) < 1e-10`:
   - Update best solution if:
     - `current_length < best_length`
     - OR `current_length == best_length` AND `current_start < best_start`

Actually, to avoid $O(N^2)$ in the final pass, we can optimize the "find best subarray" step too, but given the precision requirement and the guarantee that other subarrays are at least $10^{-10}$ smaller, we might just need to run the check logic carefully.
However, the safest "OD" approach that balances code complexity and correctness is:
1. Binary Search to find the max value `V`.
2. Iterate `start` from 0 to `N-L`.
   - We need to find the best `end` (length) for this `start`.
   - Actually, iterating all subarrays is still $O(N^2)$.
   
   **Re-evaluating the "Smallest Length" constraint:**
   The problem guarantees that the max is unique within a margin of $10^{-10}$ compared to non-max subarrays.
   The binary search finds `V`.
   We need to find a subarray where `sum / len` is effectively `V`.
   Is it possible that a longer subarray has the same average as a shorter one? Yes, if the numbers are identical.
   
   **Correct Efficient Strategy:**
   1. **Binary Search** to find the maximum geometric mean value `max_val` (in log space).
   2. **Final Scan**: We need to find the specific indices.
      Since we know the target average `max_val`, we can iterate through all possible lengths? No, that's $O(N^2)$.
      
      Let's reconsider the logic.
      If we fix the start index `i`, does the average increase or decrease as we extend? Not necessarily monotonic.
      
      However, there is a known property: The maximum average subarray of length $\ge L$ is often found by checking lengths in a specific way or using the binary search result to filter.
      
      **Simpler Approach for Code:**
      Given the constraints and the specific tie-breaking, and the fact that this is a "Huawei OD" problem, the intended solution is likely the **Binary Search on Answer** to find the value, followed by a **single pass** to find the indices.
      
      Wait, if we have `max_val`, we can compute `B[i] = log_nums[i] - max_val`.
      We need a subarray where `sum(B) >= 0` (approx 0).
      Actually, if `sum(B) > 0`, then the average is greater than `max_val`, which is impossible if `max_val` is the true maximum.
      So we are looking for subarrays where `sum(B) \approx 0`.
      
      The tie-breaking is: Min Length, then Min Start.
      We can iterate `length` from `L` to `N`? No.
      
      Let's stick to the Binary Search for the value.
      Then, to find the indices:
      We can iterate `start` from 0 to `N-L`.
      For each `start`, we want the smallest `length` such that the average is `max_val`.
      But checking every length is slow.
      
      **Alternative View:**
      Maybe the test cases aren't worst-case, and we can use the "Sliding Window" logic?
      No, sliding window works for fixed length.
      
      **Let's assume the standard solution for this specific problem (Huawei 206):**
      The solution usually involves:
      1. Log transform.
      2. Binary Search for the max average.
      3. Once the max average `ans` is found, we iterate `i` from 0 to `N-L`.
         We need to find the smallest `len` such that `prefix[i+len] - prefix[i] >= len * ans`.
         Actually, we can just check if `prefix[i+len] - prefix[i] - len * ans` is close to 0.
         But we can't check all `len`.
         
      **Is there a property?**
      If the maximum average is `M`, and we have a subarray of length `K` with average `M`, and we extend it to `K+1`, the new average will be $\le M$ (unless the added element is $> M$, which contradicts `M` being the max average of *any* subarray? No, the added element could be high, but then the new average would be higher than `M`, which is impossible).
      So, if a subarray has the maximum average `M`, extending it with any element $x$:
      - If $x < M$, average decreases.
      - If $x = M$, average stays $M$.
      - If $x > M$, average increases (contradiction, since $M$ is max).
      
      Therefore, if we find a subarray with average `M`, extending it with elements equal to `M` keeps the average `M`. Extending with elements $< M$ lowers it.
      This implies that the **shortest** subarray with average `M` is likely the one we want if we start from the beginning?
      
      Actually, the tie-breaker is "smallest length".
      So if we have `[10, 10, 5]` and $L=1$.
      Subarrays: `[10]` (avg 10), `[10, 10]` (avg 10), `[10, 10, 5]` (avg 8.3).
      Max avg is 10.
      Candidates: `[10]` (len 1), `[10]` (index 1, len 1), `[10, 10]` (len 2).
      We pick `[10]` at index 0 because length 1 < length 2.
      
      So, if we find the max average `M`, we just need to find the **first** occurrence of a number (or subarray) that has average `M` with the **smallest possible length**.
      Since the average of a subarray of length 1 is just the number itself, if the max average `M` exists as a single number, that's the shortest possible length (1, or L if L>1?).
      Wait, if $L > 1$, the minimum length is $L$.
      
      **Hypothesis:** The maximum geometric mean subarray of length $\ge L$ will almost always be of length exactly $L$, or a sequence of identical numbers forming a longer segment.
      If there is a segment of identical numbers equal to the max value, any sub-segment of length $L$ within it has the same average. The tie breaker says "smallest length". So we'd pick length $L$.
      If the max average is formed by a mix of numbers, it's likely a specific window.
      
      **Conclusion for Code:**
      1. Binary Search to find `max_avg`.
      2. Iterate `start` from 0 to `N-L`.
      3. For each `start`, we only need to check `len = L`?
         No, consider `[2, 100, 2]` with $L=1$. Max is 100 (len 1).
         Consider `[2, 2, 2]` with $L=1$. Max is 2. Subarrays `[2]` (len 1), `[2,2]` (len 2). Pick len 1.
         Consider `[2, 3, 2]` with $L=2$.
         Subarrays: `[2,3]` (2.5), `[3,2]` (2.5), `[2,3,2]` (2.33).
         Max is 2.5. Lengths are 2. First one is index 0.
         
      It seems highly probable that the optimal subarray has length **exactly L** or is composed of **identical numbers** where we just take the shortest valid length (which is L).
      **Wait**, is it possible for a longer subarray to have a higher average than any subarray of length $L$?
      Yes. Example: `[1, 100, 100, 1]`, $L=2$.
      Len 2: `[1,100]` (50.5), `[100,100]` (100), `[100,1]` (50.5).
      Len 3: `[1,100,100]` (67), `[100,100,1]` (67).
      Len 4: 50.5.
      Max is 100 (length 2).
      
      Example where longer is better?
      `[1, 2, 2, 1]`, $L=2$.
      Len 2: `[1,2]` (1.5), `[2,2]` (2), `[2,1]` (1.5).
      Len 3: `[1,2,2]` (1.66), `[2,2,1]` (1.66).
      Len 4: 1.5.
      Max is 2 (length 2).
      
      It turns out that for the **Maximum Average Subarray** problem, the optimal subarray is often of length $L$ or slightly larger if there's a cluster of high values. But mathematically, if you have a subarray of length $K > L$ with average $A$, and you remove an element $x < A$, the average increases. If you remove $x = A$, it stays same. If you remove $x > A$, it decreases.
      So, if a subarray has average $A$ (the global max), then all elements in it must be $\le A$. If any element is $< A$, removing it increases the average, which contradicts $A$ being the max.
      **Therefore, all elements in the maximum average subarray must be equal to the average.**
      If all elements are equal to $A$, then any sub-segment of that subarray also has average $A$.
      The tie-breaker says "smallest length".
      So, if the max average is $A$, we just need to find the **shortest** subarray (length $\ge L$) where all elements are $A$.
      This implies the length
"""


import math

def find_maximum_subarray(numbers, L):
    max_avg = float('-inf')  # 当前最大的几何平均值
    start = 0  # 最大几何平均值子数组的起始位置
    length = L  # 最大几何平均值子数组的长度

    for i in range(len(numbers) - L + 1):
        # 计算子数组的对数和
        log_sum = sum(math.log(num) for num in numbers[i:i+L])
        # 计算几何平均值
        avg = math.exp(log_sum / L)

        if avg > max_avg:
            max_avg = avg
            start = i
            length = L

    return start, length

# 输入示例
N, L = map(int, input().split())  # 输入数组的大小和子数组的最小长度
numbers = []
for _ in range(N):
    num = float(input())  # 将输入的数值转换为浮点数类型
    numbers.append(num)

# 查找长度至少为L且几何平均值最大的子数组
start, length = find_maximum_subarray(numbers, L)

# 输出结果
print(start, length)



