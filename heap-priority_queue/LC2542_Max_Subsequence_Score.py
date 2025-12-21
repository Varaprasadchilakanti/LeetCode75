"""
2542. Maximum Subsequence Score

You are given two 0-indexed integer arrays nums1 and nums2 of equal length n and a positive integer k. You must choose a subsequence of indices from nums1 of length k.
For chosen indices i0, i1, ..., ik - 1, your score is defined as:
The sum of the selected elements from nums1 multiplied with the minimum of the selected elements from nums2.
It can defined simply as: (nums1[i0] + nums1[i1] +...+ nums1[ik - 1]) * min(nums2[i0] , nums2[i1], ... ,nums2[ik - 1]).
Return the maximum possible score.
A subsequence of indices of an array is a set that can be derived from the set {0, 1, ..., n-1} by deleting some or no elements.

Example 1:
Input: nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3
Output: 12
Explanation: 
The four possible subsequence scores are:
- We choose the indices 0, 1, and 2 with score = (1+3+3) * min(2,1,3) = 7.
- We choose the indices 0, 1, and 3 with score = (1+3+2) * min(2,1,4) = 6. 
- We choose the indices 0, 2, and 3 with score = (1+3+2) * min(2,3,4) = 12. 
- We choose the indices 1, 2, and 3 with score = (3+3+2) * min(1,3,4) = 8.
Therefore, we return the max score, which is 12.

Example 2:
Input: nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1
Output: 30
Explanation:
Choosing index 2 is optimal: nums1[2] * nums2[2] = 3 * 10 = 30 is the maximum possible score.

Constraints:
n == nums1.length == nums2.length
1 <= n <= 105
0 <= nums1[i], nums2[j] <= 105
1 <= k <= n

Topics
Array
Greedy
Sorting
Heap (Priority Queue)

Hint 1
How can we use sorting here?
Hint 2
Try sorting the two arrays based on second array.
Hint 3
Loop through nums2 and compute the max product given the minimum is nums2[i]. Update the answer accordingly.


Developer Insights
Problem Nature
We must choose k indices such that:
score=(∑nums1[i])×min(nums2[i])
This is a greedy + heap problem.

Key Observations
The minimum of chosen nums2 dominates the multiplier.
If we sort pairs (nums1[i], nums2[i]) by nums2[i] descending, then at each step, the current nums2[i] is the minimum multiplier for subsequences including it and all later elements.
To maximize the sum of nums1, we maintain the largest k values of nums1 using a min‑heap.

Strategy
Pair up (nums1[i], nums2[i]).
Sort pairs by nums2 descending.
Iterate through pairs:
Push nums1[i] into a min‑heap.
Maintain running sum of heap elements.
If heap size exceeds k, pop smallest.
If heap size == k, compute score = sum * current nums2[i].
Track maximum score.

Complexity
Sorting: O(n log n)
Heap operations: O(n log k)
Total: O(n log n)
Space: O(k)

Edge Cases
k = 1 → simply max(nums1[i] * nums2[i])
All nums1 = 0 → score = 0
Large n (1e5) → algorithm must be O(n log n)
nums2 with duplicates → handled naturally by sorting

Pseudocode

pairs = zip(nums1, nums2)
sort pairs by nums2 descending

heap = []
sum_nums1 = 0
max_score = 0

for (a, b) in pairs:
    push a into heap
    sum_nums1 += a

    if heap size > k:
        sum_nums1 -= pop smallest from heap

    if heap size == k:
        score = sum_nums1 * b
        max_score = max(max_score, score)

return max_score


"""


from typing import List, Protocol
import heapq


# ───────────────────────────────────────────────────────────────────────────
# Strategy Interface
# ───────────────────────────────────────────────────────────────────────────

class MaxScoreStrategy(Protocol):
    """
    Protocol defining the interface for maximum subsequence score strategies.
    """
    def solve(self, nums1: List[int], nums2: List[int], k: int) -> int: ...


# ───────────────────────────────────────────────────────────────────────────
# Heap-Based Strategy
# ───────────────────────────────────────────────────────────────────────────

class HeapMaxScoreStrategy:
    """
    Heap-based greedy strategy for Maximum Subsequence Score.

    Design:
        - Sort pairs by nums2 descending.
        - Maintain a min-heap of nums1 values.
        - Track running sum of heap elements.
        - At each step, compute score using current nums2 as multiplier.

    Time Complexity:
        - O(n log n) for sorting
        - O(n log k) for heap operations
    Space Complexity: O(k)
    """

    def solve(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = sorted(zip(nums1, nums2), key=lambda x: -x[1])

        heap = []
        sum_nums1 = 0
        max_score = 0

        for a, b in pairs:
            heapq.heappush(heap, a)
            sum_nums1 += a

            if len(heap) > k:
                sum_nums1 -= heapq.heappop(heap)

            if len(heap) == k:
                max_score = max(max_score, sum_nums1 * b)

        return max_score


# ───────────────────────────────────────────────────────────────────────────
# Orchestrator — Clean Architecture
# ───────────────────────────────────────────────────────────────────────────

class Solution:
    """
    Orchestrates maximum subsequence score computation by delegating to a strategy.

    - Separation of concerns: orchestration vs. computation
    - Dependency injection: strategy is swappable
    - Defaults to Heap-based strategy for reliability
    """

    def __init__(self, strategy: MaxScoreStrategy = None) -> None:
        self.strategy = strategy if strategy is not None else HeapMaxScoreStrategy()

    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        """
        Entry point for LeetCode.

        Args:
            nums1 (List[int]): First array of integers.
            nums2 (List[int]): Second array of integers.
            k (int): Length of subsequence.

        Returns:
            int: Maximum possible subsequence score.
        """
        return self.strategy.solve(nums1, nums2, k)


# ───────────────────────────────────────────────────────────────────────────
# Usage Suite
# ───────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    solution = Solution()

    print(solution.maxScore([1, 3, 3, 2], [2, 1, 3, 4], 3))  # Expected: 12
    print(solution.maxScore([4, 2, 3, 1, 1], [7, 5, 10, 9, 6], 1))  # Expected: 30
