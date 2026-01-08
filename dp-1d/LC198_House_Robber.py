"""
198. House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 400

Topics
Array
Dynamic Programming


Developer Insights
Problem Nature
We must maximize the amount robbed without triggering alarms:
Constraint: cannot rob two adjacent houses.
This is a DP‑1D problem: the state depends on the maximum profit up to each house.

Key Observations
Define dp[i] as the maximum money robbed up to house i.
Transition: dp[i] = max(dp[i-1], dp[i-2] + nums[i]).
Base cases:
dp[0] = nums[0]
dp[1] = max(nums[0], nums[1])
Answer: dp[n-1].
Space optimization: only last two states are needed.

Strategy
Handle edge cases: length 1 or 2.
Initialize rolling variables for dp[i-2] and dp[i-1].
Iteratively compute dp[i].
Return final result.

Complexity
Time: O(n)
Space: O(1) (rolling variables)

Edge Cases
Single house → return its value.
Two houses → return max of both.
All zeros → return 0.
Large values (≤ 400 × 100 = 40,000) → safe in 32‑bit integer.

Pseudocode
function rob(nums):
    n = len(nums)
    if n == 1: return nums[0]
    if n == 2: return max(nums[0], nums[1])

    prev2 = nums[0]
    prev1 = max(nums[0], nums[1])

    for i in range(2, n):
        curr = max(prev1, prev2 + nums[i])
        prev2, prev1 = prev1, curr

    return prev1

"""

from typing import List, Protocol


# ───────────────────────────────────────────────────────────────────────────
# Strategy Interface
# ───────────────────────────────────────────────────────────────────────────

class RobberyStrategy(Protocol):
    """
    Protocol defining the interface for house robbery strategies.
    """
    def solve(self, nums: List[int]) -> int: ...


# ───────────────────────────────────────────────────────────────────────────
# Iterative DP Strategy
# ───────────────────────────────────────────────────────────────────────────

class IterativeDPRobberyStrategy:
    """
    Iterative DP strategy for maximizing robbery profit.

    Design:
        - Base cases: handle n=1 and n=2 directly.
        - Transition: dp[i] = max(dp[i-1], dp[i-2] + nums[i]).
        - Space optimized to O(1) using rolling variables.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def solve(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        prev2, prev1 = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            curr = max(prev1, prev2 + nums[i])
            prev2, prev1 = prev1, curr

        return prev1


# ───────────────────────────────────────────────────────────────────────────
# Orchestrator — Clean Architecture
# ───────────────────────────────────────────────────────────────────────────

class Solution:
    """
    Orchestrates house robbery computation by delegating to a strategy.

    - Separation of concerns: orchestration vs. computation
    - Dependency injection: strategy is swappable
    - Defaults to Iterative DP strategy
    """

    def __init__(self, strategy: RobberyStrategy = None) -> None:
        self.strategy = strategy if strategy is not None else IterativeDPRobberyStrategy()

    def rob(self, nums: List[int]) -> int:
        """
        Entry point for LeetCode.

        Args:
            nums (List[int]): Money in each house.

        Returns:
            int: Maximum money that can be robbed without alerting the police.
        """
        return self.strategy.solve(nums)


# ───────────────────────────────────────────────────────────────────────────
# Usage Suite
# ───────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    solution = Solution()

    print(solution.rob([1, 2, 3, 1]))       # Expected: 4
    print(solution.rob([2, 7, 9, 3, 1]))    # Expected: 12
    print(solution.rob([5]))                # Expected: 5
    print(solution.rob([10, 20]))           # Expected: 20
    print(solution.rob([0, 0, 0, 0]))       # Expected: 0
