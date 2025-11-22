"""
206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.


Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]


Example 2:

Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []


Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?


Topics
Linked List
Recursion


Developer Insights
Problem: Reverse a singly linked list and return the new head.

Constraints:
Up to 5000 nodes.
Values between -5000 and 5000.

Approach:
Provide two strategies: Iterative and Recursive.
Iterative: Traverse once, rewire pointers in O(n).
Recursive: Use call stack to reverse links, elegant but O(n) space due to recursion depth.

Architecture:
Define a ReverseStrategy protocol.
Implement IterativeReverseStrategy and RecursiveReverseStrategy.
Solution delegates to chosen strategy.

Complexity:
Iterative: O(n) time, O(1) space.
Recursive: O(n) time, O(n) space.


Pseudocode

function reverseList(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

Recursive:

function reverseRecursive(head):
    if head is None or head.next is None:
        return head
    new_head = reverseRecursive(head.next)
    head.next.next = head
    head.next = None
    return new_head

"""

from typing import Optional, Protocol

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        """Readable string representation of the linked list."""
        values, curr = [], self
        while curr:
            values.append(str(curr.val))
            curr = curr.next
        return "[" + ",".join(values) + "]"


class ReverseStrategy(Protocol):
    """Defines contract for linked list reversal strategies."""
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]: ...


class IterativeReverseStrategy:
    """
    Iterative reversal strategy.

    Traverses the list once, rewiring pointers in-place.
    Time: O(n), Space: O(1).
    """
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev


class RecursiveReverseStrategy:
    """
    Recursive reversal strategy.

    Uses call stack to reverse links.
    Time: O(n), Space: O(n) due to recursion depth.
    """
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        new_head = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return new_head


class Solution:
    """
    High-level orchestrator for linked list reversal.

    Depends on abstraction (ReverseStrategy).
    Default strategy: IterativeReverseStrategy.
    """
    def __init__(self, strategy: ReverseStrategy = IterativeReverseStrategy()) -> None:
        self.strategy = strategy

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverse a singly linked list.

        Args:
            head (ListNode | None): Head of the linked list.

        Returns:
            ListNode | None: New head of the reversed list.
        """
        return self.strategy.reverse(head)


# Usage Examples

# Example 1: [1,2,3,4,5] → [5,4,3,2,1]
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
solver = Solution()
print(solver.reverseList(head))  # [5,4,3,2,1]

# Example 2: [1,2] → [2,1]
head2 = ListNode(1, ListNode(2))
print(solver.reverseList(head2))  # [2,1]

# Example 3: [] → []
print(solver.reverseList(None))  # None

# Example 4: Recursive strategy
solver_recursive = Solution(strategy=RecursiveReverseStrategy())
head3 = ListNode(10, ListNode(20, ListNode(30)))
print(solver_recursive.reverseList(head3))  # [30,20,10]
