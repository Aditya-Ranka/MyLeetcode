"""
Problem: Valid Sudoku
LeetCode: https://leetcode.com/problems/valid-sudoku/
Topic: Arrays
Difficulty: Medium

Approach:
- Track seen digits per row, per column, and per 3x3 box with hash sets (box keyed by (i//3, j//3)).
- Skip '.' cells; for a filled cell, it's invalid if the value already appears in its row/col/box set.
- Otherwise add it to all three sets.

Time Complexity: O(1) (fixed 9x9 board)
Space Complexity: O(1)
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(9):
            for j in range(9):
                v = board[i][j]
                if v == ".":
                    continue
                if v in rows[i] or v in cols[j] or v in boxes[(i//3, j//3)]:
                    return False
                rows[i].add(v)
                cols[j].add(v)
                boxes[(i//3, j//3)].add(v)
        return True
