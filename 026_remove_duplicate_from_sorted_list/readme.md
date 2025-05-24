# LeetCode Problem 026: Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:
1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.

## ✅ Solutions

Maintain two lists:

unique to collect unique elements.

duplicates to collect the rest.

Start from the second element and compare it with the previous one.

If different → it's unique → add to unique.

If same → it's a duplicate → add to duplicates.


After the loop:

Special handling for edge cases:

If array has one element → return 1.

Otherwise, compare last two elements and decide where to place the last item.


Finally:

Combine unique + duplicates into the original nums.

Return the number of unique elements as index.


✅ Pros
Easy to understand and debug.

Separates unique and duplicate logic clearly.

Works correctly for edge cases like single-element arrays.


⚠️ Notes
Uses extra space (O(n)) due to unique and duplicates lists.

For interviews or optimized solutions, prefer the in-place two-pointer approach.