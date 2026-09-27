class Solution {
public:
    string reverseParentheses(string s) {
        int n=s.size();
        stack<int>openbracketsIdx;
        vector<int>pair(n);
        for(int i=0;i<n;i++){
            if(s[i]=='('){
                openbracketsIdx.push(i);
            }if(s[i]==')'){
                int j=openbracketsIdx.top();
                openbracketsIdx.pop();
                pair[i]=j;
                pair[j]=i;
            }
        }
        string result;
        for(int curridx=0,direction=1;curridx<n;curridx+=direction){
            if(s[curridx]=='(' || s[curridx]==')'){
                curridx=pair[curridx];
                direction=-direction;
            }else{
                result+=s[curridx];
            }
        }
        return result;
    }
};