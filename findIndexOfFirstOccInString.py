"""

LC: 28. Find the Index of the First Occurrence in a String

Easy

Topics
Two Pointers
String
String Matching

Companies
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
3,985,538/8.6M
Acceptance Rate
46.4%

"""
#--------------------STRING MATCHING---------------------


def strStr(haystack,needle):   
    return haystack.find(needle)

print(strStr("leetcode","leeto"))


"""

TC=>O(N*M)
SC=>O(1)

"""

#--------------------BRUTE FORCE PATTERN MATCHING SOLUTION-------------------

def strStr(haystack,needle):
    for i in range(len(haystack)):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1

print(strStr(haystack = "sadbutsad", needle = "sad"))


"""

TC=>O(N*M)
SC=>O(1)

"""
            