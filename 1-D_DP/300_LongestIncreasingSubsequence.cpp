/*
Problem: Longest Increasing Subsequence
LeetCode: https://leetcode.com/problems/longest-increasing-subsequence/description/
Topic: Dynamic Programming, Array, Binary Search
Difficulty: Medium  

Approach:
- Use dynamic programming where dp[i] represents the length of the longest increasing subsequence ending at index i
- Initialize all dp[i] = 1 (each element is a subsequence of length 1)
- For each element at index i, check all previous elements j (0 to i-1)
- If nums[j] < nums[i], update dp[i] = max(dp[i], dp[j] + 1)
- Return the maximum value in the dp array

Time Complexity: O(n^2)
Space Complexity: O(n)
*/



class Solution {
    public:
        int lengthOfLIS(vector<int>& nums) {
            vector<int> LIS(nums.size(), 1);
            for(int i = nums.size()-1; i>= 0; i--){
                for(int j = i+1; j < nums.size(); j++){
                    if(nums[i]<nums[j]){
                        LIS[i] = max(LIS[i], 1+LIS[j]);
                    }
                }
            }
            return *max_element(LIS.begin(), LIS.end());
        }
    };
