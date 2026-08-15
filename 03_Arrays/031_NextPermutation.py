"""
Problem: Next Permutation
LeetCode: https://leetcode.com/problems/next-permutation/
Topic: Arrays
Difficulty: Medium

Approach:
- Scan from the right for the first i with nums[i] < nums[i+1] (the pivot).
- If a pivot exists, find the rightmost j > i with nums[j] > nums[i] and swap them.
- Reverse the suffix after i so it becomes ascending (smallest arrangement) -> the next permutation.
- No pivot means it's the last permutation; reversing the whole array wraps to the first.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        i = n-2
        while i >= 0 and nums[i] >= nums[i+1]:
            i-=1
        if(i>=0):
            j = n-1
            while j > i and nums[j] <= nums[i]:
                j-=1
            temp = nums[j]
            nums[j] = nums[i]
            nums[i] = temp
        nums[i+1:] = reversed(nums[i+1:])
        return nums
