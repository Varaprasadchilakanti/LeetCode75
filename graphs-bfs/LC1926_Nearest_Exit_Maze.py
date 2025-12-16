"""
1926. Nearest Exit from Entrance in Maze

You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.
In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.
Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.

Example 1:
Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
Output: 1
Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
Initially, you are at the entrance cell [1,2].
- You can reach [1,0] by moving 2 steps left.
- You can reach [0,2] by moving 1 step up.
It is impossible to reach [2,3] from the entrance.
Thus, the nearest exit is [0,2], which is 1 step away.

Example 2:
Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
Output: 2
Explanation: There is 1 exit in this maze at [1,2].
[1,0] does not count as an exit since it is the entrance cell.
Initially, you are at the entrance cell [1,0].
- You can reach [1,2] by moving 2 steps right.
Thus, the nearest exit is [1,2], which is 2 steps away.

Example 3:
Input: maze = [[".","+"]], entrance = [0,0]
Output: -1
Explanation: There are no exits in this maze.

Constraints:
maze.length == m
maze[i].length == n
1 <= m, n <= 100
maze[i][j] is either '.' or '+'.
entrance.length == 2
0 <= entrancerow < m
0 <= entrancecol < n
entrance will always be an empty cell.

Topics
Array
Breadth-First Search
Matrix

Hint 1
Which type of traversal lets you find the distance from a point?
Hint 2
Try using a Breadth First Search.

Developer Insights
This problem is a shortest‑path search in an unweighted grid, which is a perfect fit for Breadth‑First Search (BFS).

Why BFS?
BFS explores level‑by‑level.
The first time we reach an exit, it is guaranteed to be the minimum number of steps.
DFS would not guarantee shortest path.

Exit Definition
A cell (r, c) is an exit if:
It is on the border: r == 0 or r == m-1 or c == 0 or c == n-1
It is not the entrance itself.

Movement Rules
Up, Down, Left, Right
Cannot step into + (walls)
Cannot go outside the maze

Complexity
Time: O(m × n)
Space: O(m × n) for visited + queue
Fully optimal for grid BFS.

Edge Cases
Entrance is on border → still NOT an exit
No reachable exit → return -1
Maze with only one row or one column
All walls except entrance

Pseudocode
queue = [(entrance_row, entrance_col, 0)]
mark entrance visited

while queue not empty:
    r, c, dist = queue.pop_left()

    for each direction (dr, dc):
        nr, nc = r + dr, c + dc

        if out of bounds or wall or visited:
            continue

        if (nr, nc) is border AND not entrance:
            return dist + 1

        mark visited
        push (nr, nc, dist + 1)

return -1

"""

from typing import List, Tuple, Protocol
from collections import deque


class StrategyInterface(Protocol):
    """
    Protocol defining the interface for maze-exit strategies.
    """
    def solve(self, maze: List[List[str]], entrance: List[int]) -> int:
        ...


class NearestExitBFSStrategy:
    """
    Strategy implementing BFS to find the nearest exit in a maze.

    BFS guarantees the shortest path in an unweighted grid.
    """

    def solve(self, maze: List[List[str]], entrance: List[int]) -> int:
        """
        Computes the minimum number of steps to reach the nearest exit.

        Args:
            maze (List[List[str]]): Grid of '.' (empty) and '+' (wall).
            entrance (List[int]): Starting cell [row, col].

        Returns:
            int: Minimum steps to nearest exit, or -1 if none exists.
        """
        m, n = len(maze), len(maze[0])
        start_r, start_c = entrance

        queue = deque([(start_r, start_c, 0)])
        visited = set([(start_r, start_c)])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def is_exit(r: int, c: int) -> bool:
            if (r, c) == (start_r, start_c):
                return False
            return r == 0 or r == m - 1 or c == 0 or c == n - 1

        while queue:
            r, c, dist = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue
                if maze[nr][nc] == "+":
                    continue
                if (nr, nc) in visited:
                    continue

                if is_exit(nr, nc):
                    return dist + 1

                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))

        return -1


class Solution:
    """
    Entry point class delegating maze-exit logic to a strategy.

    Design principles:
        - Separation of concerns: Solution orchestrates, strategy computes.
        - Dependency injection: Strategy is swappable.
        - Lazy initialization: Default strategy created only when needed.
    """

    def __init__(self, strategy: StrategyInterface = None) -> None:
        self.strategy = strategy if strategy is not None else NearestExitBFSStrategy()

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        """
        Returns the minimum number of steps to the nearest exit.

        Args:
            maze (List[List[str]]): Maze grid.
            entrance (List[int]): Starting cell.

        Returns:
            int: Minimum steps or -1.
        """
        return self.strategy.solve(maze, entrance)


# Usage Suite

if __name__ == "__main__":
    solution = Solution()

    maze1 = [
        ["+", "+", ".", "+"],
        [".", ".", ".", "+"],
        ["+", "+", "+", "."]
    ]
    print(solution.nearestExit(maze1, [1, 2]))  # Expected: 1

    maze2 = [
        ["+", "+", "+"],
        [".", ".", "."],
        ["+", "+", "+"]
    ]
    print(solution.nearestExit(maze2, [1, 0]))  # Expected: 2

    maze3 = [[".", "+"]]
    print(solution.nearestExit(maze3, [0, 0]))  # Expected: -1
