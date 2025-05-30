# LeetCode Problem 002: Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

## ✅ Solutions

Initialize a dummy node to simplify edge cases.

Use two pointers to traverse both linked lists simultaneously.

For each node, add corresponding digits plus carry from the previous addition.

Calculate the new digit (total % 10) and update carry (total // 10).

Append the new digit as a node to the result linked list.

Continue until both lists and carry are fully processed.


Complexity:
Time complexity: O(max(m, n)) where m and n are lengths of the input lists.

Space complexity: O(max(m, n)) for the output linked list.