/*
Problem: Reverse Bits
LeetCode: https://leetcode.com/problems/reverse-bits/description/
Topic: Bit Manipulation
Difficulty: Easy  

Approach:
- Iterate through all 32 bits of the input number
- Extract the least significant bit using (n & 1)
- Shift the result left and add the extracted bit
- Shift the input right to process the next bit
- Continue for all 32 bits to reverse the entire number

Time Complexity: O(1) - always 32 iterations
Space Complexity: O(1)
*/


class Solution {
    public:
        int reverseBits(int n) {
            int res = 0;
            for (int i = 0; i < 32; i++){
                res = res << 1;
                res = res ^ (n&1);
                n = n>>1;
            }
            return res;
        }
    };
