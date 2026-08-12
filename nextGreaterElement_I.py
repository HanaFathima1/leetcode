"""

LC: 496. Next Greater Element I

Easy

Topics
Mid Level
Array
Hash Table
Stack
Monotonic Stack

The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

 

Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
Example 2:

Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
 

Constraints:

1 <= nums1.length <= nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 104
All integers in nums1 and nums2 are unique.
All the integers of nums1 also appear in nums2.
 

Follow up: Could you find an O(nums1.length + nums2.length) solution?
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
1,456,567/1.9M
Acceptance Rate
76.2%

"""

#question description
"""
LeetCode 496 — Next Greater Element I (Easy Description)

You are given two arrays:

nums1
nums2

Every element of nums1 is guaranteed to be present in nums2.

For each number in nums1:

Find that number in nums2.
Look only to the right side of that number in nums2.
Find the first number that is greater than it.
If such a number exists, return it.
Otherwise, return -1.
"""
 
class MonotonicStack:
    def nextGreaterElement(self, nums1, nums2):
        n = len(nums2)
        result = [-1]*n
        stack = [0]
        
        for i in range(n):
            while stack and nums2[i] > nums2[stack[-1]]:
                index = stack.pop()
                result[index] = nums2[i]
            stack.append(i)
        
        next_greater_map = {nums2[i]:result[i] for i in range(n)}
        final_result = [next_greater_map[num] for num in nums1]
        return final_result

sol = MonotonicStack()
print(sol.nextGreaterElement([4,1,2],[1,3,4,2]))

#--------CODE2-----------------

class Solution:
    def nextGreaterElement(self, nums1, nums2):

        # Stack is used to keep numbers that are still
        # waiting for their Next Greater Element (NGE)
        stack = []

        # Dictionary to store:
        # number -> next greater element
        next_greater = {}

        # Traverse nums2 from left to right
        for num in nums2:

            # If current number is greater than the
            # top element of the stack, then current
            # number is the Next Greater Element for
            # that stack element.
            #
            # Continue popping until:
            # 1. Stack becomes empty OR
            # 2. Top element becomes greater than current number
            while stack and num > stack[-1]:

                # Remove the smaller element
                smaller = stack.pop()

                # Store its next greater element
                next_greater[smaller] = num

            # Current number has not found its
            # Next Greater Element yet,
            # so push it into the stack.
            stack.append(num)

        # After traversing nums2,
        # any elements still left in the stack
        # do not have a greater element on their right.
        while stack:

            # Assign -1 because no greater element exists
            next_greater[stack.pop()] = -1

        # Create the final answer for nums1.
        #
        # For each number in nums1,
        # look up its Next Greater Element
        # from the dictionary.
        return [next_greater[num] for num in nums1]
            
#------------DRY RUN--------------
"""

Input
nums1 = [4,1,2]
nums2 = [1,3,4,2]

Using your monotonic stack approach:

stack = []
next_greater = {}
Dry Run Table
| i | num | Stack Before | Action         | Dictionary Update | Stack After |
| - | --- | ------------ | -------------- | ----------------- | ----------- |
| 0 | 1   | []           | Push 1         | No change         | [1]         |
| 1 | 3   | [1]          | 3 > 1 → Pop 1  | 1 → 3             | []          |
| 1 | 3   | []           | Push 3         | No change         | [3]         |
| 2 | 4   | [3]          | 4 > 3 → Pop 3  | 3 → 4             | []          |
| 2 | 4   | []           | Push 4         | No change         | [4]         |
| 3 | 2   | [4]          | 2 < 4 → No Pop | No change         | [4]         |
| 3 | 2   | [4]          | Push 2         | No change         | [4,2]       |

After Loop Ends

Remaining stack:

[4,2]

These elements have no greater element on their right.

| Popped Element | Dictionary Update |
| -------------- | ----------------- |
| 2              | 2 → -1            |
| 4              | 4 → -1            |

Final Dictionary
| Number | Next Greater |
| ------ | ------------ |
| 1      | 3            |
| 3      | 4            |
| 2      | -1           |
| 4      | -1           |

{
    1:3,
    3:4,
    2:-1,
    4:-1
}
Build Answer for nums1
nums1 = [4,1,2]
| Number | Dictionary Lookup |
| ------ | ----------------- |
| 4      | -1                |
| 1      | 3                 |
| 2      | -1                |

Final Answer:

[-1,3,-1]

"""

