"""
2352. Equal Row and Column Pairs

Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.
A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).


Example 1:

Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]

Example 2:

Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]


Constraints:

n == grid.length == grid[i].length
1 <= n <= 200
1 <= grid[i][j] <= 105

Topics
Array
Hash Table
Matrix
Simulation

Hint 1
We can use nested loops to compare every row against every column.
Hint 2
Another loop is necessary to compare the row and column element by element.
Hint 3
It is also possible to hash the arrays and compare the hashed values instead.


Key Developer Insights
We need to count pairs (ri, cj) where row ri equals column cj.

Naïve approach: compare every row with every column → 𝑂(𝑛^3), too slow for 𝑛=200.

Optimal approach:
Treat each row and column as a tuple (hashable).
Use a hash map (dictionary) to count occurrences of rows.
For each column, check if it exists in the row map and add to result.


Pseudocode (Grounded in Our Principles)

function equal_pairs(grid):
    n = len(grid)
    row_map = frequency of each row (as tuple)
    result = 0

    for each column j:
        col_tuple = tuple(grid[i][j] for i in range(n))
        if col_tuple in row_map:
            result += row_map[col_tuple]

    return result

"""

from typing import List, Protocol
from collections import Counter

class EqualPairsStrategy(Protocol):
    def equal_pairs(self, grid: List[List[int]]) -> int: ...

class HashMapEqualPairsStrategy:
    """
    SRP: Encapsulates logic for counting equal row-column pairs.
    OCP: Can extend with direct comparison or optimized hashing.
    """
    def equal_pairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # Count frequency of each row
        row_map = Counter(tuple(row) for row in grid)
        result = 0

        # Build each column as tuple and compare
        for j in range(n):
            col_tuple = tuple(grid[i][j] for i in range(n))
            result += row_map[col_tuple]

        return result

class Solution:
    """
    High-level interface depending on abstraction (strategy).
    """
    def __init__(self, strategy: EqualPairsStrategy = HashMapEqualPairsStrategy()) -> None:
        self.strategy = strategy
    
    def equalPairs(self, grid: List[List[int]]) -> int:
        return self.strategy.equal_pairs(grid)


# Usage

solver = Solution()
print(solver.equalPairs([[3,2,1],[1,7,6],[2,7,7]]))  
# 1

print(solver.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))  
# 3
