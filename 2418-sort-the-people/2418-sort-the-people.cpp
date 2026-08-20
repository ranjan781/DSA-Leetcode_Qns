class Solution {
public:
    vector<string> sortPeople(vector<string>& names, vector<int>& heights) {
        int peoples=names.size();
        unordered_map<int,string>heightToName;
        for(int i=0;i<peoples;i++){
            heightToName[heights[i]]=names[i];
        }
        sort(heights.begin(),heights.end());
        vector<string>sorted_name(peoples);
        for(int i=peoples-1;i>=0;i--){
            sorted_name[peoples-i-1]=heightToName[heights[i]];  
        }
        return sorted_name;
    }
};