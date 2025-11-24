"""
104. Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:

Input: root = [1,null,2]
Output: 2


Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100

Topics
Tree
Depth-First Search
Breadth-First Search
Binary Tree


Developer Insights
Problem: Compute the maximum depth of a binary tree (longest path from root to leaf).

Constraints: Up to 10^4 nodes, values between -100 and 100.

Approach Options:
Recursive DFS: Elegant, simple, but uses O(h) stack space (h = height).
Iterative BFS: Level-order traversal using a queue, O(n) time, O(w) space (w = max width).

Architecture:
Define a DepthStrategy protocol.
Implement RecursiveDepthStrategy and BFSDepthStrategy.
Solution delegates to chosen strategy.

Complexity:
Time: O(n) for both strategies.
Space: O(h) for recursion, O(w) for BFS.

Pseudocode

Recursive DFS:

function maxDepth(root):
    if root is None:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))


Iterative BFS:

function maxDepth(root):
    if root is None:
        return 0
    queue = [root]
    depth = 0
    while queue not empty:
        size = len(queue)
        for i in range(size):
            node = queue.pop(0)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        depth += 1
    return depth

"""


from typing import Optional, Protocol
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        """Readable representation for debugging."""
        return f"TreeNode({self.val})"


class DepthStrategy(Protocol):
    """Defines contract for strategies that compute maximum depth of a binary tree."""
    def compute(self, root: Optional[TreeNode]) -> int: ...


class RecursiveDepthStrategy:
    """
    Strategy: Recursive DFS to compute maximum depth.
    Time: O(n), Space: O(h) where h is tree height.
    """
    def compute(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.compute(root.left), self.compute(root.right))


class BFSDepthStrategy:
    """
    Strategy: Iterative BFS (level-order traversal).
    Time: O(n), Space: O(w) where w is max width of tree.
    """
    def compute(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth = 0
        queue = deque([root])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        return depth


class Solution:
    """
    High-level orchestrator for maximum depth computation.

    Depends on abstraction (DepthStrategy).
    Default strategy: RecursiveDepthStrategy.
    """
    def __init__(self, strategy: DepthStrategy = RecursiveDepthStrategy()) -> None:
        self.strategy = strategy

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Compute maximum depth of a binary tree.

        Args:
            root (TreeNode | None): Root of the binary tree.

        Returns:
            int: Maximum depth of the tree.
        """
        return self.strategy.compute(root)


# Usage Examples

# Example 1: [3,9,20,null,null,15,7] → depth = 3
root1 = TreeNode(3,
                 TreeNode(9),
                 TreeNode(20, TreeNode(15), TreeNode(7)))
solver = Solution()
print(solver.maxDepth(root1))  # 3

# Example 2: [1,null,2] → depth = 2
root2 = TreeNode(1, None, TreeNode(2))
print(solver.maxDepth(root2))  # 2

# Example 3: Empty tree → depth = 0
print(solver.maxDepth(None))  # 0

# Example 4: Using BFS strategy
solver_bfs = Solution(strategy=BFSDepthStrategy())
print(solver_bfs.maxDepth(root1))  # 3
