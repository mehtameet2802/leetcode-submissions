class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int x = prices.size();
        int pro = 0;
        int minPrice = INT_MAX;
        for(int i=0;i<x;i++){
            minPrice = min(prices[i],minPrice);
            pro = max(pro,prices[i]-minPrice);
        }
        return pro;
    }
};