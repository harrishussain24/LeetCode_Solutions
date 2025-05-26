# LeetCode Problem 035: Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
 
Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104

## ✅ Solutions

Use two pointers, left and right, to track the search range in the sorted list.

While left is less than or equal to right:

Calculate mid as the midpoint of the current range.

Compare nums[mid] with target:

✅ If equal, return mid immediately.

❌ If nums[mid] is less than target, move left to mid + 1.

❌ If nums[mid] is greater than target, move right to mid - 1.

If the target is not found, return the left pointer as the insertion index.


📝 Key Points

Binary Search: Efficiently narrows down the search space by half each iteration.

Midpoint Calculation: mid = (left + right) // 2 finds the middle index.

Insert Position: When target is not found, left indicates where it should be inserted.


✅ Pros

Runs in O(log n) time, ideal for large sorted arrays.

No extra space used; operates in-place.

Clear and straightforward implementation of binary search.


⚠️ Notes

The break after return is unnecessary since return already exits the function.

This algorithm assumes the input array is sorted and contains distinct integers.