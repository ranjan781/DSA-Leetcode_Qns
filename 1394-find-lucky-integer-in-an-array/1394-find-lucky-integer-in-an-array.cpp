class Solution {
public:
    int findLucky(vector<int>& arr) {
        sort(arr.begin(),arr.end());
        unordered_map<int,int>mpp;
        for(int num:arr){
            mpp[num]++;
        }
        int maxi=-1;
        for(auto & it:mpp){
            if(it.first==it.second){
                maxi= max(maxi,it.first);
            }
        }
        return maxi;
    }
};