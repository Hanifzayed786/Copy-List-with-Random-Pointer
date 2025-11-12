from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        old_to_new_map = {}

        current = head
        while current:
            old_to_new_map[current] = Node(current.val)
            current = current.next

        current = head
        while current:
            new_node = old_to_new_map[current]
            new_node.next = old_to_new_map.get(current.next)
            new_node.random = old_to_new_map.get(current.random)
            current = current.next

        return old_to_new_map[head]

def build_list(nodes_data: list) -> Optional[Node]:
    if not nodes_data:
        return None

    nodes = [Node(val) for val, _ in nodes_data]

    for i in range(len(nodes)):
        if i < len(nodes) - 1:
            nodes[i].next = nodes[i + 1]
        
        random_index = nodes_data[i][1]
        if random_index is not None:
            nodes[i].random = nodes[random_index]
            
    return nodes[0]

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

if __name__ == "__main__":
    
    test_case = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]

    original_head = build_list(test_case)
    
    print("--- Original List ---")
    print_list(original_head)
    
    sol = Solution()
    copied_head = sol.copyRandomList(original_head)
    
    print("\n--- Copied List ---")
    print_list(copied_head)
    
    print("\n--- Verification (Memory IDs) ---")
    print(f"Original Head ID: {id(original_head)}")
    print(f"Copied Head ID:   {id(copied_head)}")
    if original_head:
        print(f"Original Head.Next ID: {id(original_head.next)}")
        print(f"Copied Head.Next ID:   {id(copied_head.next)}")
