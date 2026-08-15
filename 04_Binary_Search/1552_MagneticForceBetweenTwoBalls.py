"""
Problem: Magnetic Force Between Two Balls
LeetCode: https://leetcode.com/problems/magnetic-force-between-two-balls/
Topic: Binary Search
Difficulty: Medium

Approach:
- Sort positions, then binary search on the minimum gap (force), range [1, (max-min)//(m-1)].
- willItWork greedily places balls at least `mid` apart and checks whether all m fit.
- Feasible -> try a larger gap (l=mid+1); else smaller. Answer is l-1 (largest feasible minimum gap).

Time Complexity: O(n log(range))
Space Complexity: O(1)
"""

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def returnS(i,j):
            return position[j] - position[i]
        def willItWork(mid):
            balls = []
            noOfB = 1
            
            i,j = 0,1
            while noOfB < m and j < len(position):
                if returnS(i,j) >= mid:
                    i = j
                    j = i+1
                    noOfB+=1
                else:
                    j+=1 
            return noOfB >= m
        l = 1
        r =(position[-1] - position[0]) // (m - 1)
        while l <= r:
            mid = (l+r)//2
            res = willItWork(mid)
            if res == True:
                l = mid+1
            else:
                r = mid-1
        return l-1
