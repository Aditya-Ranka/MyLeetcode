"""
Problem: Largest Rectangle in Histogram
LeetCode: https://leetcode.com/problems/largest-rectangle-in-histogram/
Topic: Stack and Queues
Difficulty: Hard

Approach:
- Initialize maxSize and an empty stack storing (start index, height) pairs
- Iterate over heights with index i and height n, setting start=i
- While stack is non‑empty and n is less than the height at the top, pop (index,h), compute area h*(i-index), update maxSize, and set start=index
- Push (start,n) onto the stack
- After the loop, for each remaining (index,h) in the stack compute area h*(len(heights)-index) and update maxSize
- Return maxSize

Comments:
- Handles empty input returning 0; equal heights are kept to avoid redundant area calculations

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxSize = 0
        stck = []  #index, ht

        for i, n in enumerate(heights):
            start = i
            while stck and n < stck[-1][1]:
                index, h = stck.pop()
                maxSize = max(maxSize, h * (i - index))
                start = index
            stck.append((start, n))

        for index, h in stck:
            maxSize = max(maxSize, h * (len(heights) - index))

        return maxSize
