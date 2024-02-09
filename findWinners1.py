class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        defeated_players = defaultdict(int)
        players = set()
        for winner, loser in matches:
            defeated_players[loser] += 1
            players.add(winner)
            players.add(loser)

        result0, result1 = [], []

        for player in players:
            if defeated_players[player] == 0:
                result0.append(player)
            elif defeated_players[player] == 1:
                result1.append(player)

        return [sorted(result0), sorted(result1)]


        
