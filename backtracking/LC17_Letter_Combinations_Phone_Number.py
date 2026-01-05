"""
17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = "2"
Output: ["a","b","c"]

Constraints:
1 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].

Topics
Hash Table
String
Backtracking


Developer Insights
Problem Nature
We must generate all possible letter combinations for a digit string (digits 2–9).
Each digit maps to a set of letters (like a phone keypad).
We need to explore all combinations → backtracking is the natural fit.
Constraints are small (digits.length ≤ 4), so exponential exploration is feasible.

Key Observations
Each digit contributes a branching factor equal to its mapped letters.
Total combinations = product of lengths of mappings.
Backtracking builds combinations incrementally and explores all paths.
Edge case: empty input → return empty list.

Strategy
Define a mapping from digits to letters.
Use backtracking:
Maintain a current path (string).
At each step, append one letter from the current digit’s mapping.
Recurse to the next digit.
When path length == digits length → add to results.
Return results.

Complexity
Time: O(3^n × 4^m), where n = count of digits mapping to 3 letters, m = count mapping to 4 letters.
Space: O(n) recursion depth + O(total combinations) for output.

Edge Cases
Empty string → return [].
Single digit → return its mapped letters.
Digits with 4 letters (7, 9) → ensure mapping correctness.


Pseudocode

function letterCombinations(digits):
    if digits is empty:
        return []

    mapping = {
        '2': "abc", '3': "def", '4': "ghi",
        '5': "jkl", '6': "mno", '7': "pqrs",
        '8': "tuv", '9': "wxyz"
    }

    result = []

    function backtrack(index, path):
        if index == len(digits):
            result.append(path)
            return

        for letter in mapping[digits[index]]:
            backtrack(index + 1, path + letter)

    backtrack(0, "")
    return result


"""

from typing import List, Protocol


# ───────────────────────────────────────────────────────────────────────────
# Strategy Interface
# ───────────────────────────────────────────────────────────────────────────

class CombinationStrategy(Protocol):
    """
    Protocol defining the interface for letter combination strategies.
    """
    def solve(self, digits: str) -> List[str]: ...


# ───────────────────────────────────────────────────────────────────────────
# Backtracking Strategy
# ───────────────────────────────────────────────────────────────────────────

class BacktrackingCombinationStrategy:
    """
    Backtracking strategy for generating letter combinations of a phone number.

    Design:
        - Use recursion to explore all possible paths.
        - Each digit expands into its mapped letters.
        - Build combinations incrementally until full length is reached.

    Time Complexity: O(3^n × 4^m)
    Space Complexity: O(n) recursion depth + O(total combinations)
    """

    digit_map = {
        '2': "abc", '3': "def", '4': "ghi",
        '5': "jkl", '6': "mno", '7': "pqrs",
        '8': "tuv", '9': "wxyz"
    }

    def solve(self, digits: str) -> List[str]:
        if not digits:
            return []

        result: List[str] = []

        def backtrack(index: int, path: str) -> None:
            if index == len(digits):
                result.append(path)
                return

            for letter in self.digit_map[digits[index]]:
                backtrack(index + 1, path + letter)

        backtrack(0, "")
        return result


# ───────────────────────────────────────────────────────────────────────────
# Orchestrator — Clean Architecture
# ───────────────────────────────────────────────────────────────────────────

class Solution:
    """
    Orchestrates letter combination generation by delegating to a strategy.

    - Separation of concerns: orchestration vs. computation
    - Dependency injection: strategy is swappable
    - Defaults to Backtracking strategy
    """

    def __init__(self, strategy: CombinationStrategy = None) -> None:
        self.strategy = strategy if strategy is not None else BacktrackingCombinationStrategy()

    def letterCombinations(self, digits: str) -> List[str]:
        """
        Entry point for LeetCode.

        Args:
            digits (str): Input digit string (2–9).

        Returns:
            List[str]: All possible letter combinations.
        """
        return self.strategy.solve(digits)


# ───────────────────────────────────────────────────────────────────────────
# Usage Suite
# ───────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    solution = Solution()

    print(solution.letterCombinations("23"))  # Expected: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    print(solution.letterCombinations("2"))   # Expected: ["a","b","c"]
    print(solution.letterCombinations(""))    # Expected: []
