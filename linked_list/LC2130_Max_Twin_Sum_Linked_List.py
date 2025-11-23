"""
2130. Maximum Twin Sum of a Linked List

In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.


Example 1:

Input: head = [5,4,2,1]
Output: 6
Explanation:
Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
There are no other nodes with twins in the linked list.
Thus, the maximum twin sum of the linked list is 6. 


Example 2:

Input: head = [4,2,2,3]
Output: 7
Explanation:
The nodes with twins present in this linked list are:
- Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
- Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
Thus, the maximum twin sum of the linked list is max(7, 4) = 7. 
Example 3:


Input: head = [1,100000]
Output: 100001
Explanation:
There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.
 

Constraints:

The number of nodes in the list is an even integer in the range [2, 105].
1 <= Node.val <= 105

Topics
Linked List
Two Pointers
Stack

Hint 1
How can "reversing" a part of the linked list help find the answer?
Hint 2
We know that the nodes of the first half are twins of nodes in the second half, so try dividing the linked list in half and reverse the second half.
Hint 3
How can two pointers be used to find every twin sum optimally?
Hint 4
Use two different pointers pointing to the first nodes of the two halves of the linked list. The second pointer will point to the first node of the reversed half, which is the (n-1-i)th node in the original linked list. By moving both pointers forward at the same time, we find all twin sums.


Developer Insights
Problem: For a linked list of even length, compute the maximum twin sum.
Twin definition: Node i pairs with node (n-1-i).

Approach:
Use slow/fast pointers to find the midpoint.
Reverse the second half of the list.
Traverse both halves simultaneously, computing twin sums.
Track the maximum twin sum.

Complexity:
Time: O(n) — single traversal + reversal.
Space: O(1) — in-place reversal.

Architecture:
Define a TwinSumStrategy protocol.
Implement ReverseHalfTwinSumStrategy (optimal approach).
Solution delegates to chosen strategy.


Pseudocode

function pairSum(head):
    # Step 1: find midpoint
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: reverse second half
    prev, curr = None, slow
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    # Step 3: compute twin sums
    max_sum = 0
    first, second = head, prev
    while second:
        max_sum = max(max_sum, first.val + second.val)
        first = first.next
        second = second.next

    return max_sum

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
        return "[" + " -> ".join(values) + "]"


class TwinSumStrategy(Protocol):
    """Defines contract for strategies that compute maximum twin sum."""
    def compute(self, head: Optional[ListNode]) -> int: ...


class ReverseHalfTwinSumStrategy:
    """
    Strategy: Reverse second half of list, then compute twin sums.

    Steps:
        1. Find midpoint using slow/fast pointers.
        2. Reverse second half in-place.
        3. Traverse both halves simultaneously to compute twin sums.
    Complexity:
        Time: O(n), Space: O(1).
    """
    def compute(self, head: Optional[ListNode]) -> int:
        if not head:
            return 0

        # Step 1: find midpoint
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: reverse second half
        prev, curr = None, slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Step 3: compute twin sums
        max_sum = 0
        first, second = head, prev
        while second:
            max_sum = max(max_sum, first.val + second.val)
            first = first.next
            second = second.next

        return max_sum


class Solution:
    """
    High-level orchestrator for maximum twin sum computation.

    Depends on abstraction (TwinSumStrategy).
    Default strategy: ReverseHalfTwinSumStrategy.
    """
    def __init__(self, strategy: TwinSumStrategy = ReverseHalfTwinSumStrategy()) -> None:
        self.strategy = strategy

    def pairSum(self, head: Optional[ListNode]) -> int:
        """
        Compute maximum twin sum of a linked list.

        Args:
            head (ListNode | None): Head of the linked list.

        Returns:
            int: Maximum twin sum.
        """
        return self.strategy.compute(head)


# Usage Examples

# Example 1: [5,4,2,1] → max twin sum = 6
head1 = ListNode(5, ListNode(4, ListNode(2, ListNode(1))))
solver = Solution()
print(solver.pairSum(head1))  # 6

# Example 2: [4,2,2,3] → max twin sum = 7
head2 = ListNode(4, ListNode(2, ListNode(2, ListNode(3))))
print(solver.pairSum(head2))  # 7

# Example 3: [1,100000] → max twin sum = 100001
head3 = ListNode(1, ListNode(100000))
print(solver.pairSum(head3))  # 100001


