class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        result = [0] * n

        for i in range(n):
            opration = 0
            for j in range(n):
                if i == j:
                    continue
                if boxes[j] == '1':
                    opration += abs(j - i)

            result[i] = opration
        return result
                
