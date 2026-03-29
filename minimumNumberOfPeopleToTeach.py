"""

LC: 1733. Minimum Number of People to Teach

Medium

Topics
Array
Hash Table
Greedy
Biweekly Contest 44

On a social network consisting of m users and some friendships between users, two users can communicate with each other if they know a common language.

You are given an integer n, an array languages, and an array friendships where:

There are n languages numbered 1 through n,
languages[i] is the set of languages the i​​​​​​th​​​​ user knows, and
friendships[i] = [u​​​​​​i​​​, v​​​​​​i] denotes a friendship between the users u​​​​​​​​​​​i​​​​​ and vi.
You can choose one language and teach it to some users so that all friends can communicate with each other. Return the minimum number of users you need to teach.

Note that friendships are not transitive, meaning if x is a friend of y and y is a friend of z, this doesn't guarantee that x is a friend of z.
 

Example 1:

Input: n = 2, languages = [[1],[2],[1,2]], friendships = [[1,2],[1,3],[2,3]]
Output: 1
Explanation: You can either teach user 1 the second language or user 2 the first language.
Example 2:

Input: n = 3, languages = [[2],[1,3],[1,2],[3]], friendships = [[1,4],[1,2],[3,4],[2,3]]
Output: 2
Explanation: Teach the third language to users 1 and 3, yielding two users to teach.
 

Constraints:

2 <= n <= 500
languages.length == m
1 <= m <= 500
1 <= languages[i].length <= n
1 <= languages[i][j] <= n
1 <= u​​​​​​i < v​​​​​​i <= languages.length
1 <= friendships.length <= 500
All tuples (u​​​​​i, v​​​​​​i) are unique
languages[i] contains only unique values
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
18,109/35.2K
Acceptance Rate
51.4%

Hint 1
You can just use brute force and find out for each language the number of users you need to teach
Hint 2
Note that a user can appear in multiple friendships but you need to teach that user only once

"""

from typing import List
class Solution:
    def minimumTeachings(self, n:int, languages:List[List[int]], friendship:List[List[int]]) -> int:
        cncon = set()
        for u,v in friendship:
            can_comm = False
            mp = set(languages[u-1])
            for lang in languages[v-1]:
                if lang in mp:
                    can_comm = True
                    break
            if not can_comm:
                cncon.add(u-1)
                cncon.add(v-1)
        if not cncon:
            return 0
        cnt = [0]*n
        for person in cncon:
            for lang in languages[person]:
                cnt[lang-1]+=1
        max_cnt = 0
        for c in cnt:
            max_cnt = max(max_cnt,c)
        return len(cncon)-max_cnt
sol = Solution()
print(sol.minimumTeachings(n = 2, languages = [[1],[2],[1,2]], friendship = [[1,2],[1,3],[2,3]]))
print(sol.minimumTeachings(n = 3, languages = [[2],[1,3],[1,2],[3]], friendship = [[1,4],[1,2],[3,4],[2,3]]))
    

#-------------------------------------------------------------------
"""
class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        languages = [set(l) for l in languages]

        dontspeak = set()
        for u, v in friendships:
            u = u-1
            v = v-1
            if languages[u] & languages[v]: continue
            dontspeak.add(u)
            dontspeak.add(v)

        langcount = Counter()
        for f in dontspeak:
            for l in languages[f]:
                langcount[l] += 1

        return 0 if not dontspeak else len(dontspeak) - max(list(langcount.values()))
"""