/*
Problem: Number of 1 Bits
LeetCode: https://leetcode.com/problems/number-of-1-bits/description/
Topic: Bit Manipulation
Difficulty: Easy  

Approach:
- Count the number of set bits (1s) in the binary representation of n
- Use modulo and division to check each bit: if n % 2 == 1, increment count
- Right shift by dividing by 2 to process the next bit
- Continue until n becomes 0

Time Complexity: O(1) - at most 32 iterations for 32-bit integer
Space Complexity: O(1)
*/


class Solution {
public:
    int hammingWeight(int n) {
        int result;
        while(n != 0){
            if (n%2 == 1){
                result++;
            }
            n = n/2;
        }
        return result;
    }
};
