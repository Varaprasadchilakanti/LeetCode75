"""
450. Delete Node in a BST

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.
Basically, the deletion can be divided into two stages:
Search for a node to remove.
If the node is found, delete the node.

Example 1:
Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:
Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.

Example 3:
Input: root = [], key = 0
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 104].
-105 <= Node.val <= 105
Each node has a unique value.
root is a valid binary search tree.
-105 <= key <= 105
Follow up: Could you solve it with time complexity O(height of tree)?

Topics
Tree
Binary Search Tree
Binary Tree

Developer Insights:
Deleting a node in a BST requires handling three structural cases:

Case 1 — Node not found
Return the tree unchanged.

Case 2 — Node has 0 or 1 child
Replace the node with its child (or None).

Case 3 — Node has 2 children
Replace the node’s value with its inorder successor (smallest value in right subtree), then delete the successor node from the right subtree.

Why this works
The inorder successor preserves BST ordering and ensures structural correctness.
Complexity
Time: O(h) where h = tree height
Space: O(h) recursion depth
Optimal for BST deletion.

Pseudocode
function deleteNode(node, key):
    if node is null:
        return null

    if key < node.val:
        node.left = deleteNode(node.left, key)
    else if key > node.val:
        node.right = deleteNode(node.right, key)
    else:
        # Node found
        if node has no left:
            return node.right
        if node has no right:
            return node.left

        # Node has two children
        successor = findMin(node.right)
        node.val = successor.val
        node.right = deleteNode(node.right, successor.val)

    return node

"""

from typing import Optional, Protocol


class TreeNode:
    """
    Binary Search Tree node with optional left and right children.

    Attributes:
        val (int): Value stored in the node.
        left (Optional[TreeNode]): Left child.
        right (Optional[TreeNode]): Right child.

    Design notes:
        - __str__ prints the subtree for visualization.
        - __repr__ provides a concise identity for debugging.
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
    Protocol defining the interface for BST deletion strategies.
    """
    def solve(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        ...


class DeleteNodeBSTStrategy:
    """
    Strategy implementing deletion of a node in a Binary Search Tree.

    Handles:
        - Node not found
        - Node with 0 or 1 child
        - Node with 2 children (using inorder successor)

    Complexity:
        Time:  O(h)
        Space: O(h)
    """
    def solve(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        Deletes the node with value `key` from the BST and returns the updated root.

        Args:
            root (Optional[TreeNode]): Root of the BST.
            key (int): Value to delete.

        Returns:
            Optional[TreeNode]: Updated root after deletion.
        """
        if not root:
            return None

        if key < root.val:
            root.left = self.solve(root.left, key)
        elif key > root.val:
            root.right = self.solve(root.right, key)
        else:
            # Node found
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            # Node has two children: find inorder successor
            successor = self._find_min(root.right)
            root.val = successor.val
            root.right = self.solve(root.right, successor.val)

        return root

    def _find_min(self, node: TreeNode) -> TreeNode:
        """
        Returns the node with the minimum value in a BST subtree.
        """
        while node.left:
            node = node.left
        return node


class Solution:
    """
    Entry point class delegating BST deletion to a strategy.

    Design principles:
        - Separation of concerns: Solution orchestrates, strategy computes.
        - Dependency injection: Strategy is swappable.
        - Lazy initialization: Default strategy created only when needed.
    """
    def __init__(self, strategy: Optional[StrategyInterface] = None) -> None:
        self.strategy = strategy if strategy is not None else DeleteNodeBSTStrategy()

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        Deletes a node with value `key` from the BST.

        Args:
            root (Optional[TreeNode]): Root of the BST.
            key (int): Value to delete.

        Returns:
            Optional[TreeNode]: Updated root after deletion.
        """
        return self.strategy.solve(root, key)


# Usage Suite (Executable Example)

def build_example_tree():
    # Tree: [5,3,6,2,4,null,7]
    root = TreeNode(5)
    root.left = TreeNode(3, TreeNode(2), TreeNode(4))
    root.right = TreeNode(6, None, TreeNode(7))
    return root


if __name__ == "__main__":
    solution = Solution()

    root = build_example_tree()

    print("Original Tree:")
    print(root)

    print("\nDelete key = 3")
    updated = solution.deleteNode(root, 3)
    print(updated)

    print("\nDelete key = 0 (not present)")
    updated = solution.deleteNode(updated, 0)
    print(updated)
