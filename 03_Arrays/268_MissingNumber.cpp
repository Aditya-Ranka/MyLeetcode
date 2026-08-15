/*
Problem: Missing Number
LeetCode: https://leetcode.com/problems/missing-number/description/
Topic: Array, Math, Bit Manipulation
Difficulty: Easy  

Approach:
- Calculate the sum of all numbers from 0 to n (expected sum)
- Calculate the sum of all numbers in the array (actual sum)
- The missing number is the difference between expected and actual sum
- Alternative approach: Use XOR to find the missing number (commented out)

Time Complexity: O(n)
Space Complexity: O(1)
*/





class Solution {
    public:
        int missingNumber(vector<int>& nums) {
            /*int res = 0;
            for (int i = 0; i <= nums.size(); i++){
                res = res ^ i;
            }
            for(int i = 0; i < nums.size(); i++){
                res = res ^ nums[i];
            }
            return res;*/
    
            int sum1 = 0;
            int sum2 = 0;
            for (int i = 0; i <= nums.size(); i++){
                sum1 = sum1 + i;
            }
            for (int i = 0; i < nums.size(); i++){
                sum2 = sum2+nums[i];
            }
            int x = sum1-sum2;
            return x;
        }
    };
