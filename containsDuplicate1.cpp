class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        std::unordered_set<int> seen(nums.begin(), nums.end());
        return nums.size() != seen.size();
    }
};
