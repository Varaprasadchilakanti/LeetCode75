"""
1143. Longest Common Subsequence
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 
Constraints:
1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.

Topics
String
Dynamic Programming

Hint 1
Try dynamic programming. DP[i][j] represents the longest common subsequence of text1[0 ... i] & text2[0 ... j].
Hint 2
DP[i][j] = DP[i - 1][j - 1] + 1 , if text1[i] == text2[j] DP[i][j] = max(DP[i - 1][j], DP[i][j - 1]) , otherwise


Developer Insights
Problem Nature
We must compute the length of the longest common subsequence (LCS) between two strings:
Subsequence: characters in relative order, not necessarily contiguous.
Common subsequence: appears in both strings.
This is a DP‑multidimensional problem: state depends on prefixes of both strings.

Key Observations
Define dp[i][j] = LCS length of text1[:i] and text2[:j].
Transition:
If text1[i-1] == text2[j-1]:
𝑑𝑝[𝑖][𝑗]=𝑑𝑝[𝑖−1][𝑗−1]+1
Else:
𝑑𝑝[𝑖][𝑗]=max⁡(𝑑𝑝[𝑖−1][𝑗],𝑑𝑝[𝑖][𝑗−1])
Base case: dp[0][*] = dp[*][0] = 0.
Answer: dp[m][n] where m = len(text1), n = len(text2).

Strategy
Initialize a 2D DP table (m+1) × (n+1) with zeros.
Fill table using recurrence.
Return dp[m][n].
Optimize space to O(min(m, n)) if needed.

Complexity
Time: O(m × n)
Space: O(m × n) (or O(min(m, n)) with optimization)

Edge Cases
One string empty → result = 0.
Identical strings → result = length of string.
Completely disjoint strings → result = 0.
Large strings (length ≤ 1000) → DP handles efficiently.

Pseudocode
function longestCommonSubsequence(text1, text2):
    m = len(text1)
    n = len(text2)
    dp = 2D array (m+1) × (n+1) initialized to 0

    for i in range(1, m+1):
        for j in range(1, n+1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]

"""

from typing import Protocol


# ───────────────────────────────────────────────────────────────────────────
# Strategy Interface
# ───────────────────────────────────────────────────────────────────────────

class LCSStrategy(Protocol):
    """
    Protocol defining the interface for longest common subsequence strategies.
    """
    def solve(self, text1: str, text2: str) -> int: ...


# ───────────────────────────────────────────────────────────────────────────
# DP Strategy
# ───────────────────────────────────────────────────────────────────────────

class DPLCSStrategy:
    """
    Dynamic Programming strategy for computing the longest common subsequence (LCS).

    Design:
        - State: dp[i][j] = LCS length of text1[:i] and text2[:j]
        - Transition:
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        - Base case: dp[0][*] = dp[*][0] = 0
        - Result: dp[m][n]

    Time Complexity: O(m × n)
    Space Complexity: O(m × n) (can be optimized to O(min(m, n)))
    """

    def solve(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]


# ───────────────────────────────────────────────────────────────────────────
# Orchestrator — Clean Architecture
# ───────────────────────────────────────────────────────────────────────────

class Solution:
    """
    Orchestrates LCS computation by delegating to a strategy.

    - Separation of concerns: orchestration vs. computation
    - Dependency injection: strategy is swappable
    - Defaults to DP strategy
    """

    def __init__(self, strategy: LCSStrategy = None) -> None:
        self.strategy = strategy if strategy is not None else DPLCSStrategy()

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Entry point for LeetCode.

        Args:
            text1 (str): First string.
            text2 (str): Second string.

        Returns:
            int: Length of the longest common subsequence.
        """
        return self.strategy.solve(text1, text2)


# ───────────────────────────────────────────────────────────────────────────
# Usage Suite
# ───────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    solution = Solution()

    print(solution.longestCommonSubsequence("abcde", "ace"))   # Expected: 3
    print(solution.longestCommonSubsequence("abc", "abc"))     # Expected: 3
    print(solution.longestCommonSubsequence("abc", "def"))     # Expected: 0
    print(solution.longestCommonSubsequence("xyz", "xzy"))     # Expected: 2
