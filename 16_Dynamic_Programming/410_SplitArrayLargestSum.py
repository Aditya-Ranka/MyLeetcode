"""
Problem: Split Array Largest Sum
LeetCode: https://leetcode.com/problems/split-array-largest-sum/
Topic: Dynamic Programming
Difficulty: Hard

Approach:
- Define a helper function willItWork to check if it's possible to split the array into k subarrays with a maximum sum of m
- Initialize the search range with the minimum possible sum (max(nums)) and the maximum possible sum (sum(nums))
- Perform binary search to find the minimum maximum sum
- Update the search range based on the result of willItWork
- Return the minimum maximum sum found

Comments:
- The willItWork function uses a greedy approach to try to split the array into k subarrays with a maximum sum of m
- The binary search approach is used to find the minimum maximum sum, which reduces the time complexity

Time Complexity: O(n log sum)
Space Complexity: O(1)
"""

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def willItWork(m):
            number = k-1
            
            currSum = nums[0]
            i = 1
            for i in range(1,len(nums)):
                
                if nums[i] + currSum <= m:
                    currSum+=nums[i]
                    i+=1
                else:
                    currSum = nums[i]
                    number-=1
            if number >= 0:
                return True
            return False
        
        l = max(nums)
        r = sum(nums)
        while l <=r:
            m = (l+r)//2
            res = willItWork(m)
            if res:
                r = m-1
            else:
                l = m+1
        return l
