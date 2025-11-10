"""
1493. Longest Subarray of 1's After Deleting One Element

Given a binary array nums, you should delete one element from it.
Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.


Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.


Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.

Topics
Array
Dynamic Programming
Sliding Window

Hint 1
Maintain a sliding window where there is at most one zero in it.


Key Developer Insights
We must delete exactly one element, so the longest subarray must allow at most one zero.

Use a sliding window:
Expand the window while the number of zeros ≤ 1.
Shrink the window from the left when zeros exceed 1.
Track the maximum window size, subtracting one to account for the required deletion.


Pseudocode (Grounded in Our Principles)

function longest_subarray(nums):
    left = 0
    zero_count = 0
    max_length = 0

    for right from 0 to len(nums) - 1:
        if nums[right] == 0:
            increment zero_count

        while zero_count > 1:
            if nums[left] == 0:
                decrement zero_count
            increment left

        update max_length as right - left

    return max_length

"""

from typing import List, Protocol

class SubarrayStrategy(Protocol):
    def longest_subarray(self, nums: List[int]) -> int: ...

class SlidingWindowDeleteStrategy:
    """
    SRP: Encapsulates sliding window logic for longest 1s subarray after one deletion.
    OCP: Can extend with prefix-sum or DP variants.
    """
    def longest_subarray(self, nums: List[int]) -> int:
        left = 0
        zero_count = 0
        max_length = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            max_length = max(max_length, right - left)

        return max_length

class Solution:
    """
    High-level interface depending on abstraction (strategy).
    """
    def __init__(self, strategy: SubarrayStrategy = SlidingWindowDeleteStrategy()) -> None:
        self.strategy = strategy
    
    def longestSubarray(self, nums: List[int]) -> int:
        return self.strategy.longest_subarray(nums)


# Usage

solver = Solution()
print(solver.longestSubarray([1,1,0,1]))                     # 3
print(solver.longestSubarray([0,1,1,1,0,1,1,0,1]))           # 5
print(solver.longestSubarray([1,1,1]))                       # 2
