/*
Problem: Sqrt(x)
LeetCode: https://leetcode.com/problems/sqrtx/
Topic: Binary Search
Difficulty: Easy

Approach:
- Binary search for the largest integer whose square does not exceed x, over the range [1, x/2].
- Use a long for mid*mid to avoid 32-bit overflow; return mid immediately on an exact square.
- If mid*mid < x, record mid as the best answer so far and search right; otherwise search left.
- x < 2 is handled directly (sqrt of 0 or 1 is x itself).

Time Complexity: O(log x)
Space Complexity: O(1)
*/

class Solution {
public:
    int mySqrt(int x) {
        if (x < 2) return x; 

        int left = 1, right = x / 2, ans = 0;

        while (left <= right) {
            long mid = left + (right - left) / 2;
            if (mid * mid == x) return mid;
            else if (mid * mid < x) {
                ans = mid;       
                left = mid + 1;  
            } else {
                right = mid - 1; 
            }
        }
        return ans;
    }
};
