"""
Problem: Find a Peak Element II
LeetCode: https://leetcode.com/problems/find-a-peak-element-ii/
Topic: Binary Search
Difficulty: Medium

Approach:
- Initialize rows m and columns n, set binary search bounds lo=0, hi=n-1 on columns
- While lo≤hi, pick mid column and scan all rows to find the row index best with the maximum value in that column
- Compare mat[best][mid] with its left and right neighbours (using -1 as sentinel when out of bounds)
- If the current element is greater than both neighbours, return its coordinates as a peak
- Otherwise move the binary search to the side that has the larger neighbour (left → hi=mid-1, right → lo=mid+1)

Comments:
- Using -1 as a sentinel for missing neighbours assumes matrix values are non‑negative; a true negative value could break the comparison
- The algorithm runs in O(m log n) time and O(1) extra space

Time Complexity: O(m log n)
Space Complexity: O(1)
"""

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        lo, hi = 0, n - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            best = 0
            for i in range(1, m):
                if mat[i][mid] > mat[best][mid]:
                    best = i

            cur   = mat[best][mid]
            left  = mat[best][mid - 1] if mid > 0     else -1
            right = mat[best][mid + 1] if mid < n - 1 else -1

            if cur > left and cur > right:
                return [best, mid]
            if left > cur:
                hi = mid - 1
            else:
                lo = mid + 1
