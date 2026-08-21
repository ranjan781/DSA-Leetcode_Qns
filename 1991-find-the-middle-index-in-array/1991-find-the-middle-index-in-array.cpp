class Solution {
public:
    int findMiddleIndex(vector<int>& nums) {
        int right_sum=accumulate(nums.begin(),nums.end(),0);
            int leftsum=0;
            for(int i=0;i<nums.size();i++){
                right_sum-=nums[i];
                if(leftsum==right_sum){
                    return i;
                }
                leftsum+=nums[i];
            }
            return -1;
    }
};