"""
724. Find Pivot Index

Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
Return the leftmost pivot index. If no such index exists, return -1.


Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
Example 3:

Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0
 

Constraints:

1 <= nums.length <= 104
-1000 <= nums[i] <= 1000


Note: This question is the same as 1991: https://leetcode.com/problems/find-the-middle-index-in-array/


Topics
Array
Prefix Sum


Hint 1
Create an array sumLeft where sumLeft[i] is the sum of all the numbers to the left of index i.
Hint 2
Create an array sumRight where sumRight[i] is the sum of all the numbers to the right of index i.
Hint 3
For each index i, check if sumLeft[i] equals sumRight[i]. If so, return i. If no such i is found, return -1.


Key Developer Insights

The pivot index is where:
	left_sum=total_sum−left_sum−current_element
We can compute the total sum once, then iterate while maintaining a running left sum.
No need for extra arrays—just prefix tracking.

Pseudocode (Grounded in Our Principles)

function pivot_index(nums):
    total = sum(nums)
    left_sum = 0

    for i from 0 to len(nums) - 1:
        if left_sum == total - left_sum - nums[i]:
            return i
        left_sum += nums[i]

    return -1
"""

from typing import List, Protocol

class PivotStrategy(Protocol):
    def pivot_index(self, nums: List[int]) -> int: ...

class PrefixSumPivotStrategy:
    """
    SRP: Encapsulates prefix sum logic for pivot index detection.
    OCP: Can extend with full prefix array or binary search variants.
    """
    def pivot_index(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0

        for i, num in enumerate(nums):
            if left_sum == total - left_sum - num:
                return i
            left_sum += num

        return -1

class Solution:
    """
    High-level interface depending on abstraction (strategy).
    """
    def __init__(self, strategy: PivotStrategy = PrefixSumPivotStrategy()) -> None:
        self.strategy = strategy
    
    def pivotIndex(self, nums: List[int]) -> int:
        return self.strategy.pivot_index(nums)


# Usage
solver = Solution()
print(solver.pivotIndex([1,7,3,6,5,6]))  # 3
print(solver.pivotIndex([1,2,3]))        # -1
print(solver.pivotIndex([2,1,-1]))       # 0
