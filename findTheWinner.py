class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = [i for i in range(1, n+1)]
        
        def findWinnerHelper(idx:int, k:int)-> None:
            if len(players) == 1:
                return
            idx = (idx + k) % len(players)
            players.pop(idx)
            findWinnerHelper(idx, k)

        findWinnerHelper(0, k-1)
        return players[0]
            
