"""

LC: 503. Next Greater Element II

Medium

Topics
Senior Staff
Array
Stack
Monotonic Stack

Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

 

Example 1:

Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.
Example 2:

Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]
 

Constraints:

1 <= nums.length <= 104
-109 <= nums[i] <= 109
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
929,955/1.3M
Acceptance Rate
69.2%

"""

class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n=len(nums)
        ans=[-1]*n
        for i in range(n):
            for j in range(1,n):
                index=(i+j)%n
                if nums[index]>nums[i]:
                    ans[i]=nums[index]
                    break
        return ans
sol=Solution()
print(sol.nextGreaterElements(nums = [1,2,3,4,3]))
                
"""
=============DRY RUN==============

Dry Run
Initial
nums = [1, 2, 1]
index:  0  1  2

ans = [-1, -1, -1]
🔵 i = 0

We are looking for the next greater element of:

nums[0] = 1

Inner loop:

j = 1

Calculate:

index = (i + j) % n
      = (0 + 1) % 3
      = 1

So:

nums[index] = nums[1] = 2

Check:

2 > 1

✅ True.

Therefore:

ans[0] = 2

Then break.

ans = [2, -1, -1]
🔵 i = 1

Now:

nums[1] = 2

We need the next greater element after 2.

j = 1
index = (1 + 1) % 3
      = 2
nums[2] = 1

Check:

1 > 2

❌ False.

Continue.

j = 2
index = (1 + 2) % 3
      = 0

Notice how % n makes the array circular.

We go from:

1 → 2 → 1 → 2
        ↑

Now:

nums[0] = 1

Check:

1 > 2

❌ False.

No greater element was found.

So:

ans = [2, -1, -1]
🔵 i = 2

Now:

nums[2] = 1
j = 1
index = (2 + 1) % 3
      = 0

So:

nums[0] = 1

Check:

1 > 1

❌ False.

Continue.

j = 2
index = (2 + 2) % 3
      = 1

So:

nums[1] = 2

Check:

2 > 1

✅ True.

Therefore:

ans[2] = 2

Break.

ans = [2, -1, 2]
✅ Final Answer
[2, -1, 2]
Visual representation
nums = [1, 2, 1]
        ↑

For 1:
1 → 2
    ↑
next greater = 2


For 2:
2 → 1 → 1
No value > 2
next greater = -1


For 1:
1 → 1 → 2
        ↑
next greater = 2

So:

nums = [ 1,  2,  1]
ans  = [ 2, -1,  2]
⭐ The important line
index = (i + j) % n

This is what makes your solution circular.

For example, when i = 2:

j = 1 → (2+1)%3 = 0
j = 2 → (2+2)%3 = 1

So after reaching the last element, you wrap back to the beginning:

0 → 1 → 2 → 0 → 1 → ...

Your solution is O(n²) time and O(n) space.
"""     
          

#OPTIMAL SOLUTION
class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n=len(nums)
        res=[-1]*n
        stack=[]
        for i in range(2*n):
            index=i%n
            while stack and nums[index]>nums[stack[-1]]:
                prev_index=stack.pop()
                res[prev_index]=nums[index]
            if i<n:
                stack.append(index)
        return res
sol=Solution()
print(sol.nextGreaterElements([ 1,  2,  1]))
    

# EXPLANATION
class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:

        n = len(nums)

        # Initially, every answer is -1
        ans = [-1] * n

        # Stack stores indices whose next greater element
        # has not been found yet
        stack = []

        # Traverse the array twice because it is circular
        for i in range(2 * n):

            # Convert i into a circular index
            index = i % n

            # While the current element is greater than
            # the element whose index is on the stack
            while stack and nums[index] > nums[stack[-1]]:

                prev_index = stack.pop()

                ans[prev_index] = nums[index]

            # Only put each original index into the stack once
            if i < n:
                stack.append(index)

        return ans
    
