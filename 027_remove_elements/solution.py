class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        removed = []
        output = 0
        i = 0
        while i < len(nums):
            if nums[i] != val:
                output += 1
                i += 1
            else:
                removed.append(nums[i])
                nums.pop(i)

        nums = nums + removed
        return output