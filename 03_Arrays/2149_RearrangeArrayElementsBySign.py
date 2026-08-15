"""
Problem: Rearrange Array Elements by Sign
LeetCode: https://leetcode.com/problems/rearrange-array-elements-by-sign/
Topic: Arrays
Difficulty: Medium

Approach:
- Result array with two write pointers: positives to even indices (0,2,4,...), negatives to odd indices (1,3,5,...).
- Single pass preserves relative order within each sign.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        p, q = 0, 1
        for num in nums:
            if num > 0:
                res[p] = num
                p += 2
            else:
                res[q] = num
                q += 2
        return res
