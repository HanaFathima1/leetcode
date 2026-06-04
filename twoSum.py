"""

LC: 1. Two Sum

Easy

Topics
Array
Hash Table

Hint
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
18,687,186/33.2M
Acceptance Rate
56.3%

Hint 1
A really brute force way would be to search for all possible pairs of numbers but that would be too slow. Again, it's best to try out brute force solutions just for completeness. It is from these brute force solutions that you can come up with optimizations.
Hint 2
So, if we fix one of the numbers, say x, we have to scan the entire array to find the next number y which is value - x where value is the input parameter. Can we change our array somehow so that this search becomes faster?
Hint 3
The second train of thought is, without changing the array, can we use additional space somehow? Like maybe a hash map to speed up the search?

"""

#bruteForce

def twoSum(nums,target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]+nums[j] == target:
                return[i,j]
            
nums = [2,6,5,8,11]
target = 14

result = twoSum(nums,target)

print("Indices of the numbers that add up to target: ",result)
        
#hashTable

def twoSum(nums,target):
    hashmap={}
    for i,num in enumerate(nums):
        complement = target - num #You calculate what other number you need to reach the target.
        if complement in hashmap:
            return [hashmap[complement],i] #hashmap[complement] → index of the previous number, i → index of the current number
        hashmap[num] = i #If complement not found, store the current number and its index for future reference.
        
nums = [2,6,5,8,11]
target = 14
result = twoSum(nums,target)

print("Indices of the numbers that add up to target: ",result)


#Two-pointers

def twoSums(nums, target):
    n=len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]+nums[j]==target:
                return [i,j]
            else:
                i=i+1