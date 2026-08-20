"""
Problem: Search a 2D Matrix II
LeetCode: https://leetcode.com/problems/search-a-2d-matrix-ii/
Topic: Binary Search
Difficulty: Medium

Approach:
- Determine the number of rows (m) and columns (n) of the matrix.
- Iterate over each row index i from 0 to m-1.
- If the first element of the current row exceeds the target, return False immediately (no later rows can contain the target).
- Otherwise, run a binary search on the current row between column indices l and r.
- If the target is found during the binary search, return True.

Comments:
- The function may fall off the end without an explicit return, implicitly returning None instead of False when the target is not found.
- It assumes the matrix is non‑empty; calling it on an empty matrix would raise an IndexError.

Time Complexity: O(m log n)
Space Complexity: O(1)
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            if matrix[i][0] > target:
                return False
            l = 0
            r = n-1
            while l <= r and r < n:
                mid = (l+r)//2
                if matrix[i][mid] == target:
                    return True
                if matrix[i][mid] < target:
                    l = mid+1
                elif matrix[i][mid] > target:
                    r = mid - 1
