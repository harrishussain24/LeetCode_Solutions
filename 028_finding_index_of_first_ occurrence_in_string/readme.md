# LeetCode Problem 028: Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:
1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.

## ✅ Solutions

Use a while loop with a moving index inc.

At each step, extract a substring from haystack of the same length as needle.

Compare the substring with needle:

✅ If matched, return the current index.

❌ If not, increment the index and check the next slice.

If the remaining characters are fewer than the length of needle, terminate early and return -1.

📝 Key Points
String Slicing: haystack[inc: inc + len(needle)] grabs the current segment.

Bounds Check: (inc + len(needle)) > len(haystack) avoids index overflow.

Early Exit: Returns immediately when a match is found.

Not Found: If no match is found by the end, returns -1.


✅ Pros
Clear and readable logic.

Avoids unnecessary comparisons once the remaining string is too short.

Efficient for small to medium strings.


⚠️ Notes
The found flag is not necessary, since a match already returns early. You can simplify by removing it.

For very large strings or performance-critical applications, consider built-in methods like str.find() or use algorithms like KMP for better performance.