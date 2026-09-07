"""

LC:136.SINGLE NUMBER


Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]

Output: 1

Example 2:

Input: nums = [4,1,2,1,2]

Output: 4

Example 3:

Input: nums = [1]

Output: 1

 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.

"""

class Solution:
    def singleNumber(self, nums:list[int]) -> int:
        result=0
        for num in nums:
            result^=num
        return result
sol = Solution()
print(sol.singleNumber([2,2,1]))
print(sol.singleNumber([4,1,2,1,2]))
print(sol.singleNumber([1]))


"""
====DRY RUN====
[1,2,3,1,4,5,3,5,2]

Full Dry Run

Initially:

xor = 0

We go through the array one number at a time.

Step 1: num = 1
xor ^= num

means:

xor = xor ^ num
    = 0 ^ 1
    = 1

So:

xor = 1
Step 2: num = 2
xor = 1 ^ 2

Convert to binary:

1 = 001
2 = 010
---------
    011

Therefore:

xor = 3
Step 3: num = 3
xor = 3 ^ 3

Binary:

3 = 011
3 = 011
---------
    000

Therefore:

xor = 0

Notice that 3 has appeared once before and now its pair cancels it.

Step 4: num = 1
xor = 0 ^ 1
    = 1

So:

xor = 1
Step 5: num = 4
xor = 1 ^ 4

Binary:

1 = 001
4 = 100
---------
    101

101 in decimal is 5.

Therefore:

xor = 5
Step 6: num = 5
xor = 5 ^ 5

Binary:

5 = 101
5 = 101
---------
    000

Therefore:

xor = 0

Again, the pair of 5s cancels out.

Step 7: num = 3
xor = 0 ^ 3
    = 3

So:

xor = 3
Step 8: num = 5
xor = 3 ^ 5

Binary:

3 = 011
5 = 101
---------
    110

110 in decimal is 6.

Therefore:

xor = 6
Step 9: num = 2
xor = 6 ^ 2

Binary:

6 = 110
2 = 010
---------
    100

100 in decimal is 4.

Therefore:

xor = 4
Complete Dry-Run Table
Step	num	Operation	xor
Initial	—	—	0
1	1	0 ^ 1	1
2	2	1 ^ 2	3
3	3	3 ^ 3	0
4	1	0 ^ 1	1
5	4	1 ^ 4	5
6	5	5 ^ 5	0
7	3	0 ^ 3	3
8	5	3 ^ 5	6
9	2	6 ^ 2	4

Finally:

return xor

So:

ANSWER = 4
⭐ The important thing to understand

The reason this works is:

a ^ a = 0

and

a ^ 0 = a

So all the pairs disappear:

1 ^ 1 = 0
2 ^ 2 = 0
3 ^ 3 = 0
5 ^ 5 = 0

and the only number left is:

4

Therefore:

[1,2,3,1,4,5,3,5,2]
                    ↓
              XOR everything
                    ↓
                    4
"""