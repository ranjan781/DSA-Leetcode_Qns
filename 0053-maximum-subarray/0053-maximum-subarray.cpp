class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int currsum=0, maxSum=INT_MIN;
        for(int val :nums){
            currsum+=val;
            maxSum=max(currsum,maxSum);
            if(currsum<0){ 
                currsum=0;
            }
        }
        return maxSum;
        
    }
};