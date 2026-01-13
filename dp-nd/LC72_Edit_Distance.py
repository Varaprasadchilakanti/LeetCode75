#!/usr/bin/env python3
"""
72. Edit Distance

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
You have the following three operations permitted on a word:
Insert a character
Delete a character
Replace a character

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

Constraints:
0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.

Topics
String
Dynamic Programming


Developer Insights
Problem Nature
We must compute the minimum number of operations (insert, delete, replace) to convert word1 into word2.
This is a DP‑multidimensional problem: state depends on prefixes of both strings.

Key Observations
Define dp[i][j] = minimum edit distance between word1[:i] and word2[:j].
Transitions:

If word1[i-1] == word2[j-1]:
𝑑𝑝[𝑖][𝑗]=𝑑𝑝[𝑖−1][𝑗−1]
Else:
𝑑𝑝[𝑖][𝑗]=1+min⁡(𝑑𝑝[𝑖−1][𝑗],𝑑𝑝[𝑖][𝑗−1],𝑑𝑝[𝑖−1][𝑗−1])

dp[i-1][j]: delete from word1.
dp[i][j-1]: insert into word1.
dp[i-1][j-1]: replace character.

Base cases:
dp[0][j] = j (convert empty string to prefix of word2 → j inserts).
dp[i][0] = i (convert prefix of word1 to empty string → i deletes).
Answer: dp[m][n].

Strategy
Initialize DP table (m+1) × (n+1).
Fill base cases.
Iteratively compute transitions.
Return dp[m][n].
Optimize space to O(min(m, n)) if needed.

Complexity
Time: O(m × n)
Space: O(m × n) (or O(min(m, n)) with optimization)

Edge Cases
One string empty → result = length of other string.
Identical strings → result = 0.
Completely disjoint strings → result = max(len(word1), len(word2)).
Large strings (≤ 500) → DP handles efficiently.


Pseudocode
function minDistance(word1, word2):
    m = len(word1)
    n = len(word2)
    dp = 2D array (m+1) × (n+1)

    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j

    for i in range(1, m+1):
        for j in range(1, n+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

    return dp[m][n]

"""

from typing import Protocol


# ───────────────────────────────────────────────────────────────────────────
# Strategy Interface
# ───────────────────────────────────────────────────────────────────────────

class EditDistanceStrategy(Protocol):
    """
    Protocol defining the interface for edit distance strategies.
    """
    def solve(self, word1: str, word2: str) -> int: ...


# ───────────────────────────────────────────────────────────────────────────
# DP Strategy
# ───────────────────────────────────────────────────────────────────────────

class DPEditDistanceStrategy:
    """
    Dynamic Programming strategy for computing edit distance between two strings.

    Design:
        - State: dp[i][j] = min operations to convert word1[:i] → word2[:j]
        - Transition:
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        - Base cases:
            dp[i][0] = i
            dp[0][j] = j
        - Result: dp[m][n]

    Time Complexity: O(m × n)
    Space Complexity: O(m × n)
    """

    def solve(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],     # delete
                        dp[i][j - 1],     # insert
                        dp[i - 1][j - 1]  # replace
                    )

        return dp[m][n]


# ───────────────────────────────────────────────────────────────────────────
# Orchestrator — Clean Architecture
# ───────────────────────────────────────────────────────────────────────────

class Solution:
    """
    Orchestrates edit distance computation by delegating to a strategy.

    - Separation of concerns: orchestration vs. computation
    - Dependency injection: strategy is swappable
    - Defaults to DP strategy
    """

    def __init__(self, strategy: EditDistanceStrategy = None) -> None:
        self.strategy = strategy if strategy is not None else DPEditDistanceStrategy()

    def minDistance(self, word1: str, word2: str) -> int:
        """
        Entry point for LeetCode.

        Args:
            word1 (str): First string.
            word2 (str): Second string.

        Returns:
            int: Minimum number of operations to convert word1 → word2.
        """
        return self.strategy.solve(word1, word2)


# ───────────────────────────────────────────────────────────────────────────
# Usage Suite
# ───────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    solution = Solution()

    print(solution.minDistance("horse", "ros"))        # Expected: 3
    print(solution.minDistance("intention", "execution"))  # Expected: 5
    print(solution.minDistance("", "abc"))             # Expected: 3
    print(solution.minDistance("abc", ""))             # Expected: 3
    print(solution.minDistance("abc", "abc"))          # Expected: 0
