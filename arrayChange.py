class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        nums_idx = {nums[i] : i for i in range(len(nums))}

        for i, j in operations:
            idx = nums_idx[i]
            nums[idx] = j
            nums_idx[j] = nums_idx.pop(i)

        return nums
