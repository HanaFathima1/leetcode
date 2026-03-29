"""

LC: 204. Count Primes

Medium

Topics:
Array
Math
Enumeration
Number Theory

Given an integer n, return the number of prime numbers that are strictly less than n.

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0
 

Constraints:

0 <= n <= 5 * 106

Hint 1
Checking all the integers in the range [1, n - 1] is not efficient. Think about a better approach.
Hint 2
Since most of the numbers are not primes, we need a fast approach to exclude the non-prime integers.
Hint 3
Use Sieve of Eratosthenes.    
    
"""

class Solution:
    def countPrimes(self, n:int) -> int:
        if n<=2:
            return 0
        countPrimes = [True] * n
        countPrimes[0] = countPrimes[1] = False
        p=2
        while p*p < n:
            if countPrimes[p]:
                for i in range(p*p, n, p):
                    countPrimes[i] = False
            p+=1
        return sum(countPrimes) 
sol = Solution()
print(sol.countPrimes(10))       
print(sol.countPrimes(0))    
print(sol.countPrimes(1))             
            
        
        