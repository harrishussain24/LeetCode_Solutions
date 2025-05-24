# LeetCode Problem 009: Palindrome Number

Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:
-231 <= x <= 231 - 1
 
Follow up: Could you solve it without converting the integer to a string?

## ✅ Solutions

### 🔹 1. With String Conversion (`solution.py`)
This solution converts the integer to a string and checks if the reversed string matches the original. It's a simple and easy-to-understand approach that works well for most cases but does not meet the follow-up requirement of avoiding string conversion.

### 🔹 2. Without String Conversion (`solution_2.py`)
This optimized solution avoids string operations by reversing only half of the integer and comparing it to the other half. It is more efficient and satisfies the follow-up constraint of solving the problem without converting the number to a string.
