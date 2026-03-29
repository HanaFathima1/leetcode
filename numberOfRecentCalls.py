"""

LC: 933. Number of Recent Calls

Easy

Topics
Design
Queue
Data Stream
Weekly Contest 109

You have a RecentCounter class which counts the number of recent requests within a certain time frame.

Implement the RecentCounter class:

RecentCounter() Initializes the counter with zero recent requests.
int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

 

Example 1:

Input
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
Output
[null, 1, 2, 3, 3]

Explanation
RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3
 

Constraints:

1 <= t <= 109
Each test case will call ping with strictly increasing values of t.
At most 104 calls will be made to ping.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
471,517/605.3K
Acceptance Rate
77.9%

"""

from collections import deque

class RecentCounter:
    def __init__(self):
        # Initialize an empty double-ended queue to store ping timestamps
        self.q = deque()

    def ping(self, t: int) -> int:
        # Add the current ping timestamp to the right end of the queue
        self.q.append(t)

        # Remove timestamps from the left while they are strictly less than t - 3000
        # Those timestamps are older than the 3000 ms window and not counted.
        while self.q and self.q[0] < t - 3000:
            self.q.popleft()

        # After removals, queue contains only timestamps in [t-3000, t]
        # The number of such timestamps is the answer
        return len(self.q)
sol = RecentCounter()
print(sol.ping(1))      # 1
print(sol.ping(100))    # 2
print(sol.ping(3001))   # 3
print(sol.ping(3002))   # 3
