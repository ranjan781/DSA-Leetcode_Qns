class Solution {
public:
    bool isAlnum(char ch){// for checking character is alphanumeric or not
        if(ch>='0' && ch<='9' || tolower(ch)>='a' && tolower(ch)<='z'){
            return true;
        }
        return false;     
    }
    bool isPalindrome(string s) {
        int st=0,end=s.length()-1;
        while(st<=end){
            if(!isAlnum(s[st])){ //is char is not a alphanumeric
                st++;
                continue;
            }
            if(!isAlnum(s[end])){
                end--;
                continue;
            }
            if(tolower(s[st])!=tolower(s[end])){
                return false;
            }
            st++,end--;
        }
        return true;
        
    }
};