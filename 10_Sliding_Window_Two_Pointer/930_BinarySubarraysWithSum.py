"""
Problem: Binary Subarrays With Sum
LeetCode: https://leetcode.com/problems/binary-subarrays-with-sum/
Topic: Sliding Window / Two Pointer
Difficulty: Medium

Approach:
- Define helper findG(x) to count subarrays with sum ≤ x
- Initialize left pointer, current sum, and result
- Iterate right pointer, add nums[r] to current sum
- While current sum > x, move left pointer and subtract from sum
- Add (r-l+1) to result for each right position
- Return findG(goal)-findG(goal-1) as count of subarrays with sum exactly goal

Comments:
- Works only for non-negative (binary) arrays; handles goal=0 via early return
- Uses O(1) extra space

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def findG(x):
            if x < 0:
                return 0
            l = 0
            currSum = 0
            res = 0
            for r in range(len(nums)):
                currSum += nums[r]
                while currSum > x:
                    currSum -= nums[l]
                    l+=1
                res+=(r-l+1)
            return res
        
        return findG(goal) - findG(goal - 1)
