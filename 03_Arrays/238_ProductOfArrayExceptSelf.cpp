/*
Problem: Product of Array Except Self
LeetCode: https://leetcode.com/problems/product-of-array-except-self/description/
Topic: Arrays
Difficulty: Medium

Approach:
- creating a vector of size n and initializing it with 1
- by doing vector<int> output(n, 1);
- then we iterate through the array and for each element we multiply the element by the product of all the elements to the left of the current element.
- then we iterate through the array and for each element we multiply the element by the product of all the elements to the right of the current element.
- then we return the output vector.

- nums = [1,2,3,4] → prefix: [1,1,2,6]
- suffix pass: multiply by [24,12,4,1]
- result = [24,12,8,6]



Time Complexity: O(2n) = O(n)
Space Complexity: O(1)
*/


class Solution {
    public:
        vector<int> productExceptSelf(vector<int>& nums) {
            int n = nums.size();
            vector<int> output(n, 1);
            int prefix = 1;
            
            for(int i = 0; i < n; i++){
                output[i] = prefix;
                prefix = prefix * nums[i];
            }
            prefix = 1;
            for(int i = n-1; i >= 0; i--){
                output[i] = output[i] * prefix;
                prefix *= nums[i];
            }
            return output;
        }
    };
