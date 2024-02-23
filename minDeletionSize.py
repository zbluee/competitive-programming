class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
    
        for col in zip(*strs):
            for i in range(len(col) - 1):
                if col[i] > col[i+1]:
                    count += 1
                    break

        return count
