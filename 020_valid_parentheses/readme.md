# LeetCode Problem 020: Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

## ✅ Solutions

A dictionary is used to map opening brackets to their corresponding closing brackets.
A stack (checker) keeps track of unmatched opening brackets.
The string is scanned character by character:
If an opening bracket is found, it's pushed to the stack.
If a closing bracket is found:
If the stack is empty → invalid (closing without opening).
Otherwise, pop from the stack and compare using the dictionary.

After scanning:

If the stack is empty → valid.
If any unmatched brackets remain → invalid.

✅ Pros

Efficient O(n) time complexity.
Clear use of stack to model bracket pairing.
Easy to follow and debug with print statements.

⚠️ Notes

The final variable tracks whether the last bracket pair matched correctly, but is not necessary for correctness—only the stack state at the end matters.

You could simplify logic by returning False immediately on a mismatch and checking only if the stack is empty at the end.
