"""

LC: 649. Dota2 Senate

Medium

Topics
Principal
String
Greedy
Queue

In the world of Dota2, there are two parties: the Radiant and the Dire.

The Dota2 senate consists of senators coming from two parties. Now the Senate wants to decide on a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise one of the two rights:

Ban one senator's right: A senator can make another senator lose all his rights in this and all the following rounds.
Announce the victory: If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and decide on the change in the game.
Given a string senate representing each senator's party belonging. The character 'R' and 'D' represent the Radiant party and the Dire party. Then if there are n senators, the size of the given string will be n.

The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.

Suppose every senator is smart enough and will play the best strategy for his own party. Predict which party will finally announce the victory and change the Dota2 game. The output should be "Radiant" or "Dire".

 

Example 1:

Input: senate = "RD"
Output: "Radiant"
Explanation: 
The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
And the second senator can't exercise any rights anymore since his right has been banned. 
And in round 2, the first senator can just announce the victory since he is the only guy in the senate who can vote.
Example 2:

Input: senate = "RDD"
Output: "Dire"
Explanation: 
The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
And the second senator can't exercise any rights anymore since his right has been banned. 
And the third senator comes from Dire and he can ban the first senator's right in round 1. 
And in round 2, the third senator can just announce the victory since he is the only guy in the senate who can vote.
 

Constraints:

n == senate.length
1 <= n <= 104
senate[i] is either 'R' or 'D'.
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
291,792/584.3K
Acceptance Rate
49.9%

"""

#EXPLANATION
"""
Step 1: Understand the Problem in Simple Words

There are two parties:

R = Radiant
D = Dire

Each senator gets a turn.

When a senator gets a turn, they can:

✅ Ban one senator from the opposite party.

The banned senator loses all future turns.

The game continues until only one party remains.

Return:

"Radiant" if Radiant wins
"Dire" if Dire wins
Example 1
senate = "RD"
Round 1
R D
↑

R moves first.

R bans D.

Now D cannot act.

Winner:

Radiant
Example 2
senate = "RDD"
Round 1
R D D
↑

R bans first D.

Remaining:

R X D

(X means banned)

Now second D gets turn.

R X D
    ↑

D bans R.

Remaining:

X X D

Only Dire remains.

Answer:

Dire
Step 2: Key Observation

Instead of actually removing senators,

we only need to know:

Which senator gets the next turn?

The senator appearing earlier gets to act first.

This is why we store positions (indices).

Example
senate = "RDDRR"

Indices:

0 1 2 3 4
R D D R R

Store positions:

Radiant Queue = [0,3,4]

Dire Queue = [1,2]
Step 3: Why Use Queues?

The senators act in order.

Queue naturally gives:

First senator -> acts first

using:

popleft()

Perfect for this problem.
"""

#CODE
from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        n = len(senate)

        # Store positions of Radiant senators
        radiant = deque()

        # Store positions of Dire senators
        dire = deque()

        # Fill queues with indices
        for i in range(n):
            if senate[i] == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        # Continue the game as long as both parties still have senators alive.
        while radiant and dire:

            # Get the next Radiant senator
            r = radiant.popleft()

            # Get the next Dire senator
            d = dire.popleft()

            # Senator with smaller index acts first
            if r < d:

                # Radiant bans Dire
                # Radiant survives for next round
                radiant.append(r + n)

            else:

                # Dire bans Radiant
                # Dire survives for next round
                dire.append(d + n)

        # Check who remains
        return "Radiant" if radiant else "Dire"
sol = Solution()
print(sol.predictPartyVictory(senate = "RD"))
print(sol.predictPartyVictory(senate = "RDD"))

#DRY RUN
"""
senate = "RDD"

This is the smallest example where the answer is Dire.

Step 1: Store Positions

String:

Index:   0 1 2
Senate:  R D D

Create queues:

Radiant = [0]
Dire    = [1, 2]

Think of the queues as:

Radiant Queue
[0]

Dire Queue
[1, 2]
Round 1

Take the first senator from each queue.

r = 0
d = 1

Visualization:

R D D
↑ ↑
0 1

Compare:

0 < 1

Radiant comes earlier.

So Radiant gets to act first.

What does Radiant do?

Radiant bans one Dire senator.

The Dire senator at position 1 is removed.

R D D
↑ X

(X = banned)

Radiant survives

The winner gets another turn in the future.

Length of string:

n = 3

Add:

0 + 3 = 3

Back to Radiant queue.

Queues become:

Radiant = [3]
Dire    = [2]
Round 2

Take front senators:

r = 3
d = 2

Visualization:

Current Queues

Radiant = [3]
Dire    = [2]

Compare:

2 < 3

Dire comes earlier.

So Dire acts first.

What does Dire do?

Dire bans Radiant.

Radiant is removed.

Dire survives.

Add:

2 + 3 = 5

Queues become:

Radiant = []
Dire    = [5]
Stop

Radiant queue is empty.

Radiant = []
Dire = [5]

Only Dire remains.

Answer:

"Dire"
Another Dry Run (Radiant Wins)

Take:

senate = "RDR"

Length:

n = 3

Positions:

Radiant = [0, 2]
Dire    = [1]
Round 1

Take:

r = 0
d = 1

Compare:

0 < 1

Radiant acts first.

Dire gets banned.

Radiant survives.

Add:

0 + 3 = 3

Queues:

Radiant = [2, 3]
Dire    = []

Stop immediately.

Dire queue is empty.

Winner:

Radiant
"""

#TC & SC 
"""
Time Complexity

Each senator is processed at most once per survival.

Time Complexity: O(n)
Space Complexity

Two queues store indices.

Space Complexity: O(n)
"""