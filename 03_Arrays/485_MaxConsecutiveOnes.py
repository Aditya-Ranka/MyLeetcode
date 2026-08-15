"""
Problem: Max Consecutive Ones
LeetCode: https://leetcode.com/problems/max-consecutive-ones/
Topic: Arrays
Difficulty: Easy

Approach:
- Single-pass counter: +1 on a 1 and track the max; reset to 0 on any non-1.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxC = 0
        for num in nums:
            if num != 1:
                count = 0
            else:
                count+=1
                maxC = max(maxC, count)

        return maxC
