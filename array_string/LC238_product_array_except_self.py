"""
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.


Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.


Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

Topics
Array, Prefix Sum

Hint 1
Think how you can efficiently utilize prefix and suffix products to calculate the product of all elements except self for each index. Can you pre-compute the prefix and suffix products in linear time to avoid redundant calculations?
Hint 2
Can you minimize additional space usage by reusing memory or modifying the input array to store intermediate results?


Pseudocode
function product_except_self(nums):
    initialize output array of size len(nums) with 1s

    # First pass: prefix products
    prefix = 1
    for i from 0 to len(nums) - 1:
        output[i] = prefix
        prefix *= nums[i]

    # Second pass: suffix products
    suffix = 1
    for i from len(nums) - 1 to 0:
        output[i] *= suffix
        suffix *= nums[i]

    return output
"""

from typing import List, Protocol

class ProductStrategy(Protocol):
    def product_except_self(self, nums: List[int]) -> List[int]: ...

class PrefixSuffixProductStrategy:
    """
    SRP: Encapsulates prefix-suffix product logic.
    OCP: Can extend with division-based or zero-aware strategies.
    """
    def product_except_self(self, nums: List[int]) -> List[int]:
        length = len(nums)
        output = [1] * length

        # Prefix pass
        prefix = 1
        for i in range(length):
            output[i] = prefix
            prefix *= nums[i]

        # Suffix pass
        suffix = 1
        for i in reversed(range(length)):
            output[i] *= suffix
            suffix *= nums[i]

        return output

class Solution:
    """
    High-level interface depending on abstraction (strategy).
    """
    def __init__(self, strategy: ProductStrategy = PrefixSuffixProductStrategy()) -> None:
        self.strategy = strategy
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return self.strategy.product_except_self(nums)


"""
Key Developer Insights
No division allowed → must use prefix and suffix products.
O(n) time → single pass for prefix, single pass for suffix.
O(1) extra space → reuse output array for prefix, use a scalar for suffix.
"""


# Usage

solver = Solution()
print(solver.productExceptSelf([1,2,3,4]))         # [24,12,8,6]
print(solver.productExceptSelf([-1,1,0,-3,3]))     # [0,0,9,0,0]
