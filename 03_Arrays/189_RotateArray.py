"""
Problem: Rotate Array
LeetCode: https://leetcode.com/problems/rotate-array/
Topic: Arrays
Difficulty: Medium

Approach:
- k %= n so rotations wrap.
- Stash the last k elements, shift the first n-k elements right by k (iterate from the back to avoid overwrite), then drop the stashed elements into the front.

Comments:
- O(k) extra; the triple-reverse trick does it in O(1) space.

Time Complexity: O(n)
Space Complexity: O(k)
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        temp = []
        for i in range(n-k, n):
            temp.append(nums[i])
        for i in range(n-1,k-1,-1):
            nums[i] = nums[i-k]
        for i in range(k):
            nums[i] = temp[i]
