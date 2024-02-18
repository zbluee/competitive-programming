class RandomizedSet {
private:
    std::unordered_set<int> randomizedSet;
public:
    RandomizedSet() : randomizedSet({}){
        
    }
    
    bool insert(int val) {
        const auto itr = std::ranges::find_if(randomizedSet, [&](const int& value) {return val == value;});
        if(itr != randomizedSet.end()) return false;
        randomizedSet.insert(val);
        return true;
    }
    
    bool remove(int val) {
        const auto itr = std::ranges::find_if(randomizedSet, [&](const int& value) {return val == value;});
        if(itr == randomizedSet.end()) return false;
        randomizedSet.erase(val);
        return true;
    }
    
    int getRandom() {
        int idx = rand() % randomizedSet.size();
        return *std::next(randomizedSet.begin(), idx);
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */
