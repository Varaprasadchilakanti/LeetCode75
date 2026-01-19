#!/usr/bin/env python3
"""
435. Non-overlapping Intervals

Given an array of intervals intervals where intervals[i] = [starti, endi], 
return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.

Example 1:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Example 2:
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Example 3:
Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

Constraints:
1 <= intervals.length <= 105
intervals[i].length == 2
-5 * 104 <= starti < endi <= 5 * 104

Topics
Array
Dynamic Programming
Greedy
Sorting


Developer Insights
Problem Nature
We must remove the minimum number of intervals so that the rest are non‑overlapping.
This is a Greedy + Sorting problem under the Intervals category.

Key Observations
Sort intervals by end time.
Greedy choice: always keep the interval with the earliest end to maximize room for subsequent intervals.
If current interval overlaps with the last chosen one, remove it.
Count removals.

Strategy
Sort intervals by end time.
Initialize end = -∞, removals = 0.
Traverse intervals:
If start >= end: keep interval, update end = current.end.
Else: overlap → increment removals.
Return removals.

Complexity
Sorting: O(n log n).
Traversal: O(n).
Space: O(1).

Edge Cases
Single interval → removals = 0.
All intervals identical → removals = n‑1.
Touching intervals (end == start) → non‑overlapping.
Large n (≤ 10^5) handled efficiently.

Pseudocode
function eraseOverlapIntervals(intervals):
    sort intervals by end
    removals = 0
    end = -∞
    for [s, e] in intervals:
        if s >= end:
            end = e
        else:
            removals += 1
    return removals

"""

from typing import List, Protocol


# ───────────────────────────────────────────────────────────────────────────
# Strategy Interface
# ───────────────────────────────────────────────────────────────────────────

class IntervalRemovalStrategy(Protocol):
    """
    Protocol defining the interface for interval removal strategies.
    """
    def solve(self, intervals: List[List[int]]) -> int: ...


# ───────────────────────────────────────────────────────────────────────────
# Greedy Strategy
# ───────────────────────────────────────────────────────────────────────────

class GreedyIntervalRemovalStrategy:
    """
    Greedy strategy for removing overlapping intervals.

    Design:
        - Sort intervals by end time.
        - Keep interval if start >= last_end.
        - Otherwise, remove interval.
        - Count removals.

    Time Complexity: O(n log n)
    Space Complexity: O(1)
    """

    def solve(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        removals, end = 0, float("-inf")

        for start, finish in intervals:
            if start >= end:
                end = finish
            else:
                removals += 1
        return removals


# ───────────────────────────────────────────────────────────────────────────
# Orchestrator — Clean Architecture
# ───────────────────────────────────────────────────────────────────────────

class Solution:
    """
    Orchestrates interval removal computation by delegating to a strategy.

    - Separation of concerns: orchestration vs. computation
    - Dependency injection: strategy is swappable
    - Defaults to Greedy strategy
    """

    def __init__(self, strategy: IntervalRemovalStrategy = None) -> None:
        self.strategy = strategy if strategy is not None else GreedyIntervalRemovalStrategy()

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Entry point for LeetCode.

        Args:
            intervals (List[List[int]]): List of intervals [start, end].

        Returns:
            int: Minimum number of intervals to remove.
        """
        return self.strategy.solve(intervals)


# ───────────────────────────────────────────────────────────────────────────
# Usage Suite
# ───────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    solution = Solution()
    print(solution.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))  # Expected: 1
    print(solution.eraseOverlapIntervals([[1,2],[1,2],[1,2]]))        # Expected: 2
    print(solution.eraseOverlapIntervals([[1,2],[2,3]]))              # Expected: 0
    print(solution.eraseOverlapIntervals([[1,100],[11,12],[12,13]]))  # Custom: Expected: 1
