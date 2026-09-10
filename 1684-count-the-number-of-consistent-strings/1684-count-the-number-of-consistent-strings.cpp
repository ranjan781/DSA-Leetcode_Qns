class Solution {
public:
    int countConsistentStrings(string allowed, vector<string>& words) {
        int consistentCount=0;
        vector<bool>isAllowed(26,false);
        for(int i=0;i<allowed.size();i++){
            isAllowed[allowed[i]-'a']=true;
        }
        for(string word:words){
            bool isConsistent=true;
            for(int i=0;i<word.size();i++){
                if(!isAllowed[word[i]-'a']){
                    isConsistent=false;
                    break;
                }
            }
            if(isConsistent){
                consistentCount++;
            }
        }
        
        return consistentCount;
    }
};