class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.expire_time = timeToLive
        self.tokens = {}
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime + self.expire_time
        

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokens and self.tokens[tokenId] > currentTime:
            self.tokens[tokenId] = currentTime + self.expire_time
        

    def countUnexpiredTokens(self, currentTime: int) -> int:
       
        return sum([1 if expire_time > currentTime else 0 for expire_time in self.tokens.values()])
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)
