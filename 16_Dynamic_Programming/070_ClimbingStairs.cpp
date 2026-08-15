/*
Problem: Climbing Stairs
LeetCode: https://leetcode.com/problems/climbing-stairs/description/
Topic: Dynamic Programming, Math
Difficulty: Easy  

Approach:
- Use dynamic programming with Fibonacci-like recurrence relation
- For each step i, the number of ways to reach it is: dp[i] = dp[i-1] + dp[i-2]
- You can reach step i either from step i-1 (1 step) or step i-2 (2 steps)
- Can be optimized to use O(1) space by only tracking the last two values

Time Complexity: O(n)
Space Complexity: O(1) with optimization, O(n) with array
*/


class Solution {
    public:
        int climbStairs(int n) {
            if(n == 0){
                return 1;
            }
            if(n==1){
                return 1;
            }
            if(n==2){
                return 2;
            }
            int x = n;
            int count[n+1];
    
            count[0] = 0;
            count[1] = 1;
            count[2] = 2;
            for(int i = 3; i <= n; i++){
                count[i] = count[i-1] + count[i-2];
            }
            return count[x];
        }
    };
