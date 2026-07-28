class Solution {
public:
    // vector<int> primeFactor (int n ){
    // vector<int> ans ;
    // for (int i = 2 ; i <= n ; i++){
        
    //     // n %  i  == 0 means n is divisible by i 
    //     while (n % i == 0 && n > 0 ){
    //         ans.push_back(i);
    //         n = n / i ;
    //     }
    // }
    // return ans ;
//}
    bool isUgly(int n) {
        if(n==1) return true;
        if(n<=0) return false;
        while(n%2==0){
            n=n/2;
        }while(n%3==0){
            n=n/3;
        }while(n%5==0){
            n=n/5;
        }
        return n==1;
    }
};