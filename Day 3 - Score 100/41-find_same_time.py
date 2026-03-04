"""
Question
Question Description
The success rate of interface exchanges between services is a key quality characteristic of service calls. The interface failure rate within a certain time period is represented by an array, where each element is the failure rate value per unit time, and the values in the array are integers ranging from 0 to 100.
Given a value (minAverageLost) representing the tolerable average failure rate within a certain time period, that is, the average failure rate is less than or equal to "minAverageLost", find the longest time period in the array. If not found, return NULL directly.
Input and Output Area
Input
The input consists of two lines. The first line is {minAverageLost}, and the second line is {array}, with array elements separated by spaces (" ").
The value range of minAverageLost and elements in the array is integers from 0 to 100, and the number of array elements will not exceed 100.
Output
Find the longest time period with an average value less than or equal to minAverageLost, and output the array subscript pair in the format {beginindex}-{endindex} (subscripts start from 0).
If there are multiple longest time periods at the same time, output multiple subscript pairs, with three spaces ("   ") between them, and sort the multiple subscript pairs in ascending order of their subscripts.

输入
1

0 1 2 3 4

输出
0-2

输入解释：minAverageLost=1，数组[0, 1, 2, 3, 4]

前3个元素的平均值为1，因此数组第一个至第三个数组下标，即0-2


1. Define a function get_sum to calculate the sum of a subarray within an array. The input parameters are the array, the starting index, and the ending index of the subarray.
2. Define a function process to handle the input array and the minimum allowable average failure rate.
3. Initialize variables: size as the length of the array, maxLen as the maximum length, ans as the list to store results, and anssize as the length of the result.
4. Use two loops to traverse the array: the outer loop iterates over the starting indices, and the inner loop iterates over the ending indices.
5. In the inner loop, calculate the sum of the subarray (sum_val) and the length of the subarray (currLen).
6. Determine if the sum of the subarray is less than or equal to the product of the minimum allowable average failure rate and the length of the subarray.
7. If yes, format the starting index and ending index into a string tmp.
8. If the length of the current subarray is equal to the maximum length, add the string tmp to the result list ans and increment the result length anssize by 1.
9. If the length of the current subarray is greater than the maximum length, update maxLen to the current subarray length, update the result list ans to contain only the starting and ending indices of the current subarray, and set the result length anssize to 1.
10. Check if the result length anssize is 0. If yes, return the string "NULL".
11. Concatenate the starting and ending indices in the result list ans into a string, using spaces for separation, and assign it to the variable result.
12. Return the variable result.
"""
def get_sum(arr, start, end):
    sum_val = 0
    for i in range(start, end + 1):
        sum_val += arr[i]
    return sum_val

def process(arr, minAverageLost):
    size = len(arr)  # 数组长度
    maxLen = 0  # 最大长度
    ans = []  # 存储结果的列表
    ansSize = 0  # 结果的长度

    for start in range(size):  # 遍历数组，起始索引从0到size-1
        for end in range(start, size):  # 遍历数组，结束索引从start到size-1
            sum_val = get_sum(arr, start, end)  # 计算子数组的和
            currLen = end - start + 1  # 计算子数组的长度

            if sum_val <= minAverageLost * currLen:
                # 如果子数组的和小于等于minAverageLost乘以子数组长度
                tmp = f"{start}-{end}"  # 格式化起始索引和结束索引
                if maxLen == currLen:  # 如果当前子数组长度等于最大长度
                    ans.append(tmp)  # 将子数组的起始索引和结束索引添加到结果列表中
                    ansSize += 1  # 结果长度加1
                elif currLen > maxLen:  # 如果当前子数组长度大于最大长度
                    maxLen = currLen  # 更新最大长度
                    ans = [tmp]  # 更新结果列表为只包含当前子数组的起始索引和结束索引
                    ansSize = 1  # 结果长度为1

    if ansSize == 0:  # 如果结果长度为0
        return "NULL"

    result = ' '.join(ans)  # 将结果列表中的起始索引和结束索引连接成字符串
    return result

if __name__ == "__main__":
    minAverageLost = int(input().strip())
    arr = list(map(int, input().strip().split()))
    result = process(arr, minAverageLost)
    print(result)

