class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        unordered_set<int>store;
        for(int i=0;i<nums.size();i++){
            store.insert(nums[i]);
        }
        vector<int>ans;
        for(int i=1;i<=nums.size();i++){
            if(!store.count(i)){
                ans.push_back(i);
                //j++;
            }
        }
        return ans;
    }
};



// sort(begin(nums), end(nums));
//         vector<int> ans;
//         for(int i = 1; i <= size(nums); i++) 
//             if(!binary_search(begin(nums), end(nums), i))   // binary search in nums for each i
//                 ans.push_back(i);
//         return ans;