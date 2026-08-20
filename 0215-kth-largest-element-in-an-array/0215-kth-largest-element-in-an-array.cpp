class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        sort(nums.begin(),nums.end(),greater<>());
        return nums[k-1];
        // unordered_map<int,int>freq;
        // for(int num:nums){
        //     freq[num]++;
        // }
        // vector<int>unique;
        // for(auto & it :freq){
        //     unique.push_back(it.first);
        // }
        // int n=unique.size();
        // return unique[n-k];
    }
};