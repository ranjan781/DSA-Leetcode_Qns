class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        unordered_set<int>store;
        for(int i=0;i<nums.size();i++){
            if(nums[i]>0){
                store.insert(nums[i]);
            }
        }
        int maxi=INT_MIN;
        for(auto x:store){
            maxi=max(maxi,x);
        }
        for(int i=1;i<=maxi;i++){
            if(store.find(i)==store.end())
            return i;
        }
        int mxi=*max_element(nums.begin(),nums.end());
        if(mxi<=0) return 1;
        return mxi+1;
    }
};