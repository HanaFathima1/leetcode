"""

LC: 4. Median of Two Sorted Arrays

Attempted

Hard

Topics
Mid Level
Array
Binary Search
Divide and Conquer

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
4,352,947/9.3M
Acceptance Rate
46.8%

"""

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Handle edge case where both arrays are empty
        if not nums1 and not nums2:
            return 0.0

        # Merge both arrays
        merged_array = nums1 + nums2

        # Sort the merged array
        merged_array.sort()

        n = len(merged_array)
        mid = n // 2

        # If length is even, median is average of middle two elements
        if n % 2 == 0:
            return (merged_array[mid] + merged_array[mid - 1]) / 2

        # If length is odd, median is the middle element
        return merged_array[mid]
"""    
Dry Run

Input:

nums1 = [1, 2]
nums2 = [3, 4]

After merge:

merged_array = [1,2,3,4]
n = 4
mid = 2

Even length:

median = (merged_array[2] + merged_array[1]) / 2
       = (3 + 2) / 2
       = 2.5

Output:

2.5
Complexity
| Operation   | Complexity            |
| ----------- | --------------------- |
| Merge       | O(m+n)                |
| Sort        | O((m+n) log(m+n))     |
| Find Median | O(1)                  |
| Total       | **O((m+n) log(m+n))** |
| Space       | **O(m+n)**            |
"""

#=========================================================
#Optimal Solution:

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # Always perform binary search on the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)

        left, right = 0, m

        while left <= right:

            # Partition in nums1
            partitionX = (left + right) // 2

            # Partition in nums2
            partitionY = (m + n + 1) // 2 - partitionX

            # Elements around partitions
            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == m else nums1[partitionX]

            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == n else nums2[partitionY]

            # Correct partition found
            if maxLeftX <= minRightY and maxLeftY <= minRightX:

                # Odd total length
                if (m + n) % 2:
                    return max(maxLeftX, maxLeftY)

                # Even total length
                return (
                    max(maxLeftX, maxLeftY)
                    + min(minRightX, minRightY)
                ) / 2

            # Move left in nums1
            elif maxLeftX > minRightY:
                right = partitionX - 1

            # Move right in nums1
            else:
                left = partitionX + 1
                
"""

Dry Run

Input:

nums1 = [1,3]
nums2 = [2]

Since nums1 is longer:

nums1 = [2]
nums2 = [1,3]
m = 1
n = 2
Iteration 1
partitionX = 0
partitionY = 2
maxLeftX = -∞
minRightX = 2

maxLeftY = 3
minRightY = +∞

Condition:

maxLeftY <= minRightX

3 <= 2 ❌

Move right:

left = 1
Iteration 2
partitionX = 1
partitionY = 1
maxLeftX = 2
minRightX = +∞

maxLeftY = 1
minRightY = 3

Check:

2 <= 3 ✅
1 <= ∞ ✅

Correct partition found.

Total length:

3 (odd)

Median:

max(2,1) = 2

Return:

2.0
Why (m+n+1)//2?

We want the left half to contain:

(total_length + 1) // 2

elements.

Examples:

Total Length	Left Side Size
5	3
6	3
7	4

This handles both odd and even lengths with one formula.

Complexity

| Operation     | Complexity       |
| ------------- | ---------------- |
| Binary Search | O(log(min(m,n))) |
| Space         | O(1)             |

"""

