"""
Problem: 4Sum
LeetCode: https://leetcode.com/problems/4sum/
Topic: Arrays
Difficulty: Medium

Approach:
- Generalized kSum by recursion: sort, then recursively fix one index at a time until k == 2.
- `quad` holds the currently fixed numbers; skip duplicates at each level to avoid repeated results.
- Base case k == 2 is a two-pointer scan from both ends toward the remaining target, skipping duplicate left values after a hit.

Time Complexity: O(n^3)
Space Complexity: O(n) recursion depth + output
"""

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        quad = []
        res = []
        nums.sort()
        def Ksum(k, start, target):
            if k!=2:
                for i in range(start, len(nums) - k + 1,1):
                    if i > start and nums[i] == nums[i-1]:
                        continue
                    quad.append(nums[i])
                    Ksum(k-1, i+1, target - nums[i])
                    quad.pop()
                return
            else:
                l,r = start, len(nums) - 1
                
                while l < r:
                    csum = nums[l] + nums[r]
                    if csum > target:
                        r-=1
                    elif csum < target:
                        l+=1
                    elif csum == target:
                        res.append(quad + [nums[l] , nums[r]])
                        l+=1
                        while l < r and nums[l] == nums[l-1]:
                            l+=1
        Ksum(4,0,target)
        return res
