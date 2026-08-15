"""
Problem: Sort Colors
LeetCode: https://leetcode.com/problems/sort-colors/
Topic: Arrays
Difficulty: Medium

Approach:
- Counting sort over the three values: count how many 0s, 1s, 2s.
- Overwrite the array in place: the 0s, then the 1s, then the 2s.

Comments:
- Two-pass counting; the one-pass Dutch National Flag (three pointers) also works.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x = 0
        y = 0
        z = 0
        for num in nums:
            if num == 0:
                x+=1
            if num == 1:
                y+=1
            if num == 2:
                z+=1
        for i in range(x):
            nums[i] = 0
        for i in range(x, x+y):
            nums[i] = 1
        for i in range(x+y, x+y+z):
            nums[i] = 2
