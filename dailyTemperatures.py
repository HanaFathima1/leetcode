"""

739. Daily Temperatures

Medium

Topics
Staff
Array
Stack
Monotonic Stack
Weekly Contest 61

Hint
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
1,754,922/2.6M
Acceptance Rate
68.7%

Hint 1
If the temperature is say, 70 today, then in the future a warmer temperature must be either 71, 72, 73, ..., 99, or 100. We could remember when all of them occur next.

"""

class MonotonicStack:
    def dailyTemperature(self, temperatures):
        n = len(temperatures)
        result = [0]*n
        stack = []
        
        for i in range(n):
            # As long as the stack isn’t empty and the current temperature is greater than the temperature at the index on top of the stack:
            while stack and temperatures[i]>temperatures[stack[-1]]:
                #Pop the top index from the stack and store it in prev_index.
                prev_index = stack.pop()
                #Calculate the number of days between i (current day) and prev_index, and store it in result[prev_index].
                result[prev_index] = i-prev_index
            stack.append(i)
        return result
sol = MonotonicStack()
print(sol.dailyTemperature([30,40,50,60]))
        
#DRY RUNN
"""
Input
temperatures = [73,74,75,71,69,72,76,73]
Initial State
result = [0,0,0,0,0,0,0,0]
stack = []

The stack stores indices.

Dry Run Table
| i | Temp | Stack Before | Action                 | Result Update       | Stack After |
| - | ---- | ------------ | ---------------------- | ------------------- | ----------- |
| 0 | 73   | []           | Push 0                 | No change           | [0]         |
| 1 | 74   | [0]          | 74 > 73 → Pop 0        | result[0] = 1-0 = 1 | [1]         |
| 2 | 75   | [1]          | 75 > 74 → Pop 1        | result[1] = 2-1 = 1 | [2]         |
| 3 | 71   | [2]          | 71 < 75 → Push 3       | No change           | [2,3]       |
| 4 | 69   | [2,3]        | 69 < 71 → Push 4       | No change           | [2,3,4]     |
| 5 | 72   | [2,3,4]      | 72 > 69 → Pop 4        | result[4] = 5-4 = 1 | [2,3]       |
| 5 | 72   | [2,3]        | 72 > 71 → Pop 3        | result[3] = 5-3 = 2 | [2]         |
| 5 | 72   | [2]          | 72 < 75 → Stop Popping | No change           | [2]         |
| 5 | 72   | [2]          | Push 5                 | No change           | [2,5]       |
| 6 | 76   | [2,5]        | 76 > 72 → Pop 5        | result[5] = 6-5 = 1 | [2]         |
| 6 | 76   | [2]          | 76 > 75 → Pop 2        | result[2] = 6-2 = 4 | []          |
| 6 | 76   | []           | Push 6                 | No change           | [6]         |
| 7 | 73   | [6]          | 73 < 76 → Push 7       | No change           | [6,7]       |

Result Array After Each Update
| Operation     | Result            |
| ------------- | ----------------- |
| Initial       | [0,0,0,0,0,0,0,0] |
| result[0] = 1 | [1,0,0,0,0,0,0,0] |
| result[1] = 1 | [1,1,0,0,0,0,0,0] |
| result[4] = 1 | [1,1,0,0,1,0,0,0] |
| result[3] = 2 | [1,1,0,2,1,0,0,0] |
| result[5] = 1 | [1,1,0,2,1,1,0,0] |
| result[2] = 4 | [1,1,4,2,1,1,0,0] |

Final Stack
stack = [6,7]

Indices 6 and 7 never found a warmer temperature.

Therefore:

result[6] = 0
result[7] = 0

remain unchanged.

Final Answer
[1,1,4,2,1,1,0,0]
Temperature View
| Day | Temperature | Next Warmer Temperature | Wait Days |
| --- | ----------- | ----------------------- | --------- |
| 0   | 73          | 74                      | 1         |
| 1   | 74          | 75                      | 1         |
| 2   | 75          | 76                      | 4         |
| 3   | 71          | 72                      | 2         |
| 4   | 69          | 72                      | 1         |
| 5   | 72          | 76                      | 1         |
| 6   | 76          | None                    | 0         |
| 7   | 73          | None                    | 0         |

Final Output
[1,1,4,2,1,1,0,0]
"""