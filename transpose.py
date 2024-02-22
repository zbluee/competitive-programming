class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        result = [[0] * rows for _ in range(cols)]

        for ri, row in enumerate(matrix):
            for ci, col in enumerate(row):
                result[ci][ri] = matrix[ri][ci]

        return result

        
