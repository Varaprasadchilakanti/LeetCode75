"""
399. Evaluate Division

You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.
You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.
Return the answers to all queries. If a single answer cannot be determined, return -1.0.
Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.
Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

Example 1:
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0

Example 2:
Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]

Example 3:
Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]

Constraints:
1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj consist of lower case English letters and digits.

Topics
Array
String
Depth-First Search
Breadth-First Search
Union Find
Graph
Shortest Path

Hint 1
Do you recognize this as a graph problem?


Developer Insights
This problem is a weighted graph reachability problem.

Graph Model
Each equation:
A / B = k
creates two directed edges:
A → B with weight k
B → A with weight 1/k
Queries ask:
C / D = ?
This becomes: Find a path from C to D and multiply edge weights along the path.

Why DFS?
Graph is tiny (≤ 20 variables).
DFS is clean, optimal, and easy to reason about.
No need for shortest path algorithms; any valid path works.

Complexity
Graph build: O(E)
Each query DFS: O(V + E)
Worst case: O(Q * (V + E))
With constraints, this is trivial.

Edge Cases
Variable not in graph → return -1.0
Query x / x where x exists → return 1.0
No path between variables → return -1.0

Pseudocode
build graph:
    for each (A, B, k):
        add edge A -> B with weight k
        add edge B -> A with weight 1/k

function dfs(curr, target, product, visited):
    if curr == target:
        return product
    mark curr visited
    for (neighbor, weight) in graph[curr]:
        if neighbor not visited:
            result = dfs(neighbor, target, product * weight, visited)
            if result != -1:
                return result
    return -1

for each query (C, D):
    if C or D not in graph:
        answer = -1
    else:
        answer = dfs(C, D, 1, empty_set)
return answers


"""


from typing import List, Dict, Tuple, Protocol


class StrategyInterface(Protocol):
    """
    Protocol defining the interface for equation-evaluation strategies.
    """
    def solve(
        self,
        equations: List[List[str]],
        values: List[float],
        queries: List[List[str]]
    ) -> List[float]:
        ...


class EvaluateDivisionDFSStrategy:
    """
    Strategy implementing DFS-based evaluation of division equations.

    The equations form a weighted bidirectional graph:
        A / B = k  =>  A -> B (k), B -> A (1/k)

    Queries ask for the product of weights along any valid path.
    """

    def solve(
        self,
        equations: List[List[str]],
        values: List[float],
        queries: List[List[str]]
    ) -> List[float]:
        """
        Evaluates each query using DFS on a weighted graph.

        Args:
            equations: List of variable pairs.
            values: Corresponding division results.
            queries: Division queries to evaluate.

        Returns:
            List[float]: Answers for each query, or -1.0 if undefined.
        """
        graph: Dict[str, List[Tuple[str, float]]] = {}

        # Build graph
        for (a, b), k in zip(equations, values):
            graph.setdefault(a, []).append((b, k))
            graph.setdefault(b, []).append((a, 1.0 / k))

        def dfs(curr: str, target: str, product: float, visited: set) -> float:
            if curr == target:
                return product
            visited.add(curr)

            for neighbor, weight in graph.get(curr, []):
                if neighbor not in visited:
                    result = dfs(neighbor, target, product * weight, visited)
                    if result != -1.0:
                        return result

            return -1.0

        results = []
        for c, d in queries:
            if c not in graph or d not in graph:
                results.append(-1.0)
            else:
                results.append(dfs(c, d, 1.0, set()))

        return results


class Solution:
    """
    Entry point class delegating equation evaluation to a strategy.

    Design principles:
        - Separation of concerns: Solution orchestrates, strategy computes.
        - Dependency injection: Strategy is swappable.
        - Lazy initialization: Default strategy created only when needed.
    """

    def __init__(self, strategy: StrategyInterface = None) -> None:
        self.strategy = strategy if strategy is not None else EvaluateDivisionDFSStrategy()

    def calcEquation(
        self,
        equations: List[List[str]],
        values: List[float],
        queries: List[List[str]]
    ) -> List[float]:
        """
        Computes answers for each division query.

        Args:
            equations: Variable pairs.
            values: Division results.
            queries: Queries to evaluate.

        Returns:
            List[float]: Computed answers.
        """
        return self.strategy.solve(equations, values, queries)


# Usage Suite
if __name__ == "__main__":
    solution = Solution()

    eq = [["a","b"],["b","c"]]
    val = [2.0, 3.0]
    qr = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

    print(solution.calcEquation(eq, val, qr))
    # Expected: [6.0, 0.5, -1.0, 1.0, -1.0]
