class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        result = []
        for word in words:
            col1, col2, col3 = 0, 0, 0
            
            for s in set(word):
                if s.lower() in "qwertyuiop":
                    col1 += 1

                elif s.lower() in "asdfghjkl":
                    col2 += 1
                
                elif s.lower() in "zxcvbnm":
                    col3 += 1

            if (col1 == len(set(word))) or (col2 == len(set(word))) or (col3 == len(set(word))):
                result.append(word)
        
        return result
                
