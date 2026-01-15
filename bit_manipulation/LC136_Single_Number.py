#!/usr/bin/env python3
"""
136. Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1

Constraints:
1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.

Topics
Array
Bit Manipulation

Hint 1
Think about the XOR (^) operator's property.


Developer Insights
Problem Nature
We must find the single element in an array where every other element appears exactly twice.
Constraints require:
Linear runtime complexity O(n).
Constant extra space O(1).
This is a Bit Manipulation problem.

Key Observations
XOR (^) properties:
a ^ a = 0 (self‑cancellation).
a ^ 0 = a.
XOR is commutative and associative.
Therefore, XORing all elements yields the unique element:
result=𝑛𝑢𝑚𝑠[0]⊕𝑛𝑢𝑚𝑠[1]⊕⋯⊕𝑛𝑢𝑚𝑠[𝑛−1]
No extra space needed, single pass.

Strategy
Initialize result = 0.
Iterate through array, XOR each element into result.
Return result.

Complexity
Time: O(n).
Space: O(1).

Edge Cases
Array length = 1 → return that element.
Negative numbers → XOR works seamlessly.
Large arrays (≤ 30,000) → efficient with O(n).


Pseudocode
function singleNumber(nums):
    result = 0
    for num in nums:
        result = result XOR num
    return result

"""

from typing import List, Protocol


# ───────────────────────────────────────────────────────────────────────────
# Strategy Interface
# ───────────────────────────────────────────────────────────────────────────

class SingleNumberStrategy(Protocol):
    """
    Protocol defining the interface for single number strategies.
    """
    def solve(self, nums: List[int]) -> int: ...


# ───────────────────────────────────────────────────────────────────────────
# Bit Manipulation Strategy
# ───────────────────────────────────────────────────────────────────────────

class XORSingleNumberStrategy:
    """
    Bit Manipulation strategy using XOR to find the unique element.

    Design:
        - XOR all elements
        - Duplicate elements cancel out
        - Remaining element is the answer

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def solve(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result


# ───────────────────────────────────────────────────────────────────────────
# Orchestrator — Clean Architecture
# ───────────────────────────────────────────────────────────────────────────

class Solution:
    """
    Orchestrates single number computation by delegating to a strategy.

    - Separation of concerns: orchestration vs. computation
    - Dependency injection: strategy is swappable
    - Defaults to XOR strategy
    """

    def __init__(self, strategy: SingleNumberStrategy = None) -> None:
        self.strategy = strategy if strategy is not None else XORSingleNumberStrategy()

    def singleNumber(self, nums: List[int]) -> int:
        """
        Entry point for LeetCode.

        Args:
            nums (List[int]): Array of integers where every element appears twice except one.

        Returns:
            int: The unique element.
        """
        return self.strategy.solve(nums)


# ───────────────────────────────────────────────────────────────────────────
# Usage Suite
# ───────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    solution = Solution()

    print(solution.singleNumber([2, 2, 1]))       # Expected: 1
    print(solution.singleNumber([4, 1, 2, 1, 2])) # Expected: 4
    print(solution.singleNumber([1]))             # Expected: 1
    print(solution.singleNumber([-1, -1, -2]))    # Expected: -2
