"""
1004. Max Consecutive Ones III

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length

Topics
Array
Binary Search
Sliding Window
Prefix Sum

Hint 1
One thing's for sure, we will only flip a zero if it extends an existing window of 1s. Otherwise, there's no point in doing it, right? Think Sliding Window!
Hint 2
Since we know this problem can be solved using the sliding window construct, we might as well focus in that direction for hints. Basically, in a given window, we can never have > K zeros, right?
Hint 3
We don't have a fixed size window in this case. The window size can grow and shrink depending upon the number of zeros we have (we don't actually have to flip the zeros here!).
Hint 4
The way to shrink or expand a window would be based on the number of zeros that can still be flipped and so on.


Key Developer Insights
We want the longest subarray with at most k zeros flipped to ones.

Use a sliding window:
Expand the window while the number of zeros ≤ k.
Shrink the window from the left when zeros exceed k.
Track the maximum window size throughout.


Pseudocode (Grounded in Our Principles)

function longest_ones(nums, k):
    left = 0
    zero_count = 0
    max_length = 0

    for right from 0 to len(nums) - 1:
        if nums[right] == 0:
            increment zero_count

        while zero_count > k:
            if nums[left] == 0:
                decrement zero_count
            increment left

        update max_length as right - left + 1

    return max_length
"""

from typing import List, Protocol

class FlipWindowStrategy(Protocol):
    def longest_ones(self, nums: List[int], k: int) -> int: ...

class SlidingWindowFlipStrategy:
    """
    SRP: Encapsulates sliding window logic for flipping at most k zeros.
    OCP: Can extend with prefix-sum or binary search variants.
    """
    def longest_ones(self, nums: List[int], k: int) -> int:
        left = 0
        zero_count = 0
        max_length = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length

class Solution:
    """
    High-level interface depending on abstraction (strategy).
    """
    def __init__(self, strategy: FlipWindowStrategy = SlidingWindowFlipStrategy()) -> None:
        self.strategy = strategy
    
    def longestOnes(self, nums: List[int], k: int) -> int:
        return self.strategy.longest_ones(nums, k)



# Usage

solver = Solution()
print(solver.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))  # 6
print(solver.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))  # 10
