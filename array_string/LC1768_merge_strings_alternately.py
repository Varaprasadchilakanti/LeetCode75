'''
1768. Merge Strings Alternately

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d

Constraints:

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.

Topics
Two Pointers, String, Weekly Contest 229

Hint 1
Use two pointers, one pointer for each string. Alternately choose the character from each pointer, and move the pointer upwards.

Pseudocode
function merge_alternately(word1, word2):
    initialize i = 0, j = 0
    initialize merged as empty list

    while i < length of word1 or j < length of word2:
        if i < length of word1:
            append word1[i] to merged
            increment i
        if j < length of word2:
            append word2[j] to merged
            increment j

    return joined string from merged list

'''

from typing import Protocol


class MergerStrategy(Protocol):
    def merge(self, word1: str, word2: str) -> str: ...


class AlternatingMerger:
    """
    Single Responsibility: Encapsulates alternating merge logic.
    Open/Closed: Can extend with other merge strategies (e.g., start with word2).
    """

    def merge(self, word1: str, word2: str) -> str:
        i = j = 0
        merged = []

        while i < len(word1) or j < len(word2):
            if i < len(word1):
                merged.append(word1[i])
                i += 1
            if j < len(word2):
                merged.append(word2[j])
                j += 1

        return "".join(merged)


class Solution:
    """
    High-level interface depending on abstraction (strategy).
    """

    def __init__(self, strategy: MergerStrategy = AlternatingMerger()) -> None:
        self.strategy = strategy

    def mergeAlternately(self, word1: str, word2: str) -> str:
        return self.strategy.merge(word1, word2)


# Usage

solver = Solution()
print(solver.mergeAlternately("abc", "pqr"))   # "apbqcr"
print(solver.mergeAlternately("ab", "pqrs"))   # "apbqrs"
print(solver.mergeAlternately("abcd", "pq"))   # "apbqcd"


"""
Optional: Pythonic One‑Liner (for reference)
from itertools import zip_longest

class OneLinerMerger:
    def merge(self, word1: str, word2: str) -> str:
        return "".join(a + b if b else a for a, b in zip_longest(word1, word2, fillvalue=""))

"""
