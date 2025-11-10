"""
1679. Max Number of K-Sum Pairs

You are given an integer array nums and an integer k.
In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
Return the maximum number of operations you can perform on the array.

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= 109


Topics
Array
Hash Table
Two Pointers
Sorting

Hint 1
The abstract problem asks to count the number of disjoint pairs with a given sum k.
Hint 2
For each possible value x, it can be paired up with k - x.
Hint 3
The number of such pairs equals to min(count(x), count(k-x)), unless that x = k / 2, where the number of such pairs will be floor(count(x) / 2).


Key Developer Insights
We want to count disjoint pairs that sum to k.
For each number x, its complement is k - x.
Use a hash map to track frequencies.
For each x, we can form min(freq[x], freq[k - x]) pairs.
Special case: if x == k - x, we can only form freq[x] // 2 pairs.


Pseudocode (Grounded in Our Principles)

function max_operations(nums, k):
    initialize freq_map
    initialize count = 0

    for num in nums:
        complement = k - num
        if freq_map[complement] > 0:
            decrement freq_map[complement]
            increment count
        else:
            increment freq_map[num]

    return count

"""

from typing import List, Protocol
from collections import defaultdict

class KSumStrategy(Protocol):
    def max_operations(self, nums: List[int], k: int) -> int: ...

class HashMapKSumStrategy:
    """
    SRP: Encapsulates hash map logic for counting disjoint k-sum pairs.
    OCP: Can extend with sorting + two-pointer variant.
    """
    def max_operations(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        count = 0

        for num in nums:
            complement = k - num
            if freq[complement] > 0:
                freq[complement] -= 1
                count += 1
            else:
                freq[num] += 1

        return count

class Solution:
    """
    High-level interface depending on abstraction (strategy).
    """
    def __init__(self, strategy: KSumStrategy = HashMapKSumStrategy()) -> None:
        self.strategy = strategy
    
    def maxOperations(self, nums: List[int], k: int) -> int:
        return self.strategy.max_operations(nums, k)


# Usage
solver = Solution()
print(solver.maxOperations([1,2,3,4], 5))       # 2
print(solver.maxOperations([3,1,3,4,3], 6))     # 1
