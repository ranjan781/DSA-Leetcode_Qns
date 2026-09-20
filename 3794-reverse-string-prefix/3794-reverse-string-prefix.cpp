class Solution {
public:
    string reversePrefix(string s, int k) {
        if (k > s.length()) k = s.length(); 
        
        string revstr = s.substr(0, k);
        reverse(revstr.begin(), revstr.end()); //inplace reverse
        
        return revstr + s.substr(k);
    }
};