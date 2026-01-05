"""
216. Combination Sum III

Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.


Example 1:
Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.

Example 2:
Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.

Example 3:
Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.

Constraints:
2 <= k <= 9
1 <= n <= 60

Topics
Array
Backtracking


Developer Insights
Problem Nature
We must find all unique combinations of k numbers (from 1–9) that sum to n.
Each number can be used at most once.
Order of numbers in a combination doesn’t matter.
Backtracking is the natural fit: explore subsets incrementally, prune invalid paths.

Key Observations
Numbers are limited to 1–9 → small search space.
Each path must have exactly k numbers.
Pruning:
If current sum > n, stop exploring.
If path length > k, stop exploring.
Edge case: if smallest possible sum with k numbers > n, return empty.

Strategy
Use backtracking with parameters (start, path, remaining_sum).
At each step:
If len(path) == k and remaining_sum == 0 → add path to results.
Iterate from start to 9:
Append number to path.
Recurse with updated sum and next start.
Backtrack (remove last number).
Return results.

Complexity
Time: O(C(9, k)) in worst case (choose k numbers from 9).
Space: O(k) recursion depth + O(number of valid combinations).

Edge Cases
n too small or too large → return empty.
k = 2, n = 18 → only [9, 9] invalid since duplicates not allowed → empty.
k = 9, n = 45 → only [1..9] valid.


Pseudocode

function combinationSum3(k, n):
    result = []

    function backtrack(start, path, remaining):
        if len(path) == k and remaining == 0:
            result.append(path.copy())
            return
        if len(path) > k or remaining < 0:
            return

        for num in range(start, 10):
            path.append(num)
            backtrack(num + 1, path, remaining - num)
            path.pop()

    backtrack(1, [], n)
    return result


"""

from typing import List, Protocol


# ───────────────────────────────────────────────────────────────────────────
# Strategy Interface
# ───────────────────────────────────────────────────────────────────────────

class CombinationSumStrategy(Protocol):
    """
    Protocol defining the interface for combination sum strategies.
    """
    def solve(self, k: int, n: int) -> List[List[int]]: ...


# ───────────────────────────────────────────────────────────────────────────
# Backtracking Strategy
# ───────────────────────────────────────────────────────────────────────────

class BacktrackingCombinationSumStrategy:
    """
    Backtracking strategy for Combination Sum III.

    Design:
        - Explore combinations incrementally.
        - Prune paths exceeding target sum or length.
        - Ensure uniqueness by iterating forward only.

    Time Complexity: O(C(9, k))
    Space Complexity: O(k) recursion depth + O(number of valid combinations)
    """

    def solve(self, k: int, n: int) -> List[List[int]]:
        result: List[List[int]] = []

        def backtrack(start: int, path: List[int], remaining: int) -> None:
            if len(path) == k and remaining == 0:
                result.append(path.copy())
                return
            if len(path) > k or remaining < 0:
                return

            for num in range(start, 10):
                path.append(num)
                backtrack(num + 1, path, remaining - num)
                path.pop()

        backtrack(1, [], n)
        return result


# ───────────────────────────────────────────────────────────────────────────
# Orchestrator — Clean Architecture
# ───────────────────────────────────────────────────────────────────────────

class Solution:
    """
    Orchestrates Combination Sum III computation by delegating to a strategy.

    - Separation of concerns: orchestration vs. computation
    - Dependency injection: strategy is swappable
    - Defaults to Backtracking strategy
    """

    def __init__(self, strategy: CombinationSumStrategy = None) -> None:
        self.strategy = strategy if strategy is not None else BacktrackingCombinationSumStrategy()

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        """
        Entry point for LeetCode.

        Args:
            k (int): Number of elements in each combination.
            n (int): Target sum.

        Returns:
            List[List[int]]: All valid combinations.
        """
        return self.strategy.solve(k, n)


# ───────────────────────────────────────────────────────────────────────────
# Usage Suite
# ───────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    solution = Solution()

    print(solution.combinationSum3(3, 7))   # Expected: [[1, 2, 4]]
    print(solution.combinationSum3(3, 9))   # Expected: [[1,2,6],[1,3,5],[2,3,4]]
    print(solution.combinationSum3(4, 1))   # Expected: []
    print(solution.combinationSum3(3, 15))  # Example: [[1,5,9],[2,6,7],[4,5,6]]
