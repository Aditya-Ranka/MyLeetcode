"""
Problem: Frequency of the Most Frequent Element
LeetCode: https://leetcode.com/problems/frequency-of-the-most-frequent-element/
Topic: Binary Search
Difficulty: Medium

Approach:
- Sort, then sliding window: making every element in the window equal to the largest (nums[r]) costs nums[r]*windowLen - windowSum.
- Grow r; while the cost exceeds k, shrink from the left.
- The largest valid window size is the answer.

Time Complexity: O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        maxF = 1
        currS = 0
        l = 0
        for r in range(len(nums)):
            currS += nums[r]
            while (nums[r]*(r-l+1) - currS > k):
                currS -= nums[l]
                l+=1
                
            maxF = max(maxF, r-l+1)
        return maxF
