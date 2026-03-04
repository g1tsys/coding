"""
### Problem Description
The statistics page of an enterprise router requires a feature to dynamically calculate the **Top N most visited web URLs** in the system. Design an algorithm to efficiently and dynamically compute the Top N pages.

---

### Input and Output

#### Input
Each line is either a URL or a number:
- If it is a URL, it represents a web page visit within a certain time period.
- If it is a number `N`, it represents that the Top N URLs need to be output in this query.

**Input Constraints:**
1. The total number of unique web pages is less than 5000, and the number of visits to a single web page is less than 65535.
2. A web URL consists only of letters, numbers, and dots (`.`), and its length is less than 127 characters.
3. The number `N` is a positive integer and is less than or equal to the total number of unique web pages visited so far.

#### Output
Each input line corresponds to one output line:
1. Each output must count **all previous inputs**, not just the current input.
2. If two URLs have the same number of visits, they are sorted lexicographically by URL string, and the one that comes first lexicographically is ranked higher.
3. The output is the first N URLs sorted by visit count, separated by commas (`,`).

---

Would you like me to also translate the corresponding solution approach for this problem?


# Python Language Approach
1. We use a dictionary `url_counts` to record the visit count of each URL, where the URL is the key and the visit count is the value.
2. For each element in the input:
   - If it is a string `❓`, it represents a URL, and we increment its corresponding visit count by 1.
   - If it is an integer, it means we need to output the `N` URLs with the highest visit counts.
3. For each integer input, we first sort the URLs in the `url_counts` dictionary. The sorting rules are:
   - First, sort in descending order of visit count.
   - If counts are equal, sort in ascending lexicographical order of the URL string.
4. We use the `sorted` function for sorting, and specify the sorting rules via the `key` parameter. The sorted result is a list containing the ordered URLs.
5. We take the first `N` URLs from the sorted list and use the `join` function to concatenate them into a single string.
6. Finally, we print this string as the output.

---

Would you like me to also provide the full Python code implementation for this problem?
"""

from collections import defaultdict


def get_top_n_urls(urls, n):
    url_counts = defaultdict(int)  # 用于记录每个URL的访问次数

    for url in urls:
        if isinstance(url, str):
            url_counts[url] += 1  # 统计URL的访问次数
        elif isinstance(url, int):
            top_n_urls = sorted(url_counts.keys(), key=lambda x: (-url_counts[x], x))[:url]
            # 按访问次数和字符串字典序进行排序，并取出前N个URL
            print(",".join(top_n_urls))


# 测试样例
input_data = [
"news.qq.com",
"www.cctv.com",
1,
"www.huawei.com",
"www.huawei.com",
2,
3

]

get_top_n_urls(input_data, 3)

