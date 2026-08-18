"""
Problem: Fruit Into Baskets
LeetCode: https://leetcode.com/problems/fruit-into-baskets/
Topic: Sliding Window / Two Pointer
Difficulty: Medium

Approach:
- Initialize count dict, left pointer l=0, best=0
- Iterate over fruits with right index r and fruit f, increment count[f]
- If more than two fruit types in count, shrink window from left: decrement count of fruits[l], delete key if count becomes 0, and move l right
- Update best with current window size r-l+1
- Return best as the maximum window length

Comments:
- Handles empty input by returning 0
- Count dict never holds more than two keys, so space usage is O(1)

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = {}
        l = 0
        best = 0
        for r, f in enumerate(fruits):
            count[f] = count.get(f, 0) + 1          
            while len(count) > 2:                    
                count[fruits[l]] -= 1
                if count[fruits[l]] == 0:
                    del count[fruits[l]]            
                l += 1
            best = max(best, r - l + 1)            
        return best
