class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        size = len(nums)
        result = [0] * size
        pos_nums, neg_nums = [], []
        for num in nums:
            if num < 0:
                neg_nums.append(num)
                continue
            pos_nums.append(num)

        left1, left2 = 0, 0
        while left1 < size:
            result[left1] = pos_nums[left2]
            left1 += 1
            result[left1] = neg_nums[left2]
            left1 += 1
            left2 += 1

        return result
        
