class Solution {
private:
    int sumofdig(int n){
        int sum=0;
        while(n>0){
            sum+=n%10;
            n/=10;
        }
        return sum;
    }
public:
    int sumOfTheDigitsOfHarshadNumber(int x) {
        if(x%sumofdig(x)==0){
            return sumofdig(x);
        }
        return -1;
    }
};