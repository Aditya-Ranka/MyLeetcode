"""
Problem: Subsets
LeetCode: https://leetcode.com/problems/subsets/
Topic: Bit Manipulation
Difficulty: Medium

Approach:
- Initialize empty result list and a temporary current list
- Define dfs(i) that recurses on index i
- If i reaches len(nums), copy current list into result
- Otherwise, include nums[i] and recurse, then backtrack and exclude nums[i] and recurse
- Start dfs from index 0 and return the accumulated result

Comments:
- Uses curr.copy() to capture each subset without later mutation
- Recursion depth is at most n, producing subsets in inclusion‑first order

Time Complexity: O(2^n)
Space Complexity: O(n)
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        def dfs(i):
            if i >= len(nums):
                res.append(curr.copy())
                return
            curr.append(nums[i])
            dfs(i+1)
            curr.pop()
            dfs(i+1)

        dfs(0)
        return res
