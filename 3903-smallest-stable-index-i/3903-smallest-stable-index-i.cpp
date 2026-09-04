class Solution {
public:
    int firstStableIndex(vector<int>& nums, int k) {
        int n=nums.size();
        for(int i=0;i<n;i++){
            int maxval=nums[i];
            int minval=nums[i];
            for(int j=0;j<i;j++){
                maxval=max(maxval,nums[j]);
            }for(int j=i+1;j<n;j++){
                minval=min(minval,nums[j]);
            }
            if(maxval-minval<=k){
                return i;
            }
        }
        return -1;
    }
};