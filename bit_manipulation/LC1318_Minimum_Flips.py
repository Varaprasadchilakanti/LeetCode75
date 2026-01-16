#!/usr/bin/env python3
"""
1318. Minimum Flips to Make a OR b Equal to c

Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.

Example 1:
Input: a = 2, b = 6, c = 5
Output: 3
Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)

Example 2:
Input: a = 4, b = 2, c = 7
Output: 1

Example 3:
Input: a = 1, b = 2, c = 3
Output: 0

Constraints:
1 <= a <= 10^9
1 <= b <= 10^9
1 <= c <= 10^9

Topics
Bit Manipulation
Weekly Contest 171

Hint 1
Check the bits one by one whether they need to be flipped.


Developer Insights
Problem Nature
We must compute the minimum number of bit flips in a and b such that (a OR b) == c.
This is a Bit Manipulation problem: we analyze each bit position independently.

Key Observations
For each bit position i:
If (c_i == 1):
At least one of a_i or b_i must be 1.
If both are 0, we need 1 flip.
If (c_i == 0):
Both a_i and b_i must be 0.
If both are 1, we need 2 flips.
If one is 1, we need 1 flip.
Iterate bit by bit until all numbers are exhausted.

Strategy
Initialize flips = 0.
While a, b, or c > 0:
Extract lowest bits: a_bit = a & 1, b_bit = b & 1, c_bit = c & 1.
Apply rules above.
Right‑shift all numbers.
Return flips.

Complexity
Time: O(log(max(a, b, c))) → up to 30 bits.
Space: O(1).

Edge Cases
a OR b already equals c → flips = 0.
Large values (≤ 10^9) → handled efficiently with bitwise ops.
Cases where both a and b must flip at same bit.

Pseudocode
function minFlips(a, b, c):
    flips = 0
    while a > 0 or b > 0 or c > 0:
        a_bit = a & 1
        b_bit = b & 1
        c_bit = c & 1

        if c_bit == 1:
            if a_bit == 0 and b_bit == 0:
                flips += 1
        else:  # c_bit == 0
            flips += a_bit + b_bit

        a >>= 1
        b >>= 1
        c >>= 1

    return flips

"""

from typing import Protocol


# ───────────────────────────────────────────────────────────────────────────
# Strategy Interface
# ───────────────────────────────────────────────────────────────────────────

class MinFlipsStrategy(Protocol):
    """
    Protocol defining the interface for minimum flips strategies.
    """
    def solve(self, a: int, b: int, c: int) -> int: ...


# ───────────────────────────────────────────────────────────────────────────
# Bit Manipulation Strategy
# ───────────────────────────────────────────────────────────────────────────

class BitwiseMinFlipsStrategy:
    """
    Bit Manipulation strategy for computing minimum flips to satisfy (a OR b == c).

    Design:
        - Iterate bit by bit
        - Apply rules:
            if c_bit == 1:
                need at least one of a_bit or b_bit == 1
                if both 0 → flips += 1
            if c_bit == 0:
                both must be 0
                flips += (a_bit + b_bit)
        - Shift right each iteration

    Time Complexity: O(log(max(a, b, c)))
    Space Complexity: O(1)
    """

    def solve(self, a: int, b: int, c: int) -> int:
        flips = 0
        while a > 0 or b > 0 or c > 0:
            a_bit, b_bit, c_bit = a & 1, b & 1, c & 1

            if c_bit == 1:
                if a_bit == 0 and b_bit == 0:
                    flips += 1
            else:  # c_bit == 0
                flips += a_bit + b_bit

            a >>= 1
            b >>= 1
            c >>= 1

        return flips


# ───────────────────────────────────────────────────────────────────────────
# Orchestrator — Clean Architecture
# ───────────────────────────────────────────────────────────────────────────

class Solution:
    """
    Orchestrates minimum flips computation by delegating to a strategy.

    - Separation of concerns: orchestration vs. computation
    - Dependency injection: strategy is swappable
    - Defaults to Bitwise strategy
    """

    def __init__(self, strategy: MinFlipsStrategy = None) -> None:
        self.strategy = strategy if strategy is not None else BitwiseMinFlipsStrategy()

    def minFlips(self, a: int, b: int, c: int) -> int:
        """
        Entry point for LeetCode.

        Args:
            a (int): First integer.
            b (int): Second integer.
            c (int): Target integer.

        Returns:
            int: Minimum number of flips required.
        """
        return self.strategy.solve(a, b, c)


# ───────────────────────────────────────────────────────────────────────────
# Usage Suite
# ───────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    solution = Solution()

    print(solution.minFlips(2, 6, 5))  # Expected: 3
    print(solution.minFlips(4, 2, 7))  # Expected: 1
    print(solution.minFlips(1, 2, 3))  # Expected: 0
    print(solution.minFlips(8, 3, 10)) # Custom test
