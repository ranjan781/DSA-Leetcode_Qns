class Solution {
public:
    long long maxAlternatingSum(vector<int>& nums) {
        for(int i=0;i<nums.size();i++){
            nums[i]=nums[i]*nums[i];
        }
        sort(nums.begin(),nums.end());
        long res=0;
        int l=0;
        int r=nums.size()-1;
        while(l<=r){
            if(l==r){
                res+=nums[l];
            }
            else{
                res+=nums[r]-nums[l];
            }
            l++;
            r--;
        }
        return res;
    }
};