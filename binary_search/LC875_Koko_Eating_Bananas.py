"""
875. Koko Eating Bananas

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours.

 
Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:
Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:
Input: piles = [30,11,23,4,20], h = 6
Output: 23

Constraints:
1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109

Topics
Array
Binary Search
Weekly Contest 94


Developer Insights
Problem Nature
We must find the minimum eating speed k such that Koko finishes all bananas in h hours.
Each hour, she eats up to k bananas from a single pile.
If fewer than k remain, she eats them all and stops for that hour.
The total time is the sum of ceil(pile / k) across all piles.
We need the smallest k satisfying total_hours ≤ h.
This is a binary search on the answer problem.

Key Observations
Minimum possible speed = 1.
Maximum possible speed = max(piles).
The function can_finish(speed) is monotonic:
If Koko can finish at speed k, she can also finish at any speed > k.
Thus, binary search applies.

Strategy
Define helper can_finish(speed) → returns True if sum of hours ≤ h.
Binary search between low = 1 and high = max(piles).
While low < high:
Compute mid = (low + high) // 2.
If can_finish(mid) → move left (high = mid).
Else → move right (low = mid + 1).
Return low.

Complexity
Time: O(n log max(piles))
Space: O(1)

Edge Cases
Single pile → answer = ceil(pile / h).
h = n → must eat one pile per hour → answer = max(piles).
h very large → answer = 1.
Large pile values (up to 1e9) → binary search ensures efficiency.

Pseudocode
function minEatingSpeed(piles, h):
    low = 1
    high = max(piles)

    while low < high:
        mid = (low + high) // 2
        if can_finish(mid):
            high = mid
        else:
            low = mid + 1

    return low

function can_finish(speed):
    total_hours = 0
    for pile in piles:
        total_hours += ceil(pile / speed)
    return total_hours <= h


"""

from typing import List, Protocol
import math


# ───────────────────────────────────────────────────────────────────────────
# Strategy Interface
# ───────────────────────────────────────────────────────────────────────────

class EatingSpeedStrategy(Protocol):
    """
    Protocol defining the interface for Koko's eating speed strategies.
    """
    def solve(self, piles: List[int], h: int) -> int: ...


# ───────────────────────────────────────────────────────────────────────────
# Binary Search Strategy
# ───────────────────────────────────────────────────────────────────────────

class BinarySearchEatingSpeedStrategy:
    """
    Binary search strategy for finding minimum eating speed.

    Design:
        - Search space: [1, max(piles)]
        - Use binary search to minimize speed.
        - Check feasibility with helper function can_finish(speed).

    Time Complexity: O(n log max(piles))
    Space Complexity: O(1)
    """

    def solve(self, piles: List[int], h: int) -> int:
        def can_finish(speed: int) -> bool:
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile / speed)
                if total_hours > h:
                    return False
            return True

        low, high = 1, max(piles)

        while low < high:
            mid = (low + high) // 2
            if can_finish(mid):
                high = mid
            else:
                low = mid + 1

        return low


# ───────────────────────────────────────────────────────────────────────────
# Orchestrator — Clean Architecture
# ───────────────────────────────────────────────────────────────────────────

class Solution:
    """
    Orchestrates minimum eating speed computation by delegating to a strategy.

    - Separation of concerns: orchestration vs. computation
    - Dependency injection: strategy is swappable
    - Defaults to Binary Search strategy
    """

    def __init__(self, strategy: EatingSpeedStrategy = None) -> None:
        self.strategy = strategy if strategy is not None else BinarySearchEatingSpeedStrategy()

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Entry point for LeetCode.

        Args:
            piles (List[int]): Number of bananas in each pile.
            h (int): Hours available.

        Returns:
            int: Minimum eating speed.
        """
        return self.strategy.solve(piles, h)


# ───────────────────────────────────────────────────────────────────────────
# Usage Suite
# ───────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    solution = Solution()

    print(solution.minEatingSpeed([3, 6, 7, 11], 8))        # Expected: 4
    print(solution.minEatingSpeed([30, 11, 23, 4, 20], 5))  # Expected: 30
    print(solution.minEatingSpeed([30, 11, 23, 4, 20], 6))  # Expected: 23
