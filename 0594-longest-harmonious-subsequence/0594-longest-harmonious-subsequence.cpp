class Solution {
public:
    int findLHS(vector<int>& nums) {
        int maxlen=0;
        unordered_map<int,int>freq;
        for(int num:nums){
            freq[num]++;
        }
        for(auto [num,count]:freq){
            if(freq.count(num+1)){
                int currlen=count+freq[num+1];
                maxlen=max(maxlen,currlen);
            }
        }
        return maxlen;
    }
};


// sort(nums.begin(),nums.end());
//         int maxlen=0;
//         int l=0;
//         int r=0;
//         while(r<nums.size()){
//             while(nums[r]-nums[l]>1){
//                 l++;
//             }
//             if(nums[r]-nums[l]==1)  maxlen=max(maxlen,r-l+1);
            
//             r++;
//         }
//         return maxlen;