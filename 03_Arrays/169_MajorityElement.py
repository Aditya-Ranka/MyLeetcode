"""
Problem: Majority Element
LeetCode: https://leetcode.com/problems/majority-element/
Topic: Arrays
Difficulty: Easy

Approach:
- Boyer-Moore voting: keep a candidate and a count.
- When count hits 0, adopt the current number; +1 when it matches the candidate, -1 otherwise.
- The > n/2 element survives as the candidate.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cand, count = None, 0
        for num in nums:
            if count ==0:
                cand = num
            if num == cand:
                count+=1
            else:
                count-=1
        return cand
