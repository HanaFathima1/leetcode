"""

LC: 274. H-Index

Medium

Topics
Array
Sorting
Counting Sort

Hint
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.


Example 1:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
Example 2:

Input: citations = [1,3,1]
Output: 1
 

Constraints:

n == citations.length
1 <= n <= 5000
0 <= citations[i] <= 1000
 

Seen this question in a real interview before?
1/6
Yes
No
Accepted
884,767/2.1M
Acceptance Rate
41.5%

Hint 1
An easy approach is to sort the array first.
Hint 2
What are the possible values of h-index?
Hint 3
A faster approach is to use extra space.

"""

class Solution:
    def hIndex(self, citations:list[int]) -> int:
        h = 0
        citations.sort(reverse = True)
        for i in range(len(citations)):
            if citations[i] >= i+1:
                h = i+1
            else:
                break
        return h
sol = Solution()
print(sol.hIndex(citations = [3,0,6,1,5]))
print(sol.hIndex(citations = [1,3,1]))


"""

============EXPLANATION=============
This is the sentence I always remember during interviews:

"Find the largest h such that at least h papers have h or more citations."

###H-Index Problem (Easy Description)

Imagine you are a researcher and you have written several papers.

The array:

citations = [3, 0, 6, 1, 5]

means:

Paper 1 got 3 citations
Paper 2 got 0 citations
Paper 3 got 6 citations
Paper 4 got 1 citation
Paper 5 got 5 citations
What is the question asking?

Find the largest number h such that:

You have at least h papers and each of those papers has at least h citations.

Example
citations = [3, 0, 6, 1, 5]

Can we have:

h = 1 ?

Do we have at least 1 paper with at least 1 citation?

✅ Yes

h = 2 ?

Do we have at least 2 papers with at least 2 citations?

Papers with ≥ 2 citations:

3, 6, 5

There are 3 papers.

✅ Yes

h = 3 ?

Do we have at least 3 papers with at least 3 citations?

Papers with ≥ 3 citations:

3, 6, 5

There are 3 papers.

✅ Yes

h = 4 ?

Do we have at least 4 papers with at least 4 citations?

Papers with ≥ 4 citations:

6, 5

Only 2 papers.

❌ No

Since 4 is not possible, the largest valid value is:

h = 3

Answer:

3
Another Example
citations = [10, 8, 5, 4, 3]

Can we have:

1 paper with ≥1 citations? ✅
2 papers with ≥2 citations? ✅
3 papers with ≥3 citations? ✅
4 papers with ≥4 citations? ✅
5 papers with ≥5 citations? ❌ (the last paper has only 3 citations)

So:

h = 4
The Key Idea

The question is simply asking:

"What is the maximum number of papers that have at least that same number of citations?"

"""
"""

===========DRY RUN===========
Dry Run

Input:

citations = [3,0,6,1,5]

After sorting:

[6,5,3,1,0]
Iteration 1
i = 0

6 >= 1
h = 1
Iteration 2
i = 1

5 >= 2
h = 2
Iteration 3
i = 2

3 >= 3
h = 3
Iteration 4
i = 3

1 >= 4

False.

Break.

Return:

3

"""