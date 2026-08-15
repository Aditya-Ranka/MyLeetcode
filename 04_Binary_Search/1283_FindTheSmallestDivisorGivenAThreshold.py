"""
Problem: Find the Smallest Divisor Given a Threshold
LeetCode: https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/
Topic: Binary Search
Difficulty: Medium

Approach:
- Binary search on the divisor, range [1, max(nums)].
- For divisor m the cost is sum(ceil(num/m)); feasible when <= threshold.
- Feasible -> try a smaller divisor; else larger. l is the smallest divisor meeting the threshold.

Time Complexity: O(n log(max))
Space Complexity: O(1)
"""

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def smallerThanThreshold(m):
            asum = 0
            for num in nums:
                asum+= ceil(num/m)
            if asum <= threshold: #go left
                return True
            else:
                return False
        l,r = 1, max(nums) + 1
        while l <= r:
            m = (l+r)//2
            if smallerThanThreshold(m) == True:
                r = m - 1
            else:
                l = m+1
        return l
