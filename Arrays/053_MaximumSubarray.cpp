/*
Problem: Maximum Subarray
LeetCode: https://leetcode.com/problems/maximum-subarray/description/
Topic: Array, Divide and Conquer, Dynamic Programming
Difficulty: Medium  

Approach:
- Use Kadane's algorithm (dynamic programming approach)
- Keep track of the maximum sum ending at current position
- At each position, decide whether to extend the previous subarray or start a new one
- Update the global maximum whenever we find a larger sum
- If current sum becomes negative, reset it to 0 (starting fresh)

Time Complexity: O(n)
Space Complexity: O(1)
*/


class Solution {
    public:
        int maxSubArray(vector<int>& nums) {
            int currSum = 0;
            int maxSum = nums[0];
            for (int i = 0; i < nums.size(); i++){
                if(currSum < 0){
                    currSum = 0;
                }
                currSum += nums[i];
                if(maxSum < currSum){
                    maxSum = currSum;
                }
            }
            return maxSum;
        }
    };
