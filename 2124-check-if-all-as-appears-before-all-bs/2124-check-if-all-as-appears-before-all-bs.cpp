class Solution {
public:
    bool checkString(string s) {
        int n=s.size();
        int lasta=-1;
        int firstb=n;
        for(int i=0;i<s.size();i++){
            if(s[i]=='a'){
                lasta=max(lasta,i);
            }else{
                firstb=min(firstb,i);
            }
        }
        return lasta<firstb;
    }
};