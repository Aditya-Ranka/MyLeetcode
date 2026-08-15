"""
Problem: Rotate Image
LeetCode: https://leetcode.com/problems/rotate-image/
Topic: Arrays
Difficulty: Medium

Approach:
- Rotate 90 degrees clockwise via a helper matrix.
- Build the transpose: m1[j][i] = matrix[i][j].
- Write back reversing each row: matrix[i][j] = m1[i][n-1-j].

Comments:
- Uses O(n^2) extra space; the in-place transpose + row-reverse variant is O(1).

Time Complexity: O(n^2)
Space Complexity: O(n^2)
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        m1 = [[0] * n for _ in range(n)] 
        for i in range(n):
            for j in range(n):
                m1[j][i] = matrix[i][j]

        for i in range(n):
            for j in range(n):
                matrix[i][j] = m1[i][n-j-1]
