"""
Problem: Number of Provinces
LeetCode: https://leetcode.com/problems/number-of-provinces/
Topic: Misc
Difficulty: Medium

Approach:
- Initialize visited list of size n
- Define recursive dfs that marks a city and recursively visits all directly connected cities by scanning the matrix row
- Loop through each city; if unvisited, start dfs and increment province count

Comments:
- DFS recursion may exceed Python's recursion limit on very large inputs
- Scanning the entire row for each dfs call yields O(n²) time

Time Complexity: O(n^2)
Space Complexity: O(n)
"""

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visit = [False] * (n)
        def dfs(j):
            visit[j] = True
            for i in range(n):
                if isConnected[i][j] and not visit[i]:
                    dfs(i)
            
        res = 0
        for i in range(n):
            if not visit[i]:
                dfs(i)
                res+=1
        return res
