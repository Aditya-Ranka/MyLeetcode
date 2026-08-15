"""
Problem: Majority Element II
LeetCode: https://leetcode.com/problems/majority-element-ii/
Topic: Arrays
Difficulty: Medium

Approach:
- Extended Boyer-Moore for > n/3 elements: at most two can qualify, so track two candidates and two counts.
- Run the usual vote update, then a verification pass (nums.count) confirms each candidate actually exceeds n/3.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1, cand2 = None, None
        cnt1, cnt2 = 0,0
        for num in nums:
            if cand1 == num:
                cnt1+=1
            elif cand2 == num:
                cnt2+=1
            elif cnt1 == 0:
                cand1, cnt1 = num, 1
            elif cnt2 == 0:
                cand2, cnt2 = num, 1
            else:
                cnt1-=1
                cnt2-=1
        lim = len(nums)//3
        if nums.count(cand1) <= lim:
            cand1 = None
        if nums.count(cand2) <= lim:
            cand2 = None
        res = []
        if cand1 is not None:
            res.append(cand1)
        if cand2 is not None:
            res.append(cand2)
        return res
