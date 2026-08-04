class Solution {
public:
    vector<int> findMissingElements(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int n=nums.size();
        vector<int>ans;
        int max_ele=nums[n-1];
        int min_ele=nums[0];
        for(int i=0;i<n-1;i++){
            for(int j=nums[i]+1;j<nums[i+1];j++){
                ans.push_back(j);
            }
        }
        return ans;
    }
};