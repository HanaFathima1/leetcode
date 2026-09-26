"""

LC: 84. Largest Rectangle in Histogram

Hard

Topics
Array
Stack
Monotonic Stack
Range Minimum/Maximum Query

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4
 

Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
1,734,418/3.4M
Acceptance Rate
50.9%

"""

#https://leetcode.com/discuss/post/2347639/a-comprehensive-guide-and-template-for-m-irii/
"""
The key idea

For every bar, we want to know:

How far can this bar extend to the left and right while maintaining its height?"""


def largestRectangle(heights):
    maxarea=0
    for i in range(len(heights)):
        min_height=float('inf')
        for j in range(i,len(heights)):
            min_height=min(min_height,heights[j])
            width=j-i+1
            area=min_height*width
            maxarea=max(maxarea,area)
    return maxarea
print(largestRectangle(heights = [2,1,5,6,2,3]))


# OPTIMAL CODE

def largestRectangleArea(heights):

    stack = []      # stores indices
    max_area = 0

    # Add a 0 at the end.
    # This forces all remaining bars in the stack to be processed.
    heights.append(0)

    for i in range(len(heights)):

        # If current bar is smaller than the bar at stack top,
        # we found the right boundary of the taller bar.
        while stack and heights[i] < heights[stack[-1]]:

            height = heights[stack.pop()]

            # If stack is empty:
            # there is no smaller bar on the left.
            #
            # Otherwise, stack[-1] is the index of
            # the first smaller bar on the left.
            if stack:
                width = i - stack[-1] - 1
            else:
                width = i

            area = height * width

            max_area = max(max_area, area)

        stack.append(i)

    heights.pop()

    return max_area

# LeetCode 84 - Largest Rectangle in Histogram
#
# Goal:
# Given an array of bar heights, find the largest rectangle
# that can be formed using consecutive bars.
#
# Example:
# heights = [2, 1, 5, 6, 2, 3]
#
# Answer = 10
#
# The rectangle of height 5 can use bars:
#
#       5   6
#       █   █
#       █   █
#       █   █
#
#       width = 2
#       height = 5
#       area = 5 * 2 = 10
#
#
# Approach:
# We use a MONOTONIC INCREASING STACK.
#
# The stack stores INDICES, not heights.
#
# The heights corresponding to those indices will always be
# in increasing order.
#
# Example:
#
# heights = [2, 1, 5, 6, 2]
#
# Stack may contain:
#
# [1, 2, 3]
#
# heights:
#
# index 1 -> 1
# index 2 -> 5
# index 3 -> 6
#
# So the heights are:
#
# 1 < 5 < 6
#
#
# Why do we need the stack?
#
# For every bar, we want to know:
#
# 1. How far can this bar extend to the LEFT?
# 2. How far can this bar extend to the RIGHT?
#
# Once we know these two boundaries:
#
#       width = right boundary - left boundary - 1
#
# Then:
#
#       area = height * width


