"""
328. Odd Even Linked List

Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
The first node is considered odd, and the second node is even, and so on.
Note that the relative order inside both the even and odd groups should remain as it was in the input.
You must solve the problem in O(1) extra space complexity and O(n) time complexity.


Example 1:

Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:

Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]


Constraints:

The number of nodes in the linked list is in the range [0, 104].
-106 <= Node.val <= 106

Topics
Linked List


Developer Insights
Problem: Rearrange a singly linked list so that all nodes at odd indices appear first, followed by nodes at even indices.

Constraints:
Must run in O(n) time.
Must use O(1) extra space (in-place reordering).

Approach:
Use two pointers (odd, even) and maintain a reference to even_head.
Traverse the list, relinking odd and even nodes in-place.
Finally, connect the odd list to the head of the even list.

Edge Cases:
Empty list → return None.
Single node → return as-is.
Two nodes → already ordered.


Pseudocode

function oddEvenList(head):
    if head is None or head.next is None:
        return head

    odd = head
    even = head.next
    even_head = even

    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next

    odd.next = even_head
    return head

"""


from typing import Optional, Protocol

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        """Return linked list values as a string for easy printing."""
        values = []
        curr = self
        while curr:
            values.append(str(curr.val))
            curr = curr.next
        return "[" + ", ".join(values) + "]"

class OddEvenStrategy(Protocol):
    """Defines contract for strategies that reorder linked lists by odd/even indices."""
    def reorder(self, head: Optional[ListNode]) -> Optional[ListNode]: ...


class InPlaceOddEvenStrategy:
    """
    Strategy: In-place odd-even reordering of a linked list.

    - Maintains two pointers: odd and even.
    - Preserves relative order within odd and even groups.
    - Connects odd list to even list at the end.
    """
    def reorder(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd, even = head, head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head
        return head


class Solution:
    """
    High-level orchestrator for odd-even linked list reordering.

    Depends on abstraction (OddEvenStrategy) rather than concrete implementation.
    Default strategy is InPlaceOddEvenStrategy, but can inject alternatives.
    """
    def __init__(self, strategy: OddEvenStrategy = InPlaceOddEvenStrategy()) -> None:
        self.strategy = strategy

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Rearranges nodes so that odd-indexed nodes appear first,
        followed by even-indexed nodes.

        Args:
            head (ListNode | None): Head of the linked list.

        Returns:
            ListNode | None: Modified list with odd-even reordering applied.
        """
        return self.strategy.reorder(head)


# Usage Examples

# Example 1: [1,2,3,4,5] → [1,3,5,2,4]
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
solver = Solution()
new_head = solver.oddEvenList(head)
print(new_head)

# Example 2: [2,1,3,5,6,4,7] → [2,3,6,7,1,5,4]
head2 = ListNode(2, ListNode(1, ListNode(3, ListNode(5, ListNode(6, ListNode(4, ListNode(7)))))))
new_head2 = solver.oddEvenList(head2)
print(new_head2)

# Example 3: Single node [10] → [10]
head3 = ListNode(10)
new_head3 = solver.oddEvenList(head3)
print(new_head3)

# Example 4: Empty list → None
new_head4 = solver.oddEvenList(None)
print(new_head4)
