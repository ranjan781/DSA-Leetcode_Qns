class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int n=nums.size();
        int low=nums[0];
        int ans;
        int high=nums[n-1];
        sort(nums.begin(),nums.end());
        for(int i=1;i<nums.size();i++){
            if(nums[i]==nums[i-1]){
                ans=nums[i];
                break;

            }
        }
        // while(low<=high){
        //     int mid=low+(high-low)/2;
        //     if(low==high && mid==low){
        //         return nums[low];
        //     }
        //     if(nums[mid]==nums[mid-1]){
        //         return nums[mid];
        //     }
        //     if(nums[mid]<nums[mid-1])
            
        // }
        return ans;
    }
};



        // int ans;
        // for(int i=0;i<nums.size();i++){
        //     for(int j=i+1;j<nums.size();j++){
        //         if(nums[i]==nums[j]){
        //             ans=j;
        //         }
        //     }
        // }
        // return nums[ans];