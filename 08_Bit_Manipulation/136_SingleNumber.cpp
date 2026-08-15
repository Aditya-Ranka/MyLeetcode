/*
Problem: Single Number
LeetCode: https://leetcode.com/problems/single-number/description/
Topic: Array, Bit Manipulation
Difficulty: Easy  

Approach:
- Use XOR bitwise operation to find the single number
- XOR properties: a ^ a = 0, a ^ 0 = a, XOR is commutative and associative
- Since all numbers appear twice except one, XORing all numbers will cancel out pairs
- The result will be the single number that appears only once

Time Complexity: O(n)
Space Complexity: O(1)
*/




class Solution {
    public:
        int singleNumber(vector<int>& nums) {
            int result = 0;
            for (int a: nums){
                result ^= a;
            }
            return result;
        }
    };
    
