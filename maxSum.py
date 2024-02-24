class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        #there is one hourglass in 3x3 matice and the number of hourglasses in any nxm matices will be
        #(n-2) * (m-2)
        max_sum = 0
        for r in range(rows - 2):
            for c in range(cols - 2):
                hourglass_sum = sum(grid[r][c:c+3]) + grid[r+1][c+1]  + sum(grid[r+2][c:c+3])
                max_sum = max(max_sum, hourglass_sum)
                
        return max_sum
