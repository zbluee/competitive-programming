class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        original_capacity = capacity

        for i in range(len(plants)):
            if capacity >= plants[i]:
                steps += 1

            else:
                capacity = original_capacity
                steps += 2*i + 1
            
            capacity -= plants[i]

        return steps

            
            

        
