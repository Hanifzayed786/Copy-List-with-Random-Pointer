Copy Random List (Deep Copy of a Linked List)
 Description

This program creates a deep copy of a special linked list where each node has:

A next pointer (points to the next node)

A random pointer (points to any node in the list, or None)

It ensures that the copied list is completely independent of the original one — no shared nodes in memory.

 Key Idea

Use a dictionary to map original nodes → cloned nodes

First, clone all nodes.

Then, link their next and random pointers using the mapping.

🧪 Example Usage
# Each element: [value, random_pointer_index]
test_case = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]

original_head = build_list(test_case)
copied_head = Solution().copyRandomList(original_head)

Output Example
--- Original List ---
  Node 0 (Val: 7)
    -> Next: 13
    -> Random: None
  ...
--- Copied List ---
  Node 0 (Val: 7)
    -> Next: 13
    -> Random: None

 Description

This program solves the classic N-Queens problem — placing n queens on an n x n chessboard so that no two queens attack each other.

Approach

Uses backtracking to:

Place one queen per row.

Check safety before placing.

Explore all valid configurations recursively.

Example Usage

Run the script and enter a number:

Enter the number of queens: 4

📤 Output Example
[['.Q..', '...Q', 'Q...', '..Q.'],
 ['..Q.', 'Q...', '...Q', '.Q..']]
