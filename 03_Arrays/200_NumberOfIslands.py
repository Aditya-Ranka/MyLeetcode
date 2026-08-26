"""
Problem: Number of Islands
LeetCode: https://leetcode.com/problems/number-of-islands/
Topic: Arrays
Difficulty: Medium

Approach:
- Iterate over each cell in the grid
- When an unvisited land cell ('1') is encountered, launch a BFS from it
- Use a deque to pop cells and push any adjacent land cells (up, down, left, right) that are inside bounds and not yet visited
- Mark every visited cell in a set to avoid re‑processing
- After the BFS empties, increment the island counter

Comments:
- Assumes grid is non‑empty; accessing grid[0] will raise on an empty list
- The inner loop reassigns the variables r and c, but this shadowing does not affect the outer loops

Time Complexity: O(m*n)
Space Complexity: O(m*n)
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        res = 0
        def dfs(r,c):
            directions = [[0,1] , [0,-1], [1,0], [-1,0]]
            q = collections.deque()
            q.append((r,c))
            visit.add((r,c))
            while q:
                row, col = q.popleft()
                for dr,dc in directions:
                    r = row+dr
                    c = col+dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r,c) not in visit:
                        visit.add((r,c))
                        q.append((r,c))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    dfs(r,c)
                    res+=1
        return res
