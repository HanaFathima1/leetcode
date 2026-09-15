"""

LC:438. Find All Anagrams in a String

Medium

Topics
Junior
Hash Table
String
Sliding Window

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
1,299,633/2.4M
Acceptance Rate
54.5%

"""

from collections import Counter 
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        res=[]
        if len(s)<len(p):
            return []
        p_freq=Counter(p)
        for i in range(len(s)-len(p)+1):
            window=s[i:i+len(p)]
            if Counter(window)==p_freq:
                res.append(i)
        return res
sol=Solution()
print(sol.findAnagrams("cbaebabacd", "abc")) # Output: [0, 6]


"""
Let's dry run it

Input:

s = "cbaebabacd"
p = "abc"

We want windows of size:

len(p) = 3

So:

range(len(s) - len(p) + 1)

becomes:

10 - 3 + 1 = 8

Therefore:

i = 0,1,2,3,4,5,6,7
i = 0
window = s[0:3]
"cba"

Frequency:

c → 1
b → 1
a → 1

Same as "abc".

✅ Add 0

res = [0]
i = 1
window = "bae"

Not an anagram.

❌ Nothing added.

i = 2
window = "aeb"

Not an anagram.

❌

Eventually:

i = 6

window = "bac"

This is an anagram.

✅

res = [0, 6]

Final answer:

[0, 6]
"""

#====Optimized Code====
from collections import Counter

class Solution:

    def findAnagrams(self, s: str, p: str) -> list[int]:

        # Result array to store starting indices
        # of all anagrams
        res = []

        # If p is longer than s,
        # an anagram of p cannot exist in s
        if len(p) > len(s):
            return res

        # Store the frequency of every character in p
        p_freq = Counter(p)

        # Store the frequency of characters
        # in the current sliding window
        window_freq = Counter()

        # Left pointer of our window
        left = 0

        # Right pointer moves through s
        for right in range(len(s)):

            # Add the current character into the window
            window_freq[s[right]] += 1

            # If the window becomes larger than p,
            # remove the character at the left
            if right - left + 1 > len(p):

                window_freq[s[left]] -= 1

                # If frequency becomes 0,
                # remove the character from Counter
                if window_freq[s[left]] == 0:
                    del window_freq[s[left]]

                # Move left pointer forward
                left += 1

            # If the current window has exactly
            # the same character frequencies as p,
            # we found an anagram
            if window_freq == p_freq:
                res.append(left)

        return res
    
"""
Dry run

Let's use:

s = "cbaebabacd"
p = "abc"

We need a window of size:

len(p) = 3

p_freq:

{
    'a': 1,
    'b': 1,
    'c': 1
}

Initially:

left = 0
window_freq = {}
res = []
🟢 right = 0

Character:

s[0] = 'c'

Add it:

window = "c"

Frequency:

c → 1

Window size:

right - left + 1
0 - 0 + 1
= 1

Not big enough yet.

No match.

🟢 right = 1

Character:

s[1] = 'b'

Add:

window = "cb"

Frequency:

c → 1
b → 1

Window size:

1 - 0 + 1 = 2

Still smaller than 3.

No match.

🟢 right = 2

Character:

s[2] = 'a'

Add:

window = "cba"

Frequency:

c → 1
b → 1
a → 1

Window size:

2 - 0 + 1 = 3

Now compare:

window_freq = {
    c: 1,
    b: 1,
    a: 1
}

p_freq = {
    a: 1,
    b: 1,
    c: 1
}

They are equal.

✅ "cba" is an anagram of "abc".

Therefore:

res.append(left)

left = 0

res = [0]
🟢 right = 3

Character:

s[3] = 'e'

Add it:

window = "cbae"

Frequency:

c → 1
b → 1
a → 1
e → 1

But window size is:

3 - 0 + 1 = 4

That's too large.

So remove:

s[left]

left = 0

s[0] = 'c'

Remove c:

c → 0

Delete it:

del window_freq['c']

Move left:

left += 1

Now:

left = 1

Window is:

"bae"

Frequency:

b → 1
a → 1
e → 1

Not equal to abc.

❌

🟢 right = 4

Character:

s[4] = 'b'

Window temporarily becomes:

"baeb"

Too large.

Remove:

s[left]

left = 1

s[1] = 'b'

Remove b.

Then:

left = 2

Window:

"aeb"

Frequency:

a → 1
e → 1
b → 1

Not equal.

❌

🟢 right = 5

Add:

s[5] = 'a'

Window:

"aeba"

Too large.

Remove:

s[2] = 'a'

Now window:

"eba"

Frequency:

e → 1
b → 1
a → 1

Not equal because we need c.

❌

🟢 right = 6

Add:

s[6] = 'b'

Remove the leftmost character.

Window becomes:

"bab"

Frequency:

b → 2
a → 1

Not equal.

❌

🟢 right = 7

Add:

s[7] = 'a'

After removing the leftmost character, window becomes:

"aba"

Frequency:

a → 2
b → 1

Not equal.

❌

🟢 right = 8

Add:

s[8] = 'c'

After removing the leftmost character:

window = "bac"

Frequency:

b → 1
a → 1
c → 1

Compare:

window_freq = {
    b: 1,
    a: 1,
    c: 1
}

p_freq = {
    a: 1,
    b: 1,
    c: 1
}

Equal!

So:

res.append(left)

At this point:

left = 6

Therefore:

res = [0, 6]
🟢 right = 9

Add:

s[9] = 'd'

Window temporarily becomes too large.

Remove the leftmost character.

Window:

"acd"

Frequency:

a → 1
c → 1
d → 1

Not equal.

❌

Final:

res = [0, 6]
⭐ The entire dry run visually
s = c b a e b a b a c d
    └─────┘
      cba       → MATCH → index 0

      └─────┘
       bae      → no

        └─────┘
         aeb     → no

         └─────┘
          eba    → no

          └─────┘
           bab   → no

           └─────┘
            aba  → no

            └─────┘
             bac → MATCH → index 6

             └─────┘
              acd → no

Answer:

[0, 6]
"""