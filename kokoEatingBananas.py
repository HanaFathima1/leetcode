"""

LC: 875. Koko Eating Bananas

Medium

Topics
Array
Binary Search
Weekly Contest 94

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
 

Constraints:

1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
1,419,237/2.9M
Acceptance Rate
49.5%

"""
import math

class Solution:
    def minEatingSpeed(self,piles:list[int],h:int)->int:
        left=1
        right=max(piles)
        ans=right
        while left<=right:
            mid=(left+right)//2
            hours=0
            for pile in piles:
                hours+=math.ceil(pile/mid)
            if hours<=h:
                ans=mid
                right=mid-1
            else:
                left=mid+1
        return ans
sol=Solution()
print(sol.minEatingSpeed(piles = [3,6,7,11], h = 8))
print(sol.minEatingSpeed(piles = [30,11,23,4,20], h = 5))
print(sol.minEatingSpeed(piles = [30,11,23,4,20], h = 6))

"""
#explanation of the question:

Suppose Koko has these banana piles:

piles = [3, 6, 7, 11]

And the guards will return in:

h = 8 hours

The question is:

How fast should Koko eat so that she finishes all the bananas within 8 hours?

The "speed" is measured in bananas per hour.

Suppose Koko chooses a speed of 1 banana/hour

Every hour she can eat only 1 banana from a single pile.

To finish:

Pile of 3 → 3 hours
Pile of 6 → 6 hours
Pile of 7 → 7 hours
Pile of 11 → 11 hours

Total:

3 + 6 + 7 + 11 = 27 hours

But she has only 8 hours.

❌ Too slow.

Suppose she chooses 2 bananas/hour

Now:

Pile 3 → 2 hours
Pile 6 → 3 hours
Pile 7 → 4 hours
Pile 11 → 6 hours

Total:

2 + 3 + 4 + 6 = 15 hours

Still more than 8.

❌ Too slow.

Suppose she chooses 4 bananas/hour

Now:

Pile 3 → 1 hour
Pile 6 → 2 hours
Pile 7 → 2 hours
Pile 11 → 3 hours

Total:

1 + 2 + 2 + 3 = 8 hours

Exactly 8 hours.

✅ This speed works.

What if she chooses 5 bananas/hour?
Pile 3 → 1 hour
Pile 6 → 2 hours
Pile 7 → 2 hours
Pile 11 → 3 hours

Total:

8 hours

Also works.

What if she chooses 10 bananas/hour?
Pile 3 → 1 hour
Pile 6 → 1 hour
Pile 7 → 1 hour
Pile 11 → 2 hours

Total:

5 hours

Also works.

So what answer does the problem want?

It doesn't ask:

"Can she finish?"

It asks:

What is the smallest eating speed that lets her finish within h hours?

For this example:

Speed 1 → ❌
Speed 2 → ❌
Speed 3 → ❌
Speed 4 → ✅
Speed 5 → ✅
Speed 6 → ✅
...

The first speed that works is 4, so the answer is:

4
The most confusing rule

Many people misunderstand this sentence:

"Each hour, Koko chooses some pile and eats k bananas from that pile."

It means:

If k = 4 and a pile has only 3 bananas, she eats all 3 and stops for that hour.

She cannot use the remaining capacity (1 banana) to start another pile.

For example:

Pile = 3
Speed = 4

She spends 1 full hour to finish that pile.

Not 45 minutes.

Let me ask you one question.

Suppose:

piles = [8]
h = 2
"""