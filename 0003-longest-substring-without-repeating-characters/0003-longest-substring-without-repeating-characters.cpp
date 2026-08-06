class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int hash[256];
        fill(hash, hash + 256, -1);
        int n=s.size();
        int l=0;
        int r=0;
        int maxlen=0;
        while(r<n){
            if(hash[s[r]]!=-1){
                if(hash[s[r]]>=l)
                l=hash[s[r]]+1;
            }
            maxlen=max(maxlen,r-l+1);
            hash[s[r]]=r;
            r++;
        }
        return maxlen;
    }
};


// int n=s.length();
//         int maxlen=0;
//         for(int i=0;i<n;i++){
//             vector<int>charat(255,0);
//             for(int j=i;j<n;j++){
//                 if(charat[s[j]]==1){
//                     break;
//                 }
//                 int len=j-i+1;
//                 maxlen=max(len,maxlen);
//                 charat[s[j]]=1;
//             }
//         }
//         return maxlen;