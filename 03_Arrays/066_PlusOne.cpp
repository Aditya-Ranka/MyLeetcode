/*
Problem: Plus One
LeetCode: https://leetcode.com/problems/plus-one/description/
Topic: Array, Math
Difficulty: Easy  

Approach:
- Start from the rightmost digit (least significant)
- Add 1 to the current digit
- If the digit becomes 10, set it to 0 and carry over 1 to the next digit
- If no carry remains, return the result
- If all digits were 9, we need to add a new digit 1 at the beginning

Time Complexity: O(n)
Space Complexity: O(1) - excluding output array
*/


class Solution {
    public:
        vector<int> plusOne(vector<int>& digits) {
            
    
        for (int i = digits.size() - 1; i >= 0; i--) {
            digits[i]++;
            if (digits[i] < 10) return digits;
            digits[i] = 0;
        }
        digits.insert(digits.begin(), 1);
        return digits;
    }
};
