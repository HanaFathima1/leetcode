"""

LC: 567. Permutation in String

Attempted

Medium

Topics
Principal
Hash Table
Two Pointers
String
Sliding Window

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
1,635,442/3.3M
Acceptance Rate
49.7%

Hint 1
Obviously, brute force will result in TLE. Think of something else.
Hint 2
How will you check whether one string is a permutation of another string?
Hint 3
One way is to sort the string and then compare. But, Is there a better way?
Hint 4
If one string is a permutation of another string then they must have one common metric. What is that?
Hint 5
Both strings must have same character frequencies, if one is permutation of another. Which data structure should be used to store frequencies?
Hint 6
What about hash table? An array of size 26?

"""

from collections import Counter
def permutationString(s1,s2):
    if len(s1)>len(s2):
        return False
    s1_freq=Counter(s1)
    for i in range(len(s2)-len(s1)+1):
        window=s2[i:i+len(s1)]
        if Counter(window)==s1_freq:
            return True 
    return False
print(permutationString(s1 = "ab", s2 = "eidbaooo"))
    
#explanation
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # s1 cannot fit inside s2
        if len(s1) > len(s2):
            return False

        # Frequency of characters in s1
        s1_freq = Counter(s1)

        # Check every substring of s2
        # having the same length as s1
        for i in range(len(s2) - len(s1) + 1):

            # Create current substring/window
            window = s2[i:i + len(s1)]

            # Check whether window is a permutation of s1
            if Counter(window) == s1_freq:
                return True

        return False
    
"""
Detailed dry run

Input:

s1 = "ab"
s2 = "eidbaooo"

First:

s1_freq = Counter("ab")

gives:

{'a': 1, 'b': 1}
i = 0
window = s2[0:2]
"ei"

Compare:

s1     → {'a': 1, 'b': 1}
window → {'e': 1, 'i': 1}

❌ Not equal.

i = 1
window = "id"
s1     → {'a': 1, 'b': 1}
window → {'i': 1, 'd': 1}

❌ Not equal.

i = 2
window = "db"
s1     → {'a': 1, 'b': 1}
window → {'d': 1, 'b': 1}

❌ Not equal.

i = 3
window = "ba"
s1     → {'a': 1, 'b': 1}
window → {'b': 1, 'a': 1}

✅ Equal!

Therefore:

return True
"""


#
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # If s1 is longer than s2,
        # permutation of s1 cannot exist in s2
        if len(s1) > len(s2):
            return False

        # Count characters in s1
        s1_freq = Counter(s1)

        # Frequency of characters inside current window
        window_freq = Counter()

        # Window size must be equal to s1 length
        window_size = len(s1)

        for right in range(len(s2)):

            # Add current character to window
            window_freq[s2[right]] += 1

            # If window becomes bigger than s1,
            # remove the leftmost character
            if right >= window_size:
                left_char = s2[right - window_size]
                window_freq[left_char] -= 1

                # Remove character completely if frequency becomes 0
                if window_freq[left_char] == 0:
                    del window_freq[left_char]

            # If frequencies are equal,
            # current window is a permutation of s1
            if window_freq == s1_freq:
                return True

        return False

"""
dry run the code

Input:

s1 = "ab"
s2 = "eidbaooo"
s1_freq
a → 1
b → 1

Window size:

2
right = 0

Character:

e

Window:

[e]

Frequency:

e → 1

Not equal.

right = 1

Add i:

[e i]

Frequency:

e → 1
i → 1

Not equal.

right = 2

Add d:

[e i d]

Too large!

Remove the character at:

right - window_size
2 - 2 = 0

So remove:

e

Window becomes:

[i d]

Not equal.

right = 3

Add b:

[i d b]

Remove:

s2[3 - 2]
s2[1]

which is:

i

Window:

[d b]

Not equal.

right = 4

Add a:

[d b a]

Remove:

s2[4 - 2]
s2[2]

which is:

d

Window:

[b a]

Frequency:

a → 1
b → 1

Compare:

s1_freq
a → 1
b → 1

window_freq
a → 1
b → 1
🎯 MATCH!
return True
"""