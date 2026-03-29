"""

LC: 932. Beautiful Array

Medium

Topics
Array
Math
Divide and Conquer
Weekly Contest 108

An array nums of length n is beautiful if:

nums is a permutation of the integers in the range [1, n].
For every 0 <= i < j < n, there is no index k with i < k < j where 2 * nums[k] == nums[i] + nums[j].
Given the integer n, return any beautiful array nums of length n. There will be at least one valid answer for the given n.

 

Example 1:

Input: n = 4
Output: [2,1,4,3]
Example 2:

Input: n = 5
Output: [3,1,2,5,4]
 

Constraints:

1 <= n <= 1000
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
57,157/83.6K
Acceptance Rate
68.4%

"""

def beautiful(n):
    if n==1:
        return [1]
    left=beautiful((n+1)//2)
    right=beautiful(n//2)
    return [2*x-1 for x in left] + [2*x for x in right]
if __name__=="__main__":
    n=4
    res=beautiful(4)
    print(res)
    
#--------------------------

from typing import List
class Solution:
    def beautifulArray(self, n:int)->List[int]:
        return self.build(n)
    def build(self,n:int):
        if n == 1:
            return [1]
        left=self.build((n+1)//2)
        right=self.build(n//2)
        res=[]
        for x in left:
            res.append(2*x-1)
        for x in right:
            res.append(2*x)
        return res
sol=Solution()
print(sol.beautifulArray(n=4))
print(sol.beautifulArray(n=5))

#---------

from typing import List

class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        res = [1]

        while len(res) < n:
            odd = [2*x - 1 for x in res if 2*x - 1 <= n]
            even = [2*x for x in res if 2*x <= n]
            res = odd + even

        return res