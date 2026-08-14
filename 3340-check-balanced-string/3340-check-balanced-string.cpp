class Solution {
public:
    bool isBalanced(string num) {
        vector<char>store;
        for(int i=0;i<num.size();i++){
            store.push_back(num[i]);
        }
        int sum_even=0;
        int sum_odd=0;
        for(int i=0;i<store.size();i++){
            if(i%2==0){
                sum_even+=store[i]-'0';
            }
            else{
                sum_odd+=store[i]-'0';
            }
        }
        if(sum_even==sum_odd){
            return true;
        }
        return false;
    }
};