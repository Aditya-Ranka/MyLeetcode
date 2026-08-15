/*
Problem: Coin Change
LeetCode: https://leetcode.com/problems/coin-change/description/
Topic: Dynamic Programming, Array
Difficulty: Medium  

Approach:
- Core idea is to make dp from bottom till we reach the amount. 
- initialise dp[0] = 0
-run a loop of index starting from 1 till the last element we need to find
- inside the loop run a loop iterating over all coiints
- now if the index is greater than the coin in the iteration 
- we update dp[x] = minimum of dp[x] and dp[x-c] +1
    this is so because either its dp[x] or we break it down to c and dp[x-c] which we have solved before since its smaller than x.

Comments: 
- Struggled a lot. 

Time Complexity: O(amount * coins.length)
Space Complexity: O(amount)
*/




class Solution {
    public:
        int coinChange(vector<int>& coins, int amount) {
            vector<int> dp(amount + 1, amount + 1);
            dp[0] = 0;
            for(int x = 1; x <= amount; x++){
                for(int c : coins){
                    if(x-c>=0){
                        dp[x] = min(dp[x] , dp[x-c] + 1);
                    }
                }
            }
            if(dp[amount] != amount+1){
                return dp[amount];
            }
            else{
                return -1;
            }
        }
    };
    
