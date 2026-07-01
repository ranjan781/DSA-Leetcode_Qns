class Solution {
public:
    int fsearch(vector<int>&nums,int target){
        int f=-1;
        int low=0;
        int high=nums.size()-1;
        while(low<=high){
            int mid=low+(high-low)/2;
            if(nums[mid]==target){//left search
                f=mid;
                high=mid-1;
            }else if(nums[mid]<target){
                low=mid+1;
            }else{
                high=mid-1;
            }
        }
        return f;
    }
    int lsearch(vector<int>&nums,int target){
        int l=-1;
        int low=0;
        int high=nums.size()-1;
        while(low<=high){
            int mid=low+(high-low)/2;
            if(nums[mid]==target){//right search
                l=mid;
                low=mid+1;
            }else if(nums[mid]<target){
                low=mid+1;
            }else{
                high=mid-1;
            }
        }
        return l;
    }
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int>ans;
        int x=fsearch(nums,target);
        int y=lsearch(nums,target);
        ans.push_back(x);
        ans.push_back(y);
        return ans;
    }
};