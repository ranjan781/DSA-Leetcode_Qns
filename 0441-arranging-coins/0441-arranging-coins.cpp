class Solution {
public:
    int arrangeCoins(int n) {
        int left=1;
        int right=n;
        while(left<=right){
            int mid=left+(right-left)/2;
            long long coins_need = 1LL * mid * (mid + 1) / 2;
            if(coins_need==n){
                return mid;
            }else if(coins_need<n){
                left=mid+1;
            }else{
                right=mid-1;
            }
        }
        return right;
    }
};