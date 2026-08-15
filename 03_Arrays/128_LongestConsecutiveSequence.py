"""
Problem: Longest Consecutive Sequence
LeetCode: https://leetcode.com/problems/longest-consecutive-sequence/
Topic: Arrays
Difficulty: Medium

Approach:
- Put all numbers in a set for O(1) lookup.
- Only start counting a run at a number whose predecessor (num-1) is absent -> a sequence start.
- Extend while num+length is in the set; track the best length.
- Each number is touched at most twice, so it's O(n).

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        best = 0
        
        for num in s:
            if num-1 not in s:
                length = 1
                while num+length in s:
                    length+=1
                    
                best = max(best,length)

        return best
