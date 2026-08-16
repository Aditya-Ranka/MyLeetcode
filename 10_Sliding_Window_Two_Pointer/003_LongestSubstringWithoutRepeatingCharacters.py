"""
Problem: Longest Substring Without Repeating Characters
LeetCode: https://leetcode.com/problems/longest-substring-without-repeating-characters/
Topic: Sliding Window / Two Pointer
Difficulty: Medium

Approach:
- Initialize a sliding window with left and right pointers
- Use a hash table to track the last seen index of each character
- Update the left pointer when a repeating character is found
- Update the maximum length of substring without repeating characters

Comments:
- The key insight is to move the left pointer to the right of the previous occurrence of the repeating character, not just to the next character
- This approach avoids unnecessary iterations and ensures the optimal solution

Time Complexity: O(n)
Space Complexity: O(min(n, m))
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        best = 0
        for right, ch in enumerate(s):
            if ch in last_seen and last_seen[ch] >= left:
                left = last_seen[ch] + 1
            last_seen[ch] = right
            best = max(best, right - left + 1)
        return best
