"""
Problem: Merge Intervals
LeetCode: https://leetcode.com/problems/merge-intervals/
Topic: Arrays
Difficulty: Medium

Approach:
- Sort intervals by start.
- If the current interval starts within the last merged one (st <= res[-1][1]), extend its end to max(end, current end).
- Otherwise it's disjoint -> append as a new interval.

Time Complexity: O(n log n)
Space Complexity: O(n) output
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        res = [intervals[0]]

        for st,end in intervals:
            if st <= res[-1][1]:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([st,end])
        return res
