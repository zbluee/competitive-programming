class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        letter_in_s = defaultdict(int)

        for letter in s:
            letter_in_s[letter] += 1

        for letter in t:
            if letter_in_s[letter] == 0:
                return letter
            letter_in_s[letter] -= 1
        
        
