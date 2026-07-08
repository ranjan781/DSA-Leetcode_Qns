class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        vector<int>ans;
        //search  the element in nums2
        for(int i=0;i<nums1.size();i++){
            int find_idx=-1;
            for(int j=0;j<nums2.size();j++){
                if(nums1[i]==nums2[j]){
                    find_idx=j;
                    break;
                }
            }
        int nextgreater=-1;
        for(int j=find_idx+1;j<nums2.size();j++){
            if(nums2[j]>nums2[find_idx]){
                nextgreater=nums2[j];
                break;
            }
        }
        ans.push_back(nextgreater);
        }
        return ans;
    }
};