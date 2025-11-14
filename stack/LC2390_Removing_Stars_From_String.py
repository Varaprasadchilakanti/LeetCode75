"""
2390. Removing Stars From a String

You are given a string s, which contains stars *.
In one operation, you can:
Choose a star in s.
Remove the closest non-star character to its left, as well as remove the star itself.
Return the string after all stars have been removed.

Note:
The input will be generated such that the operation is always possible.
It can be shown that the resulting string will always be unique.


Example 1:

Input: s = "leet**cod*e"
Output: "lecoe"
Explanation: Performing the removals from left to right:
- The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
- The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
- The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
There are no more stars, so we return "lecoe".
Example 2:

Input: s = "erase*****"
Output: ""
Explanation: The entire string is removed, so we return an empty string.
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters and stars *.
The operation above can be performed on s.

Topics
String
Stack
Simulation

Hint 1
What data structure could we use to efficiently perform these removals?
Hint 2
Use a stack to store the characters. Pop one character off the stack at each star. Otherwise, we push the character onto the stack.


Key Developer Insights
Each * removes itself and the closest non-star character to its left.
This is a natural fit for a stack:
Push characters onto the stack.
When encountering *, pop the last character (the closest non-star) and skip pushing the star.
At the end, the stack contains the final string.


Pseudocode

function remove_stars(s):
    stack = []

    for ch in s:
        if ch == '*':
            pop from stack
        else:
            push ch onto stack

    return join(stack)

"""

from typing import Protocol

class RemoveStarsStrategy(Protocol):
    def remove_stars(self, s: str) -> str: ...

class StackRemoveStarsStrategy:
    """
    SRP: Encapsulates stack-based logic for removing stars from a string.
    OCP: Can extend with in-place list mutation or two-pointer variants.
    """
    def remove_stars(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == '*':
                if stack:  # guaranteed by problem constraints
                    stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)

class Solution:
    """
    High-level interface depending on abstraction (strategy).
    """
    def __init__(self, strategy: RemoveStarsStrategy = StackRemoveStarsStrategy()) -> None:
        self.strategy = strategy
    
    def removeStars(self, s: str) -> str:
        return self.strategy.remove_stars(s)


# Usage

solver = Solution()
print(solver.removeStars("leet**cod*e"))   # "lecoe"
print(solver.removeStars("erase*****"))    # ""
