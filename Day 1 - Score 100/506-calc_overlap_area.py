"""
# Rectangle Intersection Area Problem
## Problem Translation

**Problem Description:**
- Given 3 sets of coordinates (x, y, w, h), where -1000 < x, y < 1000, and w, h are positive integers
- (x, y, w, h) represents a rectangle in a 2D coordinate system where:
  - (x, y) is the **top-left corner** coordinate
  - w is the width (extends right)
  - h is the height (extends down)
- The rectangle spans from x to (x+w) on the x-axis and from y to (y-h) on the y-axis
- Examples:
  - (0, 0, 2, 2) represents a rectangle from x-axis [0, 2] and y-axis [0, -2]
  - (3, 5, 4, 6) represents a rectangle from x-axis [3, 7] and y-axis [5, -1]

**Task:** Calculate the area of the overlapping region of all 3 rectangles. If they don't overlap, output 0.
---

## Python Solution Approach

**Step-by-step thought process:**

1. **Convert rectangle representation**: Transform each rectangle from (x, y, w, h) format to boundary format:
   - Left boundary: x
   - Right boundary: x + w
   - Top boundary: y
   - Bottom boundary: y - h

2. **Find intersection boundaries**: For all 3 rectangles to overlap, we need:
   - **Left boundary** of intersection = maximum of all left boundaries
   - **Right boundary** of intersection = minimum of all right boundaries
   - **Top boundary** of intersection = minimum of all top boundaries
   - **Bottom boundary** of intersection = maximum of all bottom boundaries

3. **Calculate intersection area**:
   - Width = right - left
   - Height = top - bottom
   - If width ≤ 0 or height ≤ 0, rectangles don't overlap (return 0)
   - Otherwise, area = width × height

---

## Python Code

```python
def calc_overlap_area(rectangles):
    # Convert rectangles to boundary format
    left_boundaries = [rect[0] for rect in rectangles]
    right_boundaries = [rect[0] + rect[2] for rect in rectangles]
    top_boundaries = [rect[1] for rect in rectangles]
    bottom_boundaries = [rect[1] - rect[3] for rect in rectangles]
    
    # Find intersection boundaries
    left = max(left_boundaries)
    right = min(right_boundaries)
    top = min(top_boundaries)
    bottom = max(bottom_boundaries)
    
    # Calculate overlap dimensions
    width = right - left
    height = top - bottom
    
    # Return area if valid overlap exists
    if width > 0 and height > 0:
        return width * height
    else:
        return 0

# Read input
rect1 = list(map(int, input().split()))
rect2 = list(map(int, input().split()))
rect3 = list(map(int, input().split()))

# Calculate and output the overlap area
rectangles = [rect1, rect2, rect3]
result = calc_overlap_area(rectangles)
print(result)
```

---

## Example Walkthrough

**Input:**
```
0 0 2 2
1 0 3 3
0 -1 3 2
```

**Step-by-step calculation:**

**Rectangle 1:** (0, 0, 2, 2)
- Left: 0, Right: 0+2=2
- Top: 0, Bottom: 0-2=-2
- Region: x∈[0,2], y∈[-2,0]

**Rectangle 2:** (1, 0, 3, 3)
- Left: 1, Right: 1+3=4
- Top: 0, Bottom: 0-3=-3
- Region: x∈[1,4], y∈[-3,0]

**Rectangle 3:** (0, -1, 3, 2)
- Left: 0, Right: 0+3=3
- Top: -1, Bottom: -1-2=-3
- Region: x∈[0,3], y∈[-3,-1]

**Intersection calculation:**
- Left = max(0, 1, 0) = **1**
- Right = min(2, 4, 3) = **2**
- Top = min(0, 0, -1) = **-1**
- Bottom = max(-2, -3, -3) = **-2**

**Overlap dimensions:**
- Width = 2 - 1 = **1**
- Height = -1 - (-2) = **1**
- Area = 1 × 1 = **1**

**Output:** `1`
"""



def calc_overlap_area(rectangles):
    # 计算3个矩形的相交面积函数

    # 计算相交矩形的左上角和右下角坐标
    x1 = max(rectangles[0][0], rectangles[1][0], rectangles[2][0])
    y1 = min(rectangles[0][1], rectangles[1][1], rectangles[2][1])
    x2 = min(rectangles[0][0] + rectangles[0][2], rectangles[1][0] + rectangles[1][2], rectangles[2][0] + rectangles[2][2])
    y2 = max(rectangles[0][1] - rectangles[0][3], rectangles[1][1] - rectangles[1][3], rectangles[2][1] - rectangles[2][3])

    # 计算相交矩形的宽和高
    width = x2 - x1
    height = y1 - y2

    # 如果宽或高为负数，则说明三个矩形没有相交部分，返回0
    if width <= 0 or height <= 0:
        return 0
    else:
        # 计算相交矩形的面积并返回
        return width * height


# 读取3个矩形的位置
rectangles = []
for _ in range(3):
    x, y, w, h = map(int, input().split())
    rectangles.append((x, y, w, h))

# 调用函数计算相交面积
overlap_area = calc_overlap_area(rectangles)

# 输出相交面积
print(overlap_area)

