class Solution {
public:
    bool search(vector<int>& nums, int target) {
     int low=0;
        int high=nums.size()-1;
        while(low<=high){
            int mid=low+(high-low)/2;
            if(nums[mid]==target){
                return true;
            }
            else if(nums[mid] == nums[low]) {
                low++;
                continue;
            }
            else if(nums[low]<=nums[mid]){//left part sorted
                if(nums[low]<=target && target<nums[mid]){ //is there target lies btw
                    high=mid-1;
                }else{
                    low=mid+1;
                }

            }else{//right part sorted
                if(nums[mid]<target && target<=nums[high]){
                    low=mid+1;
                }else{
                    high=mid-1;
                }
            }
        }
        return false;   
    }
};