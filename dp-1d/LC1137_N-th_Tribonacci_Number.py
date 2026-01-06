"""
1137. N-th Tribonacci Number

The Tribonacci sequence Tn is defined as follows: 
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
Given n, return the value of Tn.

Example 1:
Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

Example 2:
Input: n = 25
Output: 1389537


Constraints:
0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.

Topics
Math
Dynamic Programming
Memoization
Weekly Contest 147

Hint 1
Make an array F of length 38, and set F[0] = 0, F[1] = F[2] = 1.
Hint 2
Now write a loop where you set F[n+3] = F[n] + F[n+1] + F[n+2], and return F[n].


Developer Insights
Problem Nature
We must compute the n‑th Tribonacci number:
Base cases: T0 = 0, T1 = 1, T2 = 1.
Recurrence: Tn = Tn-1 + Tn-2 + Tn-3.
Constraint: 0 ≤ n ≤ 37 → small, fits in 32‑bit integer.
This is a DP‑1D problem: iterative tabulation or memoization.

Key Observations
We only need the last three values at any time → O(1) space optimization.
For small n, return directly from base cases.
Iterative DP avoids recursion overhead.
Edge cases: n = 0, 1, 2.

Strategy
Handle base cases explicitly.
Initialize dp = [0, 1, 1].
Iteratively compute values up to n.
Return dp[n].
Optimize space by rolling variables (a, b, c).

Complexity
Time: O(n)
Space: O(1) (rolling variables)
Edge Cases
n = 0 → 0
n = 1 → 1
n = 2 → 1
n = 3 → 2
Large n = 37 → fits in 32‑bit integer.

Pseudocode
function tribonacci(n):
    if n == 0: return 0
    if n == 1 or n == 2: return 1

    a, b, c = 0, 1, 1
    for i in range(3, n+1):
        d = a + b + c
        a, b, c = b, c, d

    return c


"""

from typing import Protocol


# ───────────────────────────────────────────────────────────────────────────
# Strategy Interface
# ───────────────────────────────────────────────────────────────────────────

class TribonacciStrategy(Protocol):
    """
    Protocol defining the interface for Tribonacci strategies.
    """
    def solve(self, n: int) -> int: ...


# ───────────────────────────────────────────────────────────────────────────
# Iterative DP Strategy
# ───────────────────────────────────────────────────────────────────────────

class IterativeDPTribonacciStrategy:
    """
    Iterative DP strategy for computing the n-th Tribonacci number.

    Design:
        - Base cases: T0=0, T1=1, T2=1
        - Iteratively compute values using rolling variables.
        - Space optimized to O(1).

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def solve(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        a, b, c = 0, 1, 1
        for _ in range(3, n + 1):
            d = a + b + c
            a, b, c = b, c, d
        return c


# ───────────────────────────────────────────────────────────────────────────
# Orchestrator — Clean Architecture
# ───────────────────────────────────────────────────────────────────────────

class Solution:
    """
    Orchestrates Tribonacci computation by delegating to a strategy.

    - Separation of concerns: orchestration vs. computation
    - Dependency injection: strategy is swappable
    - Defaults to Iterative DP strategy
    """

    def __init__(self, strategy: TribonacciStrategy = None) -> None:
        self.strategy = strategy if strategy is not None else IterativeDPTribonacciStrategy()

    def tribonacci(self, n: int) -> int:
        """
        Entry point for LeetCode.

        Args:
            n (int): Index of Tribonacci number.

        Returns:
            int: The n-th Tribonacci number.
        """
        return self.strategy.solve(n)


# ───────────────────────────────────────────────────────────────────────────
# Usage Suite
# ───────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    solution = Solution()

    print(solution.tribonacci(4))   # Expected: 4
    print(solution.tribonacci(25))  # Expected: 1389537
    print(solution.tribonacci(0))   # Expected: 0
    print(solution.tribonacci(1))   # Expected: 1
    print(solution.tribonacci(2))   # Expected: 1
    print(solution.tribonacci(3))   # Expected: 2
