class Solution {
private:
    void swap(char& char1, char& char2){
        char temp = char1;
        char1 = char2;
        char2 = temp;
    }
public:

    void reverseString(vector<char>& s) {
        int left = 0, right = s.size() - 1;
        while (left < right){
            swap(s.at(left), s.at(right));
            left ++;
            right --;
        }
    }
};
