"""
2336. Smallest Number in Infinite Set

You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].
Implement the SmallestInfiniteSet class:
SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
int popSmallest() Removes and returns the smallest integer contained in the infinite set.
void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.

Example 1:
Input
["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
[[], [2], [], [], [], [1], [], [], []]
Output
[null, null, 1, 2, 3, null, 1, 4, 5]

Explanation
SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
smallestInfiniteSet.addBack(2);    // 2 is already in the set, so no change is made.
smallestInfiniteSet.popSmallest(); // return 1, since 1 is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 2, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 3, and remove it from the set.
smallestInfiniteSet.addBack(1);    // 1 is added back to the set.
smallestInfiniteSet.popSmallest(); // return 1, since 1 was added back to the set and
                                   // is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 4, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 5, and remove it from the set.

Constraints:
1 <= num <= 1000
At most 1000 calls will be made in total to popSmallest and addBack.

Topics
Hash Table
Design
Heap (Priority Queue)
Ordered Set

Hint 1
Based on the constraints, what is the maximum element that can possibly be popped?
Hint 2


Developer Insights
Problem Nature
We need to simulate an infinite set of positive integers with two operations:
popSmallest() → remove and return the smallest integer.
addBack(num) → reinsert a number if it’s not already present.

Key Observations
The set starts as [1, 2, 3, …].
Once we pop numbers sequentially, the next smallest is always the next integer.
But if we addBack, we must ensure it can be popped before larger numbers.

Strategy
Maintain a min‑heap for numbers that were popped and then added back.
Maintain a pointer (next_smallest) for the next natural integer not yet popped.
Maintain a set (in_heap) to avoid duplicates in the heap.

Complexity
popSmallest: O(log n) if heap used, O(1) otherwise.
addBack: O(log n) for heap insertion.
Space: O(k), bounded by constraints.

Edge Cases
Adding back a number already present → ignored.
Adding back a number greater than next_smallest → valid, but only matters if popped earlier.
Sequential pops without addBack → behaves like a counter.

Pseudocode
initialize:
    heap = empty min-heap
    in_heap = empty set
    next_smallest = 1

function popSmallest():
    if heap not empty:
        val = heappop(heap)
        remove val from in_heap
        return val
    else:
        val = next_smallest
        next_smallest += 1
        return val

function addBack(num):
    if num < next_smallest and num not in in_heap:
        heappush(heap, num)
        add num to in_heap


"""

from typing import Protocol
import heapq


# ───────────────────────────────────────────────────────────────────────────
# Strategy Interface
# ───────────────────────────────────────────────────────────────────────────

class InfiniteSetStrategy(Protocol):
    """
    Protocol defining the interface for infinite set strategies.
    """
    def popSmallest(self) -> int: ...
    def addBack(self, num: int) -> None: ...


# ───────────────────────────────────────────────────────────────────────────
# Heap-Based Strategy
# ───────────────────────────────────────────────────────────────────────────

class HeapInfiniteSetStrategy:
    """
    Heap-based strategy for managing the smallest number in an infinite set.

    Design:
        - Min-heap stores numbers added back.
        - Set tracks membership to avoid duplicates.
        - Counter tracks the next natural smallest integer.

    Time Complexity:
        - popSmallest: O(log n) if heap used, else O(1).
        - addBack: O(log n).
    Space Complexity: O(k).
    """

    def __init__(self) -> None:
        self.heap = []
        self.in_heap = set()
        self.next_smallest = 1

    def popSmallest(self) -> int:
        """
        Removes and returns the smallest integer in the set.

        Returns:
            int: The smallest available integer.
        """
        if self.heap:
            val = heapq.heappop(self.heap)
            self.in_heap.remove(val)
            return val
        else:
            val = self.next_smallest
            self.next_smallest += 1
            return val

    def addBack(self, num: int) -> None:
        """
        Adds a number back into the set if it was previously popped.

        Args:
            num (int): Positive integer to add back.
        """
        if num < self.next_smallest and num not in self.in_heap:
            heapq.heappush(self.heap, num)
            self.in_heap.add(num)


# ───────────────────────────────────────────────────────────────────────────
# Orchestrator — Clean Architecture
# ───────────────────────────────────────────────────────────────────────────

class SmallestInfiniteSet:
    """
    Orchestrator class delegating infinite set operations to a strategy.

    - Separation of concerns: orchestration vs. computation.
    - Dependency injection: strategy is swappable.
    - Lazy initialization: defaults to Heap-based strategy.
    """

    def __init__(self, strategy: InfiniteSetStrategy = None) -> None:
        self.strategy = strategy if strategy is not None else HeapInfiniteSetStrategy()

    def popSmallest(self) -> int:
        return self.strategy.popSmallest()

    def addBack(self, num: int) -> None:
        self.strategy.addBack(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)

# ───────────────────────────────────────────────────────────────────────────
# Usage Suite
# ───────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    obj = SmallestInfiniteSet()
    obj.addBack(2)          # 2 already in set, ignored
    print(obj.popSmallest())  # 1
    print(obj.popSmallest())  # 2
    print(obj.popSmallest())  # 3
    obj.addBack(1)          # 1 added back
    print(obj.popSmallest())  # 1
    print(obj.popSmallest())  # 4
    print(obj.popSmallest())  # 5
