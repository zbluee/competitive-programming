class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        std::unordered_set<int> seen;
        for(const int& num : nums){
            if(seen.count(num) > 0) return true;
            seen.insert(num);
        }
        return false;
    }
};
