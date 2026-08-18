"""
Problem: Count Number of Nice Subarrays
LeetCode: https://leetcode.com/problems/count-number-of-nice-subarrays/
Topic: Sliding Window / Two Pointer
Difficulty: Medium

Approach:
- Define helper atMost(x) to count subarrays with ≤x odd numbers using sliding window
- Iterate right pointer over nums, increment oddCount on odd elements
- While oddCount exceeds x, move left pointer and decrement oddCount when passing an odd
- Add current window length (r-l+1) to result for each r
- Return atMost(k)-atMost(k-1) to get exactly k odds

Comments:
- Handles k=0 by returning 0 for atMost(-1)
- Uses O(1) extra space

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMost(x):
            if x < 0:
                return 0
            l = 0
            oddCount = 0
            res = 0
            for r in range(len(nums)):
                if nums[r] % 2 == 1:
                    oddCount += 1
                while oddCount > x:
                    if nums[l] % 2 == 1:
                        oddCount -= 1
                    l += 1
                res += (r - l + 1)
            return res

        return atMost(k) - atMost(k - 1)
