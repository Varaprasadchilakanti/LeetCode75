"""
2462. Total Cost to Hire K Workers

You are given a 0-indexed integer array costs where costs[i] is the cost of hiring the ith worker.
You are also given two integers k and candidates. We want to hire exactly k workers according to the following rules:
You will run k sessions and hire exactly one worker in each session.
In each hiring session, choose the worker with the lowest cost from either the first candidates workers or the last candidates workers. Break the tie by the smallest index.
For example, if costs = [3,2,7,7,1,2] and candidates = 2, then in the first hiring session, we will choose the 4th worker because they have the lowest cost [3,2,7,7,1,2].
In the second hiring session, we will choose 1st worker because they have the same lowest cost as 4th worker but they have the smallest index [3,2,7,7,2]. Please note that the indexing may be changed in the process.
If there are fewer than candidates workers remaining, choose the worker with the lowest cost among them. Break the tie by the smallest index.
A worker can only be chosen once.
Return the total cost to hire exactly k workers.

Example 1:
Input: costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4
Output: 11
Explanation: We hire 3 workers in total. The total cost is initially 0.
- In the first hiring round we choose the worker from [17,12,10,2,7,2,11,20,8]. The lowest cost is 2, and we break the tie by the smallest index, which is 3. The total cost = 0 + 2 = 2.
- In the second hiring round we choose the worker from [17,12,10,7,2,11,20,8]. The lowest cost is 2 (index 4). The total cost = 2 + 2 = 4.
- In the third hiring round we choose the worker from [17,12,10,7,11,20,8]. The lowest cost is 7 (index 3). The total cost = 4 + 7 = 11. Notice that the worker with index 3 was common in the first and last four workers.
The total hiring cost is 11.

Example 2:
Input: costs = [1,2,4,1], k = 3, candidates = 3
Output: 4
Explanation: We hire 3 workers in total. The total cost is initially 0.
- In the first hiring round we choose the worker from [1,2,4,1]. The lowest cost is 1, and we break the tie by the smallest index, which is 0. The total cost = 0 + 1 = 1. Notice that workers with index 1 and 2 are common in the first and last 3 workers.
- In the second hiring round we choose the worker from [2,4,1]. The lowest cost is 1 (index 2). The total cost = 1 + 1 = 2.
- In the third hiring round there are less than three candidates. We choose the worker from the remaining workers [2,4]. The lowest cost is 2 (index 0). The total cost = 2 + 2 = 4.
The total hiring cost is 4.

Constraints:
1 <= costs.length <= 105 
1 <= costs[i] <= 105
1 <= k, candidates <= costs.length

Topics
Array
Two Pointers
Heap (Priority Queue)
Simulation
Weekly Contest 318

Hint 1
Maintain two minheaps: one for the left and one for the right.
Hint 2
Compare the top element from two heaps and remove the appropriate one.
Hint 3
Add a new element to the heap and maintain its size as k.


Developer Insights
Problem Nature
We must hire exactly k workers with minimum total cost, choosing each time from either:
The first candidates workers, or
The last candidates workers.
This is a simulation problem with heaps.

Key Observations
We need to efficiently pick the smallest cost among two pools (front and back).
After hiring, we must replenish the pool from the remaining workers.
Two min‑heaps (front and back) allow O(log n) extraction of the smallest cost.
Tie‑breaking by index is naturally handled if we push (cost, index) into heaps.

Strategy
Initialize two heaps:
Left heap with first candidates workers.
Right heap with last candidates workers.
Maintain pointers left and right for next available workers.
For each of k hiring sessions:
Compare top of both heaps.
Pop the smaller cost (tie broken by index).
Add cost to total.
Replenish heap from remaining workers (advance pointer).
Return total cost.

Complexity
Heap operations: O(log candidates) per session.
Total: O(k log candidates).
Space: O(candidates).

Edge Cases
candidates >= n → both heaps overlap, but logic still works.
All costs equal → tie broken by index.
k = 1 → just pick min of available.
Large n (1e5) → algorithm must remain O(k log n).

Pseudocode
function totalCost(costs, k, candidates):
    left_heap = first candidates workers (cost, index)
    right_heap = last candidates workers (cost, index)
    left_ptr = candidates
    right_ptr = n - candidates - 1
    total = 0

    for session in range(k):
        choose from left_heap or right_heap (lowest cost, tie by index)
        add chosen cost to total
        if chosen from left_heap and left_ptr <= right_ptr:
            push costs[left_ptr] into left_heap
            left_ptr += 1
        if chosen from right_heap and left_ptr <= right_ptr:
            push costs[right_ptr] into right_heap
            right_ptr -= 1

    return total

"""

from typing import List, Protocol
import heapq


# ───────────────────────────────────────────────────────────────────────────
# Strategy Interface
# ───────────────────────────────────────────────────────────────────────────

class HiringStrategy(Protocol):
    """
    Protocol defining the interface for worker hiring strategies.
    """
    def solve(self, costs: List[int], k: int, candidates: int) -> int: ...


# ───────────────────────────────────────────────────────────────────────────
# Heap-Based Strategy
# ───────────────────────────────────────────────────────────────────────────

class HeapHiringStrategy:
    """
    Heap-based strategy for minimizing total hiring cost.

    Design:
        - Two min-heaps track front and back candidate pools.
        - Each hiring session picks the lowest-cost worker.
        - Pools are replenished from remaining workers.

    Time Complexity:
        - O(k log candidates)
    Space Complexity:
        - O(candidates)
    """

    def solve(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        total = 0

        # Initialize heaps
        left_heap = [(costs[i], i) for i in range(min(candidates, n))]
        right_heap = [(costs[i], i) for i in range(max(candidates, n - candidates), n)]

        heapq.heapify(left_heap)
        heapq.heapify(right_heap)

        left_ptr = len(left_heap)
        right_ptr = n - len(right_heap) - 1

        for _ in range(k):
            # Choose from left or right heap
            if right_heap and (not left_heap or right_heap[0] < left_heap[0]):
                cost, idx = heapq.heappop(right_heap)
                total += cost
                if left_ptr <= right_ptr:
                    heapq.heappush(right_heap, (costs[right_ptr], right_ptr))
                    right_ptr -= 1
            else:
                cost, idx = heapq.heappop(left_heap)
                total += cost
                if left_ptr <= right_ptr:
                    heapq.heappush(left_heap, (costs[left_ptr], left_ptr))
                    left_ptr += 1

        return total


# ───────────────────────────────────────────────────────────────────────────
# Orchestrator — Clean Architecture
# ───────────────────────────────────────────────────────────────────────────

class Solution:
    """
    Orchestrates total cost computation by delegating to a strategy.

    - Separation of concerns: orchestration vs. computation
    - Dependency injection: strategy is swappable
    - Defaults to Heap-based strategy for reliability
    """

    def __init__(self, strategy: HiringStrategy = None) -> None:
        self.strategy = strategy if strategy is not None else HeapHiringStrategy()

    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        """
        Entry point for LeetCode.

        Args:
            costs (List[int]): Hiring costs of workers.
            k (int): Number of workers to hire.
            candidates (int): Candidate pool size from each end.

        Returns:
            int: Minimum total hiring cost.
        """
        return self.strategy.solve(costs, k, candidates)


# ───────────────────────────────────────────────────────────────────────────
# Usage Suite
# ───────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    solution = Solution()

    print(solution.totalCost([17,12,10,2,7,2,11,20,8], 3, 4))  # Expected: 11
    print(solution.totalCost([1,2,4,1], 3, 3))  # Expected: 4
