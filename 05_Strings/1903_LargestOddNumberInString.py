"""
Problem: Largest Odd Number in String
LeetCode: https://leetcode.com/problems/largest-odd-number-in-string/
Topic: Strings
Difficulty: Easy

Approach:
- Iterate while the string is non‑empty and its last digit is not odd
- If the last digit is even, drop the last character using slicing
- Return the resulting string (empty if no odd digit was found)

Comments:
- Slicing creates a new string each loop, leading to O(n^2) time in the worst case
- Handles empty input gracefully

Time Complexity: O(n^2)
Space Complexity: O(n)
"""

class Solution:
    def largestOddNumber(self, num: str) -> str:
        while num and int(num[-1])%2 != 1:
            num = num[:-1:1]
        return num
