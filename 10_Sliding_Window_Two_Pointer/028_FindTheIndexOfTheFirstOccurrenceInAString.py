"""
Problem: Find the Index of the First Occurrence in a String
LeetCode: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
Topic: Sliding Window / Two Pointer
Difficulty: Easy

Approach:
- Initialize hayP and needleP to 0
- Iterate hayP while it is less than len(haystack)
- If haystack[hayP] equals needle[needleP], compare haystack slice of length len(needle) starting at hayP with needle
- If the slice matches, return hayP
- Increment hayP and continue
- Return -1 after loop ends

Comments:
- Fails when needle is empty (IndexError)
- Runs in O(n*m) time because it creates and compares a slice at each position

Time Complexity: O(n*m)
Space Complexity: O(1)
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needleP = 0
        hayP = 0
        while hayP < len(haystack):
            if haystack[hayP]==needle[needleP]:
                if haystack[hayP:hayP+len(needle)] == needle:
                    return hayP
            
            hayP+=1
        return -1
