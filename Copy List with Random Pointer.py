from typing import Optional

# Definition for a Node in the linked list
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # If the list is empty, simply return None
        if not head:
            return None

        # Dictionary to map original nodes to their cloned nodes
        old_to_new_map = {}

        # ----- Step 1: Create all new nodes (without linking) -----
        current = head
        while current:
            # Create a new node with the same value as the original
            old_to_new_map[current] = Node(current.val)
            current = current.next

        # ----- Step 2: Link next and random pointers for new nodes -----
        current = head
        while current:
            new_node = old_to_new_map[current]
            # Connect 'next' pointer (if exists)
            new_node.next = old_to_new_map.get(current.next)
            # Connect 'random' pointer (if exists)
            new_node.random = old_to_new_map.get(current.random)
            current = current.next

        # Return the deep-copied list's head
        return old_to_new_map[head]


# Helper function to build the list for testing
def build_list(nodes_data: list) -> Optional[Node]:
    """
    nodes_data: list of [value, random_index]
    Example: [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    """
    if not nodes_data:
        return None

    # Create node objects for each element
    nodes = [Node(val) for val, _ in nodes_data]

    # Link 'next' and 'random' pointers
    for i in range(len(nodes)):
        if i < len(nodes) - 1:
            nodes[i].next = nodes[i + 1]
        random_index = nodes_data[i][1]
        if random_index is not None:
            nodes[i].random = nodes[random_index]

    return nodes[0]


# Helper function to print the linked list for visual verification
def print_list(head: Optional[Node]):
    if not head:
        print("List is empty.")
        return

    current = head
    node_count = 0
    while current:
        next_val = current.next.val if current.next else "None"
        random_val = current.random.val if current.random else "None"

        print(f"  Node {node_count} (Val: {current.val})")
        print(f"    -> Next:   {next_val}")
        print(f"    -> Random: {random_val}")

        current = current.next
        node_count += 1


# Run a sample test
if __name__ == "__main__":
    # Example test case: each element is [node_value, random_pointer_index]
    test_case = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]

    # Build the original list
    original_head = build_list(test_case)

    print("--- Original List ---")
    print_list(original_head)

    # Perform the deep copy
    sol = Solution()
    copied_head = sol.copyRandomList(original_head)

    print("\n--- Copied List ---")
    print_list(copied_head)

    # Check memory IDs to confirm deep copy (not referencing the same nodes)
    print("\n--- Verification (Memory IDs) ---")
    print(f"Original Head ID: {id(original_head)}")
    print(f"Copied Head ID:   {id(copied_head)}")
    if original_head:
        print(f"Original Head.Next ID: {id(original_head.next)}")
        print(f"Copied Head.Next ID:   {id(copied_head.next)}")
