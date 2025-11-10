"""
1456. Maximum Number of Vowels in a Substring of Given Length

Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.


Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length

Topics
String
Sliding Window

Hint 1
Keep a window of size k and maintain the number of vowels in it.
Hint 2
Keep moving the window and update the number of vowels while moving. Answer is max number of vowels of any window.


Key Developer Insights
We need the maximum number of vowels in any substring of length k.
Brute force would check every substring → 𝑂(𝑛⋅𝑘), too slow.

Optimal strategy:
Use a sliding window of size k.
Track the vowel count in the current window.
Slide the window forward, updating the count in 𝑂(1) per step.

Pseudocode (Grounded in Our Principles)

function max_vowels(s, k):
    define vowels as set('aeiou')
    count = number of vowels in first k characters
    max_count = count

    for i from k to len(s) - 1:
        if s[i - k] is vowel:
            decrement count
        if s[i] is vowel:
            increment count
        update max_count if count is greater

    return max_count
"""

from typing import Protocol

class VowelWindowStrategy(Protocol):
    def max_vowels(self, s: str, k: int) -> int: ...

class SlidingWindowVowelStrategy:
    """
    SRP: Encapsulates sliding window logic for vowel counting.
    OCP: Can extend with prefix-sum or regex-based variants.
    """
    def max_vowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        count = sum(1 for ch in s[:k] if ch in vowels)
        max_count = count

        for i in range(k, len(s)):
            if s[i - k] in vowels:
                count -= 1
            if s[i] in vowels:
                count += 1
            max_count = max(max_count, count)

        return max_count

class Solution:
    """
    High-level interface depending on abstraction (strategy).
    """
    def __init__(self, strategy: VowelWindowStrategy = SlidingWindowVowelStrategy()) -> None:
        self.strategy = strategy
    
    def maxVowels(self, s: str, k: int) -> int:
        return self.strategy.max_vowels(s, k)


# Usage

solver = Solution()
print(solver.maxVowels("abciiidef", 3))   # 3
print(solver.maxVowels("aeiou", 2))       # 2
print(solver.maxVowels("leetcode", 3))    # 2
