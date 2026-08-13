class Solution {
public:
    int maxProductDifference(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int n=nums.size();
        int maxi_value=nums[n-2]*nums[n-1];
        int min_value=nums[0]*nums[1];
        return maxi_value-min_value;
    }
};