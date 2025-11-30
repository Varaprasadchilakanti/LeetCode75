"""
236. Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”


Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.


Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.


Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1


Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.


Topics
Tree
Depth-First Search
Binary Tree


Strategy
Use DFS traversal.
At each node:
If node is None, return None.
If node is p or q, return node.
Recurse left and right.
If both sides return non-null → current node is LCA.
Else return non-null child.


Pseudocode: Lowest Common Ancestor (LCA) via DFS

function solve(root, p, q):
    if root is null:
        return null

    if root is p or root is q:
        return root

    left_result = solve(root.left, p, q)
    right_result = solve(root.right, p, q)

    if left_result is not null and right_result is not null:
        return root  // both p and q found in different subtrees

    if left_result is not null:
        return left_result  // both nodes are in left subtree

    return right_result  // both nodes are in right subtree or not found

"""

from typing import Optional, Protocol

class TreeNode:
    """
    Binary tree node with optional left and right children.
    """
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        """
        Compact string representation of the tree rooted at this node.
        Format: val(left_subtree, right_subtree)
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
    def solve(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode: ...


class LowestCommonAncestorStrategy:
    """
    Strategy to compute the lowest common ancestor (LCA) of two nodes in a binary tree.

    Uses DFS traversal. At each node:
      - If node is None → return None.
      - If node is p or q → return node.
      - Recurse left and right.
      - If both sides return non-null → current node is LCA.
      - Else return the non-null child.
    """
    def solve(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Finds the lowest common ancestor of nodes p and q in the binary tree.

        Args:
            root (TreeNode): Root of the binary tree.
            p (TreeNode): First target node.
            q (TreeNode): Second target node.

        Returns:
            TreeNode: The lowest common ancestor node.
        """
        if not root or root == p or root == q:
            return root

        left = self.solve(root.left, p, q)
        right = self.solve(root.right, p, q)

        if left and right:
            return root
        return left if left else right


class Solution:
    """
    Entry point class delegating to an LCA strategy.
    """
    def __init__(self, strategy: StrategyInterface = LowestCommonAncestorStrategy()) -> None:
        self.strategy = strategy

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Returns the lowest common ancestor of nodes p and q.

        Args:
            root (TreeNode): Root of the binary tree.
            p (TreeNode): First target node.
            q (TreeNode): Second target node.

        Returns:
            TreeNode: The lowest common ancestor node.
        """
        return self.strategy.solve(root, p, q)


# Usage Examples with Output

def build_example_1():
    # Tree: [3,5,1,6,2,0,8,null,null,7,4]
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    return root, root.left, root.right  # p = 5, q = 1

def build_example_2():
    # Same tree as example 1
    root, p, _ = build_example_1()
    q = root.left.right.right  # node 4
    return root, p, q

def build_example_3():
    # Tree: [1,2]
    root = TreeNode(1)
    root.left = TreeNode(2)
    return root, root, root.left  # p = 1, q = 2

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    root1, p1, q1 = build_example_1()
    lca1 = solution.lowestCommonAncestor(root1, p1, q1)
    print("Example 1 LCA:", lca1.val)  # Expected: 3

    # Example 2
    root2, p2, q2 = build_example_2()
    lca2 = solution.lowestCommonAncestor(root2, p2, q2)
    print("Example 2 LCA:", lca2.val)  # Expected: 5

    # Example 3
    root3, p3, q3 = build_example_3()
    lca3 = solution.lowestCommonAncestor(root3, p3, q3)
    print("Example 3 LCA:", lca3.val)  # Expected: 1
