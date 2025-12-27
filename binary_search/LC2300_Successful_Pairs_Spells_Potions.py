"""
2300. Successful Pairs of Spells and Potions
You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.
You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.
Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.

Example 1:
Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
Output: [4,0,3]
Explanation:
- 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
- 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
- 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
Thus, [4,0,3] is returned.

Example 2:
Input: spells = [3,1,2], potions = [8,5,8], success = 16
Output: [2,0,2]
Explanation:
- 0th spell: 3 * [8,5,8] = [24,15,24]. 2 pairs are successful.
- 1st spell: 1 * [8,5,8] = [8,5,8]. 0 pairs are successful. 
- 2nd spell: 2 * [8,5,8] = [16,10,16]. 2 pairs are successful. 
Thus, [2,0,2] is returned.

Constraints:
n == spells.length
m == potions.length
1 <= n, m <= 105
1 <= spells[i], potions[i] <= 105
1 <= success <= 1010

Topics
Array
Two Pointers
Binary Search
Sorting
Biweekly Contest 80

Hint 1
Notice that if a spell and potion pair is successful, then the spell and all stronger potions will be successful too.
Hint 2
Thus, for each spell, we need to find the potion with the least strength that will form a successful pair.
Hint 3
We can efficiently do this by sorting the potions based on strength and using binary search.


Developer Insights
Problem Nature
We need to count, for each spell, how many potions yield a product ≥ success.

Key Observations
If a spell × potion is successful, then the spell × all stronger potions are also successful.
Sorting potions allows us to use binary search to find the smallest potion that meets the threshold for each spell.
The count is then len(potions) - index.

Strategy
Sort potions.
For each spell:
Compute the minimum potion strength required: ceil(success / spell).
Use binary search to find the first potion ≥ required.
Count = total potions − index.
Return counts for all spells.

Complexity
Sorting: O(m log m)
For each spell: O(log m)
Total: O((n + m) log m)
Space: O(1) extra (besides output).

Edge Cases
Spell = 0 → always 0 successful pairs.
Very large success → may yield 0 pairs.
All potions strong enough → count = m for that spell.
n, m up to 1e5 → algorithm must remain O(n log m).

Pseudocode
function successfulPairs(spells, potions, success):
    sort potions
    result = []

    for spell in spells:
        required = ceil(success / spell)
        index = binary_search_first_ge(potions, required)
        count = len(potions) - index
        result.append(count)

    return result


"""

from typing import List, Protocol
import bisect
import math


# ───────────────────────────────────────────────────────────────────────────
# Strategy Interface
# ───────────────────────────────────────────────────────────────────────────

class PairsStrategy(Protocol):
    """
    Protocol defining the interface for successful pairs strategies.
    """
    def solve(self, spells: List[int], potions: List[int], success: int) -> List[int]: ...


# ───────────────────────────────────────────────────────────────────────────
# Binary Search Strategy
# ───────────────────────────────────────────────────────────────────────────

class BinarySearchPairsStrategy:
    """
    Binary search strategy for Successful Pairs of Spells and Potions.

    Design:
        - Sort potions once.
        - For each spell, compute required potion strength.
        - Use binary search to find first potion meeting requirement.
        - Count = total potions - index.

    Time Complexity:
        - O((n + m) log m)
    Space Complexity:
        - O(1) extra
    """

    def solve(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(potions)
        result = []

        for spell in spells:
            if spell == 0:
                result.append(0)
                continue

            required = math.ceil(success / spell)
            idx = bisect.bisect_left(potions, required)
            result.append(n - idx)

        return result


# ───────────────────────────────────────────────────────────────────────────
# Orchestrator — Clean Architecture
# ───────────────────────────────────────────────────────────────────────────

class Solution:
    """
    Orchestrates successful pairs computation by delegating to a strategy.

    - Separation of concerns: orchestration vs. computation
    - Dependency injection: strategy is swappable
    - Defaults to Binary Search strategy
    """

    def __init__(self, strategy: PairsStrategy = None) -> None:
        self.strategy = strategy if strategy is not None else BinarySearchPairsStrategy()

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        """
        Entry point for LeetCode.

        Args:
            spells (List[int]): Strengths of spells.
            potions (List[int]): Strengths of potions.
            success (int): Threshold for successful pairs.

        Returns:
            List[int]: Number of successful pairs for each spell.
        """
        return self.strategy.solve(spells, potions, success)


# ───────────────────────────────────────────────────────────────────────────
# Usage Suite
# ───────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    solution = Solution()

    print(solution.successfulPairs([5, 1, 3], [1, 2, 3, 4, 5], 7))  # Expected: [4, 0, 3]
    print(solution.successfulPairs([3, 1, 2], [8, 5, 8], 16))       # Expected: [2, 0, 2]
