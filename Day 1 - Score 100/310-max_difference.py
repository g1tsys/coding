"""Given an array of real numbers nums, you can split at any point in this array, making this array a two non-empty parts: left part and right part. Your task is to find the maximum difference between the maximum value of left part and the minimum value of right part. culculate both the sum and subtraction of these two parts find all split points and return the maximum difference you can find.

Input
6 
1 -2 3 4 -9 7

Output  
10

"""


def max_difference(nums) -> int:
    # this function calculates the maximum difference between the maximum value of the left part and the minimum value of the right part after splitting the array at any point.
    n = len(nums)
    # variable n stores the length of the input array nums.
    
    prefix_sum = [0] * (n + 1)
    # this line initializes an array prefix_sum of size n+1 with all elements set to 0.
    
    for i in range(1, n + 1):
    #this loop iterates through the array from index 1 to n.
        prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]
        # this loop calculates the prefix sums of the array nums and stores them in the prefix_sum array.

    suffix_sum = [0] * (n + 1)
    # this line initializes an array suffix_sum of size n+1 with all elements set to 0.
    for i in range(n - 1, -1, -1):
        suffix_sum[i] = suffix_sum[i + 1] + nums[i]
        # this loop calculates the suffix sums of the array nums and stores them in the suffix_sum array.

    max_diff = float('-inf')
    # this line initializes max_diff to negative infinity to ensure that any calculated difference will be larger.
    for i in range(1, n):
    # this loop iterates through all possible split points in the array.
        diff = abs(prefix_sum[i] - suffix_sum[i])
        # this line calculates the absolute difference between the sum of the left part and the sum of the right part at the current split point i.
        max_diff = max(max_diff, diff)  
        # this line updates max_diff to be the maximum value between the current max_diff and the newly calculated diff.
    
    return max_diff
    # the function returns the maximum difference found.


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    result = max_difference(nums)
    print(result)




# test case
# Input: 6
# 1 -2 3 4 -9 7

