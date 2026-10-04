class Solution {
public:
    bool checkValidString(string s) {
        stack<char>open;
        stack<char>star;
        for(int i=0;i<s.size();i++){
            char ch=s[i];
            if(ch=='('){
                open.push(i);
            }else if(ch=='*'){
                star.push(i);
            }else{
                if(!open.empty()){
                    open.pop();
                }else if(!star.empty()){
                    star.pop();
                }else{
                    return false;
                }
            }
        }
        while(!open.empty() && !star.empty()){
            if(open.top()>star.top()){
                return false;
            }
            star.pop();
            open.pop();
        }
        return open.empty();
    }
};