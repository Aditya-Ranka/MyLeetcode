"""
Problem: Trapping Rain Water
LeetCode: https://leetcode.com/problems/trapping-rain-water/
Topic: Stack and Queues
Difficulty: Hard

Approach:
- Initialize left and right pointers at the array ends and set maxL and maxR to the heights at those positions
- Loop while left < right, comparing maxL and maxR
- If maxL <= maxR, increment left, update maxL to the larger of current maxL and new height, and add maxL - height[left] to result
- Else, decrement right, update maxR similarly, and add maxR - height[right] to result

Comments:
- Returns 0 for an empty list
- Uses only constant extra variables, so space is O(1)

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l = 0
        r = len(height) - 1
        maxL = height[l]
        maxR = height[r]
        res = 0
        while l<r:
            if maxL <= maxR:
                l+=1
                maxL = max(maxL, height[l])
                res+= maxL - height[l]
            else:
                r-=1
                maxR = max(maxR, height[r])
                res+= maxR - height[r]
        return res
