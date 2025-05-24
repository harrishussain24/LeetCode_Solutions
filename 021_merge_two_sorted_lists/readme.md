# LeetCode Problem 021: Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.


Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
 
Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.

## ✅ Solutions

A dummy node is created to simplify list merging.
current tracks the last node in the merged list.

While both lists have nodes:

Compare heads, attach the smaller to current.next.

Move the pointer in that list forward.

Advance current.

After the loop, attach any remaining nodes.

Return dummy.next as the merged list head.

Pros
O(n + m) time, linear merge.

Dummy node avoids edge case complexity.

In-place merging without extra nodes.

Notes
Must move current after each attach.

Attach remaining list at the end.

Input lists must be sorted.
