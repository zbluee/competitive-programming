class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int curr_sum = 0, max_sum = 0;
        for(int i = 0, size = nums.size(); i < size; i ++){
            if(curr_sum < 0) curr_sum = 0;
            curr_sum += nums.at(i);
            max_sum = max(max_sum, curr_sum);
        }
        
        return max_sum;
    }
};
