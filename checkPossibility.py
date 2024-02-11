class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        modify = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                modify += 1
                if i < 1 or nums[i-1] <= nums[i+1]:
                    nums[i] = nums[i+1]
                else:
                    nums[i+1] = nums[i]

        return modify <= 1
