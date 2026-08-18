class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        int n=nums.size();
        sort(nums.begin(),nums.end());
        unordered_map<int,int>freq;
        for(int num:nums){
            freq[num]++;
        }
        vector<int>ans;
        for(auto & it:freq){
            if(it.second>1){
                ans.push_back(it.first);
            }
        }
        int idx=0;
        vector<int> hmap(n + 1, 0);
        for(int i=0;i<n;i++){
            hmap[nums[i]]=1;
        }
        for(int i=1;i<=n;i++){
            if(hmap[i]==0){
                idx=i;
                ans.push_back(idx);
                break;

            }
        }
        
        return ans;
    }
};