class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        unordered_map<int,int>mp;
        for(int i=0;i<arr.size();i++){
            mp[arr[i]]++;
        }
        unordered_set<int> uniqueCounts;
        for (const auto& [element, frequency] : mp) {
        // If the frequency is already in the set, it's not unique
           if (!uniqueCounts.insert(frequency).second) {
               return false;
        }
    }
    return true;
    }
};