"""

LC: 2215. Find the Difference of Two Arrays

Easy

Topics
Array
Hash Table
Weekly Contest 286

Hint
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.

 

Example 1:

Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]
Explanation:
For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums1. Therefore, answer[1] = [4,6].
Example 2:

Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
Output: [[3],[]]
Explanation:
For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value is only included once and answer[0] = [3].
Every integer in nums2 is present in nums1. Therefore, answer[1] = [].
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
-1000 <= nums1[i], nums2[i] <= 1000
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
589,889/727.1K
Acceptance Rate
81.1%

Hint 1
For each integer in nums1, check if it exists in nums2.
Hint 2
Do the same for each integer in nums2.

"""

class Solution:
    def findDifferences(self, nums1:list[list[int]], nums2:list[list[int]]) -> list[list[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        return [list(set1-set2), list(set2-set1)]
sol = Solution()
print(sol.findDifferences(nums1 = [1,2,3], nums2 = [2,4,6]))
print(sol.findDifferences(nums1 = [1,2,3,3], nums2 = [1,1,2,2]))


#-----------------USING HASHMAP------------------------

class Solution:
    def findDifferences(self,nums1:list[list[int]], nums2:list[list[int]]) -> list[list[int]]:
        map1, map2 = {}, {}
        #store elements in each hashmap
        #We assign 1 in map1[num] = 1 and map2[num] = 1 simply to mark that “this number exists,” making it easy and efficient to check later whether it’s present in the other array.
        for num in nums1:
            map1[num] = 1            
        for num in nums2:
            map2[num] = 1
            
        res1, res2 = [], []
        
        #Elements in nums1 but not i nums2
        
        for num in map1:
            if num not in map2:
                res1.append(num)
                
        #Elements in nums2 but not in nums1
                
        for num in map2:
            if num not in map1:
                res2.append(num)
                
        return [res1, res2]
    
sol = Solution()
print(sol.findDifferences(nums1 = [1,2,3], nums2 = [2,4,6]))             
print(sol.findDifferences(nums1 = [1,2,3,3], nums2 = [1,1,2,2]))         