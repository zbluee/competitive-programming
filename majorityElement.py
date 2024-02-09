class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = len(nums)//3
        nums_idx_pair = Counter(nums)

        result = set()
        for num in nums:
            if nums_idx_pair[num] > freq:
                result.add(num)

        return list(result)

        
