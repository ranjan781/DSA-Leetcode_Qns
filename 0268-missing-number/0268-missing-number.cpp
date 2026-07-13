class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n=nums.size();
        int idx=0;
        vector<int> hmap(n + 1, 0);
        for(int i=0;i<n;i++){
            hmap[nums[i]]=1;
        }
        for(int i=0;i<=n;i++){
            if(hmap[i]==0){
                idx=i;
                break;

            }
        }
        return idx;
    }
};