"""

GFG: Fractional Knapsack

Difficulty: Medium
Accuracy: 32.46%
Submissions: 381K+
Points: 4
Average Time: 20m

Given two arrays, val[] and wt[] , representing the values and weights of items, and an integer capacity representing the maximum weight a knapsack can hold, determine the maximum total value that can be achieved by putting items in the knapsack. You are allowed to break items into fractions if necessary.
Return the maximum value as a double, rounded to 6 decimal places.

Examples :

Input: val[] = [60, 100, 120], wt[] = [10, 20, 30], capacity = 50
Output: 240.000000
Explanation: By taking items of weight 10 and 20 kg and 2/3 fraction of 30 kg. Hence total price will be 60+100+(2/3)(120) = 240
Input: val[] = [500], wt[] = [30], capacity = 10
Output: 166.670000
Explanation: Since the item’s weight exceeds capacity, we take a fraction 10/30 of it, yielding value 166.670000.
Constraints:
1 ≤ val.size = wt.size ≤ 105
1 ≤ capacity ≤ 109
1 ≤ val[i], wt[i] ≤ 104

Expected Complexities
Time Complexity: O(n log n)
Auxiliary Space: O(n)

Company Tags
Microsoft

Topic Tags
GreedyAlgorithms

"""

def fractionalKnapsack(values,weights,capacity):
    items=[]
    for i in range(len(values)):
        ratio=values[i]/weights[i]
        items.append((ratio,values[i],weights[i]))
    items.sort(reverse=True)
    total_value=0
    for ratio,value,weight in items:
        if capacity>=weight: #Does the bag have enough space for full item?
            total_value+=value
            capacity-=weight #We placed the whole item into the bag.
        else: #We cannot take full item.
            total_value+=value*(capacity/weight) #We take only the portion that fits.
            break
    return total_value
result=fractionalKnapsack(values = [60, 100, 120], weights = [10, 20, 30], capacity = 50)
print(round(result,6))