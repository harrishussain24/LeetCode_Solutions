class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = [nums[0]]
        duplicates = []
        index = 1
        iterator = 1

        while iterator < len(nums) - 1:
            if nums[iterator] != nums[iterator - 1]:
                unique.append(nums[iterator])
                index += 1
            else:
                duplicates.append(nums[iterator])
            
            iterator += 1
        
        if len(nums) == 1:
            return 1
        elif nums[-1] != nums[-2]:
            unique.append(nums[-1])
            index += 1
        else:
            duplicates.append(nums[-1])
        
        expectedNums = unique + duplicates

        for i in range(len(expectedNums)):
            nums[i] = expectedNums[i]
        
        return index