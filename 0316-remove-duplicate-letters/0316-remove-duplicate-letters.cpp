class Solution {
public:
    string removeDuplicateLetters(string s) {
        int n=s.length();
        string result;
        vector<bool>taken(26,false);
        vector<int>lastindex(26,0);
        for(int i=0;i<n;i++){
            lastindex[s[i]-'a']=i;
        }
        for(int i=0;i<n;i++){
            char ch=s[i];
            int index=ch-'a';
            if(taken[index]==true) continue;
            while(result.length()>0 && result.back()>ch && lastindex[result.back()-'a']>i){
                taken[result.back()-'a']=false;
                result.pop_back();
            }
            result.push_back(ch);
            taken[index]=true;
        }
        return result;
    }
};