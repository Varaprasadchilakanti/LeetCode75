"""
1207. Unique Number of Occurrences

Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.


Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true


Constraints:

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000

Topics
Array
Hash Table

Hint 1
Find the number of occurrences of each element in the array using a hash map.
Hint 2
Iterate through the hash map and check if there is a repeated value.


Key Developer Insights
Step 1: Count occurrences of each number using a hash map (collections.Counter).
Step 2: Check if all occurrence counts are unique.
Convert counts to a set.
If lengths differ → duplicates exist → return False.
Otherwise → return True.


Pseudocode (Grounded in Our Principles)

function unique_occurrences(arr):
    freq_map = count occurrences of each element
    counts = values of freq_map
    return len(counts) == len(set(counts))
"""

from typing import List, Protocol
from collections import Counter

class OccurrenceStrategy(Protocol):
    def unique_occurrences(self, arr: List[int]) -> bool: ...

class HashMapOccurrenceStrategy:
    """
    SRP: Encapsulates frequency counting and uniqueness check.
    OCP: Can extend with sorting or streaming variants.
    """
    def unique_occurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr)
        counts = list(freq.values())
        return len(counts) == len(set(counts))

class Solution:
    """
    High-level interface depending on abstraction (strategy).
    """
    def __init__(self, strategy: OccurrenceStrategy = HashMapOccurrenceStrategy()) -> None:
        self.strategy = strategy
    
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return self.strategy.unique_occurrences(arr)


# Usage

solver = Solution()
print(solver.uniqueOccurrences([1,2,2,1,1,3]))          # True
print(solver.uniqueOccurrences([1,2]))                  # False
print(solver.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))  # True
