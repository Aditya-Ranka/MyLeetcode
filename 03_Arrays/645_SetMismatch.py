"""
Problem: Set Mismatch
LeetCode: https://leetcode.com/problems/set-mismatch/
Topic: Arrays
Difficulty: Easy

Approach:
- One pass with a set finds the duplicated number y and the running total.
- Missing z = ideal_sum(1..n) + y - actual_total (adding y back cancels the duplicate's double count).
- Return [duplicate, missing].

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        x = set()
        y = None
        total = 0
        for num in nums: 
            total += num
            if num in x:
                y = num
            else:
                x.add(num)
        n = len(nums)
        ideal = (n*(n+1))//2
        z = ideal +y - total
        return [y,z]
