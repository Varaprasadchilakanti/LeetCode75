"""
151. Reverse Words in a String

Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.
Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

Constraints:

1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.

Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?

Topics
Two Pointers, String

Pseudocode
function reverseWords(s):
    words = split s by whitespace
    filtered = remove empty strings
    reversed = reverse the list
    return join with single space

"""

from typing import Protocol

class WordReversalStrategy(Protocol):
    def reverse_words(self, s: str) -> str: ...

class SplitReverseJoinStrategy:
    """
    SRP: Encapsulates word reversal logic using split-filter-reverse-join.
    OCP: Can extend with in-place or regex-based strategies.
    """
    def reverse_words(self, s: str) -> str:
        # Split by whitespace, filter out empty strings, reverse, join
        return " ".join(reversed(s.split()))

class Solution:
    """
    High-level interface depending on abstraction (strategy).
    """
    def __init__(self, strategy: WordReversalStrategy = SplitReverseJoinStrategy()) -> None:
        self.strategy = strategy
    
    def reverseWords(self, s: str) -> str:
        return self.strategy.reverse_words(s)


"""
Key Developer Insights
Core Task: Reverse the order of words, not characters.

Edge Cases:
Multiple spaces between words
Leading/trailing spaces

Optimal Strategy:
Split → Filter → Reverse → Join
Use built-in string methods for clarity and performance
"""


# Usage

solver = Solution()
print(solver.reverseWords("the sky is blue"))       # "blue is sky the"
print(solver.reverseWords("  hello world  "))       # "world hello"
print(solver.reverseWords("a good   example"))      # "example good a"

"""
Follow-Up (In-Place O(1) Space)
In Python, strings are immutable, so true in-place isn’t possible.
But in languages like C++, you can:
Trim spaces
Reverse entire string
Reverse each word individually
"""
