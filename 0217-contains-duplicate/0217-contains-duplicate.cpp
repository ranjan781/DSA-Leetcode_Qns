class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> seen;
        for (int num : nums) {
            if (seen.count(num) > 0)
                return true;
            seen.insert(num);
        }
        return false;
        // int rep=0;
        // for(int i=0;i<=nums.size();i++){
        //     if(nums[i]==nums[i+1]){
        //         rep++;
        //     }
            // for(int j=i+1;j<nums.size();j++){
            //     if(nums[j]==nums[i]){
            //     return true;
            //     break;
            //     }
            // }
        
        // if(rep==1) return false;
       // return false;
    }
};