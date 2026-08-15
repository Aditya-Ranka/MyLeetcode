"""
Problem: Capacity To Ship Packages Within D Days
LeetCode: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
Topic: Binary Search
Difficulty: Medium

Approach:
- Binary search on ship capacity, range [max(weight), sum(weights)].
- willItCarry simulates loading day by day for a candidate capacity and reports whether it fits within `days`.
- Feasible -> shrink capacity; else grow. l is the minimum feasible capacity.

Time Complexity: O(n log(sum))
Space Complexity: O(1)
"""

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def willItCarry(m):
            countOfDays = 1
            currWt = 0
            for wt in weights:
                if currWt + wt <= m:
                    currWt += wt
                    continue
                else: 
                    countOfDays+=1
                    currWt = wt
            if countOfDays <= days: # go left
                return -1
            if countOfDays > days:
                return 1 #go right
            
            
        l,r = max(weights), sum(weights)
        while l <= r:
            m = (l+r)//2
            res = willItCarry(m)
            
            if res == -1:
                r = m - 1
                continue
            if res == 1:
                l = m + 1
                continue
        return l
