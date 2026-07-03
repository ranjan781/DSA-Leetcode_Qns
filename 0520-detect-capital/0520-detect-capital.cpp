class Solution {
public:
    bool detectCapitalUse(string word) {

        int upper = 0;
        int lower = 0;

        for(char c : word){
            if(isupper(c))
                upper++;
            else
                lower++;
        }

        if(upper == word.size()) return true;

        if(lower == word.size()) return true;

        if(isupper(word[0]) && lower == word.size()-1)
            return true;

        return false;
    }
};