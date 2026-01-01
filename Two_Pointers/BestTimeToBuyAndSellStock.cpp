/*
Problem: Best Time to Buy and Sell Stock
LeetCode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
Topic: Two Pointers
Difficulty: Easy

Approach:
- L, R pointers starting at 0 and 1 respectively.
- We move the R pointer to the right until we find a price that is greater than the price at the L pointer.
- We calculate the profit and update the maximum profit if the current profit is greater.
- We move the L pointer to the R pointer and repeat the process.
- We return the maximum profit.



Time Complexity: O(n)
Space Complexity: O(1)
*/



class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int l = 0;
        int r = 1;
        int profitMax = 0;
        while(r < prices.size()){
            if(prices[r] > prices[l]){
                int x = prices[r] - prices[l];
                if(profitMax < x){
                    profitMax = x;
                }
            }
            else{
                l = r;
            }
            r++;
        }
        return profitMax;
    }
};
