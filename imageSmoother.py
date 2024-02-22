class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        result = []
        rows = len(img)
        cols = len(img[0])
        for ri, row in enumerate(img):
            result.append([])
            for ci, col in enumerate(row):
                neigbor_sum, count = 0, 0
                #checking all the neignors of the current cell
                for diagnoal_idx in range(-1, 2):
                    for diagnoal_idy in range(-1, 2):
                        if 0 <= ri+diagnoal_idx < rows and 0 <= ci+diagnoal_idy < cols:
                            neigbor_sum += img[ri+diagnoal_idx][ci+diagnoal_idy]
                            count += 1
                result[-1].append(neigbor_sum // count)
        return result

