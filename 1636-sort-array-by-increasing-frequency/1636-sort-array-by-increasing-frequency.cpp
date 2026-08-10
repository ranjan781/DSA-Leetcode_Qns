class Solution {
public:
    vector<int> frequencySort(vector<int>& nums) {
        unordered_map<int,int>freq;
        for(auto num:nums){
            freq[num]++;
        }
        sort(nums.begin(),nums.end(),[&](int n1,int n2){
            if(freq[n1]!=freq[n2]){// ascending
                return freq[n1]<freq[n2];
            }else{//desencding
                return n2<n1;
            }
        });
        return nums;
    }
};