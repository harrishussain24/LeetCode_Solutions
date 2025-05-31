# LeetCode Problem 003: Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without duplicate characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

## ✅ Solutions

Solution 1: Using List and String Operations
Maintain a list lists to store characters of the current substring without duplicates.

Iterate through the string:

If the current character is already in lists, append the current substring to pos (a list of substrings), then remove all characters up to and including the first occurrence of this duplicate character.

Append the current character to lists.

After the loop, append the last substring in lists to pos.

Find the maximum length among all substrings stored in pos.


Key Points
Uses a list to keep track of the current substring.

Removes duplicates by slicing the list after the first occurrence of the duplicate.

Converts the list to string and stores all substrings to find the max length later.

Time Complexity
Worst case: O(n²) due to list slicing and searching (lists.index()) inside the loop.

Not optimal for very long strings.



Solution 2: Sliding Window with Set (Optimized)

Use two pointers left and right to define a sliding window.

Use a set char_set to store unique characters in the current window.

Expand the window by moving right pointer:

If s[right] is already in char_set, move the left pointer forward while removing characters from the set until the duplicate character is removed.

Add s[right] to char_set.

Keep track of the maximum window size (max_len) during this process.

Key Points
Efficient sliding window technique with O(n) time complexity.

Set operations (add/remove) are O(1) average.

No substring copying or extra storage needed.

Time Complexity
O(n), where n is the length of the string.

Each character is visited at most twice (once by right and once by left pointer).

