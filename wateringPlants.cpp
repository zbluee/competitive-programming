class Solution {
public:
    int wateringPlants(vector<int>& plants, int capacity) {
        int steps = 0, fullCapacity = capacity;

        for(int i = 0, size = plants.size(); i < size; i ++){
            if(plants[i] <= capacity) steps ++;
            else{
                capacity = fullCapacity;
                steps += 2 * i + 1;
            }

            capacity -= plants[i];
        }

        return steps;
        
    }
};
