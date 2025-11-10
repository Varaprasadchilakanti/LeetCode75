"""
1431. Kids With the Greatest Number of Candies

There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.
Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.
Note that multiple kids can have the greatest number of candies.

Example 1:

Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true] 
Explanation: If you give all extraCandies to:
- Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
- Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
- Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
- Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
- Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
Example 2:

Input: candies = [4,2,1,1,2], extraCandies = 1
Output: [true,false,false,false,false] 
Explanation: There is only 1 extra candy.
Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.
Example 3:

Input: candies = [12,1,12], extraCandies = 10
Output: [true,false,true]
 

Constraints:

n == candies.length
2 <= n <= 100
1 <= candies[i] <= 100
1 <= extraCandies <= 50


Topics
Array, Biweekly Contest 25

Hint 1
For each kid check if candies[i] + extraCandies ≥ maximum in Candies[i].

Pseudocode
function kidsWithCandies(candies, extraCandies):
    maxCandies = max(candies)
    result = []
    for each candy in candies:
        if candy + extraCandies >= maxCandies:
            result.append(True)
        else:
            result.append(False)
    return result
"""
from typing import List, Protocol

class CandiesStrategy(Protocol):
    def kids_with_candies(self, candies: List[int], extraCandies: int) -> List[bool]: ...

class MaxCheckStrategy:
    """
    SRP: Encapsulates the logic for determining which kids can reach the max.
    OCP: Can extend with other strategies (e.g., streaming input, lazy evaluation).
    """
    def kids_with_candies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        return [(candy + extraCandies) >= max_candies for candy in candies]

class Solution:
    """
    High-level interface depending on abstraction (strategy).
    """
    def __init__(self, strategy: CandiesStrategy = MaxCheckStrategy()) -> None:
        self.strategy = strategy
    
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return self.strategy.kids_with_candies(candies, extraCandies)



# Usage

solver = Solution()
print(solver.kidsWithCandies([2,3,5,1,3], 3))   # [True, True, True, False, True]
print(solver.kidsWithCandies([4,2,1,1,2], 1))   # [True, False, False, False, False]
print(solver.kidsWithCandies([12,1,12], 10))    # [True, False, True]


"""
Takeaway
The key optimization was precomputing the max.
Wrapping in a strategy pattern makes it extensible and testable.
The final solution is concise, efficient, and interview‑ready.
"""
