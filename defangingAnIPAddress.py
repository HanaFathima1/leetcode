"""

LC: 1108. Defanging an IP Address

Easy

Topics
String
Weekly Contest 144

Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

 

Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
 

Constraints:

The given address is a valid IPv4 address.
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
785,579/874.9K
Acceptance Rate
89.8%

"""

class Solution:
    def defangIPaddr(self, address:str) -> str:
        return address.replace(".", "[.]")
sol = Solution()
print(sol.defangIPaddr("1.1.1.1"))
print(sol.defangIPaddr("255.100.50.0"))