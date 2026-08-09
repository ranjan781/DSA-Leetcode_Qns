class Solution {
public:
    int minimizedStringLength(string s) {
        unordered_map<char,int>map;
        for(auto num:s){
            map[num]++;
        }
        return map.size();
    }
};