def largestRectangleArea(heights):

    # ---------------------------------------------------------
    # stack stores INDICES of bars.
    #
    # We store indices instead of heights because we need
    # the positions to calculate the WIDTH of the rectangle.
    #
    # Example:
    #
    # heights = [2, 1, 5, 6]
    #
    # stack = [1, 2, 3]
    #
    # means:
    #
    # index 1 -> height 1
    # index 2 -> height 5
    # index 3 -> height 6
    # ---------------------------------------------------------

    stack = []


    # ---------------------------------------------------------
    # This variable stores the largest rectangle found so far.
    #
    # Initially, we haven't found any rectangle.
    # ---------------------------------------------------------

    max_area = 0


    # ---------------------------------------------------------
    # IMPORTANT TRICK:
    #
    # Add a 0 at the end of the array.
    #
    # Why?
    #
    # Suppose:
    #
    # heights = [2, 1, 5, 6]
    #
    # At the end, the bars 5 and 6 may still be inside
    # the stack.
    #
    # We need something smaller than them to force them
    # out of the stack.
    #
    # Adding 0 does exactly that.
    #
    # heights becomes:
    #
    # [2, 1, 5, 6, 0]
    #
    # When we reach 0:
    #
    # 0 < 6
    #
    # so 6 gets popped.
    #
    # Then:
    #
    # 0 < 5
    #
    # so 5 gets popped.
    #
    # This allows us to calculate all remaining rectangles.
    # ---------------------------------------------------------

    heights.append(0)


    # ---------------------------------------------------------
    # Visit every bar from left to right.
    #
    # i = current index
    # heights[i] = current bar's height
    # ---------------------------------------------------------

    for i in range(len(heights)):


        # -----------------------------------------------------
        # We keep popping while:
        #
        # 1. Stack is not empty
        #
        # AND
        #
        # 2. Current bar is SMALLER than the bar at the
        #    top of the stack.
        #
        # Why?
        #
        # Suppose:
        #
        # heights = [5, 6, 2]
        #
        # Stack:
        #
        # [0, 1]
        #
        # heights:
        #
        # index 0 -> 5
        # index 1 -> 6
        #
        # Current height = 2
        #
        # We know:
        #
        # 2 < 6
        #
        # Therefore, the bar of height 6 CANNOT continue
        # to the right.
        #
        # So its maximum rectangle must end before index i.
        #
        # Therefore we pop it and calculate its area.
        # -----------------------------------------------------

        while stack and heights[i] < heights[stack[-1]]:


            # -------------------------------------------------
            # Remove the top index from the stack.
            #
            # Suppose:
            #
            # stack = [1, 2, 3]
            #
            # and:
            #
            # heights[3] = 6
            #
            # stack.pop() returns 3.
            #
            # So:
            #
            # index = 3
            # height = 6
            # -------------------------------------------------

            height = heights[stack.pop()]


            # -------------------------------------------------
            # Now we need to find the WIDTH of the rectangle.
            #
            # The current index i is the first smaller bar
            # on the RIGHT.
            #
            # The new stack top is the first smaller bar
            # on the LEFT.
            #
            # Example:
            #
            # heights = [1, 5, 6, 2]
            #
            # Suppose we just popped the bar 6.
            #
            # Current i = 3
            #
            # Stack after popping:
            #
            # [0, 1]
            #
            # stack[-1] = 1
            #
            # So:
            #
            # left smaller = index 1
            # right smaller = index 3
            #
            # The rectangle can occupy only:
            #
            # index 2
            #
            # Therefore:
            #
            # width = 3 - 1 - 1
            #       = 1
            #
            #
            # Why "-1"?
            #
            # Because the left and right smaller bars themselves
            # cannot be included in our rectangle.
            # -------------------------------------------------

            if stack:

                # There IS a smaller bar on the left.
                #
                # stack[-1] = index of that smaller bar
                #
                # i = index of smaller bar on the right
                #
                # Therefore:
                #
                # width = right - left - 1

                width = i - stack[-1] - 1


            else:

                # -------------------------------------------------
                # If stack is empty, there is NO smaller bar
                # on the left.
                #
                # Therefore, our rectangle can extend all the way
                # from index 0 to index i-1.
                #
                # Example:
                #
                # heights = [5, 6, 7, 2]
                #
                # When 2 arrives, all three bars can potentially
                # use the entire width from index 0 to index 2.
                #
                # width = i
                #
                # If i = 3:
                #
                # width = 3
                # -------------------------------------------------

                width = i


            # -------------------------------------------------
            # Now that we know:
            #
            # height
            # width
            #
            # we can calculate the rectangle's area.
            #
            # Formula:
            #
            # area = height × width
            # -------------------------------------------------

            area = height * width


            # -------------------------------------------------
            # Compare this rectangle with the largest rectangle
            # found so far.
            #
            # Example:
            #
            # max_area = 6
            # area = 10
            #
            # max_area becomes 10.
            # -------------------------------------------------

            max_area = max(max_area, area)


        # -----------------------------------------------------
        # After all taller bars have been removed, push the
        # current index into the stack.
        #
        # Why is it safe to push?
        #
        # Because after the while loop finishes:
        #
        # heights[i] >= heights[stack[-1]]
        #
        # Therefore, the stack remains monotonically increasing.
        #
        # Example:
        #
        # heights = [2, 1, 5, 6]
        #
        # stack might become:
        #
        # [1, 2, 3]
        #
        # corresponding heights:
        #
        # [1, 5, 6]
        #
        # which is increasing.
        # -----------------------------------------------------

        stack.append(i)


    # ---------------------------------------------------------
    # We added an artificial 0 to the original array.
    #
    # Remove it so that the input array is restored.
    # ---------------------------------------------------------

    heights.pop()


    # ---------------------------------------------------------
    # Return the largest rectangle found.
    # ---------------------------------------------------------

    return max_area



            
