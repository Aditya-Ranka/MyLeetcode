"""
Problem: Minimum Number of Days to Make m Bouquets
LeetCode: https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/
Topic: Binary Search
Difficulty: Medium

Approach:
- If m*k > number of flowers it's impossible (-1).
- Binary search on days, range [1, max(bloomDay)]; getCount greedily counts complete bouquets of k adjacent bloomed flowers by a candidate day.
- Enough bouquets -> try fewer days; else more. l is the answer.

Time Complexity: O(n log(max bloom))
Space Complexity: O(1)
"""

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if (len(bloomDay) < m*k):
            return -1
        def getCount(mid,k):
            countOfPM = 0
            count = 0
            

            for bloom in bloomDay:
                if bloom <= mid:
                    count+=1
                    if count == k:
                        countOfPM+=1
                        count = 0
                else:
                    
                    count = 0
            if countOfPM >= m:
                return -1 #go left
            else:
                return 1 #go right
        
        l,r = 1,max(bloomDay)
        while l <= r:
            mid = (l+r)//2
            res = getCount(mid, k)
            if res == -1:
                r = mid - 1
            else:
                l = mid + 1
        return l
