"""
Problem: Surrounded Regions
LeetCode: https://leetcode.com/problems/surrounded-regions/
Topic: Arrays
Difficulty: Medium

Approach:
- Check for empty board
- Mark all border 'O's as safe and enqueue them
- BFS from queue, converting connected 'O's to safe
- Flip remaining 'O's to 'X' and revert safe markers to 'O'

Comments:
- Uses a temporary marker 'S' to avoid revisiting cells
- Queue may grow to O(m*n) in worst case

Time Complexity: O(m*n)
Space Complexity: O(m*n)
"""

from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """Do not return anything, modify board in-place instead."""
        if not board or not board[0]:
            return
        rows, cols = len(board), len(board[0])
        q = deque()
        for r in range(rows):
            for c in (0, cols - 1):
                if board[r][c] == "O":
                    q.append((r, c))
                    board[r][c] = "S"
        for c in range(cols):
            for r in (0, rows - 1):
                if board[r][c] == "O":
                    q.append((r, c))
                    board[r][c] = "S"

        while q:
            r, c = q.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O":
                    board[nr][nc] = "S"
                    q.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                board[r][c] = "O" if board[r][c] == "S" else "X"
