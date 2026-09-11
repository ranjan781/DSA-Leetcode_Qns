class Solution {
private:
    void even(vector<int>& digits,vector<int>& ans,int i,int& num,vector<bool>&used){
        if(i==3){
            if(num%2==0) ans.push_back(num);
            return;
        }
        for(int k=0;k<digits.size();k++){
            if(used[k]) continue;
            if(i==0 && digits[k]==0) continue;
            num=num*10+digits[k];
            used[k]=true;
            even(digits,ans,i+1,num,used);
            used[k]=false;
            num/=10;
        }
    }
public:
    int totalNumbers(vector<int>& digits) {
        vector<int>ans;
        vector<bool>used(digits.size(),false);
        int num=0;
        sort(digits.begin(),digits.end());
        even(digits,ans,0,num,used);
        sort(ans.begin(),ans.end());
        ans.erase(unique(ans.begin(),ans.end()),ans.end());
        return ans.size();
    }
}; 