"""
443. String Compression

Given an array of characters chars, compress it using the following algorithm:
Begin with an empty string s. For each group of consecutive repeating characters in chars:
If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.
After you are done modifying the input array, return the new length of the array.
You must write an algorithm that uses only constant extra space.
Note: The characters in the array beyond the returned length do not matter and should be ignored.

Example 1:
Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

Example 2:
Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.

Example 3:
Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".

Constraints:

1 <= chars.length <= 2000
chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.

Topics
Two Pointers, String

Hint 1
How do you know if you are at the end of a consecutive group of characters?


Pseudocode (Grounded in Our Principles)

function compress(chars):
    initialize read = 0, write = 0

    while read < length of chars:
        start = read
        while read < length and chars[read] == chars[start]:
            read += 1
        count = read - start

        write chars[start] at write
        increment write

        if count > 1:
            for digit in str(count):
                write digit at write
                increment write

    return write
"""

from typing import List, Protocol

class CompressionStrategy(Protocol):
    def compress(self, chars: List[str]) -> int: ...

class InPlaceCompressionStrategy:
    """
    SRP: Encapsulates in-place string compression logic.
    OCP: Can extend with alternate encoding strategies.
    """
    def compress(self, chars: List[str]) -> int:
        read = write = 0
        n = len(chars)

        while read < n:
            start = read
            while read < n and chars[read] == chars[start]:
                read += 1
            count = read - start

            chars[write] = chars[start]
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write

class Solution:
    """
    High-level interface depending on abstraction (strategy).
    """
    def __init__(self, strategy: CompressionStrategy = InPlaceCompressionStrategy()) -> None:
        self.strategy = strategy
    
    def compress(self, chars: List[str]) -> int:
        return self.strategy.compress(chars)


"""
Key Developer Insights
We must compress in-place using constant extra space.

Use two pointers:
read to scan the input
write to overwrite compressed output

For each group of consecutive characters:
Write the character
If count > 1, write the digits of the count
"""


# Usage

solver = Solution()
chars = ["a","a","b","b","c","c","c"]
length = solver.compress(chars)
print(chars[:length])  # ['a','2','b','2','c','3']
