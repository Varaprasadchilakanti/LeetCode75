"""
394. Decode String

Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].
The test cases are generated so that the length of the output will never exceed 105.


Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"


Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].

Topics
String
Stack
Recursion


Key Developer Insights
The encoding rule is k[encoded_string].
Nested encodings are possible (3[a2[c]]).

Approach:
Use a stack to store partial results and repeat counts.
When encountering a digit, parse the full number.
When encountering [, push current string and repeat count.
When encountering ], pop from stack and expand.
Otherwise, append characters to the current string.


Pseudocode (Grounded in Our Principles)

function decode_string(s):
    stack = []
    current_str = ""
    current_num = 0

    for ch in s:
        if ch is digit:
            update current_num
        elif ch == '[':
            push (current_str, current_num) onto stack
            reset current_str, current_num
        elif ch == ']':
            prev_str, num = pop from stack
            current_str = prev_str + (current_str * num)
        else:
            append ch to current_str

    return current_str


"""

class DecodeStrategy:
    """
    SRP: Encapsulates stack-based decoding logic for encoded strings.
    OCP: Can extend with recursive or regex-based variants.
    """
    def decode(self, s: str) -> str:
        stack = []
        current_str = ""
        current_num = 0

        for ch in s:
            if ch.isdigit():
                current_num = current_num * 10 + int(ch)
            elif ch == '[':
                stack.append((current_str, current_num))
                current_str, current_num = "", 0
            elif ch == ']':
                prev_str, num = stack.pop()
                current_str = prev_str + current_str * num
            else:
                current_str += ch

        return current_str


class Solution:
    """
    High-level interface depending on abstraction (strategy).
    """
    def __init__(self, strategy: DecodeStrategy = DecodeStrategy()) -> None:
        self.strategy = strategy
    
    def decodeString(self, s: str) -> str:
        return self.strategy.decode(s)


# Usage

solver = Solution()
print(solver.decodeString("3[a]2[bc]"))       # "aaabcbc"
print(solver.decodeString("3[a2[c]]"))        # "accaccacc"
print(solver.decodeString("2[abc]3[cd]ef"))   # "abcabccdcdcdef"

