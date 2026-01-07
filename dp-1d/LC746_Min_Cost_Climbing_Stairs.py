"""
746. Min Cost Climbing Stairs

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.


Example 1:
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

Example 2:
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.

Constraints:
2 <= cost.length <= 1000
0 <= cost[i] <= 999

Topics
Array
Dynamic Programming
Weekly Contest 63

Hint 1
Build an array dp where dp[i] is the minimum cost to climb to the top starting from the ith staircase.
Hint 2
Assuming we have n staircase labeled from 0 to n - 1 and assuming the top is n, then dp[n] = 0, marking that if you are at the top, the cost is 0.
Hint 3
Now, looping from n - 1 to 0, the dp[i] = cost[i] + min(dp[i + 1], dp[i + 2]). The answer will be the minimum of dp[0] and dp[1]


Developer Insights
Problem Nature
We must compute the minimum cost to reach the top of the staircase:
At each step i, you pay cost[i].
You can climb either 1 or 2 steps.
You can start at step 0 or step 1.
This is a DP‑1D problem: the state depends on the minimum cost to reach each step.

Key Observations
Define dp[i] as the minimum cost to reach step i.
Transition: dp[i] = cost[i] + min(dp[i-1], dp[i-2]).
Answer: min(dp[n-1], dp[n-2]) where n = len(cost).
Space optimization: only last two states are needed.

Strategy
Handle base cases: dp[0] = cost[0], dp[1] = cost[1].
Iteratively compute dp[i] for i ≥ 2.
Return min(dp[n-1], dp[n-2]).
Optimize space with rolling variables.

Complexity
Time: O(n)
Space: O(1) (rolling variables)

Edge Cases
cost = [10, 15] → answer = min(10, 15).
Large n (up to 1000) → efficient with O(n).
Costs with zeros → algorithm handles naturally.

Pseudocode
function minCostClimbingStairs(cost):
    n = len(cost)
    if n == 2:
        return min(cost[0], cost[1])

    prev2 = cost[0]
    prev1 = cost[1]

    for i in range(2, n):
        curr = cost[i] + min(prev1, prev2)
        prev2, prev1 = prev1, curr

    return min(prev1, prev2)


"""

from typing import List, Protocol


# ───────────────────────────────────────────────────────────────────────────
# Strategy Interface
# ───────────────────────────────────────────────────────────────────────────

class MinCostStrategy(Protocol):
    """
    Protocol defining the interface for minimum cost climbing stairs strategies.
    """
    def solve(self, cost: List[int]) -> int: ...


# ───────────────────────────────────────────────────────────────────────────
# Iterative DP Strategy
# ───────────────────────────────────────────────────────────────────────────

class IterativeDPMinCostStrategy:
    """
    Iterative DP strategy for computing minimum cost to climb stairs.

    Design:
        - Base cases: dp[0] = cost[0], dp[1] = cost[1]
        - Transition: dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        - Answer: min(dp[n-1], dp[n-2])
        - Space optimized to O(1) using rolling variables.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def solve(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 2:
            return min(cost[0], cost[1])

        prev2, prev1 = cost[0], cost[1]
        for i in range(2, n):
            curr = cost[i] + min(prev1, prev2)
            prev2, prev1 = prev1, curr

        return min(prev1, prev2)


# ───────────────────────────────────────────────────────────────────────────
# Orchestrator — Clean Architecture
# ───────────────────────────────────────────────────────────────────────────

class Solution:
    """
    Orchestrates minimum cost climbing stairs computation by delegating to a strategy.

    - Separation of concerns: orchestration vs. computation
    - Dependency injection: strategy is swappable
    - Defaults to Iterative DP strategy
    """

    def __init__(self, strategy: MinCostStrategy = None) -> None:
        self.strategy = strategy if strategy is not None else IterativeDPMinCostStrategy()

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Entry point for LeetCode.

        Args:
            cost (List[int]): Cost of each step.

        Returns:
            int: Minimum cost to reach the top.
        """
        return self.strategy.solve(cost)


# ───────────────────────────────────────────────────────────────────────────
# Usage Suite
# ───────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    solution = Solution()

    print(solution.minCostClimbingStairs([10, 15, 20]))          # Expected: 15
    print(solution.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))  # Expected: 6
    print(solution.minCostClimbingStairs([10, 15]))              # Expected: 10
    print(solution.minCostClimbingStairs([0, 0, 0, 0]))          # Expected: 0
