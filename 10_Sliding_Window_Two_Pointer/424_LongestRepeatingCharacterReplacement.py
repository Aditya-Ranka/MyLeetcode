"""
Problem: Longest Repeating Character Replacement
LeetCode: https://leetcode.com/problems/longest-repeating-character-replacement/
Topic: Sliding Window / Two Pointer
Difficulty: Medium

Approach:
- Init left pointer l=0, result res=0, and empty count dict.
- Loop r over s with enumerate, increment count[ch].
- While window length minus max(count.values()) > k, decrement count[s[l]] and increment l.
- Update res = max(res, r-l+1) after window is valid.
- Return res.

Comments:
- max(count.values()) is recomputed each iteration, costing O(Alphabet) time (constant 26 for lowercase letters).
- Zero-frequency entries stay in the dict but do not affect correctness.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        count = {}
        for r, ch in enumerate (s):
            count[ch] = count.get(ch, 0) + 1
            while r-l+1-max(count.values()) > k:
                count[s[l]] -= 1
                l+=1
            res = max(res, r-l+1)
        return res
