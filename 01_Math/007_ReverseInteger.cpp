/*
Problem: Reverse Integer
LeetCode: https://leetcode.com/problems/reverse-integer/
Topic: Math
Difficulty: Medium

Approach:
- Pop digits off the end with %10 and rebuild the reversed number, x = x/10 each step.
- Before doing y = y*10 + t, check against INT_MAX/INT_MIN/10 bounds and bail out with 0 on overflow.
- Negatives work directly because C++ / and % keep the sign of the dividend.

Time Complexity: O(log10(x))
Space Complexity: O(1)
*/

class Solution {
public:
    int reverse(int x) {
        int y = 0;
        while(x!=0){
            int t = x%10;
            if (y > INT_MAX / 10 || (y == INT_MAX / 10 && t > 7)) return 0;
            if (y < INT_MIN / 10 || (y == INT_MIN / 10 && t < -8)) return 0;
            y = y*10+t;
            x = x/10;
        }
        return y;
    }
};
