class Solution:
    def transpose(self, strs: List[str], rows : int, cols : int) -> List[str]:
        result = [[None] * rows for _ in range(cols)]

        for ri in range(rows):
            for ci in range(cols):
                result[ci][ri] = strs[ri][ci]

        return result

    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        rows = len(strs)
        cols = len(strs[0])

        transposed = self.transpose(strs, rows, cols)

        for ri in range(cols):
            for ci in range(rows - 1):
                if transposed[ri][ci] > transposed[ri][ci+1]:
                    count += 1
                    break

        return count
