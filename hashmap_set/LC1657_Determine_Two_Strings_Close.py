"""
1657. Determine if Two Strings Are Close

Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.


Example 1:

Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"
Example 2:

Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.
Example 3:

Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"


Constraints:

1 <= word1.length, word2.length <= 105
word1 and word2 contain only lowercase English letters.

Topics
Hash Table
String
Sorting
Counting

Hint 1
Operation 1 allows you to freely reorder the string.
Hint 2
Operation 2 allows you to freely reassign the letters' frequencies.


Key Developer Insights
Two strings are close if:
Same set of characters
Because Operation 2 only allows swapping existing characters.
If word1 has a character not in word2, transformation is impossible.
Same multiset of frequencies (up to permutation)
Operation 1 allows reordering freely.
Operation 2 allows swapping frequencies between characters.
So the actual frequency distribution must match, even if assigned to different characters.


Pseudocode (Grounded in Our Principles)

function close_strings(word1, word2):
    if length(word1) != length(word2):
        return False

    freq1 = frequency_map(word1)
    freq2 = frequency_map(word2)

    if set(freq1.keys()) != set(freq2.keys()):
        return False

    if sorted(freq1.values()) != sorted(freq2.values()):
        return False

    return True
"""

from typing import Protocol
from collections import Counter

class CloseStringsStrategy(Protocol):
    def close_strings(self, word1: str, word2: str) -> bool: ...

class FrequencySetCloseStringsStrategy:
    """
    SRP: Encapsulates logic for determining if two strings are 'close'.
    OCP: Can extend with alternative checks (e.g., streaming frequency).
    """
    def close_strings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        freq1, freq2 = Counter(word1), Counter(word2)

        # Condition 1: Same set of characters
        if set(freq1.keys()) != set(freq2.keys()):
            return False

        # Condition 2: Same frequency distribution
        if sorted(freq1.values()) != sorted(freq2.values()):
            return False

        return True

class Solution:
    """
    High-level interface depending on abstraction (strategy).
    """
    def __init__(self, strategy: CloseStringsStrategy = FrequencySetCloseStringsStrategy()) -> None:
        self.strategy = strategy
    
    def closeStrings(self, word1: str, word2: str) -> bool:
        return self.strategy.close_strings(word1, word2)


# Usage

solver = Solution()
print(solver.closeStrings("abc", "bca"))       # True
print(solver.closeStrings("a", "aa"))          # False
print(solver.closeStrings("cabbba", "abbccc")) # True
