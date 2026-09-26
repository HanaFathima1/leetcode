"""

LC: 1004. Max Consecutive Ones III

Medium

Topics
Array
Binary Search
Sliding Window
Prefix Sum
Weekly Contest 126

Hint
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
1,222,837/1.8M
Acceptance Rate
66.9%

Hint 1
One thing's for sure, we will only flip a zero if it extends an existing window of 1s. Otherwise, there's no point in doing it, right? Think Sliding Window!
Hint 2
Since we know this problem can be solved using the sliding window construct, we might as well focus in that direction for hints. Basically, in a given window, we can never have > K zeros, right?
Hint 3
We don't have a fixed size window in this case. The window size can grow and shrink depending upon the number of zeros we have (we don't actually have to flip the zeros here!).
Hint 4
The way to shrink or expand a window would be based on the number of zeros that can still be flipped and so on.

"""

class Solution:
    def longestOnes(self,nums:list[int],k:int)->int:
        left=0
        max_len=0
        zero_count=0
        for right in range(len(nums)):
            if nums[right]==0:
                zero_count+=1
            while zero_count>k:
                if nums[left]==0:
                    zero_count-=1
                left+=1
            max_len=max(max_len,right-left+1)
        return max_len
sol = Solution()
print(sol.longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2))
print(sol.longestOnes(nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3))
                
                
#======explanation and dry run==========
"""
1. Start with the actual problem

Suppose:

nums = [1, 1, 0, 0, 1, 1, 1]
k = 2

k = 2 means:

I am allowed to change at most 2 zeros into 1s.

Look at this window:

[1, 1, 0, 0, 1, 1]
          ↑  ↑
        zero zero

There are 2 zeros.

We can flip both:

[1, 1, 1, 1, 1, 1]

So this is a valid window.

Therefore its length 6 could be our answer.

2. What happens when we expand the window?

We use:

for right in range(len(nums)):

Think of right as a finger that moves from left to right.

Initially:

[1, 1, 0, 0, 1, 1, 1]
 ↑
 L
 ↑
 R

Then:

[1, 1, 0, 0, 1, 1, 1]
 ↑     ↑
 L     R

Then:

[1, 1, 0, 0, 1, 1, 1]
 ↑       ↑
 L       R

The window keeps getting bigger.

3. Why do we count zeros?

Because zeros are the problem.

We can already use all the 1s.

But every 0 requires one flip.

So:

0 zeros → need 0 flips
1 zero  → need 1 flip
2 zeros → need 2 flips
3 zeros → need 3 flips

But:

k = 2

So we are only allowed:

0, 1, or 2 zeros

We therefore write:

if nums[right] == 0:
    zeros += 1

This simply means:

"The new element entering my window is zero, so I need one more flip."

4. Now the important part: while zeros > k

Suppose our window becomes:

[1, 1, 0, 0, 1, 1, 0]

Count the zeros:

[1, 1, 0, 0, 1, 1, 0]
       ↑  ↑        ↑
       1  2        3

We have:

zeros = 3
k = 2

Can we flip all 3?

❌ No.

We are only allowed 2 flips.

Therefore:

while zeros > k:

means:

"My current window is invalid. I need to make it smaller."

5. How do we make it smaller?

We remove elements from the left.

That's why:

left += 1

Suppose:

[1, 1, 0, 0, 1, 1, 0]
 ↑                 ↑
 L                 R

Move left:

[1, 1, 0, 0, 1, 1, 0]
    ↑              ↑
    L              R

We've removed the first 1.

Did that remove a zero?

No.

So:

zeros = 3

Still invalid.

Move left again:

[1, 1, 0, 0, 1, 1, 0]
       ↑           ↑
       L           R

Still removed a 1.

zeros = 3

Still invalid.

Move left again:

[1, 1, 0, 0, 1, 1, 0]
          ↑        ↑
          L        R

Now we removed the first zero.

Therefore:

if nums[left] == 0:
    zeros -= 1

So:

zeros = 2

Now:

zeros <= k
2 <= 2

✅ The window is valid again.

6. This is the entire logic

Think of it like this:

             RIGHT
               ↓
[1  1  0  0  1  1  0]
 ↑
LEFT
Right finds a new element
nums[right]

If it's zero:

zeros += 1

Then ask:

Do I have too many zeros?

If:

zeros > k

the window is invalid.

So:

Move LEFT
    ↓
Remove element
    ↓
Was it zero?
    ↓
Yes → zeros -= 1
    ↓
zeros <= k?
    ↓
Yes → stop shrinking
7. Let's trace a very small example

Take:

nums = [1, 0, 0, 1]
k = 1

We can flip only one zero.

right = 0
[1]
 ↑

Zeros:

0

Valid.

right = 1
[1, 0]

Zeros:

1

Valid because:

1 <= k

We can flip the zero:

[1, 1]

Length = 2.

right = 2

Add another zero:

[1, 0, 0]

Zeros:

2

But:

2 > 1

❌ Invalid.

So move left.

Current:

[1, 0, 0]
 ↑
 L

nums[left] = 1.

Remove it:

[0, 0]
 ↑
 L

Still:

zeros = 2

Still invalid.

Move left again.

Now we remove:

0

Therefore:

zeros = 1

Now:

[0, 0]
    ↑

Actually the remaining window is the second zero only, depending on pointer position; the important invariant is that it now contains exactly one zero and is valid.



#============================

Index:   0  1  2  3  4  5  6  7  8  9  10
         ------------------------------------
nums:   [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]

And:

k = 2

Meaning:

We can flip at most 2 zeros.

2. Initial state
left = 0
zeros = 0
max_len = 0

Our window is:

[]
🟢 right = 0
nums[0] = 1

It's not zero.

So:

zeros = 0

Window:

[1]
 ↑
 L,R

Length:

right - left + 1
= 0 - 0 + 1
= 1

Therefore:

max_len = 1
🟢 right = 1
nums[1] = 1

Still:

zeros = 0

Window:

[1, 1]
 ↑     ↑
 L     R

Length:

1 - 0 + 1 = 2
max_len = 2
🟢 right = 2
nums[2] = 1

Still:

zeros = 0

Window:

[1, 1, 1]
 ↑       ↑
 L       R

Length:

2 - 0 + 1 = 3
max_len = 3
🟢 right = 3

Now:

nums[3] = 0

So:

zeros = 1

Window:

[1, 1, 1, 0]
 ↑          ↑
 L          R

We have:

zeros = 1
k = 2

So:

1 <= 2

✅ Valid.

Length:

3 - 0 + 1 = 4
max_len = 4

We can flip that one zero:

[1,1,1,0]
       ↓
[1,1,1,1]
🟢 right = 4
nums[4] = 0

Now:

zeros = 2

Window:

[1,1,1,0,0]
 ↑            ↑
 L            R

We have:

zeros = 2
k = 2

Valid!

2 <= 2

Length:

4 - 0 + 1 = 5

Therefore:

max_len = 5

We can flip both zeros:

[1,1,1,0,0]
        ↓ ↓
[1,1,1,1,1]

So length 5 is possible.

🔴 right = 5

Now:

nums[5] = 0

Our window becomes:

[1,1,1,0,0,0]
 ↑            ↑
 L            R

Number of zeros:

zeros = 3

But:

k = 2

Therefore:

3 > 2

❌ Invalid.

We need to shrink the window.

while zeros > k

Current:

[1,1,1,0,0,0]
 ↑
left
Remove nums[left]
nums[0] = 1

It's not zero.

So:

zeros = 3

Move left:

left = 1

Window:

[1,1,0,0,0]
   ↑       ↑
  left    right

Still:

zeros = 3

Still invalid.

Remove nums[1]
nums[1] = 1

Again, not zero.

zeros = 3

Move:

left = 2

Window:

[1,0,0,0]
     ↑   ↑
    L    R

Still invalid.

Remove nums[2]
nums[2] = 1

Again:

zeros = 3

Move:

left = 3

Now:

[0,0,0]
 ↑     ↑
 L     R

Still invalid.

Remove nums[3]

Now:

nums[3] = 0

So:

zeros -= 1

Therefore:

zeros = 2

Move:

left = 4

Now window is:

[0,0]
 ↑   ↑
 L   R

We have:

zeros = 2
k = 2

✅ Valid again.

Length:

right - left + 1
= 5 - 4 + 1
= 2

max_len stays:

5
🟢 right = 6
nums[6] = 1

Zeros stay:

zeros = 2

Window:

[0,0,1]
 ↑     ↑
 L     R

Valid because:

2 <= 2

Length:

6 - 4 + 1 = 3

max_len = 5

🟢 right = 7
nums[7] = 1

Window:

[0,0,1,1]
 ↑       ↑
 L       R

Zeros:

2

Valid.

Length:

7 - 4 + 1 = 4

max_len = 5

🟢 right = 8
nums[8] = 1

Window:

[0,0,1,1,1]
 ↑         ↑
 L         R

Zeros:

2

Valid.

Length:

8 - 4 + 1 = 5

max_len = 5

🟢 right = 9
nums[9] = 1

Window:

[0,0,1,1,1,1]
 ↑           ↑
 L           R

Zeros:

2

Valid.

Length:

9 - 4 + 1 = 6

🎯 New maximum!

max_len = 6

We can flip:

0 0
↓ ↓
1 1

So:

[0,0,1,1,1,1]

becomes:

[1,1,1,1,1,1]

That's 6 consecutive ones.

🔴 right = 10

Now:

nums[10] = 0

Zeros:

zeros = 3

Window:

[0,0,1,1,1,1,0]
 ↑             ↑
 L             R

Invalid:

3 > 2

So shrink from the left.

Remove nums[4]
nums[4] = 0

Therefore:

zeros = 2

Move:

left = 5

Now:

[0,1,1,1,1,0]
 ↑           ↑
 L           R

Valid:

zeros = 2

Length:

10 - 5 + 1 = 6

So:

max_len = max(6,6)
max_len = 6
"""
        