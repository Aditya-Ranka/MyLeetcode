"""
Problem: Next Greater Element II
LeetCode: https://leetcode.com/problems/next-greater-element-ii/
Topic: Stack and Queues
Difficulty: Medium

Approach:
- Initialize result with -1 and an empty stack
- Iterate i from 0 to 2*n-1 treating the array as circular via nums[i%n]
- While the stack is non‑empty and nums[stack[-1]]<cur, pop index and set its result to cur
- Push i onto the stack only when i<n (first pass)
- Return the populated result list

Comments:
- Only indices from the first traversal are stored, so each element is considered exactly once as a candidate
- Strictly less comparison means equal values are not treated as greater, leaving -1 when no larger element exists

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []

        for i in range(2 * n):
            cur = nums[i % n]
            while stack and nums[stack[-1]] < cur:
                res[stack.pop()] = cur
            if i < n:
                stack.append(i)

        return res
