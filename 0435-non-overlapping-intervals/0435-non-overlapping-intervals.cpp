class Solution {
private:
    static bool compare(pair<int,int>a,pair<int,int>b){
      return a.second<b.second;
    }
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        int n=intervals.size();
        vector<pair<int,int>>activity;
        for(int i=0;i<n;i++){
            activity.push_back({intervals[i][0],intervals[i][1]});
        }
        sort(activity.begin(),activity.end(),compare);
        int count=1;
        int lastfinish=activity[0].second;
        for(int i=1;i<activity.size();i++){
            if(activity[i].first>=lastfinish){
                count++;
                lastfinish=activity[i].second;
            }
        }
        return n-count;
    }
};