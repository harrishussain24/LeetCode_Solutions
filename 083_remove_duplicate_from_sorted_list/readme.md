# LeetCode Problem 083: Remove Duplicates from Sorted List

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]
 

Constraints:
The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.


## ✅ Solutions

The solution uses a single traversal of the list with a current pointer to check and remove duplicates in-place.


Edge Case Handling:

If the list is empty (head is None) or has only one node (head.next is None), return it as-is—there are no duplicates to remove.

Traversal and Deduplication:

Start with current = head.

Loop through the list using while current and current.next:

If current.val == current.next.val, it means a duplicate is found. Skip the duplicate node by setting:
current.next = current.next.next

Otherwise, move the current pointer one step forward:
current = current.next

Return the updated head of the deduplicated list.

🧠 Why This Works
The input list is sorted, so duplicates are always adjacent.

We only need to check each node’s value against the next one.

This allows for an in-place and efficient O(n) solution with O(1) space.


📈 Time and Space Complexity
Time Complexity: O(n), where n is the number of nodes in the list.

Space Complexity: O(1), as no extra space is used.