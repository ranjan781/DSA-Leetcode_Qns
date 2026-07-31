class Solution {
public:
    vector<int>st;
    int trib(int n){
        if(n<=1){
            return n;
        }if(n==2){
            return 1;
        }
        if(st[n] != -1) return st[n];

        return st[n] = trib(n-1) + trib(n-2) + trib(n-3);
    };
    
    int tribonacci(int n) {
        //int ans=trib(n);
        st.resize(n+1,-1);
        return trib(n);
    }
};