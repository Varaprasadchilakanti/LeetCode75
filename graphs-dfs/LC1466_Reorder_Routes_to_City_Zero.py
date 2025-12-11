"""
1466. Reorder Routes to Make All Paths Lead to the City Zero

There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.
Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.
This year, there will be a big event in the capital (city 0), and many people want to travel to this city.
Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.
It's guaranteed that each city can reach city 0 after reorder.

Example 1:
Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).

Example 2:
Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
Output: 2
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).

Example 3:
Input: n = 3, connections = [[1,0],[2,0]]
Output: 0

Constraints:
2 <= n <= 5 * 104
connections.length == n - 1
connections[i].length == 2
0 <= ai, bi <= n - 1
ai != bi

Topics
Depth-First Search
Breadth-First Search
Graph
Weekly Contest 191
icon
Companies
Hint 1
Treat the graph as undirected. Start a dfs from the root, if you come across an edge in the forward direction, you need to reverse the edge.

Developer Insights
This problem is a tree traversal with direction awareness.

Key Observations
The graph is a tree (n nodes, n‑1 edges).
Each edge is directed, but we want all nodes to reach city 0.
If an edge is oriented away from 0, we must reverse it.

The trick:
Treat the graph as undirected for traversal.
But annotate edges with direction:
u → v means original direction.
v → u means reverse direction.
During DFS from node 0, whenever we traverse an edge that originally pointed away from 0, we increment the counter.

Complexity
Time: O(n)
Space: O(n) adjacency + recursion depth
Fully optimal for tree traversal.

Edge Cases
Already all edges point toward 0 → answer = 0
Star‑shaped tree around 0 → answer = number of outward edges
Deep chain → DFS handles naturally

Pseudocode

build adjacency list:
    for each (a, b):
        add (b, 0) to adj[a]   # original direction a → b
        add (a, 1) to adj[b]   # reverse direction b → a

dfs(node, parent):
    for (neighbor, needs_reversal) in adj[node]:
        if neighbor == parent: continue
        count += needs_reversal
        dfs(neighbor, node)

return count

"""

from typing import List, Protocol


class StrategyInterface(Protocol):
    """
    Protocol defining the interface for route-reordering strategies.
    """
    def solve(self, n: int, connections: List[List[int]]) -> int:
        ...


class ReorderRoutesDFSStrategy:
    """
    Strategy implementing DFS to count the minimum number of edges
    that must be reversed so all cities can reach city 0.

    Each directed edge (a → b) is annotated:
        - From a to b: needs_reversal = 1
        - From b to a: needs_reversal = 0

    DFS from node 0 accumulates reversals whenever we traverse
    an edge originally pointing away from 0.

    Complexity:
        Time:  O(n)
        Space: O(n)
    """
    def solve(self, n: int, connections: List[List[int]]) -> int:
        """
        Computes the minimum number of edges to reverse so that
        every city can reach city 0.

        Args:
            n (int): Number of cities.
            connections (List[List[int]]): Directed edges.

        Returns:
            int: Minimum number of reversals required.
        """
        adj = [[] for _ in range(n)]

        # Build annotated adjacency list
        for a, b in connections:
            adj[a].append((b, 1))  # original direction a → b
            adj[b].append((a, 0))  # reverse direction b → a

        visited = set()
        reversals = 0

        def dfs(node: int) -> None:
            nonlocal reversals
            visited.add(node)

            for neighbor, needs_reversal in adj[node]:
                if neighbor not in visited:
                    reversals += needs_reversal
                    dfs(neighbor)

        dfs(0)
        return reversals


class Solution:
    """
    Entry point class delegating route-reordering logic to a strategy.

    Design principles:
        - Separation of concerns: Solution orchestrates, strategy computes.
        - Dependency injection: Strategy is swappable.
        - Lazy initialization: Default strategy created only when needed.
    """
    def __init__(self, strategy: StrategyInterface = None) -> None:
        self.strategy = strategy if strategy is not None else ReorderRoutesDFSStrategy()

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        """
        Returns the minimum number of edges to reverse so all cities
        can reach city 0.

        Args:
            n (int): Number of cities.
            connections (List[List[int]]): Directed edges.

        Returns:
            int: Minimum number of reversals required.
        """
        return self.strategy.solve(n, connections)


# Usage Suite
if __name__ == "__main__":
    solution = Solution()

    n1 = 6
    c1 = [[0,1],[1,3],[2,3],[4,0],[4,5]]
    print("Example 1:", solution.minReorder(n1, c1))  # Expected: 3

    n2 = 5
    c2 = [[1,0],[1,2],[3,2],[3,4]]
    print("Example 2:", solution.minReorder(n2, c2))  # Expected: 2

    n3 = 3
    c3 = [[1,0],[2,0]]
    print("Example 3:", solution.minReorder(n3, c3))  # Expected: 0
