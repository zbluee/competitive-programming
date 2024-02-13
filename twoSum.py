class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_value_pair = {}
        for idx, num in enumerate(nums):
            if target - num in index_value_pair:
                return idx, index_value_pair[target - num]
            
            index_value_pair[num] = idx
        
        
        
