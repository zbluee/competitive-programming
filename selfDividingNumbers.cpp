class Solution {
private:
    bool isSelfDividingNumber(int num){
        int originalNum = num;
        while(num > 0){
            int digit = num % 10;
            if(digit == 0 || originalNum % digit != 0) return false;
            num /= 10;
        }
        return true;
    }
public:
    vector<int> selfDividingNumbers(int left, int right) {
      std::vector<int> res;
      res.reserve(right - left + 1);
      for(int i = left; i <= right; i ++){
          if(isSelfDividingNumber(i)) res.emplace_back(i);
      }
      return res;
    }
};