#-------------TC & SC------------------
"""
Time Complexity
O(n + m)
n = len(nums2)
m = len(nums1)

Each element is pushed and popped at most once.

Space Complexity
O(n)

for the stack and dictionary.        
"""     



"""
#===========================A COMPLETE GUIDE FOR MONOTONIC STACK PATTERN========================================

A monotonic stack maintains elements in either increasing or decreasing order. There are four standard patterns you should know for interviews and LeetCode.

1. Next Greater Element (NGE)

Find the first greater element to the right.

Example
Input : [2,1,2,4,3]
Output: [4,2,4,-1,-1]
Code
def next_greater(nums):
    n = len(nums)
    ans = [-1] * n
    stack = []                  # stores indices

    for i in range(n):
        while stack and nums[i] > nums[stack[-1]]:
            ans[stack.pop()] = nums[i]
        stack.append(i)

    return ans


nums = [2,1,2,4,3]
print(next_greater(nums))
2. Next Smaller Element (NSE)

Find the first smaller element to the right.

Example
Input : [4,8,5,2,25]
Output: [2,5,2,-1,-1]
Code
def next_smaller(nums):
    n = len(nums)
    ans = [-1] * n
    stack = []

    for i in range(n):
        while stack and nums[i] < nums[stack[-1]]:
            ans[stack.pop()] = nums[i]
        stack.append(i)

    return ans


nums = [4,8,5,2,25]
print(next_smaller(nums))
3. Previous Greater Element (PGE)

Find the first greater element to the left.

Example
Input : [10,4,2,20,40,12]
Output: [-1,10,4,-1,-1,40]
Code
def previous_greater(nums):
    n = len(nums)
    ans = [-1] * n
    stack = []

    for i in range(n):
        while stack and stack[-1] <= nums[i]:
            stack.pop()

        if stack:
            ans[i] = stack[-1]

        stack.append(nums[i])

    return ans


nums = [10,4,2,20,40,12]
print(previous_greater(nums))
4. Previous Smaller Element (PSE)

Find the first smaller element to the left.

Example
Input : [4,5,2,10,8]
Output: [-1,4,-1,2,2]
Code
def previous_smaller(nums):
    n = len(nums)
    ans = [-1] * n
    stack = []

    for i in range(n):
        while stack and stack[-1] >= nums[i]:
            stack.pop()

        if stack:
            ans[i] = stack[-1]

        stack.append(nums[i])

    return ans


nums = [4,5,2,10,8]
print(previous_smaller(nums))
One Cheat Sheet
Problem	Traverse	While Condition	Stack Type
Next Greater	Left → Right	nums[i] > nums[stack[-1]]	Decreasing
Next Smaller	Left → Right	nums[i] < nums[stack[-1]]	Increasing
Previous Greater	Left → Right	stack[-1] <= nums[i]	Decreasing
Previous Smaller	Left → Right	stack[-1] >= nums[i]	Increasing
Universal Templates
Next Greater
stack = []
ans = [-1] * len(nums)

for i in range(len(nums)):
    while stack and nums[i] > nums[stack[-1]]:
        ans[stack.pop()] = nums[i]
    stack.append(i)
Next Smaller
stack = []
ans = [-1] * len(nums)

for i in range(len(nums)):
    while stack and nums[i] < nums[stack[-1]]:
        ans[stack.pop()] = nums[i]
    stack.append(i)
Previous Greater
stack = []
ans = [-1] * len(nums)

for i in range(len(nums)):
    while stack and stack[-1] <= nums[i]:
        stack.pop()

    if stack:
        ans[i] = stack[-1]

    stack.append(nums[i])
Previous Smaller
stack = []
ans = [-1] * len(nums)

for i in range(len(nums)):
    while stack and stack[-1] >= nums[i]:
        stack.pop()

    if stack:
        ans[i] = stack[-1]

    stack.append(nums[i])
Interview Tip

A quick way to remember the patterns is:

Next problems: store indices, because you're filling answers for earlier elements when you discover the next qualifying element.
Previous problems: you can store values if you only need the previous element's value; store indices if you need positions or distances (common in problems like Largest Rectangle in Histogram or Sum of Subarray Minimums)."""