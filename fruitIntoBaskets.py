"""

LC: 904. Fruit Into Baskets

Medium

Topics
Staff
Array
Hash Table
Sliding Window
Weekly Contest 102

You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.

 

Example 1:

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.
Example 2:

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].
Example 3:

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].
 

Constraints:

1 <= fruits.length <= 105
0 <= fruits[i] < fruits.length
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
968,231/1.8M
Acceptance Rate
52.5%

"""

"""
#explanation of question
Each basket can contain only one type of fruit, so having two baskets means my subarray can contain at most two distinct fruit types. I use a sliding window with two pointers. I expand the right pointer and maintain the frequency of each fruit using a dictionary. If the window contains more than two distinct fruits, I move the left pointer and decrease the corresponding frequencies until only two types remain. Whenever the window is valid, I update the maximum window length.

Understand the problem

Suppose:

fruits = [1, 2, 1, 2, 3, 2, 2]

You have 2 baskets.

Each basket can hold only one type of fruit.

So you can have at most 2 different fruit types in your chosen contiguous section.

For example:

[1, 2, 1, 2]

There are only 2 types:

1
2

✅ Valid.

But:

[1, 2, 1, 2, 3]

has:

1
2
3

That's 3 different types.

❌ Invalid.

So the actual problem becomes:

Find the longest contiguous subarray containing at most 2 distinct values.

That's the entire problem.
"""

#brute force
def fruitIntoBaskets(fruits):
    max_len=0
    for i in range(len(fruits)):
        fruit_types=set()
        for j in range(i,len(fruits)):
            fruit_types.add(fruits[j])
            if len(fruit_types)>2:
                break
            window_len=j-i+1
            max_len=max(max_len,window_len)
    return max_len
print(fruitIntoBaskets(fruits = [0,1,2,2]))

#explanation
def totalFruit(fruits):

    max_len = 0

    # Try every possible starting position
    for i in range(len(fruits)):

        # Store the different fruit types
        fruit_types = set()

        # Extend the subarray from i to the right
        for j in range(i, len(fruits)):

            # Add the current fruit
            fruit_types.add(fruits[j])

            # If we have more than 2 types,
            # this subarray is invalid
            if len(fruit_types) > 2:
                break

            # Current subarray is valid
            window_len = j - i + 1

            # Update maximum length
            max_len = max(max_len, window_len)

    return max_len

#dry run
"""
🧪 Dry run

Take:

fruits = [1, 2, 1, 2, 3, 2, 2]
i = 0

Start:

[1]

Types:

{1}

Length:

1

Next:

[1, 2]

Types:

{1, 2}

Length:

2

Next:

[1, 2, 1]

Types:

{1, 2}

Length:

3

Next:

[1, 2, 1, 2]

Types:

{1, 2}

Length:

4

Next:

[1, 2, 1, 2, 3]

Types:

{1, 2, 3}

We have 3 types.

❌ Invalid.

So stop this j loop.

Current:

max_len = 4
i = 1

Start from index 1:

[2]

Then:

[2,1]

Then:

[2,1,2]

Then:

[2,1,2,3]

Now:

{1,2,3}

3 types → ❌ stop.

Maximum remains:

4
i = 2

Start:

[1]

Then:

[1,2]
[1,2,3]

At [1,2,3]:

3 different types

❌ stop.

i = 3

Start:

[2]
[2,3]
[2,3,2]
[2,3,2,2]

Types:

{2,3}

Length:

4

So:

max_len = 4
i = 4
[3]
[3,2]
[3,2,2]

Length:

3
i = 5
[2]
[2,2]

Length:

2
i = 6
[2]

Length:

1

Final:

max_len = 4
🎯 Answer
4

One valid longest subarray is:

[1, 2, 1, 2]

Another is:

[2, 3, 2, 2]

Both contain exactly 2 fruit types.
"""

#sliding window
class Solution:
    def totalFruit(self, fruits: list[int]) -> int:

        left = 0

        # Dictionary to store the frequency
        # of each fruit type in the current window
        fruit_count = {}

        # Store the longest valid window
        max_len = 0

        for right in range(len(fruits)):

            # Add the fruit entering from the right
            fruit = fruits[right]

            if fruit not in fruit_count:
                fruit_count[fruit] = 0

            fruit_count[fruit] += 1

            # If we have more than 2 fruit types,
            # shrink the window from the left
            while len(fruit_count) > 2:

                left_fruit = fruits[left]

                fruit_count[left_fruit] -= 1

                # If no more of this fruit exists
                # in the window, remove its key
                if fruit_count[left_fruit] == 0:
                    del fruit_count[left_fruit]

                left += 1

            # Current window contains at most 2 types
            window_len = right - left + 1

            max_len = max(max_len, window_len)

        return max_len
"""
🧪 7. Dry run

Take:

fruits = [1, 2, 1, 2, 3, 2, 2]

We want the longest window with ≤ 2 types.

Initially:

left = 0
fruit_count = {}
max_len = 0
right = 0

Fruit:

1

Dictionary:

{1: 1}

Types:

1

Valid.

Window:

[1]

Length:

1
max_len = 1
right = 1

Add 2:

{1: 1, 2: 1}

Types:

2

Valid.

Window:

[1, 2]

Length:

2
max_len = 2
right = 2

Add 1:

{1: 2, 2: 1}

Still 2 types.

Window:

[1,2,1]

Length:

3
max_len = 3
right = 3

Add 2:

{1: 2, 2: 2}

Still 2 types.

Window:

[1,2,1,2]

Length:

4
max_len = 4
🔴 right = 4

Add 3:

{1: 2, 2: 2, 3: 1}

Now:

3 different types

But we only have 2 baskets.

So:

while len(fruit_count) > 2:
Remove fruits[left]

left = 0

fruits[0] = 1

Decrease:

{1: 1, 2: 2, 3: 1}

Still 3 types.

Move:

left = 1
Remove fruits[1]
fruits[1] = 2

Decrease:

{1: 1, 2: 1, 3: 1}

Still 3 types.

Move:

left = 2
Remove fruits[2]
fruits[2] = 1

Frequency becomes zero:

{2: 1, 3: 1}

Delete 1.

Now:

2 types

✅ Valid.

Current window:

[2,3]

Length:

2

max_len remains:

4
🟢 right = 5

Add 2:

{2: 2, 3: 1}

Two types.

Window:

[2,3,2]

Length:

3

max_len = 4

🟢 right = 6

Add 2:

{2: 3, 3: 1}

Two types.

Window:

[2,3,2,2]

Length:

4

max_len = 4

Final answer:

4
📊 Dry-run table

| `right` | Fruit | Dictionary  | `left` | Window                             | Length | `max_len` |
| ------: | ----: | ----------- | -----: | ---------------------------------- | -----: | --------: |
|       0 |     1 | `{1:1}`     |      0 | `[1]`                              |      1 |         1 |
|       1 |     2 | `{1:1,2:1}` |      0 | `[1,2]`                            |      2 |         2 |
|       2 |     1 | `{1:2,2:1}` |      0 | `[1,2,1]`                          |      3 |         3 |
|       3 |     2 | `{1:2,2:2}` |      0 | `[1,2,1,2]`                        |      4 |         4 |
|       4 |     3 | `{2:2,3:1}` |      2 | `[1,2,3]` → after shrinking `[1?]` |      2 |         4 |
|       5 |     2 | `{2:2,3:1}` |      2 | `[1,2,3,2]`                        |      3 |         4 |
|       6 |     2 | `{2:3,3:1}` |      2 | `[1,2,3,2,2]`                      |      4 |         4 |

"""