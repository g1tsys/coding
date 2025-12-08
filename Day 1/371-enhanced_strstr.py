"""C language has a built-in function strstr that finds the first occurrence of a substring in a string: char *strstr(const char *haystack, const char *needle); create a haystack string and a needle string, and return the index of the first occurrence of the needle in the haystack (0-indexed). If the needle is not part of the haystack, return -1. If the needle is an empty string, return 0.
Now you are asked to implement a strengthened version of strstr, called enhanced_strstr. The enhanced_strstr function should find the first occurrence of the needle in the haystack, but with the following additional constraints:
1.This time, the needle string may contain wildcard characters to blur the searches, same as strstr to return the same index.
2. The wildcard characters are:
    - "[]": Matches any one of the characters enclosed within the square brackets. For example, "a[bc]d" matches "abd" or "acd".
3. The matching should be case-insensitive.
For example:
Input: haystack = "abcd", needle = "b[cd]"

Output: 1
Explanation: The needle "b[cd]d" can match either "bcd" or         

"""
import re


# annotate and explain the code below
def enhanced_strstr(haystack: str, needle: str) -> int:
    """Find first occurrence of needle in haystack.
    needle contains [] patterns meaning "match a OR b OR c"
    """
    needle = re.sub(r'\[(.*?)\]', lambda m: f"({'|'.join(re.escape(c) for c in m.group(1))})", needle
                    )
    # this part converts the custom [] pattern in the needle to a regex group.
    # For example, "b[cd]d" becomes "b(c|d)d
    match = re.search(needle, haystack, re.IGNORECASE)
    # this line searches for the modified needle pattern in the haystack string, ignoring case.
    return match.start() if match else -1



if __name__ == "__main__":
    haystack = input("\nEnter the haystack string: ").strip()
    # this part takes user input for the haystack string and removes any leading/trailing whitespace.


    needle = input("Enter the needle string (with [abc] patterns): ").strip()   
    # this part takes user input for the needle string and removes any leading/trailing whitespace.

    index = enhanced_strstr(haystack, needle)
    # this line calls the enhanced_strstr function with the provided haystack and needle, storing the result in index.

    print(f"The first occurrence is at index: {index}")
    # this line prints the index of the first occurrence of the needle in the haystack.


