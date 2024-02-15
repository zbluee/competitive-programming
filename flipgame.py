class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        min_good_int = 2001
        not_goods = set()

        for front, back in zip(fronts, backs):
            if front == back:
                not_goods.add(front)

        for front, back in zip(fronts, backs):
            
            if back not in not_goods:
                min_good_int = min(min_good_int, back) 

            if front not in not_goods:
                min_good_int = min(min_good_int, front)

        return 0 if min_good_int == 2001 else min_good_int
        
