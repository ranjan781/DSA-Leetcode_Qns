class Solution {
public:
    int countKDifference(vector<int>& nums, int k) {
        int pairs=0;
        int count[101]={0};
        for(int num:nums){
            count[num]++;
        }
        for(int i=1;i<101-k;i++){
            pairs+=count[i]*count[i+k];
        }
        return pairs;
    }
};

// for(int i=0;i<nums.size();i++){
//             for(int j=i+1;j<nums.size();j++){
//                 if(abs(nums[i]-nums[j])==k) pairs++;
//             }
//         }