"""
DRY RUN

1. Initial state
nums = [1, 2, 1]

index:  0  1  2
value:  1  2  1

Initially:

n = 3

ans   = [-1, -1, -1]
stack = []

We run:

for i in range(2 * n):

Since n = 3:

i = 0, 1, 2, 3, 4, 5

Why 6 iterations?

Because the array is circular, so we effectively consider:

[1, 2, 1, 1, 2, 1]
2. i = 0

Calculate:

index = i % n
      = 0 % 3
      = 0

So:

nums[index] = nums[0] = 1
Check while
while stack and nums[index] > nums[stack[-1]]:

But:

stack = []

So nothing happens.

Now:

if i < n:
0 < 3 → True

Therefore:

stack.append(index)

Stack becomes:

stack = [0]

Meaning:

index 0 → value 1

Current state:

ans   = [-1, -1, -1]
stack = [0]
3. i = 1

Calculate:

index = 1 % 3
      = 1

So:

nums[1] = 2

Stack:

[0]

Top of stack:

stack[-1] = 0

Value at that index:

nums[0] = 1

Now check:

nums[index] > nums[stack[-1]]

Becomes:

2 > 1

✅ True.

Therefore:

prev_index = stack.pop()

prev_index becomes:

0

Stack becomes:

[]

Now:

ans[prev_index] = nums[index]

Therefore:

ans[0] = nums[1]
       = 2

So:

ans = [2, -1, -1]

Now check:

if i < n:
1 < 3 → True

Push index 1:

stack = [1]

Current state:

ans   = [2, -1, -1]
stack = [1]
4. i = 2

Calculate:

index = 2 % 3
      = 2

Current value:

nums[2] = 1

Stack:

[1]

Top:

stack[-1] = 1

Value:

nums[1] = 2

Check:

1 > 2

❌ False.

So we don't pop anything.

Now:

if i < n:
2 < 3 → True

Push index 2:

stack = [1, 2]

Current state:

ans   = [2, -1, -1]
stack = [1, 2]

Notice what the stack means:

index:  1   2
value:  2   1
        ↑   ↑
       waiting for a greater element
5. i = 3

This is where the circular nature becomes important.

Calculate:

index = 3 % 3
      = 0

We are back at the beginning!

nums[0] = 1

Stack:

[1, 2]

Top:

stack[-1] = 2

Value:

nums[2] = 1

Check:

1 > 1

❌ False.

Nothing happens.

Now:

if i < n:
3 < 3 → False

So we do NOT push index 0 again.

Stack remains:

[1, 2]
6. i = 4 ⭐

Calculate:

index = 4 % 3
      = 1

So:

nums[1] = 2

Stack:

[1, 2]

Top:

stack[-1] = 2

Value:

nums[2] = 1

Check:

2 > 1

✅ True!

Therefore:

prev_index = stack.pop()
prev_index = 2

Stack:

[1]

Now:

ans[2] = nums[1]

Therefore:

ans[2] = 2

Answer becomes:

ans = [2, -1, 2]

Now check the stack again.

Top:

stack[-1] = 1

Value:

nums[1] = 2

Current value is also:

2

Check:

2 > 2

❌ False.

Stop the while loop.

Since:

i = 4

and:

4 < 3 → False

we don't push anything.

Final stack:

[1]
7. i = 5

Calculate:

index = 5 % 3
      = 2

So:

nums[2] = 1

Stack:

[1]

Top:

stack[-1] = 1

Value:

nums[1] = 2

Check:

1 > 2

❌ False.

Nothing happens.

🎯 Final result

After all iterations:

ans = [2, -1, 2]

So:

return ans

returns:

[2, -1, 2]

| `i` | `index = i%n` | Current value | Stack before | Action                   | `ans`        |
| --: | ------------: | ------------: | ------------ | ------------------------ | ------------ |
|   0 |             0 |             1 | `[]`         | Push 0                   | `[-1,-1,-1]` |
|   1 |             1 |             2 | `[0]`        | Pop 0 → answer 2; push 1 | `[2,-1,-1]`  |
|   2 |             2 |             1 | `[1]`        | Push 2                   | `[2,-1,-1]`  |
|   3 |             0 |             1 | `[1,2]`      | Nothing                  | `[2,-1,-1]`  |
|   4 |             1 |             2 | `[1,2]`      | Pop 2 → answer 2         | `[2,-1,2]`   |
|   5 |             2 |             1 | `[1]`        | Nothing                  | `[2,-1,2]`   |


i = 0
│
├── while for i=0 finishes
│
└── if i< n executes
       ↓
     i = 1
       │
       ├── while for i=1 finishes
       │
       └── if i<n executes
              ↓
            i = 2
              │
              ├── while for i=2 finishes
              │
              └── if i<n executes
                     ↓
                   i = 3
                     │
                     ├── while for i=3 finishes
                     │
                     └── if i<n executes
                            ↓
                          i = 4
                              ...
"""