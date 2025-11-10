"""
345. Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.

Topics
Two Pointers, String

Pseudocode
function reverseVowels(s):
    convert s to list (since strings are immutable)
    left = 0, right = len(s) - 1
    while left < right:
        move left forward until vowel
        move right backward until vowel
        swap s[left] and s[right]
        left++, right--
    return joined list as string
"""

from typing import Protocol

class VowelReversalStrategy(Protocol):
    def reverse_vowels(self, s: str) -> str: ...

class TwoPointerVowelReversal:
    """
    SRP: Encapsulates vowel reversal logic using two-pointer strategy.
    OCP: Can extend with regex-based or stack-based strategies.
    """
    def reverse_vowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        chars = list(s)
        left, right = 0, len(chars) - 1

        while left < right:
            while left < right and chars[left] not in vowels:
                left += 1
            while left < right and chars[right] not in vowels:
                right -= 1
            if left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1

        return "".join(chars)

class Solution:
    """
    High-level interface depending on abstraction (strategy).
    """
    def __init__(self, strategy: VowelReversalStrategy = TwoPointerVowelReversal()) -> None:
        self.strategy = strategy
    
    def reverseVowels(self, s: str) -> str:
        return self.strategy.reverse_vowels(s)


"""
Key Developer Insights
Goal: Reverse only the vowels in the string.
Constraints: Up to 300,000 characters → must be O(n) time, O(n) space.
Vowels: Case-insensitive match (a, e, i, o, u + uppercase variants).
Optimal Strategy: Use two pointers to swap vowels from both ends.
"""


# Usage

solver = Solution()
print(solver.reverseVowels("IceCreAm"))   # "AceCreIm"
print(solver.reverseVowels("leetcode"))   # "leotcede"
print(solver.reverseVowels("aA"))         # "Aa"

"""
Takeaway
Your original code had issues with:
String immutability (s[i] = ... is invalid).
Incorrect slicing (a = a[-1::] gives only one character).
Misaligned indexing between a and s.
"""
