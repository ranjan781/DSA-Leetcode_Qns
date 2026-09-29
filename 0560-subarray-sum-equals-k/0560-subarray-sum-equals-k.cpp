class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int cnt=0;
        int n=nums.size();
        vector<int>sum(n+1,0);
        for(int i=1;i<=n;i++){
            sum[i]=sum[i-1]+nums[i-1];
        }
        for(int st=0;st<n;st++){
            for(int end=st+1;end<=n;end++){
                if(sum[end]-sum[st]==k) cnt++;
            }
        }
        return cnt;
    }
};


// for(int i=0;i<nums.size();i++){
//             int sum=0;
//             for(int j=i;j<nums.size();j++){
//                 sum+=nums[j];
//                 if(sum==k) cnt++;
//             }
//         }