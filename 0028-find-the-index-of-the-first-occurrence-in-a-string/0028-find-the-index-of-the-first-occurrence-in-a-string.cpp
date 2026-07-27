class Solution {
public:
    int strStr(string haystack, string needle) {
        int index=haystack.find(needle); //return the index of first
        if(index<haystack.size()){
            return index;
        }
        return -1;
    }
};