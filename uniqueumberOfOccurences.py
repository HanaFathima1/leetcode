"""

LC: 1207. Unique Number of Occurrences

Easy

Topics
Array
Hash Table
Weekly Contest 156

Hint
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

 

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
 

Constraints:

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
913,464/1.2M
Acceptance Rate
78.5%

Hint 1
Find the number of occurrences of each element in the array using a hash map.
Hint 2
Iterate through the hash map and check if there is a repeated value.

"""

class Solution:
    def uniqueOccurences(self,arr:list[int])->bool:
        freq={}
        for num in arr:
            freq[num] = freq.get(num,0)+1
        occurences = list(freq.values())
        return len(occurences) == len(set(occurences))
sol = Solution()
print(sol.uniqueOccurences( arr = [1,2,2,1,1,3]))
print(sol.uniqueOccurences(arr = [1,2]))
print(sol.uniqueOccurences(arr = [-3,0,1,-3,1,1,1,-3,10,0]))