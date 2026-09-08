class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int>st(nums.begin(),nums.end());
        int longest=0;
        for(auto& n:st){
            if(st.contains(n-1))
                continue;
            int num=n;
            int curr=1;
            while(st.contains(num+1)){
                curr++;
                num++;
            }
            longest=max(longest,curr);
        }
        return longest;
    }
};