class Solution {
public:
    int reverse(int n) {
        int revNum=0;
        while(n!=0){
            int lastdig=n%10;
            if((revNum > INT_MAX/10) || (revNum < INT_MIN/10)){
                return 0;
            }
            revNum=revNum*10+lastdig;
            n=n/10;
        }
        return revNum;
    }

        bool isPalindrome(int n){
            if(n<0){
            return false;
            }
            int revnum=reverse(n);
            return n==revnum;
        
    }
};