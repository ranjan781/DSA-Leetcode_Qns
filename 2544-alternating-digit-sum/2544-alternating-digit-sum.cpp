class Solution {
public:
    int alternateDigitSum(int n) {
        vector<int>store;
        while(n>0){
            int digit=n%10;
            store.push_back(digit);
            n/=10;
        }
        reverse(store.begin(),store.end());
        int m=store.size();
        int sign=-1;
        for(int i=0;i<m;i++){
            if(i%2!=0){
                store[i]=store[i]*sign;
            }
        }
        int sum=0;
        for(int i=0;i<store.size();i++){
            sum+=store[i];
        }
        return sum;
    }
};