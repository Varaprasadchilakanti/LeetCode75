#!/usr/bin/env python3
"""
901. Online Stock Span

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

Topics
Stack
Design
Monotonic Stack
Data Stream
Weekly Contest 101

Developer Insights
Problem Nature
We must design a class that processes a stream of stock prices and returns the span (consecutive days backward where price ≤ today’s price).
This is a Monotonic Stack problem: we maintain a decreasing stack of prices with their spans.

Key Observations
Each day’s span depends on consecutive previous days with prices ≤ today’s price.
Naïve approach: scan backward → O(n) per query. Too slow for 10^4 calls.
Optimized approach:
Maintain stack of (price, span) in decreasing order.
When new price arrives:
Pop while stack top price ≤ current price.
Accumulate spans.
Push (price, span) back.
Each price is pushed/popped once → amortized O(1) per query.

Strategy
Initialize empty stack.
For each next(price):
Set span = 1.
While stack not empty and stack.top.price  ≤ price:
Pop and add popped span to current span.
Push (price, span).
Return span.

Complexity
Time: Amortized O(1) per query.
Space: O(n) for stack.

Edge Cases
First price → span = 1.
Strictly decreasing prices → span always = 1.
Strictly increasing prices → span grows cumulatively.
Large price values (≤ 10^5) handled efficiently.

Pseudocode
class StockSpanner:
    stack = []

    next(price):
        span = 1
        while stack not empty and stack.top.price <= price:
            span += stack.pop().span
        stack.push((price, span))
        return span

"""

from typing import List, Tuple


class StockSpanner:
    """
    Online Stock Span using Monotonic Stack.

    Design:
        - Maintain stack of (price, span).
        - For each new price:
            - Initialize span = 1.
            - Pop while stack top price <= current price, accumulate spans.
            - Push (price, span).
            - Return span.

    Time Complexity: Amortized O(1) per query.
    Space Complexity: O(n).
    """

    def __init__(self) -> None:
        # Stack stores tuples of (price, span)
        self.stack: List[Tuple[int, int]] = []

    def next(self, price: int) -> int:
        """
        Process today's price and return its span.

        Args:
            price (int): Today's stock price.

        Returns:
            int: Span of today's price.
        """
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            _, prev_span = self.stack.pop()
            span += prev_span
        self.stack.append((price, span))
        return span


# ───────────────────────────────────────────────────────────────────────────
# Usage Suite
# ───────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    stockSpanner = StockSpanner()
    print(stockSpanner.next(100))  # Expected: 1
    print(stockSpanner.next(80))   # Expected: 1
    print(stockSpanner.next(60))   # Expected: 1
    print(stockSpanner.next(70))   # Expected: 2
    print(stockSpanner.next(60))   # Expected: 1
    print(stockSpanner.next(75))   # Expected: 4
    print(stockSpanner.next(85))   # Expected: 6

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
