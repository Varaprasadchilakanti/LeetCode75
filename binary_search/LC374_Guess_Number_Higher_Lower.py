"""
374. Guess Number Higher or Lower

We are playing the Guess Game. The game is as follows:
I pick a number from 1 to n. You have to guess which number I picked (the number I picked stays the same throughout the game).
Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
You call a pre-defined API int guess(int num), which returns three possible results:
-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.

Example 1:
Input: n = 10, pick = 6
Output: 6

Example 2:
Input: n = 1, pick = 1
Output: 1

Example 3:
Input: n = 2, pick = 1
Output: 1

Constraints:
1 <= n <= 231 - 1
1 <= pick <= n

Topics
Binary Search
Interactive


Developer Insights
Problem Nature
We must guess a hidden number between 1 and n using the provided API guess(num).
The API returns:
-1 → our guess is higher than the pick.
1 → our guess is lower than the pick.
0 → our guess is correct.
This is a classic binary search problem.

Key Observations
The search space is [1, n].
Each API call tells us whether to move left or right.
Binary search guarantees O(log n) calls.
Edge cases: n = 1, pick = 1, or pick at boundaries.

Strategy
Initialize low = 1, high = n.
While low <= high:
Compute mid = (low + high) // 2.
Call guess(mid).
If result == 0 → return mid.
If result == -1 → move left (high = mid - 1).
If result == 1 → move right (low = mid + 1).

Complexity
Time: O(log n)
Space: O(1)

Pseudocode
function guessNumber(n):
    low = 1
    high = n

    while low <= high:
        mid = (low + high) // 2
        res = guess(mid)

        if res == 0:
            return mid
        elif res == -1:
            high = mid - 1
        else:
            low = mid + 1


"""

# ───────────────────────────────────────────────────────────────────────────
# Strategy Interface
# ───────────────────────────────────────────────────────────────────────────

from typing import Protocol


class GuessStrategy(Protocol):
    """
    Protocol defining the interface for guessing strategies.
    """
    def solve(self, n: int) -> int: ...


# ───────────────────────────────────────────────────────────────────────────
# Binary Search Strategy
# ───────────────────────────────────────────────────────────────────────────

class BinarySearchGuessStrategy:
    """
    Binary search strategy for the Guess Number Higher or Lower problem.

    Design:
        - Maintain search space [1, n].
        - Use binary search to minimize API calls.
        - Adjust bounds based on API feedback.

    Time Complexity: O(log n)
    Space Complexity: O(1)
    """

    def solve(self, n: int) -> int:
        low, high = 1, n

        while low <= high:
            mid = (low + high) // 2
            res = guess(mid)  # API call

            if res == 0:
                return mid
            elif res == -1:
                high = mid - 1
            else:
                low = mid + 1

        return -1  # Should never happen if constraints are valid


# ───────────────────────────────────────────────────────────────────────────
# Orchestrator — Clean Architecture
# ───────────────────────────────────────────────────────────────────────────

class Solution:
    """
    Orchestrates the guessing game by delegating to a strategy.

    - Separation of concerns: orchestration vs. computation
    - Dependency injection: strategy is swappable
    - Defaults to Binary Search strategy
    """

    def __init__(self, strategy: GuessStrategy = None) -> None:
        self.strategy = strategy if strategy is not None else BinarySearchGuessStrategy()

    def guessNumber(self, n: int) -> int:
        """
        Entry point for LeetCode.

        Args:
            n (int): Upper bound of the guessing range.

        Returns:
            int: The picked number.
        """
        return self.strategy.solve(n)


# ───────────────────────────────────────────────────────────────────────────
# Usage Suite (Illustrative)
# ───────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # In LeetCode, the guess API is provided by the system.
    # Here we simulate for demonstration.
    pick = 6

    def guess(num: int) -> int:
        if num > pick:
            return -1
        elif num < pick:
            return 1
        else:
            return 0

    solution = Solution()
    print(solution.guessNumber(10))  # Expected: 6
