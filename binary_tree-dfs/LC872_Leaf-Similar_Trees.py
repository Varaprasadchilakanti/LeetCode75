"""
872. Leaf-Similar Trees

Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
Two binary trees are considered leaf-similar if their leaf value sequence is the same.
Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.


Example 1:

Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true

Example 2:

Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false


Constraints:

The number of nodes in each tree will be in the range [1, 200].
Both of the given trees will have values in the range [0, 200].

Topics
Tree
Depth-First Search
Binary Tree
Weekly Contest 94


Developer Insights
Core Responsibility: Extract leaf sequences from both trees and compare them.
Design Choice: Use DFS traversal to collect leaves in left-to-right order.

Efficiency:
Time Complexity: 𝑂(𝑛+𝑚), where 𝑛,𝑚 are the number of nodes in each tree.Space Complexity: 𝑂(𝐿), where 𝐿 is the number of leaves (stored in lists).

Extensibility:
Strategy pattern allows swapping DFS with BFS or iterative traversal.
Leaf extraction logic is isolated for reuse.

Testability:
Each function is modular and independently testable.
Edge cases (single-node trees, skewed trees, identical vs. different leaves) are covered.


Pseudocode

function get_leaves(node):
    if node is null:
        return []
    if node.left is null and node.right is null:
        return [node.val]
    return get_leaves(node.left) + get_leaves(node.right)

function leafSimilar(root1, root2):
    leaves1 = get_leaves(root1)
    leaves2 = get_leaves(root2)
    return leaves1 == leaves2

"""

from typing import Optional, List, Protocol

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        """
        Returns a string representation of the tree rooted at this node.
        Format: val(left_subtree, right_subtree)
        Example: 3(5(6,2(7,4)),1(9,8))
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
    def solve(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool: ...


class LeafSimilarStrategy:
    """
    Strategy to determine if two binary trees are leaf-similar.
    Implements DFS traversal to collect leaf sequences.
    """
    def solve(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self._get_leaves(root1) == self._get_leaves(root2)

    def _get_leaves(self, node: Optional[TreeNode]) -> List[int]:
        """
        Collects leaf nodes in left-to-right order using DFS.
        """
        if not node:
            return []
        if not node.left and not node.right:
            return [node.val]
        return self._get_leaves(node.left) + self._get_leaves(node.right)


class Solution:
    """
    Entry point class that delegates to a strategy.
    """
    def __init__(self, strategy: StrategyInterface = LeafSimilarStrategy()) -> None:
        self.strategy = strategy

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        """
        Determines if two binary trees are leaf-similar.
        """
        return self.strategy.solve(root1, root2)


# Usage Example

if __name__ == "__main__":
    # Construct Tree 1
    root1 = TreeNode(3,
        left=TreeNode(5,
            left=TreeNode(6),
            right=TreeNode(2,
                left=TreeNode(7),
                right=TreeNode(4)
            )
        ),
        right=TreeNode(1,
            left=TreeNode(9),
            right=TreeNode(8)
        )
    )

    # Construct Tree 2
    root2 = TreeNode(3,
        left=TreeNode(5,
            left=TreeNode(6),
            right=TreeNode(7)
        ),
        right=TreeNode(1,
            left=TreeNode(4),
            right=TreeNode(2,
                left=TreeNode(9),
                right=TreeNode(8)
            )
        )
    )

    solution = Solution()
    print("Tree 1:", root1)   # Prints structured tree
    print("Tree 2:", root2)   # Prints structured tree
    print("Leaf-Similar?", solution.leafSimilar(root1, root2))  # Output: True
