class Solution {
public:
    long long sumAndMultiply(int n) {
        long long num=0;
        int count=0;
        int sum=0;
        while(n>0){
            int temp=n%10;
            n/=10;
            sum+=temp;
            if(temp!=0) num+=temp*pow(10,count++);
        }
        return sum*num;
    }
};