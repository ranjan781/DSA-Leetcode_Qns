class Solution {
public:
    int numberOfMatches(int n) {
        int noOfmatch=0;
        while(n>1){
            if(n%2==0){
                noOfmatch+=n/2;
            }else{
                noOfmatch+=(n-1)/2+1;
            }
            n/=2;
        }
        return noOfmatch;
    }
};