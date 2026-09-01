"""
Problem: Pow(x, n)
LeetCode: https://leetcode.com/problems/powx-n/
Topic: Math
Difficulty: Medium

Approach:
- If n is negative, invert x and make n positive
- Recursively compute power for n//2 using helper
- Square the result of the recursive call
- If n is odd, multiply the squared result by x
- Return the final product

Comments:
- Uses recursion depth O(log n), which may hit Python recursion limit for extremely large exponents
- Floating‑point precision errors can accumulate for large |n|

Time Complexity: O(log n)
Space Complexity: O(log n)
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if n == 0:
                return 1
            half = helper(x, n // 2)
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x
        
        if n < 0:
            x = 1 / x
            n = -n
        return helper(x, n)
