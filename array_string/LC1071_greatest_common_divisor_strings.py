"""
1071. Greatest Common Divisor of Strings

For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""

Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.


Topics
Math, String, Weekly Contest 139

Hint 1
The greatest common divisor must be a prefix of each string, so we can try all prefixes.

Pseudocode
function gcdOfStrings(str1, str2):
    if str1 + str2 != str2 + str1:
        return ""
    length = gcd(len(str1), len(str2))
    return str1[0:length]
"""

from math import gcd
from typing import Protocol

class StringGCDStrategy(Protocol):
    def gcd_of_strings(self, str1: str, str2: str) -> str: ...

class ConcatenationCheckGCD:
    """
    SRP: Encapsulates the logic for finding GCD of strings.
    OCP: Can extend with other strategies (e.g., iterative checking).
    """
    def gcd_of_strings(self, str1: str, str2: str) -> str:
        # If concatenations mismatch, no common divisor exists
        if str1 + str2 != str2 + str1:
            return ""
        # Use math.gcd on lengths to find largest repeating unit
        length = gcd(len(str1), len(str2))
        return str1[:length]

class Solution:
    """
    High-level interface depending on abstraction (strategy).
    """
    def __init__(self, strategy: StringGCDStrategy = ConcatenationCheckGCD()) -> None:
        self.strategy = strategy
    
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        return self.strategy.gcd_of_strings(str1, str2)



# Usage

solver = Solution()
print(solver.gcdOfStrings("ABCABC", "ABC"))     # "ABC"
print(solver.gcdOfStrings("ABABAB", "ABAB"))    # "AB"
print(solver.gcdOfStrings("LEET", "CODE"))      # ""


"""
Takeaway

The mathematical gcd trick makes this problem optimal.
Wrapping it in a strategy-based design keeps it extensible and clean.
This template can be reused for other string/array gcd/lcm style problems.
"""
