class Solution {
public:
    vector<int> leftRightDifference(vector<int>& nums) {
        int n=nums.size();
        vector<int>leftsum;
        vector<int>rightsum;
        int runningleftsum=0;
        for(int i=0;i<n;i++){
            leftsum.push_back(runningleftsum);
            runningleftsum+=nums[i];
        }
        int runningrightsum=0;
        for(int j=n-1;j>=0;j--){
            rightsum.push_back(runningrightsum);
            runningrightsum+=nums[j];
        }
        reverse(rightsum.begin(),rightsum.end());
        vector<int>ans;
        for (int i = 0; i < n; i++){
            ans.push_back(abs(leftsum[i]-rightsum[i]));
        }
        return ans;
    }
};