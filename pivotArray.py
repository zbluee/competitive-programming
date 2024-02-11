class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_than_pivot = []
        greater_than_pivot = []
        pivot_nums = []

        for num in nums:
            if num < pivot:
                less_than_pivot.append(num)
            elif num == pivot:
                pivot_nums.append(pivot)
            else:
                greater_than_pivot.append(num)

        return less_than_pivot + pivot_nums + greater_than_pivot

        
        
