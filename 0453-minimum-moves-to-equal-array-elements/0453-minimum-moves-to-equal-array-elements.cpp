class Solution {
public:
    int minMoves(vector<int>& nums) {
        int min_ele=*min_element(nums.begin(),nums.end());
        int moves=0;
        for(int num:nums){
            moves+=(num-min_ele);
        }
        return moves;
    }
};