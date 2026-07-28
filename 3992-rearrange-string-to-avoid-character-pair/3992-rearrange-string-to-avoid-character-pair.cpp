class Solution {
public:
    string rearrangeString(string s, char x, char y) {
        if(x>y){
            sort(s.begin(),s.end());
            return s;
        }
        sort(s.begin(),s.end(),greater<>());
        return s;
    }
};