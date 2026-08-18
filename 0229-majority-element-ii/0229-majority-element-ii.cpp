class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int n=nums.size();
        int freq=n/3;
        unordered_map<int,int>mpp;
        for(int num:nums){
            mpp[num]++;
        }
        vector<int>ans;
        for(auto& it:mpp){
            if(it.second>freq){
                ans.push_back(it.first);
            }
        }
        return ans;
    }
};