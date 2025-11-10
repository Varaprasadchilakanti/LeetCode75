"""
392. Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
 

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?

Topics
Two Pointers
String
Dynamic Programming


Key Developer Insights

A string s is a subsequence of t if we can walk through t and match all characters of s in order.
Use two pointers:
One for s, one for t
Advance s only when characters match
If s is exhausted → it's a subsequence


Pseudocode (Grounded in Our Principles)

function is_subsequence(s, t):
    i = 0  # pointer for s

    for char in t:
        if i == length of s:
            break
        if s[i] == char:
            i += 1

    return i == length of s

"""

from typing import Protocol

class SubsequenceStrategy(Protocol):
    def is_subsequence(self, s: str, t: str) -> bool: ...

class TwoPointerSubsequenceStrategy:
    """
    SRP: Encapsulates two-pointer logic for subsequence check.
    OCP: Can extend with binary search or indexed strategies for batch queries.
    """
    def is_subsequence(self, s: str, t: str) -> bool:
        i = 0
        for char in t:
            if i < len(s) and s[i] == char:
                i += 1
        return i == len(s)

class Solution:
    """
    High-level interface depending on abstraction (strategy).
    """
    def __init__(self, strategy: SubsequenceStrategy = TwoPointerSubsequenceStrategy()) -> None:
        self.strategy = strategy
    
    def isSubsequence(self, s: str, t: str) -> bool:
        return self.strategy.is_subsequence(s, t)



# Usage

solver = Solution()
print(solver.isSubsequence("abc", "ahbgdc"))  # True
print(solver.isSubsequence("axc", "ahbgdc"))  # False



"""
Follow-Up: Batch Queries (k ≥ 10⁹)
If t is fixed and many s_i are queried:
Preprocess t:
Build a map: char → sorted list of indices in t
For each s_i, use binary search to find increasing positions in t
Time per query: 
𝑂(𝑚log𝑛), where 𝑚 = len(𝑠_𝑖), 𝑛 = len(𝑡)

"""
