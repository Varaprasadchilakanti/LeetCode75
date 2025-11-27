"""
437. Path Sum III

Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.
The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).


Example 1:

Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.

Example 2:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3


Constraints:

The number of nodes in the tree is in the range [0, 1000].
-109 <= Node.val <= 109
-1000 <= targetSum <= 1000

Topics
Tree
Depth-First Search
Binary Tree



Developer Insights

Core Responsibility: Count valid paths with sum equal to targetSum.
Design Choice: Use DFS traversal with a prefix-sum hashmap to track cumulative sums efficiently.

Efficiency:
Naïve approach: 𝑂(𝑛^2) (exploring all paths).
Optimized prefix-sum approach: 𝑂(𝑛) average time, 𝑂(ℎ) space (recursion depth).
Extensibility: Strategy pattern allows swapping between brute-force DFS and optimized prefix-sum.
Testability: Modular design ensures independent testing of traversal and counting logic.
Resilience: Handles edge cases (empty tree, negative values, large target sums).


Pseudocode

function dfs(node, current_sum, prefix_map):
    if node is null:
        return 0
    
    current_sum += node.val
    count = prefix_map[current_sum - targetSum] if exists
    
    update prefix_map[current_sum] += 1
    
    count += dfs(node.left, current_sum, prefix_map)
    count += dfs(node.right, current_sum, prefix_map)
    
    revert prefix_map[current_sum] -= 1
    
    return count

function pathSum(root, targetSum):
    prefix_map = {0: 1}
    return dfs(root, 0, prefix_map)

"""

from typing import Optional, Dict, Protocol

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        """
        Compact string representation of the tree rooted at this node.
        Example: 10(5(3(3,-2),2(None,1)),-3(None,11))
        """
        left_str = str(self.left) if self.left else "None"
        right_str = str(self.right) if self.right else "None"
        return f"{self.val}({left_str},{right_str})"

    def __repr__(self) -> str:
        return f"TreeNode(val={self.val})"


class StrategyInterface(Protocol):
    def solve(self, root: Optional[TreeNode], targetSum: int) -> int: ...


class PathSumStrategy:
    """
    Optimized strategy using DFS + prefix sums to count valid paths.
    """
    def solve(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_map = {0: 1}
        return self._dfs(root, 0, targetSum, prefix_map)

    def _dfs(self, node: Optional[TreeNode], current_sum: int, targetSum: int, prefix_map: Dict[int, int]) -> int:
        if not node:
            return 0

        current_sum += node.val
        count = prefix_map.get(current_sum - targetSum, 0)

        prefix_map[current_sum] = prefix_map.get(current_sum, 0) + 1

        count += self._dfs(node.left, current_sum, targetSum, prefix_map)
        count += self._dfs(node.right, current_sum, targetSum, prefix_map)

        prefix_map[current_sum] -= 1  # backtrack

        return count


class Solution:
    """
    Entry point class delegating to a strategy.
    """
    def __init__(self, strategy: StrategyInterface = PathSumStrategy()) -> None:
        self.strategy = strategy

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        Counts the number of downward paths in the binary tree
        whose sum equals targetSum.
        """
        return self.strategy.solve(root, targetSum)


# Usage Example

if __name__ == "__main__":
    # Example 1: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
    root = TreeNode(10,
        left=TreeNode(5,
            left=TreeNode(3,
                left=TreeNode(3),
                right=TreeNode(-2)
            ),
            right=TreeNode(2,
                right=TreeNode(1)
            )
        ),
        right=TreeNode(-3,
            right=TreeNode(11)
        )
    )

    solution = Solution()
    print("Tree:", root)
    print("Path Sum Count (target=8):", solution.pathSum(root, 8))  # Output: 3

    # Example 2: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
    root2 = TreeNode(5,
        left=TreeNode(4,
            left=TreeNode(11,
                left=TreeNode(7),
                right=TreeNode(2)
            )
        ),
        right=TreeNode(8,
            left=TreeNode(13),
            right=TreeNode(4,
                left=TreeNode(5),
                right=TreeNode(1)
            )
        )
    )
    print("Tree:", root2)
    print("Path Sum Count (target=22):", solution.pathSum(root2, 22))  # Output: 3
