class Solution {
public:
    int longestMonotonicSubarray(vector<int>& nums) {
        int inclength=1;
        int declength=1;
        int maxlength=1;
        for(int pos = 0; pos < nums.size() - 1; pos++) {
            if (nums[pos + 1] > nums[pos]) {
                inclength++;
                declength = 1; 
            }else if(nums[pos+1]<nums[pos]){
                declength++;
                inclength = 1;
            }else{
                inclength=1;
                declength=1;

            }
            maxlength=max(maxlength,max(inclength,declength));
    }
    return maxlength;
    } 
};