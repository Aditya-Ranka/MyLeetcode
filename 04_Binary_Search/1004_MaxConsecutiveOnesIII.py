"""
Problem: Max Consecutive Ones III
LeetCode: https://leetcode.com/problems/max-consecutive-ones-iii/
Topic: Binary Search
Difficulty: Medium

Approach:
- Initialize a sliding window with two pointers, l and r
- Expand the window to the right and count zeros
- Shrink the window from the left when zeros exceed k
- Update the maximum length of consecutive ones

Comments:
- The key insight is to maintain a window where the number of zeros does not exceed k
- This allows us to efficiently find the longest subarray with at most k zeros

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        zeros = 0
        best = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zeros += 1
            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            best = max(best, r - l + 1)
        return best
