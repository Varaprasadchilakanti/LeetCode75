"""
700. Search in a Binary Search Tree

You are given the root of a binary search tree (BST) and an integer val.
Find the node in the BST that the node's value equals val 
and return the subtree rooted with that node.
If such a node does not exist, return null.

Example 1:
Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]

Example 2:
Input: root = [4,2,7,1,3], val = 5
Output: []

Constraints:
The number of nodes in the tree is in the range [1, 5000].
1 <= Node.val <= 107
root is a binary search tree.
1 <= val <= 107

Topics
Tree
Binary Search Tree
Binary Tree

Developer Insights
Searching in a BST is one of the most fundamental tree operations.
Because of the BST invariant:
left subtree values  < node.val < right subtree values
we can prune half the search space at each step.
Why this matters:
Optimality: O(h) time, where h is tree height (O(log n) for balanced trees).
Elegance: No need to explore both children; direction is deterministic.
Clarity: The logic is minimal and intention‑revealing.
Strategy Pattern Justification
Searching is core logic → belongs in a strategy.
Solution orchestrates and delegates → clean architecture.
Strategy is swappable → supports variants
(iterative, recursive, balanced BST search, etc.).

Pseudocode
function searchBST(node, val):
    if node is null:
        return null

    if node.val == val:
        return node

    if val < node.val:
        return searchBST(node.left, val)
    else:
        return searchBST(node.right, val)

"""
from typing import Optional, Protocol


class TreeNode:
    """
    Binary tree node with optional left and right children.

    Attributes:
        val (int): Value stored in the node.
        left (Optional[TreeNode]): Left child.
        right (Optional[TreeNode]): Right child.

    Design notes:
        - __str__ prints the subtree for quick visualization.
        - __repr__ provides a concise developer‑friendly identity.
    """
    def __init__(self, val: int = 0,
                 left: Optional['TreeNode'] = None,
                 right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        left_str = str(self.left) if self.left else "None"
        right_str = str(self.right) if self.right else "None"
        return f"{self.val}({left_str},{right_str})"

    def __repr__(self) -> str:
        return f"TreeNode(val={self.val})"


class StrategyInterface(Protocol):
    """
    Protocol defining the interface for BST search strategies.
    """
    def solve(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        ...


class SearchBSTStrategy:
    """
    Strategy implementing recursive search in a Binary Search Tree.

    The BST invariant allows pruning half the search space at each step.

    Complexity:
        Time:  O(h) where h is tree height.
        Space: O(h) recursion depth.
    """
    def solve(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        Searches for a node whose value equals `val` and returns the subtree
        rooted at that node. Returns None if not found.

        Args:
            root (Optional[TreeNode]): Root of the BST.
            val (int): Target value to search for.

        Returns:
            Optional[TreeNode]: Subtree rooted at the found node or None.
        """
        if not root:
            return None

        if root.val == val:
            return root

        if val < root.val:
            return self.solve(root.left, val)
        else:
            return self.solve(root.right, val)


class Solution:
    """
    Entry point class delegating BST search to a strategy.

    Design principles:
        - Separation of concerns: Solution orchestrates, strategy computes.
        - Dependency injection: Strategy is swappable.
        - Lazy initialization: Default strategy created only if none provided.
    """
    def __init__(self, strategy: Optional[StrategyInterface] = None) -> None:
        self.strategy = strategy if strategy is not None else SearchBSTStrategy()

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        Delegates BST search to the configured strategy.

        Args:
            root (Optional[TreeNode]): Root of the BST.
            val (int): Target value.

        Returns:
            Optional[TreeNode]: Subtree rooted at found node or None.
        """
        return self.strategy.solve(root, val)


# Usage Suite (Executable Example)

def build_example_tree():
    # Tree: [4,2,7,1,3]
    root = TreeNode(4)
    root.left = TreeNode(2, TreeNode(1), TreeNode(3))
    root.right = TreeNode(7)
    return root


if __name__ == "__main__":
    solution = Solution()

    root = build_example_tree()

    print("Search for 2:")
    result = solution.searchBST(root, 2)
    print(result)  # Expected: 2(1,None),(3,None)

    print("Search for 5:")
    result = solution.searchBST(root, 5)
    print(result)  # Expected: None
