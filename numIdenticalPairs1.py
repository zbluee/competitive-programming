class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        count_good_pairs = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i < j and nums[i] == nums[j]:
                    count_good_pairs += 1

        return count_good_pairs
                    
        
