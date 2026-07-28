class Solution {
public:
    int lengthOfLastWord(string s) {
    istringstream stream(s);
    string word;
    vector<string> words;

    // Extract word by word
    while (stream >> word) {
        words.push_back(word);
    }
    int n=words.size();
    return (words[n-1].size());
    }
};