"""
11. Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104

Topics
Array
Two Pointers
Greedy

Hint 1
If you simulate the problem, it will be O(n^2) which is not efficient.
Hint 2
Try to use two-pointers. Set one pointer to the left and one to the right of the array. Always move the pointer that points to the lower line.
Hint 3
How can you calculate the amount of water at each step?


Key Developer Insights
The area between two lines is determined by:
Area=min(height[𝑖],height[𝑗])⋅(𝑗−𝑖)

To maximize area:
Start with the widest container (left = 0, right = n - 1)
Move the pointer pointing to the shorter line, hoping to find a taller one
This greedy approach avoids 𝑂(𝑛^2) brute-force comparisons


Pseudocode (Grounded in Our Principles)

function max_area(height):
    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:
        current_area = min(height[left], height[right]) * (right - left)
        update max_area if current_area is larger

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area

"""


from typing import List, Protocol

class ContainerStrategy(Protocol):
    def max_area(self, height: List[int]) -> int: ...

class TwoPointerContainerStrategy:
    """
    SRP: Encapsulates two-pointer logic for max water container.
    OCP: Can extend with brute-force or segment-tree variants.
    """
    def max_area(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            h = min(height[left], height[right])
            w = right - left
            max_area = max(max_area, h * w)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

class Solution:
    """
    High-level interface depending on abstraction (strategy).
    """
    def __init__(self, strategy: ContainerStrategy = TwoPointerContainerStrategy()) -> None:
        self.strategy = strategy
    
    def maxArea(self, height: List[int]) -> int:
        return self.strategy.max_area(height)


"""
==============================================================
                 Trapping Rain Water — Fluid View
==============================================================

Heights: [1, 8, 6, 2, 5, 4, 8, 3, 7]

                ~ ~ ~ ~ ~ ~ ~ ~ ~
                |               |
                |     |         |
                |  |  |  |      |
                |  |  |  |  |   |
                |  |  |  |  | | |
                |  |  |  |  | | |
         |      |  |  |  |  | | |
   |     |  |   |  |  |  |  | | |   |
___|_____|__|___|__|__|__|__|_|_|___|____
  1     8   6   2   5   4   8   3   7

Legend:
    | = building/bar height
    ~ = trapped rainwater surface (steady-state level)
    _ = ground
    space = air

Concept:
    In fluid mechanics, water seeks an equal level between boundaries.
    Tall walls hold the water, valleys store it. The trapped volume
    corresponds to the total area under the '~' but above lower bars.

==============================================================
"""



# Usage

solver = Solution()
print(solver.maxArea([1,8,6,2,5,4,8,3,7]))  # 49
print(solver.maxArea([1,1]))               # 1

