"""
Problem: Permutations
LeetCode: https://leetcode.com/problems/permutations/
Topic: Arrays
Difficulty: Medium

Approach:
- Return a single‑element list when nums length is 1
- Iterate over positions by popping the first element with pop(0)
- Recursively permute the remaining list
- Append the popped element to each returned permutation
- Extend the result list and push the element back to restore nums

Comments:
- Using pop(0) shifts the whole list, adding an O(k) cost at each recursion level, so the practical runtime is higher than the theoretical O(n·n!)
- The function does not handle an empty input list; it returns [] instead of the expected [[]]

Time Complexity: O(n·n!)
Space Complexity: O(n·n!)
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) == 1:
            return [nums.copy()]
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)
        return res
