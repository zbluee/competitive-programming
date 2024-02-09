class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_idx = 2000
        list1_idx_pair = {list1[i] : i for i in range(len(list1))}
        common = {}
        for i, str2 in enumerate(list2):
            if str2 in list1_idx_pair:
                idx_sum = sum((i, list1_idx_pair[str2]))
                common[str2] = idx_sum
                min_idx = min(min_idx, idx_sum) 

        if len(common) == 1:
            return common.keys()
            
        return [k for k, v in common.items() if v == min_idx]
