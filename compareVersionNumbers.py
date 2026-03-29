"""

LC: 165. Compare Version Numbers

Medium

Topics:
Two Pointers
String

Hint
Given two version strings, version1 and version2, compare them. A version string consists of revisions separated by dots '.'. The value of the revision is its integer conversion ignoring leading zeros.

To compare version strings, compare their revision values in left-to-right order. If one of the version strings has fewer revisions, treat the missing revision values as 0.

Return the following:

If version1 < version2, return -1.
If version1 > version2, return 1.
Otherwise, return 0.
 

Example 1:

Input: version1 = "1.2", version2 = "1.10"

Output: -1

Explanation:

version1's second revision is "2" and version2's second revision is "10": 2 < 10, so version1 < version2.

Example 2:

Input: version1 = "1.01", version2 = "1.001"

Output: 0

Explanation:

Ignoring leading zeroes, both "01" and "001" represent the same integer "1".

Example 3:

Input: version1 = "1.0", version2 = "1.0.0.0"

Output: 0

Explanation:

version1 has less revisions, which means every missing revision are treated as "0".

 

Constraints:

1 <= version1.length, version2.length <= 500
version1 and version2 only contain digits and '.'.
version1 and version2 are valid version numbers.
All the given revisions in version1 and version2 can be stored in a 32-bit integer.
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
624,194/1.4M
Acceptance Rate
44.4%

Hint 1
You can use two pointers for each version string to traverse them together while comparing the corresponding segments.
Hint 2
Utilize the substring method to extract each version segment delimited by '.'. Ensure you're extracting the segments correctly by adjusting the start and end indices accordingly.

"""

class Solution:
    def comapareVersion(self, version1:str, version2:str) -> int:
        revisions1 = version1.split('.')
        revisions2 = version2.split('.')
        
        len1, len2 = len(revisions1), len(revisions2)
        
        max_len = max(len1, len2)
        
        for i in range(max_len):
            r1 = int(revisions1[i] if i<len1 else 0)
            r2 = int(revisions2[i] if i<len2 else 0)
            
            if r1 < r2:
                return -1
            elif r1 > r2:
                return 1
        return 0
    
sol = Solution()
print(sol.comapareVersion(version1 = "1.2", version2 = "1.10"))
print(sol.comapareVersion(version1 = "1.01", version2 = "1.001"))
print(sol.comapareVersion(version1 = "1.0", version2 = "1.0.0.0"))