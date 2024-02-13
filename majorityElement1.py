class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_element = len(nums) // 2
        c = Counter(nums)
        for num in nums:
            if c[num] > majority_element:
                return num
            

        
