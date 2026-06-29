class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.length()!=t.length()){
            return false;
        }
        int freq[26]={0};
        for(int i=0;i<s.length();i++){ //counting no. of each characters
            freq[s[i]-'a']++;
        }
        for(int i=0;i<t.length();i++){ //counting no. of each characters
            freq[t[i]-'a']--;
        }
        for(int i=0;i<26;i++){
            if(freq[i]!=0){
                return false;
            }
        }
        return true;
    }
};



// if(s.length()==t.length()){
//             sort(s.begin(),s.end());
//             sort(t.begin(),t.end());
//             int i=0;
//             int j=0;
//             while(i<=s.length()){
//                 if(s[i]==t[j]){
//                     i++;
//                     j++;
//                 }else{
//                     return false;
//                 }
//             }
//             return true;
//         }
//         return false;
//     }