class Solution {
public:
    int subtractProductAndSum(int n) {
        long sum=0;
        long prod=1;
        while(n>0){
            prod*=n%10;
            sum+=n%10;
            n/=10;
        }
        return prod-sum;
    }
};