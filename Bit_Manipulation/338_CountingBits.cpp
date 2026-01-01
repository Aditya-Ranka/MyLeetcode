/*
Problem: Counting Bits
LeetCode: https://leetcode.com/problems/counting-bits/description/
Topic: Dynamic Programming, Bit Manipulation
Difficulty: Easy  

Approach:
- Use dynamic programming with bit manipulation
- For each number i, the number of 1's can be found using: dp[i] = dp[i >> 1] + (i & 1)
- i >> 1 removes the least significant bit (same as i / 2)
- i & 1 checks if the least significant bit is 1
- This reuses previously computed results for smaller numbers

Time Complexity: O(n)
Space Complexity: O(n) for the output array
*/


class Solution {
    public:
        vector<int> countBits(int n) {
            vector<int> res(n+1,0);
            for(int i = 1; i<n+1 ; i++){
                res[i] = res[i>>1] + res[i & 1];
            }
            return res;
        }
    };


