#!/usr/bin/env python3
"""
338. Counting Bits

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), 
ans[i] is the number of 1's in the binary representation of i.

Example 1:
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Example 2:
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

Constraints:
0 <= n <= 105

Follow up:
It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?

Topics
Dynamic Programming
Bit Manipulation

Hint 1
You should make use of what you have produced already.
Hint 2
Divide the numbers in ranges like [2-3], [4-7], [8-15] and so on. And try to generate new range from previous.
Hint 3
Or does the odd/even status of the number help you in calculating the number of 1s?


Developer Insights
Problem Nature
We must compute the number of 1s in the binary representation of each integer from 0 to n.
This is a Bit Manipulation + DP problem:
Naïve approach: count bits for each number individually → O(n log n).
Optimized approach: reuse previously computed results → O(n).

Key Observations
For any integer i:
If i is even: bits[i] = bits[i // 2] (right shift removes trailing zero).
If i is odd: bits[i] = bits[i // 2] + 1 (odd numbers have one extra 1).
This recurrence allows linear time computation.
Base case: bits[0] = 0.

Strategy
Initialize result array of length n+1.
Fill base case bits[0] = 0.
For each i from 1 to n:
Use recurrence relation.
Return result array.

Complexity
Time: O(n)
Space: O(n)

Edge Cases
n = 0 → result = [0].
Large n (≤ 100,000) → efficient with O(n).


Pseudocode
function countBits(n):
    ans = array of length n+1
    ans[0] = 0

    for i in range(1, n+1):
        ans[i] = ans[i // 2] + (i % 2)

    return ans

"""

from typing import List, Protocol


# ───────────────────────────────────────────────────────────────────────────
# Strategy Interface
# ───────────────────────────────────────────────────────────────────────────

class BitCountStrategy(Protocol):
    """
    Protocol defining the interface for bit counting strategies.
    """
    def solve(self, n: int) -> List[int]: ...


# ───────────────────────────────────────────────────────────────────────────
# DP + Bit Manipulation Strategy
# ───────────────────────────────────────────────────────────────────────────

class DPBitCountStrategy:
    """
    Dynamic Programming + Bit Manipulation strategy for counting bits.

    Design:
        - Recurrence:
            ans[i] = ans[i // 2] + (i % 2)
        - Base case:
            ans[0] = 0
        - Result:
            ans array of length n+1

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def solve(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans


# ───────────────────────────────────────────────────────────────────────────
# Orchestrator — Clean Architecture
# ───────────────────────────────────────────────────────────────────────────

class Solution:
    """
    Orchestrates bit counting computation by delegating to a strategy.

    - Separation of concerns: orchestration vs. computation
    - Dependency injection: strategy is swappable
    - Defaults to DP + Bit Manipulation strategy
    """

    def __init__(self, strategy: BitCountStrategy = None) -> None:
        self.strategy = strategy if strategy is not None else DPBitCountStrategy()

    def countBits(self, n: int) -> List[int]:
        """
        Entry point for LeetCode.

        Args:
            n (int): Upper bound integer.

        Returns:
            List[int]: Array of bit counts for each integer from 0 to n.
        """
        return self.strategy.solve(n)


# ───────────────────────────────────────────────────────────────────────────
# Usage Suite
# ───────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    solution = Solution()

    print(solution.countBits(2))   # Expected: [0, 1, 1]
    print(solution.countBits(5))   # Expected: [0, 1, 1, 2, 1, 2]
    print(solution.countBits(0))   # Expected: [0]
    print(solution.countBits(10))  # Expected: [0,1,1,2,1,2,2,3,1,2,2]
