"""
Problem: Find Peak Element
LeetCode: https://leetcode.com/problems/find-peak-element/
Topic: Binary Search
Difficulty: Medium

Approach:
- Binary search on the slope; a peak is guaranteed by the nums[-1]=nums[n]=-inf framing.
- Handle both ends up front (strictly greater than the lone neighbor => peak).
- If the left neighbor is larger, a peak exists to the left (r=m); if the right neighbor is larger, one exists to the right (l=m); if both neighbors are smaller, mid is a peak.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        if l==r:
            return l
        if(nums[l] > nums[l+1]):
            return l
        if(nums[r] > nums[r-1]):
            return r
        while True:
            m = (l+r)//2
            ml = m-1
            mr = m+1
            
            if nums[ml] < nums[m] and nums[mr] < nums[m]:
                return m
            
            if nums[ml] > nums[m]:
                r = m
                continue
            if nums[mr] > nums[m]:
                l = m
                continue
