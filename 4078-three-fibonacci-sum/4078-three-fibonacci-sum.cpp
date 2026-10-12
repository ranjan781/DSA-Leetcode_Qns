class Solution {
public:
    bool threeFibonacciSum(int n) {
        int a=0;
        int b=1;
        int c=0;
        while(a+b+c<=n){
            a=b;
            b=c;
            c=a+b;
            if(a+b+c==n) return true;
        }
        return false;
    }
};