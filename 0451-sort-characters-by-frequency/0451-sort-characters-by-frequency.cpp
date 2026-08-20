class Solution {
public:
    string frequencySort(string s) {
        string ans="";
        unordered_map<char,int>mp;
        for(char ch:s){
            mp[ch]++;
        }
        priority_queue<pair<int,char>> pq;
        for(auto it:mp){
            pq.push({it.second,it.first});
        }
        while(!pq.empty()){
            int x=pq.top().first;
            char ch=pq.top().second;
            while(x--){
                ans+=ch;
            }
            pq.pop();
        }
        return ans;
        
    }
};