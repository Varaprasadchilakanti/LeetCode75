"""
334. Increasing Triplet Subsequence

Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: One of the valid triplet is (3, 4, 5), because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

Constraints:

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1

Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?

Topics
Array, Greedy

Pseudocode (Grounded in Our Principles)

function increasing_triplet(nums):
    first = infinity
    second = infinity

    for num in nums:
        if num <= first:
            first = num
        elif num <= second:
            second = num
        else:
            return True  # num > second > first

    return False
"""

from typing import List, Protocol

class TripletStrategy(Protocol):
    def has_increasing_triplet(self, nums: List[int]) -> bool: ...

class GreedyTripletStrategy:
    """
    SRP: Encapsulates greedy logic for detecting increasing triplet.
    OCP: Can extend with DP or stack-based variants.
    """
    def has_increasing_triplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True  # Found third > second > first

        return False

class Solution:
    """
    High-level interface depending on abstraction (strategy).
    """
    def __init__(self, strategy: TripletStrategy = GreedyTripletStrategy()) -> None:
        self.strategy = strategy
    
    def increasingTriplet(self, nums: List[int]) -> bool:
        return self.strategy.has_increasing_triplet(nums)


"""
Key Developer Insights
We’re looking for three increasing numbers at indices 𝑖<𝑗<𝑘.
We don’t need the actual triplet—just to know if one exists.
Greedy strategy: Track the smallest and second smallest numbers seen so far.
If we find a number greater than both → triplet exists.
"""


# Usage

solver = Solution()
print(solver.increasingTriplet([1,2,3,4,5]))       # True
print(solver.increasingTriplet([5,4,3,2,1]))       # False
print(solver.increasingTriplet([2,1,5,0,4,6]))     # True
