"""
199. Binary Tree Right Side View

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.


Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,2,3,4,null,null,null,5]
Output: [1,3,4,5]

Example 3:
Input: root = [1,null,3]
Output: [1,3]

Example 4:
Input: root = []
Output: []


Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100


Topics
Tree
Depth-First Search
Breadth-First Search
Binary Tree


Developer Insights
Problem: Return the list of rightmost nodes visible from top to bottom when viewing a binary tree from the right side.
Approach: Use level-order traversal (BFS). At each level, the last node encountered is the rightmost visible node.
Why BFS: It naturally processes nodes level by level, allowing us to capture the last node per level efficiently.

Complexity:
Time: O(n) — each node visited once.
Space: O(w) — width of the tree (max queue size).


Pseudocode
function rightSideView(root):
    if root is null:
        return []

    queue = [root]
    result = []

    while queue is not empty:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.pop(0)
            if i == level_size - 1:
                result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result

"""

from typing import Optional, List, Protocol
from collections import deque

class TreeNode:
    """
    Binary tree node with optional left and right children.

    Attributes:
        val (int): Integer value stored in the node.
        left (Optional[TreeNode]): Reference to the left child node.
        right (Optional[TreeNode]): Reference to the right child node.

    Design notes:
        - __str__ provides compact subtree visualization.
        - __repr__ aids debugging with node identity.
    """
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
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
    def solve(self, root: Optional[TreeNode]) -> List[int]: ...


class RightSideViewStrategy:
    """
    Strategy to compute the right side view of a binary tree using level-order traversal.

    At each level, the last node encountered is visible from the right side.

    Complexity:
        - Time: O(n)
        - Space: O(w), where w is the maximum width of the tree.
    """
    def solve(self, root: Optional[TreeNode]) -> List[int]:
        """
        Returns the list of node values visible from the right side of the binary tree.

        Args:
            root (Optional[TreeNode]): Root of the binary tree.

        Returns:
            List[int]: Rightmost node values from top to bottom.
        """
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                if i == level_size - 1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result


class Solution:
    """
    Entry point class that delegates to a right side view strategy.

    Design principles:
        - Separation of concerns: Solution orchestrates, strategy computes.
        - Dependency injection: Allows strategy substitution for testing or variants.
    """
    def __init__(self, strategy: Optional[StrategyInterface] = None) -> None:
        self.strategy = strategy if strategy is not None else RightSideViewStrategy()

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Returns the list of node values visible from the right side of the binary tree.

        Args:
            root (Optional[TreeNode]): Root of the binary tree.

        Returns:
            List[int]: Rightmost node values from top to bottom.
        """
        return self.strategy.solve(root)


# Usage Suite: Right Side View

def build_example_1():
    # Input: [1,2,3,null,5,null,4]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)
    return root

def build_example_2():
    # Input: [1,2,3,4,null,null,null,5]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(5)
    return root

def build_example_3():
    # Input: [1,null,3]
    root = TreeNode(1)
    root.right = TreeNode(3)
    return root

def build_example_4():
    # Input: []
    return None

if __name__ == "__main__":
    solution = Solution()

    root1 = build_example_1()
    print("Example 1 Output:", solution.rightSideView(root1))  # Expected: [1, 3, 4]

    root2 = build_example_2()
    print("Example 2 Output:", solution.rightSideView(root2))  # Expected: [1, 3, 4, 5]

    root3 = build_example_3()
    print("Example 3 Output:", solution.rightSideView(root3))  # Expected: [1, 3]

    root4 = build_example_4()
    print("Example 4 Output:", solution.rightSideView(root4))  # Expected: []

