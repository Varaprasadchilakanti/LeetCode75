"""
1161. Maximum Level Sum of a Binary Tree

Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
Return the smallest level x such that the sum of all the values of nodes at level x is maximal.


Example 1:
Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.

Example 2:
Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2

Constraints:
The number of nodes in the tree is in the range [1, 10^4].
-10^5 <= Node.val <= 10^5

Topics
Tree
Depth-First Search
Breadth-First Search
Binary Tree


Hint 1
Calculate the sum for each level then find the level with the maximum sum.
Hint 2
How can you traverse the tree ?
Hint 3
How can you sum up the values for every level ?
Hint 4
Use DFS or BFS to traverse the tree keeping the level of each node, and sum up those values with a map or a frequency array.


Developer Insights:
Problem: Find the level (1-indexed) of a binary tree with the maximum sum of node values.
Approach: Use Breadth-First Search (BFS) to traverse level by level, summing node values per level.
Why BFS: It naturally processes nodes level by level, making it ideal for aggregating level sums.

Complexity:
Time: O(n) — each node visited once.
Space: O(w) — width of the tree (max queue size).


Pseudocode

function maxLevelSum(root):
    if root is null:
        return 0

    queue = [root]
    max_sum = -infinity
    max_level = 1
    current_level = 1

    while queue is not empty:
        level_size = len(queue)
        level_sum = 0

        for i in range(level_size):
            node = queue.pop(0)
            level_sum += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if level_sum > max_sum:
            max_sum = level_sum
            max_level = current_level

        current_level += 1

    return max_level

"""


from typing import Optional, Protocol
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
    def solve(self, root: Optional[TreeNode]) -> int: ...


class MaxLevelSumStrategy:
    """
    Strategy to compute the level with the maximum sum in a binary tree using BFS.

    At each level:
        - Aggregate node values.
        - Track maximum sum and corresponding level.

    Complexity:
        - Time: O(n)
        - Space: O(w), where w is the maximum width of the tree.
    """
    def solve(self, root: Optional[TreeNode]) -> int:
        """
        Returns the smallest level x such that the sum of all node values at level x is maximal.

        Args:
            root (Optional[TreeNode]): Root of the binary tree.

        Returns:
            int: Level index (1-based) with the maximum sum.
        """
        if not root:
            return 0

        queue = deque([root])
        max_sum = float('-inf')
        max_level = 1
        current_level = 1

        while queue:
            level_size = len(queue)
            level_sum = 0

            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                max_level = current_level

            current_level += 1

        return max_level


class Solution:
    """
    Entry point class that delegates to a level sum strategy.

    Design principles:
        - Separation of concerns: Solution orchestrates, strategy computes.
        - Dependency injection: Allows strategy substitution for testing or variants.
    """
    def __init__(self, strategy: Optional[StrategyInterface] = None) -> None:
        self.strategy = strategy if strategy is not None else MaxLevelSumStrategy()

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        """
        Returns the level with the maximum sum of node values.

        Args:
            root (Optional[TreeNode]): Root of the binary tree.

        Returns:
            int: Level index (1-based) with the maximum sum.
        """
        return self.strategy.solve(root)


# Usage Suite

def build_example_1():
    # Input: [1,7,0,7,-8,null,null]
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(0)
    root.left.left = TreeNode(7)
    root.left.right = TreeNode(-8)
    return root

def build_example_2():
    # Input: [989,null,10250,98693,-89388,null,null,null,-32127]
    root = TreeNode(989)
    root.right = TreeNode(10250)
    root.right.left = TreeNode(98693)
    root.right.right = TreeNode(-89388)
    root.right.right.right = TreeNode(-32127)
    return root

if __name__ == "__main__":
    solution = Solution()

    root1 = build_example_1()
    print("Example 1 Output:", solution.maxLevelSum(root1))  # Expected: 2

    root2 = build_example_2()
    print("Example 2 Output:", solution.maxLevelSum(root2))  # Expected: 2
