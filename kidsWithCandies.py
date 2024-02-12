class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_ = max(candies)
        result = [False for _ in candies]
        for i in range(len(candies)):
            if candies[i] + extraCandies < max_:
                continue
            result[i] = True

        return result

        
