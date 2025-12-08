"""Problem Description:
- Sun WUkong sneaks into a peach garden with N trees, each bearing a certain number of peaches.Guards will return in H hours. He eats at speed K peaches/hour from one tree at a time. Find the minimum speed K needed to finish all peaches before the guards return. 


KEY CONSTRAINTS: 

1. If a tree has fewer than K peaches, he eats all of them in that hour(doesn't move to another tree)

2. K must be an integer

3. H >/ N (hours available >/ number of trees)

Solution Hints from the Page:

Binary Search on the answer:
1. Search range: K ranges from 1 (minimum) to max(peaches) (maximum peaches on a tree)
2. Binary Search Logic: FOr each candidate speed K, calculate if all peaches can be eaten within H hours.

3. Time calculation: For each tree with peaches[i], it takes [peaches[i/] / k] hours (ceiling division)

4. IF total time </ H, try a slower speed; if > H, need faster speed. 

The page promises solutions in C++, Java, Python, C, and JavaScript with detailed explanations, though the actual code is behind a subscription paywall. """

def canFinish(peaches, K, H):
    hours_needed = 0
    for p in peaches:
        hours_needed += (p + K - 1) // K  # Ceiling division to calculate hours needed for each tree
    return hours_needed <= H

def minEatingSpeed(peaches, H):
    left, right = 1, max(peaches)
    while left < right:
        mid = (left + right) // 2
        if canFinish(peaches, mid, H):
            right = mid  # Try a smaller speed
        else:
            left = mid + 1  # Increase speed
    return left


try:
    peaches = list(map(int, input("Enter the number of peaches on each tree (space-separated): ").strip().split()))
    H = int(input("Enter the number of hours before the guards return: ").strip())
    if H < len(peaches):
        raise ValueError("H must be at least the number of trees.")
    
    K = minEatingSpeed(peaches, H)
    print(f"The minimum eating speed K to finish all peaches before the guards return is: {
K}")
except ValueError as e:
    print(f"Invalid input: {e}")

"""The inputs are the shuffled string and an integer representing the length or the  number of consecutive positive numbers in the original array."""
