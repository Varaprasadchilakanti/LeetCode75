"""
62. Unique Paths

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
The robot can only move either down or right at any point in time.
Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
The test cases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Constraints:
1 <= m, n <= 100

Topics
Math
Dynamic Programming
Combinatorics


Developer Insights
Problem Nature
We must compute the number of unique paths from the top‑left to the bottom‑right of an m × n grid:
Moves allowed: right or down only.
This is a DP‑multidimensional problem (grid traversal).
Alternatively, it can be solved via combinatorics: total moves = (m-1) + (n-1); choose (m-1) downs or (n-1) rights.

Key Observations
DP approach:
Define dp[i][j] = number of ways to reach cell (i, j).
Transition: dp[i][j] = dp[i-1][j] + dp[i][j-1].
Base case: first row and first column = 1 (only one way to reach).

Combinatorial approach:
Total moves = m+n-2.
Choose (m-1) downs → result = C(m+n-2, m-1).
Both approaches yield the same result.
For clarity and pedagogy, we implement DP.

Strategy
Initialize a 2D DP table of size m × n.
Fill first row and column with 1.
Iteratively compute dp[i][j].
Return dp[m-1][n-1].
Optimize space to O(n) if needed.

Complexity
Time: O(m × n)
Space: O(m × n) (or O(n) with optimization)

Edge Cases
m = 1 or n = 1 → only one path.
Small grids (2×2, 3×2) → verify correctness.
Large grids (100×100) → DP handles efficiently.

Pseudocode
function uniquePaths(m, n):
    dp = 2D array of size m × n
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[m-1][n-1]

"""

from typing import Protocol


# ───────────────────────────────────────────────────────────────────────────
# Strategy Interface
# ───────────────────────────────────────────────────────────────────────────

class UniquePathsStrategy(Protocol):
    """
    Protocol defining the interface for unique paths strategies.
    """
    def solve(self, m: int, n: int) -> int: ...


# ───────────────────────────────────────────────────────────────────────────
# DP Strategy
# ───────────────────────────────────────────────────────────────────────────

class DPUniquePathsStrategy:
    """
    Dynamic Programming strategy for computing unique paths in an m×n grid.

    Design:
        - Base cases: first row and first column = 1
        - Transition: dp[i][j] = dp[i-1][j] + dp[i][j-1]
        - Result: dp[m-1][n-1]

    Time Complexity: O(m × n)
    Space Complexity: O(m × n) (can be optimized to O(n))
    """

    def solve(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]


# ───────────────────────────────────────────────────────────────────────────
# Orchestrator — Clean Architecture
# ───────────────────────────────────────────────────────────────────────────

class Solution:
    """
    Orchestrates unique paths computation by delegating to a strategy.

    - Separation of concerns: orchestration vs. computation
    - Dependency injection: strategy is swappable
    - Defaults to DP strategy
    """

    def __init__(self, strategy: UniquePathsStrategy = None) -> None:
        self.strategy = strategy if strategy is not None else DPUniquePathsStrategy()

    def uniquePaths(self, m: int, n: int) -> int:
        """
        Entry point for LeetCode.

        Args:
            m (int): Number of rows.
            n (int): Number of columns.

        Returns:
            int: Number of unique paths from top-left to bottom-right.
        """
        return self.strategy.solve(m, n)


# ───────────────────────────────────────────────────────────────────────────
# Usage Suite
# ───────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    solution = Solution()

    print(solution.uniquePaths(3, 7))  # Expected: 28
    print(solution.uniquePaths(3, 2))  # Expected: 3
    print(solution.uniquePaths(1, 1))  # Expected: 1
    print(solution.uniquePaths(2, 2))  # Expected: 2
    print(solution.uniquePaths(10, 10))  # Stress test
