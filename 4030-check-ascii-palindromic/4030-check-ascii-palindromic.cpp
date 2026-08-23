class Solution {
public:
    string toBinary(char c){
        int n=c;
        string s;
        while(n){
            s+=n%2+'0';
            n/=2;
        }
        while(s.size()!=8){
            s+='0';
        }
        reverse(s.begin(),s.end());
        return s;
    }
    bool isPalindromic(string s) {
        string ans;
        for(char &c:s){
            ans+=toBinary(c);
        }
        for(int i=0,j=ans.size()-1;i<j;i++,j--){
            if(ans[i]!=ans[j]){
                return false;
            }
        }
        return true;
    }
};