"""
215. Kth Largest Element in an Array

Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4


Constraints:
- 1 <= k <= nums.length <= 1e5
- -1e4 <= nums[i] <= 1e4

Topics:
Array, Divide and Conquer, Sorting, Heap (Priority Queue), Quickselect
"""

# ───────────────────────────────────────────────────────────────────────────
# Developer Insights — Quickselect Strategy
# ───────────────────────────────────────────────────────────────────────────
"""
Quickselect is the selection algorithm behind QuickSort. It locates the element
that would appear at index (len(nums) - k) in a sorted array.

Strengths:
- Average Time: O(n)
- Space: O(1)
- Avoids full sorting (O(n log n))

Mechanics:
- Choose a pivot
- Partition into < pivot | pivot | > pivot
- Recurse only into the region containing the target index

Limitations:
- Worst-case O(n^2)
- Sensitive to repeated or adversarial inputs
- Python recursion depth can be limiting
"""

# ───────────────────────────────────────────────────────────────────────────
# Developer Insights — Min-Heap Strategy (Recommended for Python)
# ───────────────────────────────────────────────────────────────────────────
"""
The min-heap approach is robust and predictable, making it ideal for Python.

Strengths:
- Guaranteed O(n log k)
- Stable across all input distributions
- No recursion
- Memory footprint O(k)

Mechanics:
- Maintain a min-heap of size k
- Push each number
- If heap exceeds size k, pop the smallest
- After processing all numbers, heap[0] is the kth largest

This strategy avoids Quickselect’s worst-case behavior entirely.
"""

# ───────────────────────────────────────────────────────────────────────────
# Pseudocode — Quickselect
# ───────────────────────────────────────────────────────────────────────────
"""
target = len(nums) - k

function quickselect(left, right):
    pivot = nums[right]
    partition array around pivot

    if pivot_index == target:
        return nums[pivot_index]
    elif pivot_index < target:
        return quickselect(pivot_index + 1, right)
    else:
        return quickselect(left, pivot_index - 1)
"""

# ───────────────────────────────────────────────────────────────────────────
# Pseudocode — Min-Heap
# ───────────────────────────────────────────────────────────────────────────
"""
function findKthLargest(nums, k):
    heap = empty min-heap

    for num in nums:
        push num into heap
        if heap size > k:
            pop smallest

    return heap[0]
"""

# ───────────────────────────────────────────────────────────────────────────
# Implementation
# ───────────────────────────────────────────────────────────────────────────

from typing import List, Protocol
import heapq


class StrategyInterface(Protocol):
    """
    Interface for kth-largest element strategies.
    """
    def solve(self, nums: List[int], k: int) -> int:
        ...


# ───────────────────────────────────────────────────────────────────────────
# Strategy 1 — Quickselect (Fast on average, unsafe on adversarial inputs)
# ───────────────────────────────────────────────────────────────────────────

class QuickselectKthLargestStrategy:
    """
    Quickselect-based strategy for finding the kth largest element.

    Pros:
        - Average O(n)
        - In-place, minimal memory usage

    Cons:
        - Worst-case O(n^2)
        - Sensitive to repeated values and pivot choice
    """

    def solve(self, nums: List[int], k: int) -> int:
        target = len(nums) - k

        def partition(left: int, right: int) -> int:
            """
            Partition nums[left:right] around nums[right] as pivot.
            Returns the pivot's final index.
            """
            pivot = nums[right]
            store = left

            for i in range(left, right):
                if nums[i] < pivot:
                    nums[i], nums[store] = nums[store], nums[i]
                    store += 1

            nums[store], nums[right] = nums[right], nums[store]
            return store

        def quickselect(left: int, right: int) -> int:
            """
            Iteratively selects the element at index `target`.
            """
            while left <= right:
                pivot_index = partition(left, right)

                if pivot_index == target:
                    return nums[pivot_index]
                elif pivot_index < target:
                    left = pivot_index + 1
                else:
                    right = pivot_index - 1

            return nums[left]

        return quickselect(0, len(nums) - 1)


# ───────────────────────────────────────────────────────────────────────────
# Strategy 2 — Min-Heap (Guaranteed performance, recommended)
# ───────────────────────────────────────────────────────────────────────────

class MinHeapKthLargestStrategy:
    """
    Min-heap strategy for finding the kth largest element.

    Pros:
        - Guaranteed O(n log k)
        - Stable across all inputs
        - No recursion

    Cons:
        - Uses O(k) extra memory
    """

    def solve(self, nums: List[int], k: int) -> int:
        """
        Returns the kth largest element using a min-heap of size k.
        """
        heap = []

        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]


# ───────────────────────────────────────────────────────────────────────────
# Orchestrator — Clean Architecture
# ───────────────────────────────────────────────────────────────────────────

class Solution:
    """
    Orchestrates kth-largest computation by delegating to a strategy.

    - Separation of concerns: orchestration vs. computation
    - Dependency injection: strategy is swappable
    - Defaults to Min-Heap strategy for reliability
    """

    def __init__(self, strategy: StrategyInterface = None) -> None:
        self.strategy = strategy if strategy is not None else MinHeapKthLargestStrategy()

    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Entry point for LeetCode.

        Args:
            nums (List[int]): Input array.
            k (int): Rank of largest element.

        Returns:
            int: The kth largest element.
        """
        return self.strategy.solve(nums, k)


# ───────────────────────────────────────────────────────────────────────────
# Usage Suite
# ───────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=== Min-Heap Strategy ===")
    solution = Solution()
    print(solution.findKthLargest([3, 2, 1, 5, 6, 4], 2))  # 5
    print(solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # 4

    print("\n=== Quickselect Strategy ===")
    solution = Solution(QuickselectKthLargestStrategy())
    print(solution.findKthLargest([3, 2, 1, 5, 6, 4], 2))  # 5
    print(solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # 4
