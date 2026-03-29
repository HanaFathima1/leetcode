"""

LC: 901. Online Stock Span

Medium

Topics
Stack
Design
Monotonic Stack
Data Stream
Weekly Contest 101

Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

The span of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward) for which the stock price was less than or equal to the price of that day.

For example, if the prices of the stock in the last four days is [7,2,1,2] and the price of the stock today is 2, then the span of today is 4 because starting from today, the price of the stock was less than or equal 2 for 4 consecutive days.
Also, if the prices of the stock in the last four days is [7,34,1,2] and the price of the stock today is 8, then the span of today is 3 because starting from today, the price of the stock was less than or equal 8 for 3 consecutive days.
Implement the StockSpanner class:

StockSpanner() Initializes the object of the class.
int next(int price) Returns the span of the stock's price given that today's price is price.
 

Example 1:

Input
["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
[[], [100], [80], [60], [70], [60], [75], [85]]
Output
[null, 1, 1, 1, 2, 1, 4, 6]

Explanation
StockSpanner stockSpanner = new StockSpanner();
stockSpanner.next(100); // return 1
stockSpanner.next(80);  // return 1
stockSpanner.next(60);  // return 1
stockSpanner.next(70);  // return 2
stockSpanner.next(60);  // return 1
stockSpanner.next(75);  // return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
stockSpanner.next(85);  // return 6
 

Constraints:

1 <= price <= 105
At most 104 calls will be made to next.
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
538,268/787.4K
Acceptance Rate
68.4%

"""

class StockSpanner:
    def __init__(self):
        self.stack=[]
    def next(self,price:int)->int:
        span=1
        while self.stack and self.stack[-1][0]<=price:
            prev_price,prev_span=self.stack.pop()
            span+=prev_span
        self.stack.append([price,span])
        return span
sp = StockSpanner()
print(sp.next(100))  # 1
print(sp.next(80))   # 1
print(sp.next(60))   # 1
print(sp.next(70))   # 2
print(sp.next(60))   # 1
print(sp.next(75))   # 4
print(sp.next(85))   # 6
        
        
"""

How this works (in simple terms)

We keep a monotonic decreasing stack of [price, span].

For each price:

Start span = 1 (today itself).

While the top of the stack has price <= current price, pop it and add its span to current span.

Because if today’s price is higher (or equal), those previous days are all included in today’s span.

Push [price, span] back to the stack.

Return span.

Tiny dry run

For prices: 100, 80, 60, 70, 60, 75, 85

100 → span = 1 → stack = [[100, 1]]

80 → 80 < 100, so no pop → span = 1 → stack = [[100,1],[80,1]]

60 → 60 < 80, so no pop → span = 1 → stack = [[100,1],[80,1],[60,1]]

70 → pop [60,1] (60 <= 70), span=1+1=2 → stop (80>70) → push [70,2]

60 → 60 < 70 → span=1 → push [60,1]

75 → pop [60,1], span=2 → pop [70,2], span=4 → stop (80>75) → push [75,4]

85 → pop [75,4], span=5 → pop [80,1], span=6 → pop [100,1]? no (100>85) so stop → push [85,6]

Spans = [1, 1, 1, 2, 1, 4, 6].

"""