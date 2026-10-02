class Solution {
public:
    int earliestTime(vector<vector<int>>& tasks) {
        if (tasks.empty()) return 0;
        vector<int>store_time;
        for(int i=0;i<tasks.size();i++){
            store_time.push_back(tasks[i][0]+tasks[i][1]);
        }
        int idx=*min_element(store_time.begin(),store_time.end());
        return  idx;
    }
};