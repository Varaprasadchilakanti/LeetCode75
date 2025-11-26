"""
1448. Count Good Nodes in Binary Tree

Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
Return the number of good nodes in the binary tree.


Example 1:

Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.


Example 2:

Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.


Example 3:

Input: root = [1]
Output: 1
Explanation: Root is considered as good.


Constraints:

The number of nodes in the binary tree is in the range [1, 10^5].
Each node's value is between [-10^4, 10^4].


Topics
Tree
Depth-First Search
Breadth-First Search
Binary Tree
Biweekly Contest 26


Hint 1
Use DFS (Depth First Search) to traverse the tree, and constantly keep track of the current path maximum.


Developer Insights

Core Responsibility: Traverse the tree and count nodes that satisfy the "good" condition.
Design Choice: Use DFS traversal while maintaining the maximum value seen along the path.

Efficiency:
Time Complexity: 𝑂(𝑛), visiting each node once.
Space Complexity: 𝑂(ℎ), recursion stack depth (where ℎ is tree height).
Extensibility: Strategy pattern allows swapping DFS with BFS if needed.
Testability: Modular design ensures independent testing of traversal and condition logic.
Resilience: Handles edge cases (single-node tree, skewed tree, negative values).


Pseudocode

function dfs(node, max_so_far):
    if node is null:
        return 0
    good = 1 if node.val >= max_so_far else 0
    new_max = max(max_so_far, node.val)
    return good + dfs(node.left, new_max) + dfs(node.right, new_max)

function goodNodes(root):
    return dfs(root, root.val)

"""

from typing import Optional, Protocol

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        """
        Compact string representation of the tree rooted at this node.
        Example: 3(1(3,None),4(1,5))
        """
        left_str = str(self.left) if self.left else "None"
        right_str = str(self.right) if self.right else "None"
        return f"{self.val}({left_str},{right_str})"

    def __repr__(self) -> str:
        """
        Developer-friendly representation for debugging.
        """
        return f"TreeNode(val={self.val})"


class StrategyInterface(Protocol):
    def solve(self, root: Optional[TreeNode]) -> int: ...


class GoodNodesStrategy:
    """
    Strategy to count 'good' nodes in a binary tree.
    A node is good if no ancestor has a value greater than it.
    """
    def solve(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self._dfs(root, root.val)

    def _dfs(self, node: Optional[TreeNode], max_so_far: int) -> int:
        if not node:
            return 0
        good = 1 if node.val >= max_so_far else 0
        new_max = max(max_so_far, node.val)
        return good + self._dfs(node.left, new_max) + self._dfs(node.right, new_max)


class Solution:
    """
    Entry point class that delegates to a strategy.
    """
    def __init__(self, strategy: StrategyInterface = GoodNodesStrategy()) -> None:
        self.strategy = strategy

    def goodNodes(self, root: Optional[TreeNode]) -> int:
        """
        Counts the number of good nodes in the binary tree.
        """
        return self.strategy.solve(root)

# Usage Example

if __name__ == "__main__":
    # Example 1: root = [3,1,4,3,null,1,5]
    root = TreeNode(3,
        left=TreeNode(1,
            left=TreeNode(3)
        ),
        right=TreeNode(4,
            left=TreeNode(1),
            right=TreeNode(5)
        )
    )

    solution = Solution()
    print("Tree:", root)  # Prints structured tree
    print("Good Nodes Count:", solution.goodNodes(root))  # Output: 4

    # Example 2: root = [3,3,null,4,2]
    root2 = TreeNode(3,
        left=TreeNode(3,
            left=TreeNode(4),
            right=TreeNode(2)
        )
    )
    print("Tree:", root2)
    print("Good Nodes Count:", solution.goodNodes(root2))  # Output: 3

    # Example 3: root = [1]
    root3 = TreeNode(1)
    print("Tree:", root3)
    print("Good Nodes Count:", solution.goodNodes(root3))  # Output: 1
