"""
Problem: 01 Matrix
LeetCode: https://leetcode.com/problems/01-matrix/
Topic: Dynamic Programming
Difficulty: Medium

Approach:
- Initialize queue with all zero cells and mark others as -1
- Perform BFS expanding from zeros
- Set each unvisited neighbor to current distance+1 and enqueue it
- Repeat until queue is empty

Comments:
- In‑place modification uses -1 as unvisited marker
- Queue may hold up to O(m·n) cells in worst case

Time Complexity: O(m*n)
Space Complexity: O(m*n)
"""

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        q = collections.deque()
        directions = [[1,0], [0,1], [-1,0] , [0,-1]]
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    q.append((i,j))
                else:
                    mat[i][j] = -1
        while q:
            row,col = q.popleft()
            for dr,dc in directions:
                r = row + dr
                c = col + dc
                if r in range(rows) and c in range(cols) and mat[r][c] == -1:
                    q.append((r,c))
                    mat[r][c] = mat[row][col] + 1
        return mat
