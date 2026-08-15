"""
Problem: Median of Two Sorted Arrays
LeetCode: https://leetcode.com/problems/median-of-two-sorted-arrays/
Topic: Binary Search
Difficulty: Hard

Approach:
- Binary search the partition point, always on the SMALLER array, so it runs in O(log(min(m,n))).
- For a cut m in nums1 and n = (a+b)//2 - m in nums2, compute the 4 border values left1/right1/left2/right2 with -inf/+inf sentinels at the edges.
- A partition is valid when left1 <= right2 and left2 <= right1.
- Even total -> average of max(lefts) and min(rights); odd total -> min(rights).
- If left1 > right2 move the cut left, else move it right.

Comments:
- `flag` distinguishes even vs odd total length.

Time Complexity: O(log(min(m, n)))
Space Complexity: O(1)
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        a = len(nums1)
        b = len(nums2)
        p = a+b
        q = p//2
        if p%2 == 0:
            flag = 0
        else:
            flag = 1
        l = 0
        r = a
        while l <= r:
            m = (l+r)//2
            n = q-m
            left1  = nums1[m - 1] if m > 0 else float('-inf')
            right1 = nums1[m]     if m < a else float('inf')
            left2  = nums2[n - 1] if n > 0 else float('-inf')
            right2 = nums2[n]     if n < b else float('inf')

            if left1 <= right2 and left2 <= right1:
                if flag == 0 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                return min(right1, right2)
            elif left1 > right2:
                r = m - 1
            else:
                l = m + 1
                continue
        return -1
