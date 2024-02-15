class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        std::vector<int> result(nums.size(), 1);
        int prefixProd = 1, postfixProd = 1;

        for(int i = 0, size = nums.size(); i < size; i ++){
            result[i] *= prefixProd;
            prefixProd *= nums[i];
        }

        for(int j = nums.size() - 1; j > -1; j --){
            result[j] *= postfixProd;
            postfixProd *= nums[j];
        }

        return result;
    }
};
