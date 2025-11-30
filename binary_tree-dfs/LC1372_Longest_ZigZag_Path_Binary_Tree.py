"""
1372. Longest ZigZag Path in a Binary Tree

You are given the root of a binary tree.
A ZigZag path for a binary tree is defined as follow:
Choose any node in the binary tree and a direction (right or left).
If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
Change the direction from right to left or from left to right.
Repeat the second and third steps until you can't move in the tree.
Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.


Example 1:

Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
Output: 3
Explanation: Longest ZigZag path in blue nodes (right -> left -> right).

Example 2:

Input: root = [1,1,1,null,1,null,null,1,1,null,1]
Output: 4
Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).

Example 3:

Input: root = [1]
Output: 0


Constraints:

The number of nodes in the tree is in the range [1, 5 * 104].
1 <= Node.val <= 100

Topics
Dynamic Programming
Tree
Depth-First Search
Binary Tree

Hint 1
Create this function maxZigZag(node, direction) maximum zigzag given a node and direction (right or left).


Developer Insights
State management: path_length is stored in the strategy instance to accumulate results during DFS. Instantiating a new strategy per Solution ensures no stale state leaks across calls.
Protocol delegation: StrategyInterface defines the contract. Solution depends on the abstraction, not the implementation, enabling easy substitution.
DFS design: Alternation is enforced by flipping goLeft at each recursive step. Resetting steps to 1 when starting a new path ensures correctness.
Extensibility: Alternative strategies (iterative, memoized) can be injected without modifying Solution.

Pseudocode

function longestZigZag(root):
    pathLength = 0

    function dfs(node, goLeft, steps):
        if node is null:
            return
        pathLength = max(pathLength, steps)

        if goLeft:
            dfs(node.left, false, steps + 1)  // continue ZigZag
            dfs(node.right, true, 1)          // start new path
        else:
            dfs(node.left, false, 1)          // start new path
            dfs(node.right, true, steps + 1)  // continue ZigZag

    dfs(root, true, 0)
    return pathLength
"""


from typing import Optional, Protocol

class TreeNode:
    """
    Binary tree node with optional left and right children.

    Attributes:
        val (int): Integer value stored in the node.
        left (Optional[TreeNode]): Reference to the left child node.
        right (Optional[TreeNode]): Reference to the right child node.

    Design notes:
        - Provides __str__ for compact visualization of the subtree.
        - Provides __repr__ for developer-friendly inspection.
        - Intended for use in algorithmic problems where tree traversal is required.
    """
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        """
        Returns a compact string representation of the subtree rooted at this node.

        Format:
            val(left_subtree, right_subtree)

        Example:
            1(None,1(1,1(None,None)))

        This aids debugging and quick visualization of tree structure.
        """
        left_str = str(self.left) if self.left else "None"
        right_str = str(self.right) if self.right else "None"
        return f"{self.val}({left_str},{right_str})"

    def __repr__(self) -> str:
        """
        Developer-friendly representation focused on the node identity.

        Example:
            TreeNode(val=5)

        Useful for logging and debugging without expanding the entire subtree.
        """
        return f"TreeNode(val={self.val})"


class StrategyInterface(Protocol):
    """
    Protocol defining the interface for strategy classes.

    Methods:
        solve(root: Optional[TreeNode]) -> int
            Computes a problem-specific result given the root of a binary tree.
    """
    def solve(self, root: Optional[TreeNode]) -> int: ...


class LongestZigZagStrategy:
    """
    Strategy to compute the longest ZigZag path in a binary tree using DFS with directional state.

    Problem definition:
        - A ZigZag path alternates direction at every step (left → right → left → ...).
        - Path length is defined as the number of edges traversed.
        - The goal is to return the maximum ZigZag path length across the tree.

    Approach:
        - Use depth-first search (DFS) with parameters:
            node: current TreeNode
            goLeft: boolean indicating whether the next step continues left
            steps: current ZigZag length in edges
        - At each node:
            1. Update global maximum with current steps.
            2. If continuing left:
                - Recurse to left child with flipped direction and steps+1.
                - Recurse to right child starting a new path with steps=1.
            3. If continuing right:
                - Recurse to left child starting a new path with steps=1.
                - Recurse to right child with flipped direction and steps+1.

    Complexity:
        - Time: O(n), each node visited a constant number of times.
        - Space: O(h) recursion depth, worst-case O(n).

    Attributes:
        path_length (int): Tracks the maximum ZigZag path length found during traversal.
    """
    def __init__(self) -> None:
        self.path_length = 0

    def solve(self, root: Optional[TreeNode]) -> int:
        """
        Computes the length of the longest ZigZag path in the binary tree.

        Args:
            root (Optional[TreeNode]): Root of the binary tree.

        Returns:
            int: Maximum ZigZag path length (number of edges).
        """
        def dfs(node: Optional[TreeNode], goLeft: bool, steps: int) -> None:
            if node:
                # Update global maximum with the current path length
                self.path_length = max(self.path_length, steps)

                if goLeft:
                    # Continue ZigZag by going left; next step must go right
                    dfs(node.left, False, steps + 1)
                    # Start a new ZigZag at right child
                    dfs(node.right, True, 1)
                else:
                    # Start a new ZigZag at left child
                    dfs(node.left, False, 1)
                    # Continue ZigZag by going right; next step must go left
                    dfs(node.right, True, steps + 1)

        # Initiate DFS from root; recursion covers both directions and resets
        dfs(root, True, 0)
        return self.path_length


class Solution:
    """
    Entry point class that delegates to a ZigZag strategy.

    Design principles:
        - Separation of concerns: Solution orchestrates, strategy computes.
        - Dependency injection: Allows swapping in alternative strategies for testing or extension.
        - Ensures fresh strategy instance per Solution to avoid stale state.

    Methods:
        longestZigZag(root: Optional[TreeNode]) -> int
            Returns the length of the longest ZigZag path in the binary tree.
    """
    def __init__(self, strategy: Optional[StrategyInterface] = None) -> None:
        self.strategy = strategy if strategy is not None else LongestZigZagStrategy()

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        """
        Returns the length of the longest ZigZag path in the binary tree.

        Args:
            root (Optional[TreeNode]): Root of the binary tree.

        Returns:
            int: Maximum ZigZag path length (number of edges).
        """
        return self.strategy.solve(root)


def build_example_1():
    # Input: [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
    root = TreeNode(1)
    root.right = TreeNode(1)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(1)
    root.right.left.left = TreeNode(1)
    root.right.left.right = TreeNode(1)
    root.right.left.left.right = TreeNode(1)
    return root

def build_example_2():
    # Input: [1,1,1,null,1,null,null,1,1,null,1]
    root = TreeNode(1)
    root.left = TreeNode(1)
    root.right = TreeNode(1)
    root.left.right = TreeNode(1)
    root.left.right.left = TreeNode(1)
    root.left.right.left.right = TreeNode(1)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(1)
    return root

def build_example_3():
    # Input: [1]
    return TreeNode(1)

if __name__ == "__main__":

    # Example 1
    solution = Solution()
    root1 = build_example_1()
    result1 = solution.longestZigZag(root1)
    print("Example 1 Output:", result1)  # Expected: 3

    # Example 2
    solution = Solution()
    root2 = build_example_2()
    result2 = solution.longestZigZag(root2)
    print("Example 2 Output:", result2)  # Expected: 4

    # Example 3
    solution = Solution()
    root3 = build_example_3()
    result3 = solution.longestZigZag(root3)
    print("Example 3 Output:", result3)  # Expected: 0
