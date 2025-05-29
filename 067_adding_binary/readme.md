# LeetCode Problem 067: Adding Binary

Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
 
Constraints:
1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.

## ✅ Solutions

Pad shorter string: Add leading zeros so both have equal length.

Initialize: carry = 0, output = "".

Iterate from right to left:

Sum bits from a, b, and carry.

Current bit = total % 2.

Update carry = total // 2.

Prepend bit to output.

If carry remains, prepend it.

Return the final output.

Key Points
% 2 gets the current bit.

// 2 gets the carry for the next position.

Builds the result string from least significant bit to most.


Pros
Simple, clear logic simulating manual binary addition.

Handles inputs of different lengths efficiently (O(n)).