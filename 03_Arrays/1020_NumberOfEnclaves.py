"""
Problem: Number of Enclaves
LeetCode: https://leetcode.com/problems/number-of-enclaves/
Topic: Arrays
Difficulty: Medium

Approach:
- Count all land cells (value 1) in the grid
- Add every border land cell to a queue, mark it visited, and subtract it from the count
- Perform BFS from the queue, visiting 4‑directionally adjacent land cells, marking them visited and subtracting each from the count
- Return the remaining count as the number of enclave cells

Comments:
- Uses a separate visited set; could reuse the grid to achieve O(1) extra space
- Range checks (r in range(rows)) create a new range object each iteration but are still O(1)

Time Complexity: O(rows * cols)
Space Complexity: O(rows * cols)
"""

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = collections.deque()
        count = 0
        directions = [[0,1], [1,0], [-1,0], [0,-1]]
        visited = set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    count+=1
        for i in (0,rows-1):
            for j in range(cols):
                if grid[i][j] == 1 and ((i,j)) not in visited:
                    q.append((i,j))
                    visited.add((i,j))
                    count-=1
        for i in range(rows):
            for j in (0, cols-1):
                if grid[i][j] == 1 and ((i,j)) not in visited:
                    q.append((i,j))
                    visited.add((i,j))
                    count-=1


        while q:
            row, col = q.popleft()
            for dr,dc in directions:
                r = row + dr
                c = col + dc
                if r in range(rows) and c in range(cols) and ((r,c)) not in visited and grid[r][c] == 1:
                    q.append((r,c))
                    count -=1
                    visited.add((r,c))
        return count
