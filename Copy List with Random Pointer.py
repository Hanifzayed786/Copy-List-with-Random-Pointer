"""
Problem: Copy List with Random Pointer
-------------------------------------

A linked list is given where each node contains:
  - a value (val)
  - a pointer to the next node (next)
  - a random pointer (random) that can point to any node in the list or None.

Goal:
Create a deep copy of this list — meaning all new nodes, with both
next and random pointers correctly assigned.

Constraints:
- 0 <= n <= 1000
- -10^4 <= Node.val <= 10^4
- Node.random is None or points to some node in the list.

Approach:
1. For each node, create a copy of it and insert it right next to the original node.
2. Assign random pointers for the newly created nodes.
3. Separate the original and copied nodes into two different lists.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


def copyRandomList(head):
    if not head:
        return None

    # Step 1: Create new nodes and insert them after each original node
    current = head
    while current:
        copy_node = Node(current.val)
        copy_node.next = current.next
        current.next = copy_node
        current = copy_node.next

    # Step 2: Assign random pointers for the copied nodes
    current = head
    while current:
        if current.random:
            current.next.random = current.random.next
        current = current.next.next

    # Step 3: Separate the original list and the copied list
    original = head
    copy_head = head.next
    copy_current = copy_head

    while original:
        original.next = original.next.next
        if copy_current.next:
            copy_current.next = copy_current.next.next
        original = original.next
        copy_current = copy_current.next

    return copy_head