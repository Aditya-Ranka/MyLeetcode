"""
Problem: Longest Palindromic Substring
LeetCode: https://leetcode.com/problems/longest-palindromic-substring/
Topic: Dynamic Programming
Difficulty: Medium

Approach:
- Iterate each character as a potential palindrome center
- Expand outward while characters match for odd‑length palindromes
- Expand outward while characters match for even‑length palindromes and update longest found

Comments:
- Handles empty input by returning an empty string
- Time complexity O(n^2) due to nested expansions, space complexity O(1)

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            l,r = i,i
            while l >= 0 and r < len(s) and s[r] == s[l]:
                if (r-l+1) > len(res):
                    res = s[l:r+1]
                l-=1
                r+=1
            l,r = i, i+1
            while l >= 0 and r < len(s) and s[r] == s[l]:
                if (r-l+1) > len(res):
                    res = s[l:r+1]
                l-=1
                r+=1
        return res
