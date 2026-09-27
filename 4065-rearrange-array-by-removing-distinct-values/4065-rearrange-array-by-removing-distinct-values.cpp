class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        vector<int>ans;
        unordered_map<int,int>mpp;//store the element and its freq
        for(auto it:nums){
            mpp[it]++;
        }
        while(mpp.size()!=0){
            vector<int>temp;
            for(auto it=mpp.begin();it!=mpp.end();){
                temp.push_back(it->first);
                it->second--;

                if(it->second==0) it=mpp.erase(it);
                else it++;
            }
            sort(temp.begin(),temp.end());
            for(int i=0;i<temp.size();i++){
            ans.push_back(temp[i]);
            }
        }
        return ans;
    }
};