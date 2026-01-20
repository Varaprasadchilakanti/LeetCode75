#!/usr/bin/env python3
"""
739. Daily Temperatures

Given an array of integers temperatures represents the daily temperatures, return an array answer 
such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.


Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]

Constraints:
1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100

Topics
Array
Stack
Monotonic Stack
Weekly Contest 61

Hint 1
If the temperature is say, 70 today, 
then in the future a warmer temperature must be either 71, 72, 73, ..., 99, or 100. 
We could remember when all of them occur next.


Developer Insights
Problem Nature
We must compute, for each day, how many days until a warmer temperature occurs.
This is a Monotonic Stack problem: we track indices of decreasing temperatures.

Key Observations
If today’s temperature is warmer than the temperature at the top of the stack, we’ve found the next warmer day for that index.
Stack stores indices of unresolved days in monotonic decreasing order of temperatures.
Each element is resolved when a warmer temperature appears.

Strategy
Initialize answer = [0] * n.
Use stack to store indices of unresolved days.
Traverse temperatures:
While stack not empty and current temp > temp[stack[-1]]:
Pop index, compute difference, update answer.
Push current index.
Return answer.

Complexity
Time: O(n) (each index pushed/popped once).
Space: O(n) for stack + answer.

Edge Cases
Strictly decreasing temperatures → all answers = 0.
Strictly increasing temperatures → answers = [1,1,…,0].
Single element → answer = [0].


Pseudocode
function dailyTemperatures(temperatures):
    n = len(temperatures)
    answer = [0] * n
    stack = []
    for i in range(n):
        while stack not empty and temperatures[i] > temperatures[stack.top]:
            prev = stack.pop()
            answer[prev] = i - prev
        stack.push(i)
    return answer

"""

from typing import List, Protocol


# ───────────────────────────────────────────────────────────────────────────
# Strategy Interface
# ───────────────────────────────────────────────────────────────────────────

class TemperatureStrategy(Protocol):
    """
    Protocol defining the interface for daily temperature strategies.
    """
    def solve(self, temperatures: List[int]) -> List[int]: ...


# ───────────────────────────────────────────────────────────────────────────
# Monotonic Stack Strategy
# ───────────────────────────────────────────────────────────────────────────

class MonotonicStackTemperatureStrategy:
    """
    Monotonic Stack strategy for computing days until warmer temperatures.

    Design:
        - Traverse temperatures.
        - Maintain stack of indices with decreasing temperatures.
        - Resolve indices when warmer temperature found.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def solve(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack: List[int] = []

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev = stack.pop()
                answer[prev] = i - prev
            stack.append(i)

        return answer


# ───────────────────────────────────────────────────────────────────────────
# Orchestrator — Clean Architecture
# ───────────────────────────────────────────────────────────────────────────

class Solution:
    """
    Orchestrates daily temperature computation by delegating to a strategy.

    - Separation of concerns: orchestration vs. computation
    - Dependency injection: strategy is swappable
    - Defaults to Monotonic Stack strategy
    """

    def __init__(self, strategy: TemperatureStrategy = None) -> None:
        self.strategy = strategy if strategy is not None else MonotonicStackTemperatureStrategy()

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Entry point for LeetCode.

        Args:
            temperatures (List[int]): List of daily temperatures.

        Returns:
            List[int]: Days until warmer temperature for each day.
        """
        return self.strategy.solve(temperatures)


# ───────────────────────────────────────────────────────────────────────────
# Usage Suite
# ───────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    solution = Solution()
    print(solution.dailyTemperatures([73,74,75,71,69,72,76,73]))  # Expected: [1,1,4,2,1,1,0,0]
    print(solution.dailyTemperatures([30,40,50,60]))              # Expected: [1,1,1,0]
    print(solution.dailyTemperatures([30,60,90]))                 # Expected: [1,1,0]
    print(solution.dailyTemperatures([90,80,70]))                 # Expected: [0,0,0]
