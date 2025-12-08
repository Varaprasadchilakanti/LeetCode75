"""
841. Keys and Rooms

There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.
When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.
Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.

Example 1:
Input: rooms = [[1],[2],[3],[]]
Output: true
Explanation: 
We visit room 0 and pick up key 1.
We then visit room 1 and pick up key 2.
We then visit room 2 and pick up key 3.
We then visit room 3.
Since we were able to visit every room, we return true.

Example 2:
Input: rooms = [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can not enter room number 2 since the only key that unlocks it is in that room.

Constraints:
n == rooms.length
2 <= n <= 1000
0 <= rooms[i].length <= 1000
1 <= sum(rooms[i].length) <= 3000
0 <= rooms[i][j] < n
All the values of rooms[i] are unique.

Topics
Depth-First Search
Breadth-First Search
Graph


Developer Insights:

This problem is a classic reachability question in a directed graph:
Each room is a node.
Keys represent directed edges to other rooms.
Room 0 is the only initially unlocked node.
We must determine whether all nodes are reachable from node 0.
Why DFS works well
Graph is small (≤ 1000 nodes).
DFS explores all reachable rooms efficiently.
No need for extra structures beyond a visited set.
Complexity
Time: O(V + E)
Space: O(V) recursion depth + visited set
Fully optimal for this problem.


Pseudocode:

function canVisitAllRooms(rooms):
    n = len(rooms)
    visited = set()

    function dfs(room):
        mark room visited
        for key in rooms[room]:
            if key not visited:
                dfs(key)

    dfs(0)
    return len(visited) == n

"""

from typing import List, Protocol


class StrategyInterface(Protocol):
    """
    Protocol defining the interface for room‑visitation strategies.
    """
    def solve(self, rooms: List[List[int]]) -> bool:
        ...


class DFSRoomsStrategy:
    """
    Strategy implementing DFS to determine whether all rooms can be visited.

    Each room is treated as a graph node, and keys represent directed edges.
    DFS explores all reachable rooms starting from room 0.

    Complexity:
        Time:  O(V + E)
        Space: O(V)
    """
    def solve(self, rooms: List[List[int]]) -> bool:
        """
        Returns True if all rooms can be visited starting from room 0.

        Args:
            rooms (List[List[int]]): Adjacency list where rooms[i] contains keys to other rooms.

        Returns:
            bool: True if all rooms are reachable, False otherwise.
        """
        n = len(rooms)
        visited = set()

        def dfs(room: int) -> None:
            visited.add(room)
            for key in rooms[room]:
                if key not in visited:
                    dfs(key)

        dfs(0)
        return len(visited) == n


class Solution:
    """
    Entry point class delegating room‑visitation logic to a strategy.

    Design principles:
        - Separation of concerns: Solution orchestrates, strategy computes.
        - Dependency injection: Strategy is swappable.
        - Lazy initialization: Default strategy created only when needed.
    """
    def __init__(self, strategy: StrategyInterface = None) -> None:
        self.strategy = strategy if strategy is not None else DFSRoomsStrategy()

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """
        Determines whether all rooms can be visited.

        Args:
            rooms (List[List[int]]): Graph representation of rooms and keys.

        Returns:
            bool: True if all rooms are reachable, False otherwise.
        """
        return self.strategy.solve(rooms)


# Usage Suite (Executable Example)
if __name__ == "__main__":
    solution = Solution()

    rooms1 = [[1], [2], [3], []]
    print("Example 1:", solution.canVisitAllRooms(rooms1))  # Expected: True

    rooms2 = [[1, 3], [3, 0, 1], [2], [0]]
    print("Example 2:", solution.canVisitAllRooms(rooms2))  # Expected: False

    rooms3 = [[1, 2], [3], [3], []]
    print("Example 3:", solution.canVisitAllRooms(rooms3))  # Expected: True
