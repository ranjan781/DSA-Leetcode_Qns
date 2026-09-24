class Solution {
    int gcd(int a, int b) {
    return b == 0 ? a : gcd(b, a % b);
}
public:
    int findGCD(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int max_ele=nums[nums.size()-1];
        int min_ele=nums[0];
        int result=gcd(min_ele,max_ele);
        return result;
    }
};
