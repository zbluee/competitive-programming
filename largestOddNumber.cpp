class Solution {
public:
    string largestOddNumber(string num) {
        int right = num.size() - 1;

        while (right > -1){
            if ( int(num.at(right)) % 2 == 1)
                return num.substr(0, right + 1);
            
            right --;
        }
        return "";
    }
};
