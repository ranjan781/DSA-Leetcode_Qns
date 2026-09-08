class Solution {
public:
    int maxIceCream(vector<int>& costs, int coins) {
        int count=0;
        sort(costs.begin(),costs.end());
        for(int num:costs){
            if(coins<num){
                break;
            }
            count++;
            coins=coins-num;
        }
        return count;
    }
};