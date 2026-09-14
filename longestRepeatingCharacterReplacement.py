"""

LC: 424. Longest Repeating Character Replacement

Medium

Topics
Junior
Hash Table
String
Sliding Window

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.

Seen this question in a real interview before?
1/6
Yes
No
Accepted
1,769,432/2.9M
Acceptance Rate
60.6%

"""

#brute force
from collections import Counter
def characterReplacement(s,k):
    answer=0
    for left in range(len(s)):
        for right in range(left,len(s)):
            substring=s[left:right+1]
            substring_freq=Counter(substring)
            max_freq=max(substring_freq.values())
            window_length=right-left+1
            replacement=window_length-max_freq
            if replacement<=k:
                answer=max(answer,window_length)
    return answer
print(characterReplacement(s = "AABABBA", k = 1))

#===explanation====
from collections import Counter

def characterReplacement(s, k):

    answer = 0

    # Try every possible starting position
    for left in range(len(s)):

        # Try every possible ending position
        for right in range(left, len(s)):

            # Get the current substring
            substring = s[left:right + 1]

            # Count frequency of every character
            freq = Counter(substring)

            # Find the character that occurs the most
            max_freq = max(freq.values())

            # Length of current substring
            window_length = right - left + 1

            # Characters that are NOT the most frequent
            # characters need to be replaced.
            replacements = window_length - max_freq

            # If we can replace those characters using
            # at most k replacements, this substring is valid.
            if replacements <= k:

                # Keep the longest valid substring
                answer = max(answer, window_length)

    return answer

"""
Brute Force Dry Run

Let's use:

s = "AABABBA"
k = 1

Indexes:

 0 1 2 3 4 5 6
 A A B A B B A

We try every possible substring.

left = 0
right = 0

Substring:

"A"

Frequency:

A → 1

Most frequent:

1

Length:

1

Replacements:

1 - 1 = 0

Since:

0 <= 1

valid.

answer = 1
right = 1

Substring:

"AA"

Frequency:

A → 2
length = 2
max_freq = 2

replacements = 2 - 2
             = 0

Valid.

answer = 2
right = 2

Substring:

"AAB"

Frequency:

A → 2
B → 1

Most frequent = 2

length = 3

replacements = 3 - 2
             = 1

Valid because:

1 <= k

So:

answer = 3

We can turn:

AAB

into:

AAA

with one replacement.

right = 3

Substring:

"AABA"

Frequency:

A → 3
B → 1

Therefore:

length = 4
max_freq = 3

replacements = 4 - 3
             = 1

Valid.

answer = 4

We can do:

A A B A
    ↓
A A A A

One replacement.

right = 4

Substring:

"AABAB"

Frequency:

A → 3
B → 2

Therefore:

length = 5
max_freq = 3

replacements = 5 - 3
             = 2

But:

k = 1

So:

2 > 1

❌ Invalid.

We cannot make all five characters equal using only one replacement.

right = 5

Substring:

"AABABB"

Frequency:

A → 3
B → 3
length = 6
max_freq = 3

replacements = 6 - 3
             = 3
3 > 1

❌ Invalid.

right = 6

Substring:

"AABABBA"

Frequency:

A → 4
B → 3
length = 7
max_freq = 4

replacements = 7 - 4
             = 3

❌ Invalid.

Then we repeat the same process for:

left = 1
left = 2
left = 3
...

Eventually we discover that no valid substring is longer than 4.

Therefore:

answer = 4
"""

#sliding window
def characterReplacement(s,k):
    ans=0
    left=0
    max_freq=0
    freq=Counter()
    for right in range(len(s)):
        freq[s[right]]+=1
        max_freq=max(max_freq,freq[s[right]])
        while (right-left+1)-max_freq>k:
            freq[s[left]]-=1
            left+=1
        ans=max(ans,right-left+1)
    return ans
print(characterReplacement(s = "AABABBA", k = 1))
    


#===explanation====
from collections import Counter

def characterReplacement(s, k):

    # Stores frequency of characters
    # inside our current window.
    freq = Counter()

    # Left boundary of the window
    left = 0

    # Frequency of the most common character
    # seen in the current/previous windows.
    max_freq = 0

    # Longest valid window found so far
    answer = 0

    # Move the right pointer through the string
    for right in range(len(s)):

        # Add the new character to our window
        freq[s[right]] += 1

        # Update the maximum frequency
        max_freq = max(max_freq, freq[s[right]])

        # Current window:
        # s[left ... right]
        #
        # Its length is:
        # right - left + 1
        #
        # Characters that need to be replaced:
        # window length - most frequent character count
        #
        # If this is greater than k,
        # we cannot make the entire window the same.
        while (right - left + 1) - max_freq > k:

            # Remove the leftmost character
            # because the window is invalid.
            freq[s[left]] -= 1

            # Move left pointer forward
            left += 1

        # The current window is valid.
        # Check whether it is the largest one so far.
        answer = max(answer, right - left + 1)

    return answer


"""
Detailed Dry Run of the Optimized Solution

Again:

s = "AABABBA"
k = 1

Start:

left = 0
max_freq = 0
answer = 0
Step 1 — right = 0

Character:

A

Window:

[A]
 ↑
left/right

Frequency:

A → 1
max_freq = 1

Window length:

0 - 0 + 1 = 1

Replacements:

1 - 1 = 0

Valid.

answer = 1
Step 2 — right = 1

Add:

A

Window:

[A A]
 ↑   ↑
 L   R

Frequency:

A → 2
max_freq = 2

Window length:

1 - 0 + 1 = 2

Replacements:

2 - 2 = 0

Valid.

answer = 2
Step 3 — right = 2

Add:

B

Window:

[A A B]
 ↑     ↑
 L     R

Frequency:

A → 2
B → 1

Maximum frequency:

max_freq = 2

Window length:

2 - 0 + 1 = 3

Replacements:

3 - 2 = 1

Since:

1 <= k

valid.

answer = 3

We can change:

A A B
    ↓
A A A
Step 4 — right = 3

Add A.

Window:

[A A B A]
 ↑       ↑
 L       R

Frequency:

A → 3
B → 1
max_freq = 3

Window length:

3 - 0 + 1 = 4

Replacements:

4 - 3 = 1

Valid.

answer = 4
Step 5 — right = 4

Add B.

Window:

[A A B A B]
 ↑         ↑
 L         R

Frequency:

A → 3
B → 2
max_freq = 3

Window length:

5

Replacements:

5 - 3 = 2

But:

k = 1

Therefore:

2 > 1

❌ Window is invalid.

So we execute:

freq[s[left]] -= 1
left += 1

Remove the first A.

Now:

    [A B A B]
     ↑     ↑
    left  right

Frequency:

A → 2
B → 2

The window is still technically evaluated using:

window length = 4
max_freq = 3

and this is an important implementation detail: max_freq is allowed to remain the historical maximum.

So:

4 - 3 = 1

The window is accepted.

"""