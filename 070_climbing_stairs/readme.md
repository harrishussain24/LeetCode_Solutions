# LeetCode Problem 070: Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:
1 <= n <= 45

## ✅ Solutions

This is a classic dynamic programming problem that follows the Fibonacci pattern:

Logic:
To reach step n, you could have come from:

Step n-1 (by taking 1 step)

Step n-2 (by taking 2 steps)

So, ways(n) = ways(n-1) + ways(n-2)


⏱ Time & Space Complexity
Time Complexity: O(n)

Space Complexity: O(1)
→ Uses only constant space for variables a, b, and c.