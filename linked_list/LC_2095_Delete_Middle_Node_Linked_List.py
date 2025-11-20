"""
2095. Delete the Middle Node of a Linked List

You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.
The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.
For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.


Example 1:

Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation:
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node. 

Example 2:

Input: head = [1,2,3,4]
Output: [1,2,4]
Explanation:
The above figure represents the given linked list.
For n = 4, node 2 with value 3 is the middle node, which is marked in red.
Example 3:


Input: head = [2,1]
Output: [2]
Explanation:
The above figure represents the given linked list.
For n = 2, node 1 with value 1 is the middle node, which is marked in red.
Node 0 with value 2 is the only node remaining after removing node 1.


Constraints:

The number of nodes in the list is in the range [1, 105].
1 <= Node.val <= 105

Topics
Linked List
Two Pointers

Hint 1
If a point with a speed s moves n units in a given time, a point with speed 2 * s will move 2 * n units at the same time. Can you use this to find the middle node of a linked list?
Hint 2
If you are given the middle node, the node before it, and the node after it, how can you modify the linked list?


Developer Insights
Responsibility: Delete the middle node of a singly linked list.
Middle definition: Index ⌊n/2⌋ (0‑based).
Constraints: Up to 10^5 nodes → O(n) solution required.

Approach:
If list has only one node → return None.
Use slow/fast pointer technique:
fast moves 2 steps, slow moves 1 step.
When fast reaches end, slow is at middle.
Maintain prev (node before slow) to unlink the middle.

Complexity:
Time: O(n) — single traversal.
Space: O(1) — constant extra memory.


Pseudocode

function deleteMiddle(head):
    if head.next is None:
        return None

    slow, fast = head, head
    prev = None

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    prev.next = slow.next
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


class DeleteMiddleStrategy(Protocol):
    """Defines contract for strategies that delete the middle node of a linked list."""
    def delete(self, head: Optional[ListNode]) -> Optional[ListNode]: ...


class TwoPointerDeleteStrategy:
    """
    Strategy: Use slow/fast pointers to locate and delete the middle node.

    - slow advances one step, fast advances two steps.
    - when fast reaches end, slow is at middle.
    - prev tracks node before slow to unlink middle.
    """
    def delete(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        slow, fast = head, head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # unlink the middle node
        prev.next = slow.next
        return head


class Solution:
    """
    High-level orchestrator for deleting the middle node.

    Depends on abstraction (DeleteMiddleStrategy) rather than concrete implementation.
    Default strategy is TwoPointerDeleteStrategy, but can inject alternatives.
    """
    def __init__(self, strategy: DeleteMiddleStrategy = TwoPointerDeleteStrategy()) -> None:
        self.strategy = strategy

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Delete the middle node of a linked list.

        Args:
            head (ListNode | None): Head of the linked list.

        Returns:
            ListNode | None: Modified list with middle node removed.
        """
        return self.strategy.delete(head)


# Usage Example

# Build linked list: [1,3,4,7,1,2,6]
head = ListNode(1, ListNode(3, ListNode(4, ListNode(7, ListNode(1, ListNode(2, ListNode(6)))))))
solver = Solution()
new_head = solver.deleteMiddle(head)
# Result: [1,3,4,1,2,6]
print(new_head)
