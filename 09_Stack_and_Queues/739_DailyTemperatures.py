"""
Problem: Daily Temperatures
LeetCode: https://leetcode.com/problems/daily-temperatures/
Topic: Stack and Queues
Difficulty: Medium

Approach:
- Initialize empty stack and result array of zeros
- Iterate over each index i in temperatures
- While stack not empty and temperatures[i] > temperatures[stack[-1]], pop index and set res[index]=i-index
- Push i onto stack
- Return the result array

Comments:
- Works for empty or single‑element input; uses a monotonic decreasing stack to ensure each index is processed at most once

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stck = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stck and temperatures[stck[-1]] < temperatures[i]:
                ind = stck.pop()
                res[ind] = i - ind
            stck.append(i)
        return res
