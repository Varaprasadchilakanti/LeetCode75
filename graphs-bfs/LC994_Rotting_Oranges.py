"""
994. Rotting Oranges

You are given an m x n grid where each cell can have one of three values:
0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.

Topics
Array
Breadth-First Search
Matrix

Developer Insights
This problem is a classic multi‑source BFS on a grid.

Why BFS?
All initially rotten oranges act as simultaneous sources.
BFS spreads rot level‑by‑level.
The last level reached gives the minimum minutes required.
If any fresh orange is unreachable, the answer is -1.

Key Observations
Push all rotten oranges into the queue at time 0.
Count fresh oranges.
Each BFS step rots adjacent fresh oranges.
When all fresh oranges are processed, the last timestamp is the answer.

Complexity
Time: O(m × n)
Space: O(m × n)
Optimal for grid BFS.

Edge Cases
No fresh oranges → return 0
Fresh oranges exist but no rotten ones → impossible → return -1
Grid with only one cell
Isolated fresh oranges blocked by walls (0s)

Pseudocode

queue = all rotten oranges with time = 0
fresh_count = number of fresh oranges

while queue not empty:
    r, c, t = queue.pop()

    for each direction:
        nr, nc = neighbor cell
        if inside grid AND fresh:
            rot it
            fresh_count -= 1
            queue.push(nr, nc, t+1)
            update answer = t+1

if fresh_count > 0:
    return -1
else:
    return answer

"""


from typing import List, Protocol
from collections import deque


class StrategyInterface(Protocol):
    """
    Protocol defining the interface for rotting-orange strategies.
    """
    def solve(self, grid: List[List[int]]) -> int:
        ...


class RottingOrangesBFSStrategy:
    """
    BFS strategy for computing the minimum minutes required
    for all fresh oranges to rot.
    """

    def solve(self, grid: List[List[int]]) -> int:
        """
        Performs a multi-source BFS from all initially rotten oranges.

        Args:
            grid (List[List[int]]): 2D grid representing orange states.

        Returns:
            int: Minimum minutes to rot all oranges, or -1 if impossible.
        """
        m, n = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        # Collect initial rotten oranges and count fresh ones
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        minutes = 0

        while queue:
            r, c, t = queue.popleft()
            minutes = max(minutes, t)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc, t + 1))

        return minutes if fresh == 0 else -1


class Solution:
    """
    Orchestrator class delegating computation to a strategy.

    - Separation of concerns: Solution orchestrates, strategy computes.
    - Dependency injection: Strategy is swappable.
    - Lazy initialization: Default strategy created only when needed.
    """

    def __init__(self, strategy: StrategyInterface = None) -> None:
        self.strategy = strategy if strategy is not None else RottingOrangesBFSStrategy()

    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Entry point for LeetCode.

        Args:
            grid (List[List[int]]): Orange grid.

        Returns:
            int: Minimum minutes to rot all oranges.
        """
        return self.strategy.solve(grid)


# Usage Suite
if __name__ == "__main__":
    solution = Solution()

    grid1 = [[2,1,1],[1,1,0],[0,1,1]]
    print(solution.orangesRotting(grid1))  # Expected: 4

    grid2 = [[2,1,1],[0,1,1],[1,0,1]]
    print(solution.orangesRotting(grid2))  # Expected: -1

    grid3 = [[0,2]]
    print(solution.orangesRotting(grid3))  # Expected: 0
