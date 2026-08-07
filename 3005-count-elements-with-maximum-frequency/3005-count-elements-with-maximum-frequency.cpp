class Solution {
public:
    int maxFrequencyElements(vector<int>& nums) {
        unordered_map<int,int>mpp;
        int total_occurences=0;
        for(int num:nums){
            mpp[num]++;
        }
        int maxi=0;
        for(auto it:mpp){
            maxi=max(maxi,it.second);
        }
        for(auto it:mpp){
            if(it.second==maxi){
                total_occurences+=it.second;
            }
        }
        return total_occurences;

    }
};