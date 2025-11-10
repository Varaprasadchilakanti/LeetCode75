"""
605. Can Place Flowers

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length

Topics
Array, Greedy

Pseudocode
function canPlaceFlowers(flowerbed, n):
    count = 0
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0 and
           (i == 0 or flowerbed[i-1] == 0) and
           (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
            flowerbed[i] = 1
            count += 1
    return count >= n
"""

from typing import List, Protocol

class FlowerPlacementStrategy(Protocol):
    def can_place(self, flowerbed: List[int], n: int) -> bool: ...

class GreedyPlacementStrategy:
    """
    SRP: Encapsulates greedy flower placement logic.
    OCP: Can extend with alternate rules (e.g., 2-space gap, circular beds).
    """
    def can_place(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        length = len(flowerbed)
        
        for i in range(length):
            if flowerbed[i] == 0:
                empty_left = (i == 0 or flowerbed[i - 1] == 0)
                empty_right = (i == length - 1 or flowerbed[i + 1] == 0)
                
                if empty_left and empty_right:
                    flowerbed[i] = 1
                    count += 1
                    if count >= n:
                        return True
        return count >= n

class Solution:
    """
    High-level interface depending on abstraction (strategy).
    """
    def __init__(self, strategy: FlowerPlacementStrategy = GreedyPlacementStrategy()) -> None:
        self.strategy = strategy
    
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        return self.strategy.can_place(flowerbed, n)


"""
Key Developer Insights
Greedy Strategy: Place flowers only when the current plot and its neighbors are empty.
Edge Handling: Treat boundaries carefully—avoid index errors.
Efficiency: One pass, no extra space.
Extensibility: Design for alternate rules (e.g., 2-space gap, circular beds).
"""


# Usage

solver = Solution()
print(solver.canPlaceFlowers([1,0,0,0,1], 1))  # True
print(solver.canPlaceFlowers([1,0,0,0,1], 2))  # False
print(solver.canPlaceFlowers([0,0,0,0,0], 3))  # True

"""
Extensibility Ideas
Add a strategy for circular flowerbeds.
Add a rule for minimum 2-space gap.
Add logging for auditability in production.
"""
