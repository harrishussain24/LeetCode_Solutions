# LeetCode Problem 069: Sqrt(x)

Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned. 

Constraints:
0 <= x <= 231 - 1

## ✅ Solutions

This solution uses Binary Search to efficiently find the square root of x.

We initialize low = 1 and high = x // 2 (since no number greater than x // 2 can be its square root for x > 1).

We search for the square root by checking if mid * mid == x.

If mid * mid < x, we move right to search larger values and update the answer.

If mid * mid > x, we move left.

We return the last valid mid where mid * mid <= x.

🧮 Time Complexity
O(log x) — due to binary search.

📦 Space Complexity
O(1) — no extra space used.