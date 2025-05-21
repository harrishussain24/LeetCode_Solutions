# LeetCode Problem 04: Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""

Explanation: There is no common prefix among the input strings. 

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.

## ✅ Solutions

The implemented solution iterates character by character across all strings in the list, comparing each position:

1. A reference character is taken from the first string.
2. For every index `j`, it checks whether all other strings have the same character at that index.
3. If a mismatch is found or any string is shorter than the current index, the loop breaks.
4. The result is returned as the common prefix built so far.

---

## 🧠 Time & Space Complexity

- **Time Complexity:** O(n * m)  
  Where `n` is the number of strings and `m` is the length of the shortest string.

- **Space Complexity:** O(1) (excluding output)

---

## ✅ Pros

- Simple and readable logic
- No use of built-in Python functions like `zip` or `all`, making it easy to follow
- Efficient for small to moderately sized inputs

⚠️ Note
This solution assumes the input list strs is non-empty and all strings are non-null. Make sure to handle edge cases as needed in production use.
