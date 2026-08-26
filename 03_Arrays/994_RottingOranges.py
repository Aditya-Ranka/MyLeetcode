"""
Problem: Rotting Oranges
LeetCode: https://leetcode.com/problems/rotting-oranges/
Topic: Arrays
Difficulty: Medium

Approach:
- Collect positions of all initially rotten oranges and count fresh oranges
- Perform BFS level‑by‑level using a deque for the current layer and another for the next layer
- For each rotten orange, infect adjacent fresh oranges, enqueue them, decrement fresh count, and mark them rotten
- Replace current layer with the next layer and increment elapsed time
- After BFS, return -1 if any fresh orange remains, otherwise return elapsed time

Comments:
- Uses two separate deques to isolate each BFS level, simplifying time increment logic
- Range membership checks (r in range(rows)) create a new range each call; a simple bounds check (0<=r<rows) would be marginally faster

Time Complexity: O(m*n)
Space Complexity: O(m*n)
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        curr = collections.deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    curr.append((i,j))
                if grid[i][j] == 1:
                    count+=1
        
        while count and curr:
                q = collections.deque()
                directions = [[1,0], [0,1], [-1,0], [0,-1]]
                while curr:
                    row,col = curr.popleft()
                    for dr,dc in directions:
                        r = row + dr
                        c = col + dc
                        if r in range(rows) and c in range(cols) and grid[r][c] == 1:
                            q.append((r,c))
                            count-=1
                            grid[r][c] = 2
                curr = q
                time+=1
        if count != 0:
            return -1
        return time
