"""
Problem: Longest Common Prefix
LeetCode: https://leetcode.com/problems/longest-common-prefix/
Topic: Tries
Difficulty: Easy

Approach:
- Check for empty input list and return empty string if so
- Initialize result list and index i to 0
- Loop: if i reaches length of first string, return accumulated prefix
- Take character x at position i of first string
- Compare x with character at same position in each other string; if any string is shorter or mismatches, return prefix
- If all match, append x to result and increment i

Comments:
- Handles empty list and strings of varying lengths; builds prefix in a list before joining

Time Complexity: O(n*m)
Space Complexity: O(m)
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        res = []
        i = 0
        while True:
            if i >= len(strs[0]):
                return ''.join(res)

            x = strs[0][i]

            for s in strs[1:]:
                # stop if this string is too short, or its char doesn't match
                if i >= len(s) or s[i] != x:
                    return ''.join(res)

            res.append(x)
            i += 1
