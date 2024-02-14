class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        #Calculate the manhattan distance of the player
        player_distance = abs(target[0] - 0) + abs(target[1] - 0)

        for x, y in ghosts:
            #Calculate the manhattan distance of the each ghost
            ghost_distance = abs(target[0] - x) + abs(target[1] - y)
            #If one ghost is closer to the target than the player, can't escape
            if player_distance >= ghost_distance:
                return False

        return True
