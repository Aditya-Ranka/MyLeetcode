"""
Problem: Single Element in a Sorted Array
LeetCode: https://leetcode.com/problems/single-element-in-a-sorted-array/
Topic: Binary Search
Difficulty: Medium

Approach:
- Binary search on index parity: in a fully paired sorted array, pairs start at even indices; the single element breaks that parity.
- Use the segment sizes around mid to decide which half still pairs evenly and move toward the half where the parity is broken.

Comments:
- The code special-cases the small windows right around mid explicitly.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l,r = 0, len(nums) - 1
        while True:
            if l==r:
                return nums[r]
            m = (l+r)//2
            if nums[m] != nums[m+1] and nums[m]!= nums[m-1]:
                return nums[m]
            if nums[m] == nums[m-1] and m!=0:
                m-=1
            if m-l <= 1 and m!=l:
                return nums[l]
            if r-m <= 2 and r!=m:
                return nums[r]
            x = m-l
            y = r-m-1
            if y%2 == 0:
                r = m-1
                continue
            if x%2== 0:
                l = m+2
                continue
