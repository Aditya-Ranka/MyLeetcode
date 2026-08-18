"""
Problem: Subarrays with K Different Integers
LeetCode: https://leetcode.com/problems/subarrays-with-k-different-integers/
Topic: Sliding Window / Two Pointer
Difficulty: Hard

Approach:
- Define helper to count subarrays with at most x distinct
- Iterate right pointer, update frequency map
- Shrink left pointer while distinct count exceeds x
- Add (r-l+1) to result for each right

Comments:
- Handles x<0 by returning 0, so k=0 yields 0
- Uses O(k) extra space for the hashmap

Time Complexity: O(n)
Space Complexity: O(k)
"""

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def helper(x):
            if x<0:
                return 0
            res = 0
            l = 0
            count = {}
            for r, num in enumerate(nums):
                count[num] = count.get(num, 0) + 1
                while (len(count)) > x:
                    count[nums[l]] -= 1
                    if (count[nums[l]] == 0):
                        del count[nums[l]]
                    l+=1
                res+=(r-l+1)
            return res
        return helper(k) - helper(k-1)
