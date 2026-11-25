class Solution {
private:
    bool ispal(string &s,int i,int j){
        while(i<j){
            if(s[i++]!=s[j--]){
            return false;
            }
        }
        return true;
    }
public:
    bool validPalindrome(string s) {
        int left=0;
        int right=s.size()-1;
        while(left<right){
            if(s[left]!=s[right]){
                return ispal(s,left+1,right) || ispal(s,left,right-1);
            }
            left++;
            right--;
        }
        return true;
    }
};