class Solution {
public:
    int countSpecialIntegers(vector<int>& nums) {
        int count=0;
        int n=nums.size();
        unordered_map<int,vector<int>>indexmp;
        for(int i=0;i<nums.size();i++){
            indexmp[nums[i]].push_back(i);
        }
        for(const auto& [num,index]:indexmp){
            if(index.size()>=3){
                bool valid=true;
                int diff=index[1]-index[0];
                for(int i=2;i<index.size();i++){
                    if(index[i]-index[i-1]!=diff){
                        valid=false;
                        break;
                    }
                }
                if(valid)
                   count++;
            }
        }
        return count;
    }
};