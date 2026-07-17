class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        int n=nums.size();
        vector<int>ps;
        vector<int>ng;
        //storing elements
        for(int i=0;i<n;i++){
            if(nums[i]<0){
                ng.push_back(nums[i]);
            }else{
                ps.push_back(nums[i]);
            }
        }
        //for ans
        vector<int>ans;
        int low=0,high=0;
        for(int i=0;i<n;i++){
            if(i%2==0){
                ans.push_back(ps[low]);
                low=low+1;
            }else{
                ans.push_back(ng[high]);
                high=high+1;
            }
        }
        return ans;
    }
};