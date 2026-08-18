"""
Problem: Maximum Points You Can Obtain from Cards
LeetCode: https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
Topic: Sliding Window / Two Pointer
Difficulty: Medium

Approach:
- Compute total sum of all cards
- If k >= n return total
- Initialize sum of first n-k cards as current window sum
- Slide window across array updating sum and track minimum window sum
- Return total minus the minimum window sum

Comments:
- Handles k equal to array length by early return; sliding window size zero works correctly

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l = 0
        r = len(cardPoints)-k
        currSum = 0
        total = sum(cardPoints)
        if k >= len(cardPoints):
            return total
        for i in range(len(cardPoints) - k):
            currSum += cardPoints[i]
        res = currSum
        while r < len(cardPoints):
            currSum -= cardPoints[l]
            currSum += cardPoints[r]
            res = min(res, currSum)
            l+=1
            r+=1
        return total - res
