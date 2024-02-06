class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive = 0
        count = 0
        for num in nums:
            if num == 0:
                max_consecutive = max(max_consecutive, count)
                count = 0
                continue
            count += 1

        return max(max_consecutive, count)
        
