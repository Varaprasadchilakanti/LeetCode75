"""
283. Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you minimize the total number of operations done?

Topics
Array, Two Pointers

Hint 1
In-place means we should not be allocating any space for extra array. But we are allowed to modify the existing array. However, as a first step, try coming up with a solution that makes use of additional space. For this problem as well, first apply the idea discussed using an additional array and the in-place solution will pop up eventually.
Hint 2
A two-pointer approach could be helpful here. The idea would be to have one pointer for iterating the array and another pointer that just works on the non-zero elements of the array.


Key Developer Insights
Goal: Move all zeros to the end, preserving the order of non-zero elements.
Constraints: Must be done in-place, no extra array.
Optimal Strategy: Use two pointers:
write tracks where the next non-zero should go.
read scans the array.


Pseudocode (Grounded in Our Principles)

function move_zeroes(nums):
    write = 0

    for read from 0 to len(nums) - 1:
        if nums[read] != 0:
            nums[write] = nums[read]
            write += 1

    for i from write to len(nums) - 1:
        nums[i] = 0

"""

from typing import List, Protocol

class ZeroMoverStrategy(Protocol):
    def move_zeroes(self, nums: List[int]) -> None: ...

class TwoPointerZeroMover:
    """
    SRP: Encapsulates in-place zero shifting logic.
    OCP: Can extend with swap-based or stable-partition variants.
    """
    def move_zeroes(self, nums: List[int]) -> None:
        write = 0

        for read in range(len(nums)):
            if nums[read] != 0:
                nums[write] = nums[read]
                write += 1

        for i in range(write, len(nums)):
            nums[i] = 0

class Solution:
    """
    High-level interface depending on abstraction (strategy).
    """
    def __init__(self, strategy: ZeroMoverStrategy = TwoPointerZeroMover()) -> None:
        self.strategy = strategy
    
    def moveZeroes(self, nums: List[int]) -> None:
        self.strategy.move_zeroes(nums)



# Usage

solver = Solution()
nums = [0,1,0,3,12]
solver.moveZeroes(nums)
print(nums)  # [1,3,12,0,0]
