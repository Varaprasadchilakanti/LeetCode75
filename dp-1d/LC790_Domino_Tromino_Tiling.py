"""
790. Domino and Tromino Tiling

You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.
Given an integer n, return the number of ways to tile an 2 x n board.
Since the answer may be very large, return it modulo 10**9 + 7.
In a tiling, every square must be covered by a tile.
Two tilings are different if and only if there are two 4-directionally adjacent cells on the board
such that exactly one of the tilings has both squares occupied by a tile.

Example 1:
Input: n = 3
Output: 5
Explanation: The five different ways are shown above.

Example 2:
Input: n = 1
Output: 1

Constraints:
1 <= n <= 1000

Topics
Dynamic Programming
Weekly Contest 73


Developer Insights
Problem Nature
We must count the number of ways to tile a 2×n board using:
Dominoes: 2×1 tiles (vertical or horizontal).
Trominoes: L-shaped tiles covering 3 squares (rotatable).
This is a DP-1D combinatorics problem with recurrence relations.

Key Observations
Let dp[n] be the number of ways to tile a 2×n board.
Base cases:
dp[0] = 1 (empty board)
dp[1] = 1 (one vertical domino)
dp[2] = 2 (two vertical or two horizontal dominoes)

Recurrence:
𝑑𝑝[𝑛]=𝑑𝑝[𝑛−1]+𝑑𝑝[𝑛−2]+2⋅(𝑖=0)∑(𝑛−3)𝑑𝑝[𝑖]

Optimized recurrence:
𝑑𝑝[𝑛]=2⋅𝑑𝑝[𝑛−1]+𝑑𝑝[𝑛−3]
This avoids recomputing the sum.

Strategy
Initialize base cases for dp[0], dp[1], dp[2].
Use iterative DP to compute up to dp[n].
Apply modulo 10**9+7 at each step.

Return dp[n].

Complexity
Time: O(n)
Space: O(n) or O(1) with rolling variables

Edge Cases
n = 1 → return 1
n = 2 → return 2
Large n → modulo arithmetic ensures safety

Pseudocode
function numTilings(n):
    if n == 0: return 1
    if n == 1: return 1
    if n == 2: return 2

    dp = [0] * (n + 1)
    dp[0], dp[1], dp[2] = 1, 1, 2

    for i in range(3, n + 1):
        dp[i] = (2 * dp[i - 1] + dp[i - 3]) % MOD

    return dp[n]

"""

from typing import Protocol


MOD = 10**9 + 7


# ───────────────────────────────────────────────────────────────────────────
# Strategy Interface
# ───────────────────────────────────────────────────────────────────────────

class TilingStrategy(Protocol):
    """
    Protocol defining the interface for tiling strategies.
    """
    def solve(self, n: int) -> int: ...


# ───────────────────────────────────────────────────────────────────────────
# Iterative DP Strategy
# ───────────────────────────────────────────────────────────────────────────

class IterativeDPTilingStrategy:
    """
    Iterative DP strategy for counting tilings of a 2×n board using dominoes and trominoes.

    Design:
        - Base cases: dp[0]=1, dp[1]=1, dp[2]=2
        - Recurrence: dp[n] = 2*dp[n-1] + dp[n-3]
        - Modulo arithmetic for large values

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def solve(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2

        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2] = 1, 1, 2

        for i in range(3, n + 1):
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % MOD

        return dp[n]


# ───────────────────────────────────────────────────────────────────────────
# Orchestrator — Clean Architecture
# ───────────────────────────────────────────────────────────────────────────

class Solution:
    """
    Orchestrates tiling computation by delegating to a strategy.

    - Separation of concerns: orchestration vs. computation
    - Dependency injection: strategy is swappable
    - Defaults to Iterative DP strategy
    """

    def __init__(self, strategy: TilingStrategy = None) -> None:
        self.strategy = strategy if strategy is not None else IterativeDPTilingStrategy()

    def numTilings(self, n: int) -> int:
        """
        Entry point for LeetCode.

        Args:
            n (int): Width of the 2×n board.

        Returns:
            int: Number of valid tilings modulo 10^9 + 7.
        """
        return self.strategy.solve(n)


# ───────────────────────────────────────────────────────────────────────────
# Usage Suite
# ───────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    solution = Solution()

    print(solution.numTilings(1))   # Expected: 1
    print(solution.numTilings(2))   # Expected: 2
    print(solution.numTilings(3))   # Expected: 5
    print(solution.numTilings(4))   # Expected: 11
    print(solution.numTilings(1000))  # Stress test
