class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split(" ")
        result = []
        for i in range(len(words) - 1, -1, -1):
            if words[i] == '':
                continue
            result.append(words[i].strip())

        return " ".join(result)
        
