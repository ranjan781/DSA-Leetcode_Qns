class Solution {
public:
    bool isValid(string str) {
        stack<char>st;
        for(int i=0;i<str.size();i++){
            if(str[i]=='(' || str[i]=='{' || str[i]=='['){//for opening brackets
                st.push(str[i]);
            }else{// for closing brackets
                if(st.size()==0){//if closing brackets>opening brackets
                    return false;
                }if(st.top()=='(' && str[i]==')' ||
                    st.top()=='{' && str[i]=='}' ||
                    st.top()=='[' && str[i]==']'){// stack top element matches with string char
                        st.pop();
                    }else{//no match with string char
                        return false;
                    }
            }
        }
        return st.size()==0;
    }
};