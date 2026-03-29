"""

LC: 374. Guess Number Higher or Lower

Easy

Topics
Binary Search
Interactive

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked (the number I picked stays the same throughout the game).

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.

 

Example 1:

Input: n = 10, pick = 6
Output: 6
Example 2:

Input: n = 1, pick = 1
Output: 1
Example 3:

Input: n = 2, pick = 1
Output: 1
 

Constraints:

1 <= n <= 231 - 1
1 <= pick <= n
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
960,933/1.7M
Acceptance Rate
56.9%

"""


PICKED_NUMBER = 6   # 👈 change this to test different cases

def guess(num: int) -> int:
    if num > PICKED_NUMBER:
        return -1
    elif num < PICKED_NUMBER:
        return 1
    else:
        return 0

class Solution:
    def guessNumber(self,n:int)->int:
        low=1
        high=n
        while low<=high:
            mid=(low+high)//2
            res=guess(mid)
            if res==0:
                return mid
            elif res==-1:
                return mid-1
            else:
                return mid+1

# ------------------------
# Run and test
# ------------------------

if __name__ == "__main__":
    sol = Solution()
    n = 10
    ans = sol.guessNumber(n)
    print("Guessed Number:", ans)