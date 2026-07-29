class Solution {
public:
    int thirdMax(vector<int>& nums) {
        int n=nums.size();
        sort(nums.begin(),nums.end(),greater<>());
        int prevele=nums[0];
        int elecounted=1;
        for(int i=1;i<n;i++){
            if(nums[i]!=prevele){
                elecounted++;
                prevele=nums[i];
            }
            if(elecounted==3){
                return nums[i];
            }
        }
        return nums[0];
    }
};