"""

LC: 735. Asteroid Collision

Medium

Topics
Array
Stack
Simulation
Weekly Contest 60

Hint
We are given an array asteroids of integers representing asteroids in a row. The indices of the asteroid in the array represent their relative position in space.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
Example 4:

Input: asteroids = [3,5,-6,2,-1,4]​​​​​​​
Output: [-6,2,4]
Explanation: The asteroid -6 makes the asteroid 3 and 5 explode, and then continues going left. On the other side, the asteroid 2 makes the asteroid -1 explode and then continues going right, without reaching asteroid 4.
 

Constraints:

2 <= asteroids.length <= 104
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
916,259/2M
Acceptance Rate
46.4%

Hint 1
Say a row of asteroids is stable. What happens when a new asteroid is added on the right?

"""

class Solution:
    def asteriodCollision(self,asteroids:list[int])->list[int]:
        stack=[]
        for a in asteroids:
            while stack and a<0<stack[-1]:
                if abs(a)>stack[-1]:
                    stack.pop()
                elif abs(a)==stack[-1]:
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(a)
        return stack
sol=Solution()
print(sol.asteriodCollision(asteroids = [5,10,-5]))
print(sol.asteriodCollision(asteroids = [8,-8]))
print(sol.asteriodCollision(asteroids = [10,2,-5]))


#--------------SAME CODE WITH EXPLANATION----------------

class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        # Initialize an empty stack that will store the final remaining asteroids
        stack = []
        
        # Loop through each asteroid in the given list
        for a in asteroids:
            
            # While there is something in the stack AND
            # the current asteroid 'a' is moving left (a < 0) AND
            # the last asteroid in the stack is moving right (stack[-1] > 0):
            # → This is the only situation where a collision can happen.
            while stack and a < 0 < stack[-1]:
                
                # Case 1: Current asteroid (a) is bigger → it destroys the last asteroid in stack
                if abs(a) > stack[-1]:
                    stack.pop()           # Remove the asteroid in the stack and continue checking
                
                # Case 2: Both asteroids are equal in size → both get destroyed
                elif abs(a) == stack[-1]:
                    stack.pop()           # Remove the asteroid from stack
                    break                 # Current asteroid also gets destroyed → stop processing 'a'
                
                # Case 3: Stack asteroid is bigger → current asteroid gets destroyed
                else:
                    break                 # Do not add 'a' to stack → it is gone
            
            # This *else* belongs to the WHILE loop, not the IF.
            # The else executes only if the WHILE loop did NOT break.
            # That means: no collision destroyed 'a', so we safely push it to stack.
            else:
                stack.append(a)
        
        # After processing all asteroids, return the remaining ones
        return stack
