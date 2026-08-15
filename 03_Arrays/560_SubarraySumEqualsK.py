"""
Problem: Subarray Sum Equals K
LeetCode: https://leetcode.com/problems/subarray-sum-equals-k/
Topic: Arrays
Difficulty: Medium

Approach:
- Prefix sum + hash map of prefix-sum frequencies, seeded with {0:1}.
- For running prefix p, the number of subarrays ending here with sum k is how many times (p-k) has appeared.
- Add that to the answer, then record p.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        count = {0:1}
        p = 0
        for num in nums:
            p += num
            res += count.get(p-k, 0)
            if p in count:
                count[p] += 1
            else:
                count[p] = 1
        return res