"""
Full Dry Run

Let's dry-run:

[2,1,5,6,2,3]

We first add 0:

[2,1,5,6,2,3,0]

The final 0 is a trick to force the remaining stack elements to be processed.

i = 0

Current:

height = 2

Stack is empty.

So:

stack.append(0)

Stack:

[0]

Heights:

[2]
i = 1

Current:

height = 1

Top of stack:

heights[0] = 2

Since:

1 < 2

we pop 0.

height = 2

Stack becomes:

[]

Since stack is empty:

width = i

Therefore:

width = 1

Area:

2 × 1 = 2

So:

max_area = 2

Now push index 1.

stack = [1]
i = 2

Current:

height = 5

Top:

heights[1] = 1

Since:

5 > 1

nothing is popped.

Push 2.

stack = [1,2]
i = 3

Current:

height = 6

Top:

height = 5

Since:

6 > 5

push 3.

stack = [1,2,3]
i = 4

Current:

height = 2

Stack:

[1,2,3]

Heights:

index 1 → 1
index 2 → 5
index 3 → 6

Current height:

2
First pop

Top is 6.

2 < 6

Pop index 3.

height = 6

Stack:

[1,2]

Width:

width = i - stack[-1] - 1

Therefore:

width = 4 - 2 - 1
      = 1

Area:

6 × 1 = 6

Maximum remains:

max_area = 6
Second pop

Now top is 5.

2 < 5

Pop index 2.

height = 5

Stack:

[1]

Width:

width = 4 - 1 - 1
      = 2

So:

area = 5 × 2
     = 10

Update:

max_area = 10

This is our answer candidate.

Now:

2 > 1

So stop popping.

Push 4.

stack = [1,4]
i = 5

Current:

height = 3

Top:

heights[4] = 2

Since:

3 > 2

push 5.

stack = [1,4,5]
i = 6

This is the artificial 0.

height = 0

Now we pop everything that is taller.

First:

3 > 0

Pop index 5.

height = 3

Stack:

[1,4]

Width:

6 - 4 - 1 = 1

Area:

3 × 1 = 3

Next:

2 > 0

Pop index 4.

height = 2

Stack:

[1]

Width:

6 - 1 - 1
= 4

Area:

2 × 4
= 8

Finally:

1 > 0

Pop index 1.

height = 1

Stack becomes empty.

Therefore:

width = i
      = 6

Area:

1 × 6
= 6

No improvement.

Final:

max_area = 10
8. Dry-run table
| i | Current height | Stack after processing |           Area calculated |    max |
| - | -------------: | ---------------------- | ------------------------: | -----: |
| 0 |              2 | `[0]`                  |                         — |      0 |
| 1 |              1 | `[1]`                  |                   `2×1=2` |      2 |
| 2 |              5 | `[1,2]`                |                         — |      2 |
| 3 |              6 | `[1,2,3]`              |                         — |      2 |
| 4 |              2 | `[1,4]`                |         `6×1=6`, `5×2=10` | **10** |
| 5 |              3 | `[1,4,5]`              |                         — |     10 |
| 6 |              0 | `[]`                   | `3×1=3`, `2×4=8`, `1×6=6` | **10** |


Answer:

10
"""