class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums) 
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0

        i = 0
        for j in range(len(nums)):
            if nums[j] !=0:
                result[i] = nums[j]
                i += 1
 
        return result
        
