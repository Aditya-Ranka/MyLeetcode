"""
Problem: Power of Two
LeetCode: https://leetcode.com/problems/power-of-two/
Topic: Bit Manipulation
Difficulty: Easy

Approach:
- Return False if n is non‑positive
- Loop while n>1, compute n%2
- If remainder not zero, return False
- Divide n by 2 using /= operator
- After loop, return True

Comments:
- Uses '/' causing n to become float, which may introduce precision issues for large numbers

Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0: return False
        while n > 1:
            x = n%2
            if x != 0:
                return False
            n /= 2
        return True
