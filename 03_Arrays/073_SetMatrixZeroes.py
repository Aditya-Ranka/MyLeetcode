"""
Problem: Set Matrix Zeroes
LeetCode: https://leetcode.com/problems/set-matrix-zeroes/
Topic: Arrays
Difficulty: Medium

Approach:
- First pass records which rows and columns contain a 0 into two sets.
- Second pass zeroes any cell whose row or column was marked.
- Two passes avoid a freshly written 0 cascading into more zeros.

Comments:
- O(m+n) extra space; the O(1) version reuses the first row/column as markers.

Time Complexity: O(m*n)
Space Complexity: O(m+n)
"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        rows, cols = set(), set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for i in range(m):
            for j in range(n):
                if i in rows or j in cols:
                    matrix[i][j] = 0
