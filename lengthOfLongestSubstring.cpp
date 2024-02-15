class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        std::unordered_set<int> seen;
        int left = 0, result = 0;

        for(int right = 0, size = s.size(); right < size; right++){
            while(seen.contains(s.at(right))){
                seen.erase(s.at(left));
                left ++;
            }
            seen.insert(s.at(right));
            result = max(result, right - left + 1);
        }

        return result;
    }
};
