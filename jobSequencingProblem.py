"""

GFG: Job Sequencing Problem

Difficulty: Medium
Accuracy: 34.51%
Submissions: 367K+
Points: 4

You are given two arrays: deadline[], and profit[], which represent a set of jobs, where each job is associated with a deadline, and a profit. Each job takes 1 unit of time to complete, and only one job can be scheduled at a time. You will earn the profit associated with a job only if it is completed by its deadline.

Your task is to find:

The maximum number of jobs that can be completed within their deadlines.
The total maximum profit earned by completing those jobs.
Examples :

Input: deadline[] = [4, 1, 1, 1], profit[] = [20, 10, 40, 30]
Output: [2, 60]
Explanation: Job1 and Job3 can be done with maximum profit of 60 (20+40).
Input: deadline[] = [2, 1, 2, 1, 1], profit[] = [100, 19, 27, 25, 15]
Output: [2, 127]
Explanation: Job1 and Job3 can be done with maximum profit of 127 (100+27).
Input: deadline[] = [3, 1, 2, 2], profit[] = [50, 10, 20, 30]
Output: [3, 100]
Explanation: Job1, Job3 and Job4 can be completed with a maximum profit of 100 (50 + 20 + 30).
Constraints:
1 ≤ deadline.size() = profit.size() ≤ 105
1 ≤ deadline[i] ≤ deadline.size()
1 ≤ profit[i] ≤ 500

Expected Complexities
Time Complexity: O(n log n)
Auxiliary Space: O(n)

Company Tags
Flipkart
Accolite
Microsoft

Topic Tags
GreedyAlgorithmsDisjoint Set
Related Interview Experiences
Accolite Interview Experience Set 15 CampusMicrosoft Interview Experience For Software Engineering Internship 2019

Related Articles
Job Sequencing Problem Using Disjoint 
SetJob Sequencing Problem

"""

import heapq
def jobSequencing(jobs,n):
    jobs.sort(key=lambda x:x[1])
    min_heap=[]
    for job in jobs:
        deadline=job[1]
        profit=job[2]
        heapq.heappush(min_heap,profit)
        if len(min_heap)>deadline:
            heapq.heappop(min_heap)
    total_profit=sum(min_heap)
    count=len(min_heap)
    return count,total_profit

jobs=[
    (1,2,100),
    (2,1,19),
    (3,2,27),
    (4,1,25),
    (5,3,15)
]
n=len(jobs)
res=jobSequencing(jobs,n)
print(res)