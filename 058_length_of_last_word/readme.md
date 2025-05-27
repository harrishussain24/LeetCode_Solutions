# LeetCode Problem 058: Length of Last Word

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
 
Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 
Constraints:
1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.

## ✅ Solutions

Split the String:
Use split(" ") to separate words based on spaces. This can result in empty strings ("") if there are multiple consecutive spaces.

Remove Empty Strings:
Loop through the split list and remove all empty strings to isolate actual words.

Return Length of Last Word:
After filtering, the last word will be at the end of the list. Return the length of this word.


🧠 Key Concepts
String Splitting:
s.split(" ") splits by spaces but may leave empty elements.

In-place Removal:
Empty strings are removed using a while loop and pop(i) to clean the list.

Accessing Last Word:
trim[-1] fetches the last valid word in the list.


✅ Pros
Clear and intuitive logic.

Avoids counting or reversing.

Works reliably even with leading/trailing/multiple spaces.


⚠️ Notes
Uses extra space due to list creation (split()).

A more Pythonic solution would be s.split() (without " ") which automatically removes empty strings caused by multiple spaces.


📈 Time and Space Complexity
Time Complexity: O(n)
(Where n is the length of the string s)

Space Complexity: O(n)
(For the list of split words)