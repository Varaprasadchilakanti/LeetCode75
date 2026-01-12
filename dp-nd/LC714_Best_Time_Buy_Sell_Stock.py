"""
714. Best Time to Buy and Sell Stock with Transaction Fee

You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.
Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.
Note:
You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
The transaction fee is only charged once for each stock purchase and sale.

Example 1:
Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

Example 2:
Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6

Constraints:
1 <= prices.length <= 5 * 104
1 <= prices[i] < 5 * 104
0 <= fee < 5 * 104

Topics
Array
Dynamic Programming
Greedy

Hint 1
Consider the first K stock prices. At the end, the only legal states are that you don't own a share of stock, or that you do. Calculate the most profit you could have under each of these two cases.


Developer Insights
Problem Nature
We must maximize profit with unlimited transactions, but each transaction incurs a fee:
Constraint: cannot hold multiple stocks simultaneously.
States:
Hold: maximum profit when holding a stock.
Cash: maximum profit when not holding a stock.
This is a DP‑multidimensional problem: state depends on day index and whether we hold a stock.

Key Observations
Define:
cash[i]: max profit on day i when not holding stock.
hold[i]: max profit on day i when holding stock.
Transitions:
cash[i] = max(cash[i-1], hold[i-1] + prices[i] - fee)
hold[i] = max(hold[i-1], cash[i-1] - prices[i])
Base cases:
cash[0] = 0
hold[0] = -prices[0]
Answer: cash[n-1].

Strategy
Initialize base states.
Iteratively update cash and hold.
Return final cash.
Optimize space: only last day’s states are needed.

Complexity
Time: O(n)
Space: O(1) (rolling variables)

Edge Cases
Single day → profit = 0 (cannot sell).
Fee ≥ price differences → profit = 0.
Large arrays (length ≤ 50,000) → efficient with O(n).


Pseudocode
function maxProfit(prices, fee):
    cash = 0
    hold = -prices[0]

    for i in range(1, len(prices)):
        cash = max(cash, hold + prices[i] - fee)
        hold = max(hold, cash - prices[i])

    return cash

"""

from typing import List, Protocol


# ───────────────────────────────────────────────────────────────────────────
# Strategy Interface
# ───────────────────────────────────────────────────────────────────────────

class StockProfitStrategy(Protocol):
    """
    Protocol defining the interface for stock profit strategies.
    """
    def solve(self, prices: List[int], fee: int) -> int: ...


# ───────────────────────────────────────────────────────────────────────────
# DP Strategy
# ───────────────────────────────────────────────────────────────────────────

class DPSingleFeeStockProfitStrategy:
    """
    Dynamic Programming strategy for maximizing profit with transaction fee.

    Design:
        - States:
            cash[i]: max profit on day i without stock
            hold[i]: max profit on day i with stock
        - Transitions:
            cash[i] = max(cash[i-1], hold[i-1] + prices[i] - fee)
            hold[i] = max(hold[i-1], cash[i-1] - prices[i])
        - Base cases:
            cash[0] = 0
            hold[0] = -prices[0]
        - Result: cash[n-1]

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def solve(self, prices: List[int], fee: int) -> int:
        cash, hold = 0, -prices[0]
        for price in prices[1:]:
            cash = max(cash, hold + price - fee)
            hold = max(hold, cash - price)
        return cash


# ───────────────────────────────────────────────────────────────────────────
# Orchestrator — Clean Architecture
# ───────────────────────────────────────────────────────────────────────────

class Solution:
    """
    Orchestrates stock profit computation by delegating to a strategy.

    - Separation of concerns: orchestration vs. computation
    - Dependency injection: strategy is swappable
    - Defaults to DP strategy
    """

    def __init__(self, strategy: StockProfitStrategy = None) -> None:
        self.strategy = strategy if strategy is not None else DPSingleFeeStockProfitStrategy()

    def maxProfit(self, prices: List[int], fee: int) -> int:
        """
        Entry point for LeetCode.

        Args:
            prices (List[int]): Stock prices by day.
            fee (int): Transaction fee.

        Returns:
            int: Maximum profit achievable.
        """
        return self.strategy.solve(prices, fee)


# ───────────────────────────────────────────────────────────────────────────
# Usage Suite
# ───────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    solution = Solution()

    print(solution.maxProfit([1, 3, 2, 8, 4, 9], 2))   # Expected: 8
    print(solution.maxProfit([1, 3, 7, 5, 10, 3], 3))  # Expected: 6
    print(solution.maxProfit([5], 2))                  # Expected: 0
    print(solution.maxProfit([1, 2, 3, 4, 5], 10))     # Expected: 0
