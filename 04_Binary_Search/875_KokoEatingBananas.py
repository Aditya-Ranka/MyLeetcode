"""
Problem: Koko Eating Bananas
LeetCode: https://leetcode.com/problems/koko-eating-bananas/
Topic: Binary Search
Difficulty: Medium

Approach:
- Binary search on the eating speed (the answer), range [1, max(pile)].
- For speed m, hours = sum(ceil(pile/m)); feasible if <= h.
- Feasible -> try slower (r=m-1); else faster (l=m+1). l converges to the minimum workable speed.

Time Complexity: O(n log(max pile))
Space Complexity: O(1)
"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l <= r:
            m = (l+r)//2
            time = 0
            for i in range(len(piles)):
                if piles[i] <= m:
                    time+=1
                    continue
                time+=ceil(piles[i]/m)
            if time <= h:
                r = m -1
                continue
            
            else:
                l = m+1
                continue
        return l
