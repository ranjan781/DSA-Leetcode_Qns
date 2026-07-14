class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string>result;
        if(nums.empty()){
            return result;
        }
        int j;
        for(int i=0;i<nums.size();i=j+1){
            int st=nums[i];
            j=i;
            while(j+1<nums.size() && nums[j+1]==nums[j]+1){
                j++;
            }
            if(nums[j]==st){
                result.push_back(to_string(st));
            }else{
                result.push_back(to_string(st)+ "->" + to_string(nums[j]));
            }
        }
        return result;
    }
};