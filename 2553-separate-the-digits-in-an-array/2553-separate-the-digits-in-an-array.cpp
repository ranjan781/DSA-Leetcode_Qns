class Solution {
public:
    vector<int> separateDigits(vector<int>& nums) {
        vector<int>ans;
        for(int i=0;i<nums.size();i++){
            string num=to_string(nums[i]);
            for(auto chr:num){
                ans.push_back(chr-'0');
            }
        }
        return ans;
    }
};