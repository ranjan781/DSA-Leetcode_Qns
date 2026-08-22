class Solution {
public:
    int countPairs(vector<int>& nums, int target) {
        sort(nums.begin(),nums.end());
        int cnt=0;
        int n=nums.size();
        int left=0;
        int right=nums.size()-1;
        while(left<right){//O(nlogn)
            int sum=nums[left]+nums[right];
            if(sum<target){
                cnt+=right-left;
                left++;
            }else{
                right--;
            }
        }
        return cnt;
    }
};


// for(int i=0;i<n;i++){ //O(n^2)
//             for(int j=i+1;j<n;j++){
//                 if(nums[i]+nums[j]<target){
//                     cnt_pair++;
//                 }
//             }
//         }