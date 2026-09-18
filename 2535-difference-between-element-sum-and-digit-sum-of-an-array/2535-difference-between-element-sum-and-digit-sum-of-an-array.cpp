class Solution {
public:
    int differenceOfSum(vector<int>& nums) {
        int elementsum=accumulate(nums.begin(),nums.end(),0);
        int digitsum=0;
        for(int i=0;i<nums.size();i++){
            while(nums[i]>0){
                digitsum+=nums[i]%10;
                nums[i]/=10;
            }
        }
        return abs(digitsum-elementsum);
    }
};