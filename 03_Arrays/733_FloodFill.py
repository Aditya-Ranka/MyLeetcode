"""
Problem: Flood Fill
LeetCode: https://leetcode.com/problems/flood-fill/
Topic: Arrays
Difficulty: Easy

Approach:
- If starting pixel already has target color, return image
- Store original color and initialize BFS queue with starting coordinates
- Mark starting pixel with new color
- While queue not empty, pop a pixel and examine its four neighbors
- If neighbor is inside bounds and has original color, enqueue it and recolor it
- Continue until all reachable original‑color pixels are recolored

Comments:
- Early exit avoids infinite loop when new color equals original color
- Uses range() checks for bounds each iteration

Time Complexity: O(m*n)
Space Complexity: O(m*n)
"""

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        ogColor = image[sr][sc]
        rows = len(image)
        cols = len(image[0])
        q = collections.deque()
        q.append((sr,sc))
        image[sr][sc] = color
        while q:
            row, col = q.popleft()
            directions = [[1,0], [0,1], [-1,0], [0,-1]]
            for dr,dc in directions:
                r = row + dr
                c = col + dc
                if r in range(rows) and c in range(cols) and image[r][c] == ogColor:
                    q.append((r,c))
                    image[r][c] = color
        return image
