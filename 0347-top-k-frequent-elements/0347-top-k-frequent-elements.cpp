class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int>store;
        for(int num:nums){
            store[num]++;
        }
        priority_queue<pair<int,int>>pq;//maxheap
        for(auto it:store){
            pq.push({it.second,it.first});
        }
        vector<int>ans;
        while(k--){
            ans.push_back(pq.top().second);
            pq.pop();
        }
        return ans;
    }
};