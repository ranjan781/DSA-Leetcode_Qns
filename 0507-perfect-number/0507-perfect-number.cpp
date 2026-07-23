class Solution {
public:
    int SumofDiv(int &num){
        int sum=0;
        for(int i=1;i<num;i++){
            if(num%i==0){
                sum=sum+i;
            }else{
                continue;
            }
        }
        return sum;
    }
    bool checkPerfectNumber(int num) {
        int ans=SumofDiv(num);
        if(num==ans){
            return true;
        }
        return false;
    }
};