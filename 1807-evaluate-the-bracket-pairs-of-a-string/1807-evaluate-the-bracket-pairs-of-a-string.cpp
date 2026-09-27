class Solution {
public:
    string evaluate(string s, vector<vector<string>>& knowledge) {
        unordered_map<string,string>mpp;
        for(auto it:knowledge){
            mpp[it[0]]=it[1];
        }
        string result="";
        int i=0;
        while(i<s.length()){
            if(isalpha(s[i])){
                result+=s[i];
            }else{
                i++;
                string temp;
                while(s[i]!=')' && i<s.length()){
                    temp+=s[i];
                    i++;
                }
                result+=mpp.count(temp)?mpp[temp]:"?";
            }
            i++;
        }
        return result;
    }
};