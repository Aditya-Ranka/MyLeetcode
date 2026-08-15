/*
Problem: Maximum Product Subarray
LeetCode: https://leetcode.com/problems/maximum-product-subarray/description/
Topic: Dynamic Programming, Array
Difficulty: Medium  

Approach:
- Use dynamic programming tracking both max and min product ending at each position
- Since negative numbers can flip min to max, we need to track both
- For each element, update currMax and currMin considering:
  - Multiplying current element with previous max
  - Multiplying current element with previous min
  - Starting fresh with current element
- Reset to 1 when encountering 0
- Keep track of global maximum throughout

Time Complexity: O(n)
Space Complexity: O(1)
*/





class Solution {
    public:
        int maxProduct(vector<int>& nums) {
            int max = nums[0];
            for(int i = 0; i < nums.size(); i++){
                if (nums[i] > max){
                    max = nums[i];
                }
            }
            int currMin = 1;
            int currMax = 1;
            for(int i = 0; i < nums.size(); i++){
                if(nums[i] == 0){
                    currMin, currMax = 1, 1;
                }
                int temp = currMax;
                currMax = std::max({currMax*nums[i], currMin*nums[i], nums[i]});
                currMin = std::min({temp*nums[i], currMin*nums[i], nums[i]});
                max = std::max(currMax, max);
            }
            return max;
        }
    };
