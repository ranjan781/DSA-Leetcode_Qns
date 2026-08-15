class Solution {
public:
    int maximumLengthSubstring(string s) {
        int i=0;
        int j=0;
        unordered_map<char,int>freq;
        int n=s.size();
        int res=0;
        while(j<n){
            freq[s[j]]++;
            while(freq[s[j]]>2){
                freq[s[i]]--;
                i++;
            }
            res=max(res,j-i+1);
            j++;
        }
        return res;
    }
};