class Solution {
public:
    int maximumProduct(vector<int>& nums) {
        int n=nums.size();
        sort(nums.begin(),nums.end());
        int val1=nums[0]*nums[1]*nums[n-1];
        int val2=1LL*nums[n-1]*nums[n-2]*nums[n-3];
        if(val1>val2){
            return val1;
        }
        return val2;        
    }
};