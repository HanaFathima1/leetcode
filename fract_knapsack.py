# What is the Knapsack Problem?
# Imagine you are a thief breaking into a store with a knapsack (bag) that can hold a maximum weight capacity.
# There are several items in the store, each with:

# a weight

# and a value

# You have to choose a set of items to carry in your bag so that:

# The total weight doesn’t exceed the bag’s capacity.

# The total value you carry is maximized.

# Fractional Knapsack Problem
# You can take fractional parts of items.

# Example: If an item weighs 10kg, you can take 3kg of it.




class Item:
    def __init__(self,value,weight):
        self.value=value
        self.weight=weight
def fractional_knapsack(W,items):
    items.sort(key=lambda x : x.value/x.weight, reverse=True)
    
    total_value = 0.0
    for item in items:
        if item.weight<=W:
            W-=item.weight
            total_value+=item.value
        else:
            total_value+=item.value*(W/item.weight)
            break
    return total_value
items = [Item(60, 10), Item(100, 20), Item(120, 30)]
W = 50

print("Maximum value in Fractional Knapsack =", fractional_knapsack(W, items))



