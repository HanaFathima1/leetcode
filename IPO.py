"""

LC: 502. IPO

Hard

Topics
Principal
Array
Greedy
Sorting
Heap (Priority Queue)

Companies
Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.

You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of capital[i] is needed to start it.

Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.

Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the final maximized capital.

The answer is guaranteed to fit in a 32-bit signed integer.

 

Example 1:

Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
Output: 4
Explanation: Since your initial capital is 0, you can only start the project indexed 0.
After finishing it you will obtain profit 1 and your capital becomes 1.
With capital 1, you can either start the project indexed 1 or the project indexed 2.
Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.
Example 2:

Input: k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
Output: 6
 

Constraints:

1 <= k <= 105
0 <= w <= 109
n == profits.length
n == capital.length
1 <= n <= 105
0 <= profits[i] <= 104
0 <= capital[i] <= 109
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
304,635/571.5K
Acceptance Rate
53.3%

"""

import heapq

class Solution:
    def findMaximisedCapital(self,k,w,profits,capital):
        projects=list(zip(capital,profits))
        projects.sort()
        max_heap=[]
        i=0
        n=len(projects)
        for _ in  range(k):
            while i<n and projects[i][0]<=w:
                heapq.heappush(max_heap,-projects[i][1])
                i+=1
            if not max_heap:
                break
            w += -heapq.heappop(max_heap)
        return w
sol=Solution()
print(sol.findMaximisedCapital(k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]))


#EXPLANATION OF CODE

import heapq

class Solution:

    def findMaximisedCapital(self, k, w, profits, capital):
        # Combine capital requirement and profit of each project
        # Example:
        # capital = [0,1,1]
        # profits = [1,2,3]
        # projects = [(0,1), (1,2), (1,3)]
        projects = list(zip(capital, profits))

        # Sort projects by capital required
        # This allows us to efficiently find all projects
        # that can be started with current capital 'w'
        projects.sort()

        # Python heapq is a min-heap.
        # To simulate a max-heap, we store negative profits.
        max_heap = []

        # Pointer to traverse sorted projects
        i = 0

        # Total number of projects
        n = len(projects)

        # We can choose at most k projects
        for _ in range(k):

            # Add all projects that are currently affordable
            # (capital required <= current capital w)
            while i < n and projects[i][0] <= w:

                # Push negative profit to create max-heap behavior
                heapq.heappush(max_heap, -projects[i][1])

                i += 1

            # If no affordable projects exist, stop early
            if not max_heap:
                break

            # Select the most profitable project available
            # heappop returns the smallest negative value,
            # which corresponds to the largest profit
            w += -heapq.heappop(max_heap)

        # Return final maximized capital
        return w


# Create object
sol = Solution()

# Example:
# Initial capital = 0
# Can choose at most 2 projects
# profits = [1,2,3]
# capital = [0,1,1]
print(sol.findMaximisedCapital(
    k=2,
    w=0,
    profits=[1, 2, 3],
    capital=[0, 1, 1]
))


#DRY RUN
"""
Dry Run

Input:

k = 2
w = 0
profits = [1,2,3]
capital = [0,1,1]

Projects after sorting:

[(0,1), (1,2), (1,3)]
Iteration 1

Current capital:

w = 0

Affordable projects:

(0,1)

Heap:

[-1]

Choose highest profit:

profit = 1

New capital:

w = 0 + 1 = 1
Iteration 2

Current capital:

w = 1

New affordable projects:

(1,2), (1,3)

Heap:

[-3, -2]

Choose highest profit:

profit = 3

New capital:

w = 1 + 3 = 4

Loop ends (k = 2 projects chosen).

Output:

4
=========================================
Core Idea
Sort projects by capital required.
As your capital grows, keep adding newly affordable projects into a max heap.
Always pick the project with the highest profit among the affordable ones.
Repeat at most k times.
=========================================
Time Complexity
Sorting projects: O(n log n)
Each project is pushed and popped from heap at most once: O(n log n)
Overall: O(n log n)
=========================================
Space Complexity
Projects list: O(n)
Heap: O(n)

Overall space: O(n).
"""