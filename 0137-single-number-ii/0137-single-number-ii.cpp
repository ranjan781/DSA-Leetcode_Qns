class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int n=nums.size();
        unordered_map<int,int>mp;
        for(int num:nums){
            mp[num]++;
        }
        int ans;
        for(auto it:mp){
            if(it.second==1){
                ans=it.first;
                break;
            }
        }
        return ans;
    }
};