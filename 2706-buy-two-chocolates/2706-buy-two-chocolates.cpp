class Solution {
public:
    int buyChoco(vector<int>& prices, int money) {
        sort(prices.begin(),prices.end());
        int priceoftwo=prices[0]+prices[1];
        if(money>=priceoftwo) return money-priceoftwo;
        return money;
        
    }
};