class Solution {
public:
    vector<int> addToArrayForm(vector<int>& nums, int k) {
        int carry=0;
        int n=nums.size();
        vector<int>ans;
        int i=nums.size()-1;
        while(i>=0 || k>0 || carry){
            int sum=carry;
            if(i>=0){
                sum=sum+nums[i];
                i--;
            }
            if(k > 0){
                sum += k % 10;
                k /= 10;
            }
            ans.push_back(sum%10);
            carry=sum/10;
        }
        reverse(ans.begin(),ans.end());
        return ans;
    }
};