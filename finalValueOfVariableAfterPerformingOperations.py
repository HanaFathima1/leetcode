"""

LC: 2011. Final Value of Variable After Performing Operations

Easy

Topics:
Array
String
Simulation
Weekly Contest 259

There is a programming language with only four operations and one variable X:

++X and X++ increments the value of the variable X by 1.
--X and X-- decrements the value of the variable X by 1.
Initially, the value of X is 0.

Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.

 

Example 1:

Input: operations = ["--X","X++","X++"]
Output: 1
Explanation: The operations are performed as follows:
Initially, X = 0.
--X: X is decremented by 1, X =  0 - 1 = -1.
X++: X is incremented by 1, X = -1 + 1 =  0.
X++: X is incremented by 1, X =  0 + 1 =  1.
Example 2:

Input: operations = ["++X","++X","X++"]
Output: 3
Explanation: The operations are performed as follows:
Initially, X = 0.
++X: X is incremented by 1, X = 0 + 1 = 1.
++X: X is incremented by 1, X = 1 + 1 = 2.
X++: X is incremented by 1, X = 2 + 1 = 3.
Example 3:

Input: operations = ["X++","++X","--X","X--"]
Output: 0
Explanation: The operations are performed as follows:
Initially, X = 0.
X++: X is incremented by 1, X = 0 + 1 = 1.
++X: X is incremented by 1, X = 1 + 1 = 2.
--X: X is decremented by 1, X = 2 - 1 = 1.
X--: X is decremented by 1, X = 1 - 1 = 0.
 

Constraints:

1 <= operations.length <= 100
operations[i] will be either "++X", "X++", "--X", or "X--".

Seen this question in a real interview before?
1/5
Yes
No
Accepted
491,547/548.6K
Acceptance Rate
89.6%

Hint 1
There are only two operations to keep track of.
Hint 2
Use a variable to store the value after each operation.

"""

class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        X=0
        for op in operations:
            if op=='X++':
                X=X+1
            if op=='++X':
                X=X+1
            if op=='X--':
                X=X-1            
            if op=='--X':
                X=X-1
        return X
sol=Solution()
print(sol.finalValueAfterOperations(["--X","X++","X++"]))
print(sol.finalValueAfterOperations(["++X","++X","X++"]))
print(sol.finalValueAfterOperations(["X++","++X","--X","X--"]))

            
            
    