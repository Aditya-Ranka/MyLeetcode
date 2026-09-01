"""
Problem: Reverse String
LeetCode: https://leetcode.com/problems/reverse-string/
Topic: Sliding Window / Two Pointer
Difficulty: Easy

Approach:
- Initialize left index l=0 and right index r=len(s)-1
- Iterate floor(len(s)/2) times using a for‑loop
- Swap s[l] and s[r] with a temporary variable, then increment l and decrement r

Comments:
- Handles empty or single‑element lists gracefully; uses integer division to compute half length

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) - 1
        for _ in range((r+1)//2):
            temp = s[l]
            s[l] = s[r]
            s[r] = temp
            l+=1
            r-=1
