"""
Problem: Kth Smallest Element in a Sorted Matrix
LeetCode: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
Topic: Heaps
Difficulty: Medium

Approach:
- Set n as matrix dimension and define isFeasible(mid) to count elements ≤mid by iterating rows bottom‑up and columns left‑to‑right, breaking when a value exceeds mid
- Initialize search bounds ansL and ansR to the smallest and largest matrix entries
- Binary‑search while ansL≤ansR: compute mid, call isFeasible(mid); if true move ansR left, else move ansL right
- After loop, return ansL as the kth smallest value

Comments:
- The double loop in isFeasible runs O(n²) in the worst case, so the overall complexity is O(n²·log (range)) rather than the optimal O(n·log range)
- Duplicates are handled because the check uses count≥k; the algorithm assumes matrix values fit in Python int range

Time Complexity: O(n^2 log D)
Space Complexity: O(1)
"""

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        def isFeasible(mid):
            count = 0
            for i in range(n-1,-1,-1):
                for j in range(0,n):
                    if matrix[i][j] <= mid:
                        count+=1
                    else:
                        break
            if count >= k:
                return True
            else: #count <= k
                return False
                    
        ansL = matrix[0][0]
        ansR = matrix[n-1][n-1]
        while ansL <= ansR:
            mid = (ansL + ansR)//2
            if isFeasible(mid):
                ansR = mid - 1
                continue
            else:
                ansL = mid + 1
                continue
        return ansL
