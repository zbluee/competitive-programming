class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_len, word2_len = len(word1), len(word2)
        short_word = word1_len if word1_len < word2_len else word2_len
        
        left = 0
        result = ""
        
        while left < short_word:
            result += word1[left] + word2[left]
            left += 1
            
        return result + word2[left:] if short_word == word1_len else result + word1[left:]
