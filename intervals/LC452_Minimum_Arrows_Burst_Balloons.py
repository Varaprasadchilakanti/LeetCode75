#!/usr/bin/env python3
"""
452. Minimum Number of Arrows to Burst Balloons

There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.
Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.
Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

Example 1:
Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].

Example 2:
Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.

Example 3:
Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
- Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].

Constraints:
1 <= points.length <= 105
points[i].length == 2
-231 <= xstart < xend <= 231 - 1

Topics
Array
Greedy
Sorting


Developer Insights
Problem Nature
We must find the minimum number of arrows required to burst all balloons represented by intervals [xstart, xend].
This is a Greedy + Sorting problem under the Intervals category.

Key Observations
Each arrow can burst all balloons overlapping at its chosen x‑coordinate.
Greedy choice: always shoot at the end of the current interval (like interval scheduling).
Sort intervals by end coordinate.
Traverse intervals:
If current balloon starts after the last arrow position → need a new arrow.
Else → balloon overlaps, already burst by existing arrow.

Strategy
Sort balloons by end coordinate.
Initialize arrows = 0, end = -∞.
Traverse intervals:
If start > end: need new arrow, increment arrows, update end = current.end.
Else: balloon already burst.
Return arrows.

Complexity
Sorting: O(n log n).
Traversal: O(n).
Space: O(1).

Edge Cases
Single balloon → arrows = 1.
All disjoint balloons → arrows = n.
Fully overlapping balloons → arrows = 1.
Large n (≤ 10^5) handled efficiently.

Pseudocode
function findMinArrowShots(points):
    sort points by end
    arrows = 0
    end = -∞
    for [s, e] in points:
        if s > end:
            arrows += 1
            end = e
    return arrows

"""

from typing import List, Protocol


# ───────────────────────────────────────────────────────────────────────────
# Strategy Interface
# ───────────────────────────────────────────────────────────────────────────

class ArrowStrategy(Protocol):
    """
    Protocol defining the interface for minimum arrow strategies.
    """
    def solve(self, points: List[List[int]]) -> int: ...


# ───────────────────────────────────────────────────────────────────────────
# Greedy Strategy
# ───────────────────────────────────────────────────────────────────────────

class GreedyArrowStrategy:
    """
    Greedy strategy for finding minimum arrows to burst balloons.

    Design:
        - Sort intervals by end coordinate.
        - Shoot arrow at end of current interval if not overlapping.
        - Count arrows.

    Time Complexity: O(n log n)
    Space Complexity: O(1)
    """

    def solve(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        arrows, end = 0, float("-inf")

        for start, finish in points:
            if start > end:
                arrows += 1
                end = finish
        return arrows


# ───────────────────────────────────────────────────────────────────────────
# Orchestrator — Clean Architecture
# ───────────────────────────────────────────────────────────────────────────

class Solution:
    """
    Orchestrates minimum arrow computation by delegating to a strategy.

    - Separation of concerns: orchestration vs. computation
    - Dependency injection: strategy is swappable
    - Defaults to Greedy strategy
    """

    def __init__(self, strategy: ArrowStrategy = None) -> None:
        self.strategy = strategy if strategy is not None else GreedyArrowStrategy()

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        Entry point for LeetCode.

        Args:
            points (List[List[int]]): List of balloon intervals [xstart, xend].

        Returns:
            int: Minimum number of arrows required.
        """
        return self.strategy.solve(points)


# ───────────────────────────────────────────────────────────────────────────
# Usage Suite
# ───────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    solution = Solution()
    print(solution.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))  # Expected: 2
    print(solution.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))    # Expected: 4
    print(solution.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))    # Expected: 2
    print(solution.findMinArrowShots([[1,10],[2,9],[3,8]]))         # Expected: 1
