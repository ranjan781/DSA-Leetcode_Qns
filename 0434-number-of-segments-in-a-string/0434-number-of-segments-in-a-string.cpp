class Solution {
public:
    int countSegments(string s) {
        stringstream ss(s);
        string word;
        vector<string>words;
        while(ss>> word){
            words.push_back(word);
        }
        return words.size();
    }
};