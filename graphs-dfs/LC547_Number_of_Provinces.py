"""
547. Number of Provinces

There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
A province is a group of directly or indirectly connected cities and no other cities outside of the group.
You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
Return the total number of provinces.

Example 1:
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Example 2:
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3

Constraints:
1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]

Topics
Depth-First Search
Breadth-First Search
Union Find
Graph

Developer Insights
This problem is a classic connected components in an undirected graph task.

Graph Interpretation
Each city is a node.
isConnected[i][j] = 1 means an undirected edge between i and j.
A province is simply a connected component.

Why DFS?
Graph size is small (≤ 200 nodes).
DFS is clean, optimal, and easy to reason about.
No need to build adjacency lists — matrix is direct.

Complexity
Time: O(n²) — scanning adjacency matrix
Space: O(n) — visited set + recursion depth
Fully optimal for this problem.

Edge Cases
Single city → 1 province
Fully connected → 1 province
No cross‑connections → n provinces

Pseudocode
function findCircleNum(matrix):
    n = len(matrix)
    visited = set()
    provinces = 0

    function dfs(city):
        mark city visited
        for neighbor in range(n):
            if matrix[city][neighbor] == 1 and neighbor not visited:
                dfs(neighbor)

    for city in range(n):
        if city not visited:
            provinces += 1
            dfs(city)

    return provinces


"""

from typing import List, Protocol


class StrategyInterface(Protocol):
    """
    Protocol defining the interface for province-counting strategies.
    """
    def solve(self, isConnected: List[List[int]]) -> int:
        ...


class DFSProvincesStrategy:
    """
    Strategy implementing DFS to count the number of provinces.

    Each city is treated as a graph node. A province corresponds to a
    connected component in the undirected graph represented by the adjacency matrix.

    Complexity:
        Time:  O(n^2)
        Space: O(n)
    """
    def solve(self, isConnected: List[List[int]]) -> int:
        """
        Counts the number of provinces (connected components) in the graph.

        Args:
            isConnected (List[List[int]]): Adjacency matrix representing city connections.

        Returns:
            int: Number of provinces.
        """
        n = len(isConnected)
        visited = set()
        provinces = 0

        def dfs(city: int) -> None:
            visited.add(city)
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and neighbor not in visited:
                    dfs(neighbor)

        for city in range(n):
            if city not in visited:
                provinces += 1
                dfs(city)

        return provinces


class Solution:
    """
    Entry point class delegating province-counting logic to a strategy.

    Design principles:
        - Separation of concerns: Solution orchestrates, strategy computes.
        - Dependency injection: Strategy is swappable.
        - Lazy initialization: Default strategy created only when needed.
    """
    def __init__(self, strategy: StrategyInterface = None) -> None:
        self.strategy = strategy if strategy is not None else DFSProvincesStrategy()

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        Returns the number of provinces in the given adjacency matrix.

        Args:
            isConnected (List[List[int]]): Graph adjacency matrix.

        Returns:
            int: Number of provinces.
        """
        return self.strategy.solve(isConnected)


# Usage Suite
if __name__ == "__main__":
    solution = Solution()

    matrix1 = [[1,1,0],
               [1,1,0],
               [0,0,1]]
    print("Example 1:", solution.findCircleNum(matrix1))  # Expected: 2

    matrix2 = [[1,0,0],
               [0,1,0],
               [0,0,1]]
    print("Example 2:", solution.findCircleNum(matrix2))  # Expected: 3

    matrix3 = [[1,1,1],
               [1,1,1],
               [1,1,1]]
    print("Example 3:", solution.findCircleNum(matrix3))  # Expected: 1
