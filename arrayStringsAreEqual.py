class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        str1 = "".join(word1)
        str2 = "".join(word2)

        left1, left2 = 0, 0
        while left1 < len(str1) and left2 < len(str2):
            if str1[left1] != str2[left2]:
                return False

            left1 += 1
            left2 += 1
        
        return True if left1 == len(str1) and left2 == len(str2) else False
        
