class Solution:
    def freqAlphabets(self, s: str) -> str:
        result = ""
        right = len(s) - 1
        
        while right > -1:
            if s[right]  == '#':
                num = s[right - 2] + s[right - 1] 
                result = chr(int(num) + 96) + result

                right -= 2
            else:
                result = chr(int(s[right]) + 96) + result

            right -= 1

        return result
