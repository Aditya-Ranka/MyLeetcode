"""
Problem: Spiral Matrix
LeetCode: https://leetcode.com/problems/spiral-matrix/
Topic: Arrays
Difficulty: Medium

Approach:
- Keep four shrinking boundaries: left, right, top, bottom.
- Each layer: top row L->R (top++), right column T->B (right--), guard-check, bottom row R->L (bottom--), left column B->T (left++).
- The inner guard `if not (left<right and top<bottom): break` avoids re-reading a middle row/column on odd sizes.

Time Complexity: O(m*n)
Space Complexity: O(1) extra
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        res = []
        while left < right and top < bottom:
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            right -= 1
            if not (left < right and top < bottom):
                break
            for i in range(right -1, left -1, -1):
                res.append(matrix[bottom-1][i])
            bottom -= 1
            for i in range(bottom-1, top-1, -1):
                res.append(matrix[i][left])
            left += 1
            
        return res
