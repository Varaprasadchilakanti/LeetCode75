"""
643. Maximum Average Subarray I

You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.


Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
 

Constraints:

n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104

Topics
Array
Sliding Window


Key Developer Insights

We need the maximum average of any contiguous subarray of length k.
Brute force (checking all subarrays) would be 𝑂(𝑛⋅𝑘), too slow for 𝑛=10^5.
Optimal approach:
Use a sliding window of size k.
Compute the sum of the first k elements.
Slide the window across the array, updating the sum in 𝑂(1) per step.
Track the maximum sum, then divide by k.


Pseudocode (Grounded in Our Principles)

function find_max_average(nums, k):
    window_sum = sum of first k elements
    max_sum = window_sum

    for i from k to len(nums) - 1:
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum / k
"""

from typing import List, Protocol

class MaxAverageStrategy(Protocol):
    def find_max_average(self, nums: List[int], k: int) -> float: ...

class SlidingWindowMaxAverage:
    """
    SRP: Encapsulates sliding window logic for maximum average subarray.
    OCP: Can extend with prefix-sum or segment-tree variants.
    """
    def find_max_average(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)

        return max_sum / k

class Solution:
    """
    High-level interface depending on abstraction (strategy).
    """
    def __init__(self, strategy: MaxAverageStrategy = SlidingWindowMaxAverage()) -> None:
        self.strategy = strategy
    
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        return self.strategy.find_max_average(nums, k)



# Usage

solver = Solution()
print(solver.findMaxAverage([1,12,-5,-6,50,3], 4))  # 12.75
print(solver.findMaxAverage([5], 1))               # 5.0
