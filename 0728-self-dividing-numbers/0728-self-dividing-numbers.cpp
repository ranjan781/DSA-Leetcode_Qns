class Solution {
public:
    bool sdn(int num){
        int temp=num;
        while(temp>0){
            int digit=temp%10;
            if(digit==0 || num%digit!=0){
                return false;
            }
            temp=temp/10;
        }
        return true;
    };
    vector<int> selfDividingNumbers(int left, int right) {
        vector<int>ans;
        for(int i=left;i<=right;i++){
            if(sdn(i)){
                ans.push_back(i);
            }else{
                continue;
            }
        }
        return ans;
    }
};