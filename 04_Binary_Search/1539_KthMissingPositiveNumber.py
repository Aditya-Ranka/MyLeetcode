"""
Problem: Kth Missing Positive Number
LeetCode: https://leetcode.com/problems/kth-missing-positive-number/
Topic: Binary Search
Difficulty: Easy

Approach:
- Binary search: at index i, arr[i]-i-1 is how many positive integers are missing before arr[i].
- Find the boundary where the missing count first reaches k; the answer is l + k.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        def findMissing(i):
            return arr[i] - i - 1
        l, r = 0, len(arr) - 1
        while l <= r:
            m = (l+r)//2
            res = findMissing(m)
            if res < k:
                l = m+1
                continue
            else:
                r = m-1
                continue
        return l+k
